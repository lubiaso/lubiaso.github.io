# Formatos y safe areas

Medidas de plataformas cambian: si la pieza es crítica, verifica la especificación vigente
antes de exportar.

## Instagram

| Pieza | Lienzo | Notas |
|---|---|---|
| Post / carrusel vertical | 1080 × 1350 (4:5) | Formato por defecto: ocupa más pantalla |
| Post cuadrado | 1080 × 1080 | Solo si el sistema visual lo pide |
| Stories / Reels | 1080 × 1920 (9:16) | |
| Portada de Reel | 1080 × 1920, con foco central | El grid de perfil recorta a vertical: mantén texto en el centro |

**Safe areas en 1080 × 1920**: deja libres ~250px arriba y ~420px abajo de texto y logo.
Ahí van los botones, el usuario y el copy. En carruseles 4:5 deja ~150px inferiores sin
información crítica.

## Otros

| Pieza | Lienzo |
|---|---|
| Portada de podcast (Spotify/Apple) | 3000 × 3000, RGB, texto legible a 55px de ancho |
| Miniatura YouTube | 1280 × 720 |
| TikTok | 1080 × 1920 |
| Presentación | 1920 × 1080 |
| Banner web hero | 2560 × 1440 (exportar @1x y @2x) |

## Exportación

- Social: PNG si hay texto plano o gráficos; JPG calidad 90 si domina la foto. Instagram
  recomprime: exporta a 1080px de ancho exacto, ni más ni menos, para evitar doble resample.
- Impresión: PDF/X, CMYK, 300 dpi, 3mm de sangrado, negros ricos solo en masas grandes
  (C40 M30 Y30 K100), nunca en texto pequeño.
- Logo: entrega siempre SVG además del PNG.
