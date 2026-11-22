# Michelle González | Portafolio de interiorismo

Sitio bilingüe y estático. Abrí esta carpeta en VS Code. Para revisarlo en tu computadora, ejecutá `python3 -m http.server 8000 --bind 127.0.0.1 --directory public` y abrí http://127.0.0.1:8000. También podés abrir public/index.html directamente.

## Edición con Codex
Los textos en español e inglés, las palabras clave, las referencias y los proyectos están en build.py. El diseño está en public/style.css. Después de editar el contenido o links.json, ejecutá `python build.py`. Los archivos generados ya están incluidos.

## Enlaces y documentos
En links.json se configuran el perfil de LinkedIn, el correo de contacto y el repositorio. Usá direcciones https completas para linkedin y github, y una dirección de correo para email. Si github queda vacío, el generador intenta usar el remoto origin de GitHub. Los enlaces sin destino se ocultan. Los PDF de public/cv son versiones resumidas preparadas a partir del CV bilingüe de Michelle y sus proyectos. Podés sustituirlos conservando los nombres.

## Publicación en Cloudflare Pages
Para desplegar desde GitHub, conectá este repositorio a Pages. El directorio de salida es public. Como el HTML generado se incluye en Git, podés dejar vacío el comando de compilación si ejecutás build.py antes de cada commit. Para publicar de forma manual, cargá solo el contenido web de public mediante Direct Upload. Elegí el método al crear el proyecto de Pages.

## Referencia del diseño
https://github.com/GaZeLa28/Portafolio sirvió como referencia de estructura: navegación por secciones, perfil bilingüe, proyectos y currículum. La implementación es independiente y el contenido corresponde a Michelle González.
