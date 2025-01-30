import reflex as rx
import Esteban.constants as const
import Esteban.style.style as styles
from Esteban.pages.index import index
from Esteban.pages.courses import courses
from Esteban.pages.cotizar import cotizar
# from Esteban.api.api import repo, live, featured,api_Muebles,api_Modelos

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    head_components=[
        rx.script(
            src=f"https://www.googletagmanager.com/gtag/js?id={const.G_TAG}"),
        rx.script(
            f"""
window.dataLayer = window.dataLayer || [];
function gtag(){{dataLayer.push(arguments);}}
gtag('js', new Date());
gtag('config', '{const.G_TAG}');
"""
        ),
    ],
)
# app.add_page(index),
# app.api.add_api_route("/repo", repo)
# app.api.add_api_route("/live/{user}", live)
# app.api.add_api_route("/featured", featured)
# app.api.add_api_route("/api_Muebles",api_Muebles)
# app.api.add_api_route("/api_Modelos",api_Modelos)