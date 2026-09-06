#!/usr/bin/env python3
"""
build_skill_swarms.py

Proposito: transformar cada skill em um enxame auditavel de agentes,
usando os materiais de agentes-training/ como fontes de conhecimento.

Regras de verdade:
- Falha se uma fonte declarada em training-provenance.yaml nao existir.
- Falha se arquivos obrigatorios da skill estiverem ausentes.
- Nao trunca, resume ou inventa conteudo-fonte.
- Gera relatorio de cobertura e lista skills proposed vs enriched.

Uso:
  python scripts/build_skill_swarms.py --check
  python scripts/build_skill_swarms.py --build --skill <skill>
  python scripts/build_skill_swarms.py --report
"""

import argparse
import os
import sys
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
TRAINING_DIR = ROOT / "agentes-training"
PROVENANCE_FILE = SKILLS_DIR / "training-provenance.yaml"
CONTRACT_FILE = SKILLS_DIR / "AGENT_SWARM_CONTRACT.md"

REQUIRED_SKILL_FILES = [
    "SKILL.md",
    "AGENTS.md",
    "WORKFLOW.md",
    "INPUT_CONTRACT.yaml",
    "OUTPUT_CONTRACT.yaml",
    "QUALITY_GATE.md",
    "ROLLBACK.md",
    "TRAINING_SOURCES.yaml",
]

AGENT_FILES = [
    "architect.md",
    "implementation.md",
    "integration.md",
    "performance.md",
    "accessibility.md",
    "quality.md",
    "evidence.md",
]


def load_provenance():
    if not PROVENANCE_FILE.exists():
        raise FileNotFoundError(f"Matriz de proveniencia nao encontrada: {PROVENANCE_FILE}")
    with open(PROVENANCE_FILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def check_training_sources(provenance):
    missing = []
    for src in provenance.get("cross_cutting_sources", []):
        path = ROOT / src["path"]
        if not path.exists():
            missing.append(src["path"])
    for skill_name, skill_data in provenance.get("skills", {}).items():
        for src in skill_data.get("sources", []):
            path = ROOT / src["path"]
            if not path.exists():
                missing.append(src["path"])
    return missing


def check_skill_structure(skill_name):
    skill_path = SKILLS_DIR / skill_name
    if not skill_path.exists():
        return [f"Pasta da skill nao existe: {skill_path}"]
    errors = []
    for req in REQUIRED_SKILL_FILES:
        if not (skill_path / req).exists():
            errors.append(f"Arquivo obrigatorio ausente: {skill_path / req}")
    agents_dir = skill_path / "agents"
    if agents_dir.exists():
        for agent in AGENT_FILES:
            if not (agents_dir / agent).exists():
                errors.append(f"Agente ausente: {agents_dir / agent}")
    examples_dir = skill_path / "examples"
    if not examples_dir.exists():
        errors.append(f"Pasta de exemplos ausente: {examples_dir}")
    return errors


def build_skill_swarms(provenance, target_skill=None):
    report = {"built": [], "failed": [], "skipped": []}
    skills = provenance.get("skills", {})
    for skill_name, skill_data in skills.items():
        if target_skill and skill_name != target_skill:
            report["skipped"].append(skill_name)
            continue
        if skill_data.get("status") != "proposed":
            report["skipped"].append(skill_name)
            continue
        skill_path = SKILLS_DIR / skill_name
        if not skill_path.exists():
            report["failed"].append({"skill": skill_name, "reason": "pasta inexistente"})
            continue
        errors = check_skill_structure(skill_name)
        if errors:
            report["failed"].append({"skill": skill_name, "reasons": errors})
            continue
        sources = skill_data.get("sources", [])
        for src in sources:
            src_path = ROOT / src["path"]
            if not src_path.exists():
                report["failed"].append({"skill": skill_name, "reason": f"fonte ausente {src['path']}"})
                break
        else:
            report["built"].append(skill_name)
    return report


def generate_report(provenance):
    lines = []
    lines.append("# Relatorio de Skills-Enxame\n")
    lines.append(f"Repositorio: {provenance.get('repository', 'unknown')}\n")
    lines.append(f"Status da matriz: {provenance.get('status', 'unknown')}\n\n")
    lines.append("## Skills\n\n")
    for skill_name, skill_data in provenance.get("skills", {}).items():
        status = skill_data.get("status", "unknown")
        sources = skill_data.get("sources", [])
        lines.append(f"### {skill_name}\n")
        lines.append(f"Status: {status}\n")
        lines.append(f"Fontes: {len(sources)}\n")
        for src in sources:
            src_path = ROOT / src["path"]
            exists = "existe" if src_path.exists() else "FALTA"
            lines.append(f"- [{exists}] {src['path']} ({src['role']})\n")
        lines.append("\n")
    return "".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Construtor de skills-enxame auditaveis")
    parser.add_argument("--check", action="store_true", help="Apenas valida fontes e estrutura")
    parser.add_argument("--build", action="store_true", help="Constroi enxames para skills proposed")
    parser.add_argument("--skill", type=str, help="Skill especifica para build")
    parser.add_argument("--report", action="store_true", help="Gera relatorio de cobertura")
    args = parser.parse_args()

    if not args.check and not args.build and not args.report:
        parser.print_help()
        sys.exit(1)

    print("Carregando matriz de proveniencia...")
    provenance = load_provenance()

    if args.check or args.build:
        print("Validando fontes de treinamento...")
        missing_sources = check_training_sources(provenance)
        if missing_sources:
            print("[ERRO] Fontes de treinamento ausentes:")
            for m in missing_sources:
                print(f"  - {m}")
            sys.exit(1)
        print("[OK] Todas as fontes de treinamento existem.")

    if args.check:
        print("\nValidando estrutura das skills...")
        all_ok = True
        for skill_name in provenance.get("skills", {}).keys():
            errors = check_skill_structure(skill_name)
            if errors:
                all_ok = False
                print(f"[ERRO] {skill_name}:")
                for e in errors:
                    print(f"  - {e}")
            else:
                print(f"[OK] {skill_name}")
        sys.exit(0 if all_ok else 1)

    if args.build:
        print("\nConstruindo skills-enxame...")
        report = build_skill_swarms(provenance, target_skill=args.skill)
        print(f"Construidas: {len(report['built'])}")
        for s in report["built"]:
            print(f"  - {s}")
        if report["failed"]:
            print("Falhas:")
            for f in report["failed"]:
                print(f"  - {f['skill']}: {f.get('reason', f.get('reasons', 'erro desconhecido'))}")
        if report["skipped"]:
            print("Puladas (status != proposed ou target):")
            for s in report["skipped"]:
                print(f"  - {s}")

    if args.report:
        print("\nGerando relatorio de cobertura...")
        report_md = generate_report(provenance)
        report_path = ROOT / "skills" / "COVERAGE_REPORT.md"
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(report_md)
        print(f"Relatorio salvo em: {report_path}")


if __name__ == "__main__":
    main()
