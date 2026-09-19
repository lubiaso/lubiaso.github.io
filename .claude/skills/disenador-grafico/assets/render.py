#!/usr/bin/env python3
"""Renderiza una pieza HTML a PNG y verifica que las fuentes de marca cargaron.

Uso:  python3 render.py pieza.html salida.png [ancho] [alto] [--fuentes "Syne,Public Sans"]

Por qué existe la verificación: document.fonts.check() devuelve True aunque la
fuente no haya cargado, porque responde sobre el fallback. La única prueba fiable
es medir el ancho de un texto con la fuente declarada y compararlo con un
fallback genérico: si miden igual, la fuente NO cargó y la pieza sale con la
tipografía equivocada. Eso rompe la marca sin que se note a simple vista.
"""
import sys, pathlib
from playwright.sync_api import sync_playwright

SONDA = """
(familia) => {
  const medir = (f) => {
    const s = document.createElement('span');
    s.textContent = 'ABCDEFGHIJ abcdefghij 0123456789';
    s.style.cssText = 'position:absolute;visibility:hidden;white-space:nowrap;'
                    + 'font-size:120px;font-weight:800;font-family:' + f;
    document.body.appendChild(s);
    const w = s.getBoundingClientRect().width;
    s.remove();
    return w;
  };
  // Se mide la MISMA familia con dos fallbacks de métricas distintas.
  // Si carga, manda ella y ambos anchos coinciden. Si no carga, cada medición
  // cae en su fallback y los anchos difieren. No se compara contra un ancho
  // "de referencia": eso daba falso negativo cuando la fuente de marca es
  // monoespaciada y coincide con el fallback monospace.
  const conMono  = medir(`"${familia}", monospace`);
  const conSerif = medir(`"${familia}", serif`);
  return { cargada: Math.abs(conMono - conSerif) < 0.5, ancho: conMono };
}
"""

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    familias = []
    if "--fuentes" in sys.argv:
        familias = [f.strip() for f in sys.argv[sys.argv.index("--fuentes") + 1].split(",")]

    entrada = args[0] if args else "pieza.html"
    salida  = args[1] if len(args) > 1 else "pieza.png"
    ancho   = int(args[2]) if len(args) > 2 else 1080
    alto    = int(args[3]) if len(args) > 3 else 1350

    ruta = pathlib.Path(entrada).resolve()
    if not ruta.exists():
        sys.exit(f"No existe: {ruta}")

    with sync_playwright() as p:
        try:
            nav = p.chromium.launch()
        except Exception:
            nav = p.chromium.launch(
                executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
                args=["--no-sandbox"])
        pg = nav.new_page(viewport={"width": ancho, "height": alto}, device_scale_factor=1)
        fallos = []
        pg.on("requestfailed", lambda r: fallos.append(r.url))
        pg.goto(ruta.as_uri())
        try:
            pg.evaluate("document.fonts.ready")
        except Exception:
            pass
        pg.wait_for_timeout(2500)

        problemas = []
        for f in familias:
            r = pg.evaluate(SONDA, f)
            estado = "OK" if r["cargada"] else "NO CARGÓ"
            print(f"  fuente {f!r}: {estado}")
            if not r["cargada"]:
                problemas.append(f)

        destino = pg.locator(".pieza")
        (destino if destino.count() else pg).screenshot(path=salida)
        nav.close()

    print(f"Renderizado: {salida}")
    if fallos:
        print("Peticiones fallidas:")
        for u in dict.fromkeys(fallos):
            print("  -", u[:110])
    if problemas:
        print("\n*** NO ENTREGAR ESTA PIEZA COMO FINAL ***")
        print("Fuentes de marca que no cargaron:", ", ".join(problemas))
        print("Arreglo: pon los .ttf en assets/fonts/ y usa @font-face con ruta local,")
        print("o produce la pieza en Canva, donde las fuentes de marca sí están.")
        sys.exit(1)

if __name__ == "__main__":
    main()
