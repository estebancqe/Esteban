import reflex as rx
import Esteban.utils as utils
import Esteban.style.style as styles
from Esteban.components.navbar import navbar
from Esteban.components.footer import footer
from Esteban.views.header import header
from Esteban.views.index_links import index_links
from Esteban.views.sponsors import sponsors
from Esteban.style.style import Size
from Esteban.swiper.carousel_container import carousel_container
from Esteban.swiper.swiper import swiper_component
from Esteban.swiper.state_swiper import SwiperState
from Esteban.swiper.carrusel_tailwind import carrusel_tailwind


@rx.page(
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.index_meta,
    
)
def prueba() -> rx.Component:
    return rx.box(
        rx.script(
            src="https://unpkg.com/swiper/swiper-bundle.min.css",
            type="text/css"
        ),
        rx.script(
            src="https://unpkg.com/swiper/swiper-bundle.min.js",
            on_ready=SwiperState.init_swiper,  # Asegúrate de definir SwiperState si es necesario
        ),
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                rx.vstack(
                    rx.heading("Carrusel de Imágenes"),
                    carrusel_tailwind(), 
                    carousel_container(),
                    rx.text("GALERÍA"),
                        rx.grid(
                            swiper_component(),
                            width="100%",
                            margin_y="4"
                        ),
                    align="center",
                    width="100%",
                    spacing="4",
                    padding="4",
                ),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )