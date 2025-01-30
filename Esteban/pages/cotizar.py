import reflex as rx
import Esteban.utils as utils
import Esteban.style.style as styles
from Esteban.routes import Route
from Esteban.components.navbar import navbar
from Esteban.components.footer import footer
from Esteban.views.header import header
from Esteban.views.cotizar_links import cotizar_links
from Esteban.views.sponsors import sponsors
from Esteban.style.style import Size
# from Esteban.state.PageState import PageState


@rx.page(
    route=Route.COTIZAR.value,
    title=utils.courses_title,
    description=utils.courses_description,
    image=utils.preview,
    meta=utils.courses_meta,
    # on_load=[PageState.muebles_links,PageState.modelo_links]
)
def cotizar() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(False),
                cotizar_links(
                    # PageState.mueble_info,
                    # PageState.modelo_info,
                    
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