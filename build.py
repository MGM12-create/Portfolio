"""Generate the Spanish and English portfolio pages from project content."""
from pathlib import Path
from html import escape
from urllib.parse import quote, urlparse
import json
import subprocess

ROOT = Path(__file__).resolve().parent
PUBLIC = ROOT / "public"
links = json.loads((ROOT / "links.json").read_text())
email = links.get("email", "").strip()
if not links["github"]:
    origin = subprocess.run(["git", "config", "--get", "remote.origin.url"], cwd=ROOT,
                            capture_output=True, text=True).stdout.strip()
    origin = origin.replace("git@github.com:", "https://github.com/").removesuffix(".git")
    if urlparse(origin).hostname == "github.com" and origin.lower() != "https://github.com/gazela28/portafolio":
        links["github"] = origin

projects = [
    ("Restaurante Luna", "luna", "41zohzijkpnqaip",
     ("Iluminación comercial", "En la barra, la luz cálida revela la veta del nogal. En las mesas se vuelve más suave y, al fondo, pequeños acentos separan los cuadros del muro color ciruela. Tres formas de iluminar acompañan tres momentos de la visita."),
     ("Hospitality lighting", "Warm light brings out the walnut grain at the bar. Softer light settles over the tables, while small accents draw the artwork forward against the plum wall. Each layer suits a different moment of the visit.")),
    ("Casa M&M", "jardin", "nnrv6c98b4fl7xy",
     ("Remodelación y paisajismo", "La remodelación empieza en el jardín. Un sendero entre árboles lleva a la terraza y, desde allí, a una sala donde el ratán, el yute y el lino dan textura a los tonos arena y marfil."),
     ("Renovation and landscape", "The renovation begins in the garden. A path between the trees leads to the terrace and into a living room where rattan, jute and linen give texture to a palette of sand and ivory.")),
    ("Casa Doré", "dore", "pjuh55f2u64yrvx",
     ("Investigación y diseño residencial", "Proyecto de bachillerato que reinterpreta el art déco de los años veinte en una vivienda contemporánea. La selección de colores y materiales parte de ese referente y responde a criterios de confort y diseño bioclimático."),
     ("Residential design research", "A bachelor's degree project reinterpreting 1920s Art Deco for a contemporary home. The choice of colours and materials draws on the period while responding to comfort and bioclimatic design principles.")),
]
for lang in ["es", "en"]:
    es = lang == "es"
    def tr(spanish, english):
        return spanish if es else english
    title = tr("Diseño de interiores", "Interior design")
    bio = tr("Mi trabajo en interiorismo parte de observar cómo se vive un espacio. En Casa M&M, el recorrido desde el jardín orientó la remodelación. En Restaurante Luna, estudié cómo cambia una conversación según la luz que llega a la mesa. En Casa Doré, llevé esa mirada a la investigación del art déco y su relación con la vivienda contemporánea.",
             "My interior design work starts with how people use a space. At Casa M&M, the route from the garden shaped the renovation. At Restaurante Luna, I explored how light at the table can change the mood of a conversation. Casa Doré brought that interest into my research on Art Deco and contemporary living.")
    work = tr("Proyectos", "Projects")
    about = tr("Perfil", "Profile")
    terms = tr("Interiorismo residencial · Diseño de iluminación · Paisajismo · Remodelación · Materiales y texturas · Art déco", "Residential interiors · Lighting design · Landscape design · Renovation · Materials and textures · Art Deco")
    software = ["SketchUp", "Twinmotion", "AutoCAD", "D5 Render", "Adobe Illustrator", "Adobe InDesign", "Autodesk Revit"]
    cards = []
    sources = []
    for name, img, short, spanish, english in projects:
        category, description = spanish if es else english
        url = "https://canva.link/" + short
        cards.append(f'<article><a href="{url}" aria-label="{escape(name)}"><img loading="lazy" src="img/{img}.webp" alt="{escape(name)}"></a><small>{category}</small><h3>{escape(name)}</h3><p>{description}</p><a class="under" href="{url}">{tr("Ver presentación","View presentation")}</a></article>')
        sources.append(f'<li>González, Michelle. <a href="{url}"><i>{escape(name)}</i></a>. {category}. Canva.</li>')
    resources = ['<a href="cv/michelle-gonzalez-es.pdf">CV · Español (PDF)</a>', '<a href="cv/michelle-gonzalez-en.pdf">CV · English (PDF)</a>']
    if email:
        resources.append(f'<a href="mailto:{quote(email, safe="@")}">{escape(email)}</a>')
    for key,label in [('linkedin','LinkedIn'),('github',tr('Código en GitHub','Source on GitHub'))]:
        if urlparse(links[key]).scheme == "https":
            resources.append(f'<a href="{escape(links[key],quote=True)}">{label}</a>')
    page = f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Michelle González | {title}</title><meta name="description" content="{escape(bio)}"><meta name="keywords" content="{terms.replace(' · ', ', ')}, {', '.join(software)}"><link rel="stylesheet" href="style.css"></head>
<body><header><a class="brand" href="#top">Michelle González</a><nav aria-label="{tr('Navegación','Navigation')}"><a href="#projects">{work}</a><a href="#profile">{about}</a><a href="#cv">CV</a><a lang="{tr('en','es')}" href="{tr('en.html','index.html')}">{tr('English','Español')}</a></nav></header>
<main id="top"><section class="hero"><div><small>{title}</small><h1>Michelle<br>González</h1><p>{tr('Proyectos de vivienda, paisaje e iluminación.','Projects in residential interiors, landscape and lighting.')}</p><a class="under" href="#projects">{tr('Explorar proyectos','Explore projects')}</a></div><img src="img/sala.webp" alt="{tr('Sala de Casa M&amp;M con ventanales y mobiliario de fibras naturales','Casa M&amp;M living room with tall windows and woven furniture')}"></section>
<section id="projects"><h2>{tr('Proyectos seleccionados','Selected projects')}</h2><div class="grid">{''.join(cards)}</div></section>
<section class="profile" id="profile"><div><small>{about}</small><h2>{tr('Sobre mí','About me')}</h2></div><div><p>{bio}</p><p class="terms">{terms}</p><h3>{tr("Herramientas","Software")}</h3><p class="terms">{" · ".join(software)}</p></div></section>
<section id="cv"><h2>{tr('Currículum y enlaces','Résumé and links')}</h2><div class="resources">{''.join(resources)}</div></section>
<footer><details><summary>{tr('Fuentes del portafolio','Portfolio references')}</summary><ul>{''.join(sources)}</ul></details><span>Michelle González</span></footer></main></body></html>"""
    (PUBLIC / tr("index.html", "en.html")).write_text(page, encoding="utf-8")
