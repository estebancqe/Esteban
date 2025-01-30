import reflex as rx
import Esteban.utils as utils
import Esteban.style.style as styles
from Esteban.routes import Route
from Esteban.components.navbar import navbar
from Esteban.components.footer import footer
from Esteban.views.header import header
from Esteban.views.courses_links import courses_links
from Esteban.views.sponsors import sponsors
from Esteban.style.style import Size
# from Esteban.state.PageState import PageState


@rx.page(
    route=Route.COURSES.value,
    title=utils.courses_title,
    description=utils.courses_description,
    image=utils.preview,
    meta=utils.courses_meta
)
def courses() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(False),
                courses_links(),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )