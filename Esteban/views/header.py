import reflex as rx
import datetime
import Esteban.constants as const
from Esteban.style.style import Size,Spacing
from Esteban.style.colors import Color, TextColor
from Esteban.components.link_icon import link_icon
from Esteban.components.info_text import info_text
from Esteban.components.link_button import link_button
# from Esteban.state.PageState import PageState


def header(details=True) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            
            rx.avatar(
                    name="Esteban Quiña",
                    size=Spacing.MEDIUM_BIG.value,
                    src="/creyenteLogo.jpg",
                    radius="full",
                    color=TextColor.BODY.value,
                    bg=Color.CONTENT.value,
                    padding="2px",
                    border=f"4px solid {Color.PRIMARY.value}"
                ),
            rx.vstack(
                rx.heading(
                    "ESTEBAN QUIÑA",
                    size=Spacing.BIG.value
                ),
                rx.text(
                    "Paginas web y aplicaciones",
                    margin_top=Size.ZERO.value,
                    color=Color.PRIMARY.value
                ),
                rx.hstack(
                    link_icon(
                        "/icons/instagram.svg",
                        const.INSTAGRAM,
                        "email@email.com"
                    ),
                    link_icon(
                        "/icons/facebook.svg",
                        const.FACEBOOK,
                        "facebook"
                    ),
                    link_icon(
                        "/icons/book-solid.svg",
                        const.CATALOGO,
                        "catalogo"
                    ),
                    link_icon(
                        "/icons/whatsapp.svg",
                        const.WHATSAPP,
                        "whatssap"
                    ),
                    spacing=Spacing.LARGE.value,
                    padding_top=Size.SMALL.value,
                ),
                spacing=Spacing.ZERO.value,
                align_items="start",
            ),
            align="end",
            spacing=Spacing.DEFAULT.value,
        ),      
        rx.cond(  
            details,
            rx.vstack(
                rx.flex(
                    info_text(
                        f"{experience()}+",
                        "años de experiencia"
                    ),
                    rx.spacer(),#crea un espacio ficticio entre texto
                    info_text(
                        "ateción","al detalle"
                    ),
                    rx.spacer(), 
                    info_text(
                        "trabajo","certificado"
                    ),
                    width="100%",
                ),
                rx.text(
                    f"""
                    Bienvenido a nuestro sitio especializado en trabajos en madera y melamina. Desde muebles a medida hasta soluciones de almacenamiento, fusionamos la tradición con la innovación para crear piezas únicas que realzan cualquier espacio. ¡Explore nuestro portafolio y dé vida a sus proyectos con nosotros!""",
                    font_size=Size.DEFAULT.value,
                    color=TextColor.BODY.value
                ),
                width="100%",  
                spacing=Spacing.BIG.value,
                
            )            
        ),  
        width="100%",
        spacing=Spacing.BIG.value,                     #espacion entre las 2 secciones
        align_items="start", #alinear todo al inicio
        # on_mount=PageState.check_live
        
    )
    
def experience() -> int:
    return datetime.date.today().year - 2020
    