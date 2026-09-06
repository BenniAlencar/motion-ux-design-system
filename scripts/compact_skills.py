#!/usr/bin/env python3
"""
Compacta todas as skills em uma unica pasta skills-compact/
Cada skill vira um unico arquivo: skills-compact/{skill}.md

Uso:
  python scripts/compact_skills.py

Output:
  skills-compact/gsap-scrolltrigger.md
  skills-compact/lenis.md
  skills-compact/r3f-threejs-drei.md
  ...
"""

import os

SKILLS_DIR = "skills"
OUTPUT_DIR = "skills-compact"

FILES_TO_INCLUDE = [
    "SKILL.md",
    "AGENTS.md",
    "WORKFLOW.md",
    "INPUT_CONTRACT.yaml",
    "OUTPUT_CONTRACT.yaml",
    "PATTERNS.md",
    "IMPLEMENTATION.md",
    "QUALITY_GATE.md",
    "EVALS.md",
]

def compact_skill(skill_path, skill_name):
    """Compacta todos os arquivos de uma skill em um unico arquivo .md"""
    
    output_lines = []
    output_lines.append(f"# {skill_name}\n")
    output_lines.append(f"Skill compactada — todo o conteudo em um unico arquivo\n")
    output_lines.append("=" * 80 + "\n\n")
    
    # Arquivos principais
    for filename in FILES_TO_INCLUDE:
        filepath = os.path.join(skill_path, filename)
        
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            output_lines.append(f"\n{'=' * 80}")
            output_lines.append(f"## {filename}")
            output_lines.append(f"{'=' * 80}\n")
            output_lines.append(content)
    
    # Exemplos
    examples_dir = os.path.join(skill_path, "examples")
    if os.path.exists(examples_dir) and os.path.isdir(examples_dir):
        output_lines.append(f"\n\n{'=' * 80}")
        output_lines.append(f"## examples/")
        output_lines.append(f"{'=' * 80}\n")
        
        for filename in sorted(os.listdir(examples_dir)):
            filepath = os.path.join(examples_dir, filename)
            if os.path.isfile(filepath):
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                ext = "yaml" if filename.endswith(".yaml") or filename.endswith(".yml") else ""
                ext = "tsx" if filename.endswith(".tsx") or filename.endswith(".ts") else ext
                ext = "md" if filename.endswith(".md") else ext
                
                output_lines.append(f"\n### {filename}\n")
                output_lines.append(f"```{ext}\n")
                output_lines.append(content)
                output_lines.append("\n```\n")
    
    # Salvar arquivo
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_filename = f"{skill_name}.md"
    output_path = os.path.join(OUTPUT_DIR, output_filename)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(output_lines))
    
    # Calcular tamanho
    size_kb = os.path.getsize(output_path) / 1024
    print(f"✓ {skill_name}: {output_filename} ({size_kb:.1f} KB)")
    
    return size_kb

def main():
    print("=" * 80)
    print("Compactando skills em skills-compact/")
    print("=" * 80 + "\n")
    
    skills = sorted([s for s in os.listdir(SKILLS_DIR) if os.path.isdir(os.path.join(SKILLS_DIR, s))])
    total_size = 0
    
    for skill_name in skills:
        skill_path = os.path.join(SKILLS_DIR, skill_name)
        size = compact_skill(skill_path, skill_name)
        total_size += size
    
    print(f"\n{'=' * 80}")
    print(f"✓ {len(skills)} skills compactadas")
    print(f"✓ Total: {total_size:.1f} KB")
    print(f"✓ Output: {OUTPUT_DIR}/")
    print("=" * 80)

if __name__ == "__main__":
    main()
