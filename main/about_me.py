import reflex as rx
from rxconfig import config
from .modulos import sidebar_bottom_profile


def about_me() -> rx.Component:
    """Página About Me."""
    return rx.box(
        rx.center(
            rx.vstack(
                sidebar_bottom_profile(),
                rx.heading("About Me Page", size="3xl", color="white"),
                rx.text(
                    "Hello! I am Arnaldo, a professional in data analysis, system design, and development.",
                    size="lg",
                    color="gray.200",
                    text_align="center",
                ),
            ),
            padding="2em",
        ),
        min_height="100vh",
        background="linear-gradient(to bottom, #002266, #001122)",
    )


