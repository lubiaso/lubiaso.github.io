# Checklist de QA — correr antes de entregar

## Fuentes de marca (primero, porque invalida todo lo demás)
- [ ] El render verificó que las fuentes de marca cargaron (`render.py --fuentes`).
- [ ] Si alguna no cargó: la pieza NO se entrega como final. Se arregla o se produce
      en Canva, y se dice explícitamente qué pasó.

## Legibilidad
- [ ] Contraste texto/fondo ≥ 4.5:1 (≥ 3:1 si ≥24px o ≥19px bold).
- [ ] Ningún texto bajo 28px en lienzo de 1080px.
- [ ] Texto sobre foto tiene overlay, degradado o caja.
- [ ] La pieza se entiende vista al 25% de tamaño (prueba de miniatura).

## Jerarquía
- [ ] Hay un solo foco evidente.
- [ ] Máximo 3 niveles de jerarquía.
- [ ] Los grupos se leen como grupos (espaciado coherente).

## Sistema
- [ ] Máximo 2 familias tipográficas.
- [ ] Colores solo de la paleta definida, con sus roles.
- [ ] La pieza es de UNA sola marca: nada de mezclar el rosa del podcast con LUBIASO.
- [ ] LUBIASO: un solo elemento rojo en toda la pieza, y el rojo no está en texto pequeño.
- [ ] Márgenes y espaciado en múltiplos de la unidad base.
- [ ] Logo en posición y tamaño consistentes con el resto del sistema.

## Detalle
- [ ] Sin viudas ni huérfanas en titulares.
- [ ] Alineaciones exactas, no a ojo.
- [ ] Ortografía y tildes revisadas (incluye mayúsculas acentuadas).
- [ ] Imágenes sin deformar ni pixelar; nada escalado por encima del 100%.
- [ ] Safe areas respetadas para la plataforma destino.

## Salida
- [ ] Lienzo y formato correctos para la plataforma.
- [ ] Nombre de archivo legible: `marca_pieza_fecha_v1`.
- [ ] Si es serie: las piezas se ven como familia puestas una al lado de otra.
