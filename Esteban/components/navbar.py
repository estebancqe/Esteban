import reflex as rx
import Esteban.style.style as styles
from Esteban.routes import Route
from Esteban.style.style import Size
from Esteban.style.style import Color


def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.box(
                rx.text("esteban", as_="span", color=Color.PRIMARY.value),
                rx.text("developer", as_="span", color=Color.SECONDARY.value),
                style=styles.navbar_title_style
            ),
            href=Route.INDEX.value
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )