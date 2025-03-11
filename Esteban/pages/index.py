import reflex as rx
import Esteban.utils as utils
import Esteban.style.style as styles
from Esteban.components.navbar import navbar
from Esteban.components.footer import footer
from Esteban.views.header import header
from Esteban.views.index_links import index_links
from Esteban.views.sponsors import sponsors
from Esteban.style.style import Size
from Esteban.components.link_button import link_button
from Esteban.routes import Route
from Esteban.style.style import Color
# from Esteban.state.PageState import PageState


@rx.page(
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.index_meta,
    
)
def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                link_button(
                    "Swiper",
                    "Carrusel de Imágenes",
                    "/icons/book-solid.svg",
                    Route.PRUEBA.value,
                    False,
                    Color.CONTENT.value
                ),
                header(),
                index_links(   
                ),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )