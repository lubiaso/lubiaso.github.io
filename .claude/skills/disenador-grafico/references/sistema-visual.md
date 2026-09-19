# Sistema visual: tipografía y color

## Escala tipográfica

Usa una escala modular, no tamaños arbitrarios. Razón 1.25 (suave, editorial) o 1.333
(dramática, social). Base 16px para web, 48px para pieza social 1080px.

Ejemplo razón 1.333 sobre base 48 (lienzo 1080x1350):
`48 → 64 → 85 → 114 → 151 → 201`

Reglas:
- **Interlineado**: 1.1–1.2 en titulares grandes, 1.4–1.6 en textos de lectura. A más
  grande la fuente, más apretado el interlineado.
- **Longitud de línea**: 45–75 caracteres en texto corrido. En pieza social, 20–35.
- **Tracking**: negativo leve (−1% a −3%) en titulares grandes; positivo (+5% a +10%) solo
  en mayúsculas pequeñas tipo etiqueta.
- **Jerarquía por peso antes que por tamaño** cuando el espacio es poco.
- Nada de texto por debajo de 28px en un lienzo de 1080px: no se lee en el feed.

## Elección tipográfica

Combina por contraste real, no por parecido: sans geométrica + serif editorial, o una sola
familia con muchos pesos (superfamilia). Dos sans neutras juntas = error.

Combinaciones seguras y gratis (Google Fonts):
- Editorial: `Playfair Display` (títulos) + `Inter` (texto)
- Moderna limpia: `Archivo` / `Archivo Black` (títulos) + `Inter` (texto)
- Cálida: `Fraunces` (títulos) + `Work Sans` (texto)
- Técnica: `Space Grotesk` + `IBM Plex Mono` (datos)
- Una sola familia: `Inter`, `Manrope` o `Figtree` usando 700/500/400

## Color

Estructura mínima de paleta (no más de esto):
- **1 primario de marca** — identidad, no necesariamente el más usado.
- **1 acento** — solo CTA y énfasis. Si se usa en más del 10% de la pieza, deja de ser acento.
- **2 neutros** — un claro de fondo y un oscuro de texto. Nunca #000 puro sobre #FFF puro:
  usa #111418 sobre #FAFAF8, se ve más caro y cansa menos.
- **Opcional: 1–2 de soporte** para categorías o pilares de contenido.

Reglas:
- **Proporción 60/30/10**: fondo dominante / secundario / acento.
- Genera variantes de un color cambiando luminosidad y saturación a la vez (bajar L sin
  bajar S produce colores sucios).
- Verifica contraste siempre (`checklist-qa.md`). Un acento vibrante casi nunca pasa AA con
  texto blanco encima: úsalo como fondo de bloque grande o como filete, no como color de
  texto pequeño.
- Modo oscuro: no invierte literalmente. Baja saturación del acento y sube luminosidad del
  texto a ~#E8E8E6, fondo ~#14161A.

## Sistema, no pieza suelta

Si vas a producir más de tres piezas, define primero: retícula, escala tipográfica, paleta
con roles, tratamiento de foto (filtro, recorte, overlay) y ubicación fija del logo.
Después produce. Sin eso, la cuenta se ve desordenada aunque cada pieza esté bien.
