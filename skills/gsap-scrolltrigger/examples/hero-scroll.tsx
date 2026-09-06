// Exemplo: Hero Scroll com GSAP + Lenis
// Uso: Copiar para seu projeto Next.js

'use client'
import { useEffect, useRef } from 'react'
import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import Lenis from 'lenis'

gsap.registerPlugin(ScrollTrigger)

export function HeroScroll() {
  const heroRef = useRef<HTMLDivElement>(null)
  const productsRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    // Lenis smooth scroll
    const lenis = new Lenis({
      duration: 1.2,
      smoothWheel: true,
    })

    // Sync Lenis + ScrollTrigger
    lenis.on('scroll', ScrollTrigger.update)
    gsap.ticker.add((time) => {
      lenis.raf(time * 1000)
    })
    gsap.ticker.lagSmoothing(0)

    // Cleanup
    return () => {
      lenis.destroy()
    }
  }, [])

  useEffect(() => {
    const ctx = gsap.context()

    // Hero title - fade out on scroll
    gsap.to(heroRef.current?.querySelector('.hero_title'), {
      scrollTrigger: {
        trigger: heroRef.current,
        start: 'top top',
        end: 'bottom top',
        scrub: true,
      },
      y: -100,
      opacity: 0,
      duration: 1,
    })

    // Product grid - pin + scale reveal
    gsap.to(productsRef.current?.querySelectorAll('.product_card'), {
      scrollTrigger: {
        trigger: productsRef.current,
        start: 'top center',
        end: 'bottom center',
        scrub: 1,
        pin: true,
      },
      scale: 1,
      opacity: 1,
      stagger: { amount: 0.1, from: 'center' },
      duration: 1,
      ease: 'power2.inOut',
    })

    return () => ctx.revert()
  }, [])

  return (
    <>
      {/* Hero Section */}
      <section ref={heroRef} className="hero" style={{ height: '100vh', display: 'grid', placeItems: 'center' }}>
        <h1 className="hero_title" style={{ fontSize: '4rem', fontWeight: 'bold' }}>
          Minha Marca
        </h1>
        <p className="hero_subtitle" style={{ fontSize: '1.5rem', opacity: 0.8 }}>
          Transformando o futuro
        </p>
      </section>

      {/* Products Section */}
      <section ref={productsRef} className="products" style={{ minHeight: '100vh', padding: '4rem 2rem' }}>
        <h2 style={{ fontSize: '2.5rem', marginBottom: '3rem' }}>Nossos Produtos</h2>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '2rem' }}>
          {['Produto 1', 'Produto 2', 'Produto 3'].map((name, i) => (
            <div
              key={i}
              className="product_card"
              style={{
                background: '#f5f5f5',
                padding: '2rem',
                borderRadius: '1rem',
                opacity: 0,
                scale: 0.9,
              }}
            >
              <h3 style={{ fontSize: '1.5rem', marginBottom: '1rem' }}>{name}</h3>
              <p style={{ opacity: 0.7 }}>Descricao do produto...</p>
            </div>
          ))}
        </div>
      </section>

      {/* Reduced Motion */}
      <style jsx global>{`
        @media (prefers-reduced-motion: reduce) {
          .hero_title,
          .product_card {
            transition: opacity 0.5s ease !important;
            transform: none !important;
          }
        }
      `}</style>
    </>
  )
}
