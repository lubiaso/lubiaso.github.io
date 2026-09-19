# Fuentes de marca

Pon aquí los `.ttf` del kit para que las piezas se rendericen con la tipografía correcta
sin depender de internet. El render las busca con estos nombres exactos:

- `Syne-ExtraBold.ttf`
- `PublicSans-Regular.ttf`
- `PublicSans-Bold.ttf`

Vienen en la carpeta `04_tipografias/` de `KIT_MARCA_LUBIASO_Filo.zip`. También sirven si
están instaladas en el sistema: la plantilla las busca primero ahí con `local()`.

No se suben a este repositorio por licencia y peso; van en tu máquina.

Para comprobar que cargaron:

```bash
python3 ../render.py pieza.html salida.png 1080 1350 --fuentes "Syne,Public Sans"
```

Si dice `NO CARGÓ`, la pieza sale con otra tipografía aunque se vea bien. No la entregues.
