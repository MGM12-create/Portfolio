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
    ("Restaurante Luna", "luna.webp", "41zohzijkpnqaip",
     ("Iluminación comercial", "En la barra, la luz cálida revela la veta del nogal. En las mesas se vuelve más suave y, al fondo, pequeños acentos separan los cuadros del muro color ciruela. Tres formas de iluminar acompañan tres momentos de la visita."),
     ("Hospitality lighting", "Warm light brings out the walnut grain at the bar. Softer light settles over the tables, while small accents draw the artwork forward against the plum wall. Each layer suits a different moment of the visit.")),
    ("Casa M&M", "jardin.webp", "nnrv6c98b4fl7xy",
     ("Remodelación y paisajismo", "La remodelación empieza en el jardín. Un sendero entre árboles lleva a la terraza y, desde allí, a una sala donde el ratán, el yute y el lino dan textura a los tonos arena y marfil."),
     ("Renovation and landscape", "The renovation begins in the garden. A path between the trees leads to the terrace and into a living room where rattan, jute and linen give texture to a palette of sand and ivory.")),
    ("Casa Doré", "casa-dore.png", "pjuh55f2u64yrvx",
     ("Investigación y diseño residencial", "Proyecto de bachillerato que reinterpreta el art déco de los años veinte en una vivienda contemporánea. La selección de colores y materiales parte de ese referente y responde a criterios de confort y diseño bioclimático."),
     ("Residential design research", "A bachelor's degree project reinterpreting 1920s Art Deco for a contemporary home. The choice of colours and materials draws on the period while responding to comfort and bioclimatic design principles.")),
]
for lang in ["es", "en"]:
    es = lang == "es"

    def tr(spanish, english):
        return spanish if es else english

    title = tr("Diseñadora de interiores", "Interior designer")
    bio = tr(
        "Soy diseñadora de interiores egresada de la Universidad Latina de Costa Rica. "
        "Trabajo la distribución de espacios y la selección de materiales, acabados y mobiliario. "
        "Uso el modelado y el renderizado 3D para desarrollar y comunicar mis propuestas.",
        "I'm an interior designer and a graduate of Universidad Latina de Costa Rica. "
        "My work includes space planning and selecting materials, finishes and furniture. "
        "I use 3D modeling and rendering to develop and communicate my proposals.",
    )
    cards = []
    presentation = tr("Ver presentación", "View presentation")
    for name, img, short, spanish, english in projects:
        category, description = spanish if es else english
        url = "https://canva.link/" + short
        project_name = escape(name)
        cards.append(f"""
          <article class="project">
            <a class="project-image" href="{url}" aria-label="{presentation}: {project_name}">
              <img loading="lazy" src="img/{img}" alt="{project_name}">
            </a>
            <p class="project-category">{category}</p>
            <h3>{project_name}</h3>
            <p>{description}</p>
            <a class="project-link" href="{url}" aria-label="{presentation}: {project_name}">{presentation}</a>
          </article>""")

    cv_es = '<a class="button" href="cv/michelle-gonzalez-es.pdf" lang="es" hreflang="es">CV en español <span>PDF</span></a>'
    cv_en = '<a class="button" href="cv/michelle-gonzalez-en.pdf" lang="en" hreflang="en">English résumé <span>PDF</span></a>'
    cv_links = tr(cv_es + cv_en, cv_en + cv_es)
    contact_links = []
    if email:
        contact_links.append(f'<li><a href="mailto:{quote(email, safe="@")}">{escape(email)}</a></li>')
    if urlparse(links["linkedin"]).scheme == "https":
        contact_links.append(f'<li><a href="{escape(links["linkedin"], quote=True)}">LinkedIn</a></li>')
    contact = ""
    if contact_links:
        contact = f"""
        <div class="contact">
          <h3>{tr('Contacto', 'Contact')}</h3>
          <ul>{''.join(contact_links)}</ul>
        </div>"""
    github = ""
    if urlparse(links["github"]).scheme == "https":
        github = f'<a href="{escape(links["github"], quote=True)}">{tr("Código en GitHub", "Source on GitHub")}</a>'

    page = f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Michelle González | {title}</title>
  <meta name="description" content="{escape(bio, quote=True)}">
  <link rel="stylesheet" href="style.css">
</head>
<body id="top">
  <header class="site-header">
    <a class="brand" href="#top">Michelle González</a>
    <nav aria-label="{tr('Navegación principal', 'Main navigation')}">
      <a href="#projects">{tr('Proyectos', 'Projects')}</a>
      <a href="#profile">{tr('Perfil', 'Profile')}</a>
      <a href="#cv">{tr('CV y contacto', 'Résumé &amp; contact')}</a>
      <a class="language" lang="{tr('en', 'es')}" hreflang="{tr('en', 'es')}" href="{tr('en.html', 'index.html')}">{tr('English', 'Español')}</a>
    </nav>
  </header>
  <main>
    <section class="hero">
      <div>
        <p class="profession">{title}</p>
        <h1>Michelle<br>González</h1>
        <p class="location">Alajuela, Costa Rica</p>
        <p class="hero-intro">{tr('Proyectos de vivienda, paisaje e iluminación con atención a los materiales y a cómo se recorre cada espacio.', 'Residential, landscape and lighting projects shaped by materials and how people move through each space.')}</p>
        <a class="button primary" href="#projects">{tr('Ver proyectos', 'Explore projects')}</a>
      </div>
      <figure>
        <img src="img/portada-dormitorio.png" width="1570" height="880" alt="{tr('Dormitorio con iluminación cálida y una terraza visible a través de los ventanales', 'Warmly lit bedroom with a terrace visible through floor-to-ceiling windows')}">
      </figure>
    </section>
    <section class="projects" id="projects">
      <h2>{tr('Proyectos seleccionados', 'Selected projects')}</h2>
      <div class="project-grid">{''.join(cards)}
      </div>
    </section>
    <section class="profile" id="profile">
      <div class="profile-intro">
        <h2>{tr('Sobre mí', 'About me')}</h2>
        <div>
          <p class="bio">{bio}</p>
        </div>
      </div>
      <div class="profile-details">
        <div>
          <h3>{tr('Formación e idiomas', 'Education and languages')}</h3>
          <dl>
            <dt>{tr('Diseño y Decoración de Interiores', 'Interior Design and Decoration')}</dt>
            <dd>Universidad Latina de Costa Rica · 2021–2026</dd>
            <dt>{tr('Idiomas', 'Languages')}</dt>
            <dd>{tr('Español nativo · Inglés avanzado', 'Native Spanish · Advanced English')}</dd>
          </dl>
        </div>
        <div>
          <h3>{tr('Herramientas', 'Software')}</h3>
          <dl>
            <dt>{tr('Diseño y modelado', 'Design and modeling')}</dt>
            <dd>SketchUp · AutoCAD · Autodesk</dd>
            <dt>{tr('Renderizado', 'Rendering')}</dt>
            <dd>Twinmotion · D5 Render</dd>
            <dt>{tr('Diseño gráfico', 'Graphic design')}</dt>
            <dd>Adobe InDesign · Adobe Illustrator</dd>
          </dl>
        </div>
      </div>
    </section>
    <section class="cv" id="cv">
      <div>
        <h2>{tr('Currículum', 'Résumé')}</h2>
        <div class="cv-links">{cv_links}</div>
      </div>{contact}
    </section>
  </main>
  <footer class="site-footer">
    {github}
  </footer>
</body>
</html>
"""
    (PUBLIC / tr("index.html", "en.html")).write_text(page, encoding="utf-8")
