import reflex as rx
from rxconfig import config
from .modulos import sidebar_bottom_profile


def skills() -> rx.Component:
    """Página About Me."""
    return rx.box(
        rx.center(
            rx.vstack(
                sidebar_bottom_profile(),
                rx.heading("Skills Page", size="3xl", color="white"),
                rx.text(
                    "Let me show you my skills.",
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