# Fuentes de marca

Pon aquí los `.ttf` del kit para que las piezas se rendericen con la tipografía correcta
sin depender de internet. El render las busca con estos nombres exactos:

- `Newsreader-SemiBold.ttf`
- `PublicSans-Regular.ttf`
- `PublicSans-Bold.ttf`

Public Sans viene en el kit. **Newsreader NO viene en el kit**: se descarga de
fonts.google.com/specimen/Newsreader (sustituyó a Syne en la versión 3 del manual).
También sirven instaladas en el sistema: la plantilla las busca primero ahí con `local()`.

No se suben a este repositorio por licencia y peso; van en tu máquina.

Para comprobar que cargaron:

```bash
python3 ../render.py pieza.html salida.png 1080 1350 --fuentes "Newsreader,Public Sans"
```

Si dice `NO CARGÓ`, la pieza sale con otra tipografía aunque se vea bien. No la entregues.
