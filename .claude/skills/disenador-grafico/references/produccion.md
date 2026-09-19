# Producción: cómo sale la pieza hecha

No entregues solo instrucciones. Produce la pieza. Elige la vía en este orden:

## 1. HTML + render a imagen (vía por defecto)

Sirve para casi todo: posts, carruseles, stories, portadas, banners, miniaturas.
Copia `assets/plantilla-pieza.html`, ajusta variables y contenido, y renderiza con el
script incluido:

```bash
python3 assets/render.py pieza.html pieza.png 1080 1350 --fuentes "Syne,Public Sans"
```

El script hace tres cosas: renderiza, recorta exacto al elemento `.pieza`, y **verifica
que las fuentes de marca cargaron de verdad**. Si alguna no cargó, sale con error y la
pieza no se entrega.

### Por qué la verificación no es opcional

`document.fonts.check()` devuelve `true` aunque la fuente no exista, porque responde sobre
el fallback. Una pieza puede renderizar perfecta y estar en la tipografía equivocada sin
que se note a simple vista. El script mide el mismo texto con dos fallbacks de métricas
distintas: si la fuente cargó, ambos anchos coinciden; si no, difieren.

Causas frecuentes de que no cargue: sin red hacia Google Fonts, proxy que bloquea el CDN,
o el `.ttf` no está en `assets/fonts/`. Arreglo: copiar los `.ttf` del kit de marca a
`assets/fonts/` o instalarlos en el sistema. Nunca sustituyas la fuente de marca por otra
parecida sin decirlo.

Para un carrusel: un archivo HTML por slide, mismo bloque `:root`, y renderiza en bucle a
`slide-01.png`, `slide-02.png`…

Si no hay Playwright ni forma de renderizar, no te detengas: entrega el HTML, di
explícitamente que no pudiste verificar las fuentes, y sigue con el resto del entregable.

## 2. SVG

Para logos, marcas de agua, iconos, diagramas y cualquier cosa que deba escalar sin
perder nitidez. Escribe el SVG a mano, con `viewBox` limpio y sin capas basura.
Convierte el texto a trazos solo en el archivo final de entrega, nunca en el editable.

## 3. Canva

Cuando la pieza deba quedar editable por una persona, cuando forme parte de plantillas ya
existentes, o **cuando las fuentes de marca no carguen fuera de Canva**: dentro de Canva sí
están, vía el Kit de Marca.

Kits de marca disponibles: LUBIASO (`kAHUpyry43w`) y PODCAST (`kAHUp7rPFQo`).

Antes de crear algo nuevo, busca si ya existe la plantilla: las de LUBIASO viven en la
carpeta `FAHUphLtvJM` y se duplican, no se rediseñan.

## 4. Imágenes generadas

Para fondos, texturas y elementos abstractos de apoyo, no para el protagonista de la
pieza si hay una foto real disponible. Si hay un generador de imágenes en la sesión,
úsalo pidiendo: sujeto, encuadre, iluminación, paleta y espacio libre para el texto.
Nunca generes caras de personas reales ni imites el estilo de un artista vivo.

## Entrega de archivos

- Muestra siempre la pieza renderizada, no solo el código.
- Nombra: `marca_pieza_fecha_v1.png`.
- Si es serie, muestra las piezas juntas para verificar que se vean como familia.
