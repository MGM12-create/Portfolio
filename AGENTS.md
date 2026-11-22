# Portafolio de Michelle González

## Objetivo
Portafolio bilingüe (español e inglés) de interiorismo que presenta tres proyectos de Michelle y permite consultar sus presentaciones y dos currículos. El destino del código es https://github.com/MGM12-create/Portfolio. La publicación en Cloudflare Pages corresponde a una etapa posterior.

## Perfil y fuentes
- Restaurante Luna: diseño de iluminación comercial. La barra de nogal, la luz suave sobre las mesas y la iluminación de acento de los cuadros explican la intención del proyecto. https://canva.link/41zohzijkpnqaip
- Casa M&M: remodelación residencial y paisajismo. El estilo boho combina ratán, yute, lino y tonos claros. La presentación contiene la distribución original y la propuesta amueblada. https://canva.link/nnrv6c98b4fl7xy
- Casa Doré: proyecto académico que reinterpreta el art déco de los años veinte en una vivienda contemporánea. https://canva.link/pjuh55f2u64yrvx
- Herramientas confirmadas por Michelle: SketchUp, Twinmotion, AutoCAD, D5 Render, Adobe Illustrator, Adobe InDesign y Autodesk Revit. Los niveles de dominio y la asignación de programas a proyectos concretos están por confirmar.
- GaZeLa28/Portafolio sirvió como referencia de estructura. Mantener el perfil, los enlaces y la trayectoria de Michelle diferenciados de los del autor de esa referencia.
- Escribir en un tono natural y profesional. Mantener el contenido equivalente en ambos idiomas y evitar la raya larga.

## Cómo trabajar
El sitio entregado es estático. Los textos y la plantilla están en build.py y las direcciones configurables en links.json. Tras modificar cualquiera de esos dos archivos, ejecutar python build.py con Python 3 (python3 en macOS/Linux si corresponde). Mantener en Git los HTML generados. El CSS, las imágenes y los PDF están en public/. Para la vista local ejecutar python -m http.server 8000 --directory public y abrir http://localhost:8000. El sitio ya generado también abre desde public/index.html.

## Estado del portafolio
El sitio contiene las dos páginas, tres fichas con fuentes Canva, un perfil bilingüe actualizado con los CV ATS de Michelle, herramientas, imágenes locales y los dos PDF originales en public/cv. El LinkedIn confirmado, el correo de contacto y el enlace al repositorio se configuran en links.json. Los próximos cambios se versionan en este mismo repositorio.

## Siguiente sesión
1. Comprobar en una ventana privada si las tres presentaciones de Canva abren con acceso de lectura para visitantes.
2. Conectar el repositorio a Cloudflare Pages cuando Michelle decida publicar. El directorio de salida es public.
