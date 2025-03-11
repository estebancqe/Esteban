import reflex as rx
from Esteban.swiper.carousel_state import CarouselState

def carousel_container():
    return rx.vstack(
        rx.image(
            src=CarouselState.images[CarouselState.current_image],
            width="100%",
            height="auto",
        ),
        rx.hstack(
            rx.button(
                "Anterior",
                on_click=CarouselState.prev_image,
                color_scheme="gray",
            ),
            rx.button(
                "Siguiente",
                on_click=CarouselState.next_image,
                color_scheme="gray", 
            ),
            spacing="3",
            justify="end",
        ),
        width="100%",
        spacing="4",
    )