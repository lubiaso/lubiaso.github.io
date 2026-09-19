# Marcas del usuario

Lee este archivo antes de diseñar. Si la pieza es para una de estas marcas, usa su sistema
tal cual y no preguntes. Los datos de LUBIASO y del podcast salen de sus manuales y de las
piezas reales en Canva; no los cambies por criterio propio.

## Regla que no se rompe nunca

**LUBIASO y el podcast son dos lenguajes distintos y no se mezclan.** LUBIASO prohíbe el
rosado; el podcast se construye sobre rosa y rojo. Una pieza de LUBIASO con el rosa del
podcast está mal aunque se vea bien, y al revés. Antes de elegir un color, define de qué
marca es la pieza.

---

# LUBIASO (@lubiaso) — marca personal · Sistema FILO v3

Fuente: manual "Sistema Filo · v3", 13 de septiembre de 2026. **Reemplaza al kit y al
inventario anteriores.** Si algo no está en el manual, no es regla.

Kit de Marca en Canva: https://www.canva.com/brand/kAHUpyry43w
Carpeta de Canva: https://www.canva.com/folder/FAHUphLtvJM

## Color

| Rol | Hex | Uso | Contraste |
|---|---|---|---|
| Papel | `#FBFAF8` | fondo de todo. No es blanco puro y no se cambia por blanco puro | — |
| Negro | `#111111` | todo el texto, y el único fondo alternativo (cierre de carrusel y destacadas) | — |
| Corte | `#C3352B` | líneas de acento y el corte del logotipo. **Nunca texto pequeño** | 4,4:1 sobre papel · 2,8:1 sobre negro (solo línea con grosor) |
| Acero | `#B9BDC0` | bloques, separadores finos, marcos de guía, el numerador. **Nunca como texto de lectura, nunca en el logo** | 1,9:1 sobre papel |
| Grafito | `#5F5D58` | bajada de la portada del carrusel y metadatos, solo sobre papel | — |

**Cero rosado. En nada. Nunca.**

Dos rojos en una misma pieza y ninguno manda: si el numerador va en rojo, la línea va en
negro. (En v3 el numerador pasó a acero, justamente por la regla 2.)

## Tipografía

- Titulares: **Newsreader SemiBold (600)**, nunca otro peso. En Canva: Newsreader, estilo
  SemiNegrita.
- Cuerpo: **Public Sans** — 400 para leer, 700 para remarcar.
- Dos tipografías, nunca tres.

**Newsreader sustituye a Syne.** Cualquier pieza o plantilla en Syne es de la versión
anterior. Newsreader no viene en el kit: se descarga de
fonts.google.com/specimen/Newsreader.

## Las cinco reglas

1. Un solo elemento rojo por pieza.
2. El rojo nunca en texto pequeño.
3. El texto sobre foto solo va sobre degradado de contraste, nunca sobre la imagen limpia.
4. Dos tipografías, nunca tres.
5. Si dudas si algo sobra, sobra.

## Escala — en PUNTOS de Canva

El manual está escrito en unidades de Canva: letra en puntos, medidas en centímetros. El
número de la tabla es exactamente el que se escribe en el campo de tamaño de letra. **No se
convierte.**

| Nivel | Fuente | pt | Interlineado |
|---|---|---|---|
| Titular de portada de reel | Newsreader 600 | 32 | 1,16 |
| Titular de historia | Newsreader 600 | 20 | 1,18 |
| Titular de portada de carrusel | Newsreader 600 | 30 | 1,16 |
| Bajada de portada | Public Sans 400 | 18 | 1,45 · grafito |
| Numerador (02) | Newsreader 600 | 50 | acero · arriba izquierda |
| Titular de página interna | Newsreader 600 | 20 | 1,18 |
| Cuerpo | Public Sans 400 | 18 | 1,5 |
| Frase que remata | Public Sans 700 | 18 | 1,5 |
| Frase de cierre | Newsreader 600 | 24 | 1,18 · sobre negro |
| CTA | Public Sans 700 | 18 | 1,4 |
| Logo de pie | Newsreader 600 | 14 | abajo derecha |

El interlineado importa más que el tamaño. El 1,5 del cuerpo es lo que más cambia la
sensación de que algo se ve mal.

### Al producir fuera de Canva (HTML, SVG)

Los lienzos son de 96 dpi (1080 px = 28,6 cm), así que **1 pt = 1,333 px** y
**1 cm = 37,8 px**. Conversiones de la tabla: 32 pt = 43 px · 30 pt = 40 px ·
24 pt = 32 px · 20 pt = 27 px · 18 pt = 24 px · 50 pt = 67 px · 14 pt = 19 px.

Estos tamaños son pequeños en proporción al lienzo y el numerador es más grande que el
titular: es intencional en v3 (el número "grande y apagado" en acero). No los subas por tu
cuenta; si una pieza no se lee, dilo y propón el cambio.

## Zonas seguras (verificadas, septiembre 2026)

| Pieza | Lienzo | Se pierde | Útil |
|---|---|---|---|
| Portada de reel | 1080 × 1920 | 285 arriba · 320 abajo · 70 izq. · 130 der. | 880 × 1315 |
| Carrusel | 1080 × 1350 | 135 arriba y abajo · 60 a los lados | 960 × 1080 |
| Historia | 1080 × 1920 | 250 arriba y abajo; los lados libres | 1080 × 1420 |
| Destacada | 1080 × 1920 | círculo recortado que ocupa todo el ancho | cuadrado central 720 × 720 |

**La portada de reel NO se arma al tamaño del grid.** Se sube a 1080 × 1920 e Instagram
recorta el centro para el perfil. Armada a 1350 pierde el logo y la línea roja.

El degradado y las fotos sí llegan al borde del lienzo: esos no se recortan, se sangran.
El texto y el logotipo caben en el área útil sin tocar el borde.

Las guías `GUIA_zonas-*` se ponen de fondo al armar y **se borran al final**. No se publican.

## Plantillas

Las `OVERLAY` tienen fondo transparente: son capas. La foto va debajo y llega al borde; el
degradado se le monta encima. Una plantilla opaca no sirve: la foto la tapa entera.

**Las bandas ya no existen. Entró el degradado.**

- `REEL_degradado-abajo_OVERLAY_1080x1920` — velo negro que sube desde el borde inferior y
  se disuelve a media altura. Titular y logotipo anclados al borde inferior del área útil.
  Titular Newsreader SemiBold 27 pt, de tres a seis palabras; logotipo 7,4 cm de ancho.
- `REEL_degradado-arriba_OVERLAY` — el mismo velo invertido, para sujeto en la mitad de abajo.
- `CARRUSEL_degradado-abajo · arriba_OVERLAY_1080x1350` — los mismos dos velos para portada.
- `CARRUSEL_1-portada_FONDO` — portada de papel, cuando no hay foto que valga.
- `CARRUSEL_2-cuerpo_FONDO` — página de idea: número en acero, titular y bajada.
- `CARRUSEL_3-cierre_FONDO` — negro. Frase de cierre y logotipo al pie.
- `MARCA_esquina-clara · oscura_OVERLAY` — sustituye al cierre de marca en video.
- `CAPTURA_marco_OVERLAY` — ventana transparente para encuadrar capturas igual siempre.

Márgenes del carrusel: 1,6 cm por lado (≈60 px) y 3,6 cm arriba y abajo (≈135 px).

Al colocar el velo: estirarlo hasta que toque los dos lados y el borde. Pecar de grande,
nunca de chica. Al escalar todo se expande desde el centro, lo cercano al borde se sale.

**La portada del carrusel se apoya abajo**, anclada al borde inferior del área útil, igual
que el reel, para que las dos portadas se lean como la misma mano.

**El cierre negro es la única página negra** y no rota: aunque cambie la dirección visual,
se queda. Es lo que hace reconocible la pieza. Frase de cierre en Newsreader SemiBold 24 pt,
nunca en Public Sans.

**Las historias no llevan plantilla.** Un overlay sobre video obliga a exportar desde
CapCut o Canva: cinco minutos por historia, y a los tres días se deja de publicar. En
historias va el texto nativo de Instagram y el logotipo como sticker.

## Logo

Cuatro versiones sin fondo, en SVG y PNG: logo negro, logo blanco, monograma negro,
monograma blanco. Cada una en dos pesos de archivo (grande para impresión, ligero para
correo y chat). El monograma no lleva caja.

- Aire mínimo: la altura de la letra U por cada lado. El corte rojo es del ancho exacto de
  la palabra: nunca más largo, nunca más corto.
- Mínimos: digital 3,2 cm el logotipo, 1,1 cm el monograma. Impreso 2,5 cm y 1 cm.
  Por debajo de eso el corte se pierde: ahí va el monograma, nunca el logotipo completo.
- Línea de acento: 5,3 × 0,24 cm, y vive solo en las piezas de papel (cierre de carrusel,
  destacadas, media kit, propuesta). En portadas sobre foto **no va línea suelta**: el rojo
  entra dentro del logotipo. La banda de las destacadas es aparte, va en 1,6 cm.
- **Sobre foto**: el logotipo va en su versión de dos tintas (blanco o negro más el corte
  rojo) y **siempre sobre degradado de contraste**. Sin degradado no va logo. No existe una
  versión de una tinta: los cuatro archivos del kit llevan rojo.
- Usar SVG siempre que la herramienta lo acepte. El Kit de Marca de Canva rechaza SVG: ahí
  van los PNG grandes.
- Nunca: estirar, inclinar, cambiar el color de las letras, añadir sombra, poner el logo a
  color sobre foto.
- El avatar circular es para correo, papelería y plataformas que piden ícono.
  **La foto de perfil de Instagram es su cara, no el logo.**

## Destacadas

1080 × 1920, sin texto: el nombre lo pone Instagram.

| Archivo | Destacada |
|---|---|
| 01 negro arriba | MARCAS |
| 02 negro abajo | PODCAST |
| 03 negro entero | SANSA |
| 04 solo el corte | USTEDES |

Cuatro estados, no una progresión: Instagram las reordena por última actualización y no se
pueden fijar. La línea roja va centrada en las cuatro, entre 24,6 y 26,2 cm — es la
constante del juego. El arte se compone dentro del cuadrado central de 19,1 cm y los bordes
se extienden con el color de la orilla.

## Qué no hacer (cada uno costó una pieza rehecha)

- Armar la portada de reel al tamaño del grid.
- Convertir los tamaños de letra: los puntos del manual ya son los de Canva.
- Estirar una caja de texto por las esquinas o los lados: escala las letras y el número
  deja de corresponder.
- Poner la foto encima del OVERLAY. Va debajo.
- Publicar una pieza con la guía de zonas puesta.
- Usar overlays de historia sobre video.
- Exportar la pieza final desde el lienzo de plantillas: las fuentes no viajan.
- Aceptar las plantillas que Canva sugiere del podcast (micrófono y rosado).
- Dos elementos rojos en una pieza.
- Poner el logo a color sobre foto.
- Recuperar el diseño de destacadas con íconos.
- Rosado. En nada. Nunca.

---

# Se lo dices tú podcast (@selodicestupodcast)

Conversación entre Luciana (Lu) y Adriana sobre tener 40 y pico. Tres años al aire, 181+
episodios, episodio nuevo cada dos viernes. Audiencia: mujeres de 40 a 55, España, México y
Latinoamérica. Promesa: "No estás sola, y encima nos vamos a reír de esto."

Kit de Marca en Canva: brand kit `kAHUp7rPFQo` (PODCAST)
Sistema de portadas y stories: https://www.canva.com/d/69Fp6mFyNh0OasS

## Color (extraído de las piezas vigentes)

| Rol | Hex | Uso |
|---|---|---|
| Tinta | `#12090D` | fondo oscuro y texto sobre crema |
| Crema | `#FBEEF2` | bandas claras y texto sobre tinta |
| Rojo | `#E63455` | filetes, etiquetas, acento principal |
| Rosa | `#FF7AA2` | resalte dentro del titular, una palabra nada más |

Aquí el rosa **sí** va: es el lenguaje del podcast.

## Tipografía

**Figtree**, una sola familia en dos pesos: **800 (ultrabold)** para titulares y etiquetas,
**600 (semibold)** para pies y datos.

Es de Google Fonts. Para producir fuera de Canva, el archivo variable está en
fonts.google.com/specimen/Figtree; guárdalo como `assets/fonts/Figtree.ttf` y verifica
con `--fuentes "Figtree"` antes de entregar.

## Escala verificada (portadas y stories, 1080 × 1920, margen izquierdo 60)

| Elemento | Tamaño | Peso | Interlineado | Tracking | Color |
|---|---|---|---|---|---|
| Titular sobre foto | 104 | ultrabold | 0,96 | −0,035 | crema, una palabra en rosa |
| Titular sobre banda crema | 78 | ultrabold | 0,98 | −0,035 | tinta |
| Etiqueta ("Episodio 12") | 24 | semibold | 1,4 | +0,16 | rojo |
| Etiqueta sobre caja roja | 28 | ultrabold | 1,4 | +0,16 | crema |
| Pie ("Ya está en YouTube y Spotify") | 30 | semibold | 1,4 | +0,14 | crema, opacidad 0,9 |

- Banda crema de 380 px de alto con un filete rojo vertical de 26 px pegado al borde
  izquierdo. Ese filete es la firma del sistema.
- El resalte en rosa es **una palabra o dos**, nunca la frase entera.

## Formatos

Portada de episodio 3000 × 3000 · post 1080 × 1350 · story y clip 1080 × 1920 ·
miniatura YouTube 1280 × 720.

---

# Sansa Cosmetics

El usuario lleva la comunidad. **No hay manual de marca cargado aquí todavía.**

Antes de producir para Sansa, pide el kit de marca o los colores oficiales. Si no hay forma
de obtenerlos, dilo claramente y usa neutros, nunca inventes la paleta de una marca que
existe.

Criterio del rubro, que sí aplica: en cosmética manda el color real del producto. El fondo
no compite con él, y ningún overlay ni filtro puede alterar el tono del producto en la foto
— eso es engañoso y además genera devoluciones.

---

# Cómo agregar una marca

Copia la estructura de arriba. Mínimo indispensable: paleta con rol de cada color, dos
tipografías con pesos, escala tipográfica por pieza, zonas seguras y reglas del logo.
