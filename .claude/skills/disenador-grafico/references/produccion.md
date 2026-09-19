# Producción: cómo sale la pieza hecha

No entregues solo instrucciones. Produce la pieza. Elige la vía en este orden:

## 1. HTML + render a imagen (vía por defecto)

Sirve para casi todo: posts, carruseles, stories, portadas, banners, miniaturas.
Copia `assets/plantilla-pieza.html`, ajusta variables y contenido, y renderiza.

```bash
# Renderizar a PNG (requiere Playwright: pip install playwright && playwright install chromium)
python3 - <<'PY'
from playwright.sync_api import sync_playwright
import pathlib
ruta = pathlib.Path("pieza.html").resolve().as_uri()
with sync_playwright() as p:
    b = p.chromium.launch()   # si falla: launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome", args=["--no-sandbox"])
    pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
    pg.goto(ruta); pg.wait_for_timeout(2500)   # espera a que carguen las fuentes
    pg.locator(".pieza").screenshot(path="pieza.png")   # recorta exacto al lienzo
    b.close()
PY
```

Para un carrusel: un archivo HTML por slide, mismo `:root`, y renderiza en bucle a
`slide-01.png`, `slide-02.png`…

Si Playwright no está disponible, no te detengas: entrega el HTML, di que se abre en el
navegador y se captura a 1080px de ancho, y sigue con el resto del entregable.

## 2. SVG

Para logos, marcas de agua, iconos, diagramas y cualquier cosa que deba escalar sin
perder nitidez. Escribe el SVG a mano, con `viewBox` limpio y sin capas basura.
Convierte el texto a trazos solo en el archivo final de entrega, nunca en el editable.

## 3. Canva

Cuando la pieza deba quedar editable por una persona, o forme parte de plantillas ya
existentes. Usa el conector de Canva para crear o editar el diseño **después** de haber
fijado la especificación. Antes de crear algo nuevo, busca si ya existe una plantilla de
marca que se deba reutilizar.

## 4. Imágenes generadas

Para fondos, texturas y elementos abstractos de apoyo, no para el protagonista de la
pieza si hay una foto real disponible. Si hay un generador de imágenes en la sesión,
úsalo pidiendo: sujeto, encuadre, iluminación, paleta y espacio libre para el texto.
Nunca generes caras de personas reales ni imites el estilo de un artista vivo.

## Entrega de archivos

- Muestra siempre la pieza renderizada, no solo el código.
- Nombra: `marca_pieza_fecha_v1.png`.
- Si es serie, muestra las piezas juntas para verificar que se vean como familia.
