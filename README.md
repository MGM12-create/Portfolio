# Michelle González | Portafolio de interiorismo

Soy Michelle González, diseñadora de interiores egresada de la Universidad Latina de Costa Rica. Trabajo en la distribución de espacios y en la selección de materiales, acabados y mobiliario. Utilizo el modelado y la visualización 3D para estudiar cómo se ve una propuesta desde distintos puntos de la habitación y comunicar las decisiones de diseño.

Este repositorio contiene mi portafolio en español e inglés. Reúne tres proyectos que muestran distintas facetas de mi trabajo, desde la iluminación de un restaurante hasta la relación entre una vivienda y su jardín.

[CV en español (PDF)](public/cv/michelle-gonzalez-es.pdf) · [English résumé (PDF)](public/cv/michelle-gonzalez-en.pdf) · [LinkedIn](https://www.linkedin.com/in/michelle-gonzalez-1055b81a6) · [Correo de contacto](mailto:michi.gonzalez00@gmail.com)

## Proyectos seleccionados

### Restaurante Luna | Iluminación comercial

¿Cómo puede una mesa sentirse íntima en un salón lleno? En Luna, la barra de nogal recibe a los comensales con una luz cálida que revela la veta de la madera. Sobre las mesas, la iluminación se suaviza para favorecer la conversación. Al fondo del salón, la luz de acento destaca los cuadros contra los nichos de color ciruela. [Ver presentación de Restaurante Luna](https://canva.link/41zohzijkpnqaip)

### Casa M&M | Remodelación residencial y paisajismo

La propuesta aborda la vivienda y el jardín como un mismo recorrido. El sendero conduce a la terraza y los ventanales prolongan esa relación hacia la sala. El ratán, el yute y el lino aportan distintas texturas a una paleta clara de inspiración boho. La presentación incluye la distribución original y la propuesta amueblada para apreciar los cambios. [Ver presentación de Casa M&M](https://canva.link/nnrv6c98b4fl7xy)

### Casa Doré | Investigación y diseño residencial

Mi proyecto de bachillerato explora qué elementos del art déco de los años veinte tienen sentido en una vivienda contemporánea. La investigación sobre su paleta y sus materiales orienta la propuesta interior, junto con criterios de confort y diseño bioclimático. [Ver presentación de Casa Doré](https://canva.link/pjuh55f2u64yrvx)

## Herramientas e idiomas

| Área | Herramientas con las que he trabajado |
| --- | --- |
| Dibujo y modelado | AutoCAD, SketchUp y Autodesk Revit |
| Visualización arquitectónica | Twinmotion y D5 Render |
| Diseño gráfico y editorial | Adobe Illustrator y Adobe InDesign |

Español nativo e inglés avanzado.

## Cómo funciona el sitio

El portafolio es un sitio estático en HTML y CSS. Un script de Python genera las dos versiones a partir de una plantilla compartida. Cada ficha abre la presentación original en Canva. Las imágenes de portada y los PDF se sirven desde el propio repositorio.

| Archivo o carpeta | Contenido |
| --- | --- |
| `build.py` | Plantilla, biografía, proyectos, enlaces de Canva y textos en ambos idiomas. |
| `links.json` | Correo, perfil de LinkedIn y enlace al repositorio. |
| `public/index.html` y `public/en.html` | Páginas generadas en español e inglés. |
| `public/style.css` | Tipografía, colores y distribución de la página. |
| `public/img/` y `public/cv/` | Imágenes de los proyectos y currículos en PDF. |
| `AGENTS.md` | Contexto del proyecto e indicaciones para trabajar con Codex. |

### Vista previa local

Desde la raíz del repositorio, con Python 3 instalado, ejecutá:

```bash
python3 -m http.server 8000 --bind 127.0.0.1 --directory public
```

Abrí [la vista previa local](http://127.0.0.1:8000) y usá el selector de idioma para revisar ambas versiones.

### Actualización y publicación

- **Textos o enlaces.** Editá `build.py` o `links.json`, ejecutá `python3 build.py` e incluí las dos páginas generadas en el mismo commit.
- **Presentaciones.** Los cambios guardados en el diseño original de Canva se ven desde el enlace existente. Si reemplazás una presentación por otra, actualizá su enlace en `build.py`. Para cambiar la imagen que aparece en la web, actualizá también el recurso de `public/img/`.
- **Currículos.** Para actualizar una descarga, sustituí el PDF del idioma correspondiente en `public/cv/` conservando su nombre.
- **Cloudflare Pages.** El directorio de publicación es `public`. Si los HTML generados ya están en Git, el comando de compilación puede quedar vacío.
