import reflex as rx
from rxconfig import config
from .modulos import sidebar_bottom_profile, form_example
from .about_me import about
from .skills import skills
from .proyects import proyects

class State(rx.State):
    """The main application state."""
    pass


def index() -> rx.Component:
    """Componente principal que renderiza la vista principal de la app."""
    return rx.box(
        rx.hstack(
            sidebar_bottom_profile(),
            rx.container(
                rx.vstack(
                    rx.heading(
                        rx.fragment(
                            rx.text("Data scientist"), 
                            rx.text("& Data analyst"),
                        ),
                        size="6"
                    ),
                    rx.image(
                        src="https://github.com/arnaldoquinones/portfolio/blob/master/assets/foto_perfil.png?raw=true",
                        width="150px",
                        height="auto",
                        border_radius="50%",
                        alt="Foto de perfil",
                    ),
                    rx.text(
                        """ "...Scientia est potentia..." """,
                        font_size="2em",
                        font_style="italic",
                        text_align="center",
                        color="white",
                    ),  # Texto añadido aquí
                    rx.flex(
                        rx.text(
                            """ Con más de 24 años de experiencia en el ambito bancario financiero, he desempeñado roles tanto en el área administrativa como en el comercial, específicamente como oficial de cuentas y negocios. Durante mi tiempo en el area administrativa adquirí habilidades significativas en la preparación de informes empleando herramientas de BDD, contribuyendo así a la eficiencia operativa y la toma de decisiones informadas."""
                        ),
                        justify="center",
                        align="center",
                        height="200px",
                        width="400px",
                        text_align="justify",
                    ),
                    rx.hstack(
                        rx.link(
                            rx.button("GitHub", border_radius="20px", width="120px"),
                            href="https://github.com/arnaldoquinones",
                            is_external=True,
                        ),
                        rx.link(
                            rx.button("Linkedin", border_radius="20px", width="120px"),
                            href="https://www.linkedin.com/in/apquinones/",
                            is_external=True,
                        ),
                        rx.button(
                            "Messages",
                            border_radius="20px",
                            width="120px",
                            # on_click=lambda: State.set_show_popup(True),  # Abre el modal
                        ),
                        spacing="4",
                        align="center",
                    ),
                    spacing="5",
                    justify="center",
                ),
                padding="1em",
                flex="1",
            ),
        ),
        min_height="100vh",
        width="100vw",
        background="linear-gradient(to bottom, #000066, #000000)",
        overflow_y="auto",
    )



app = rx.App()

# ---------------------------
# -- ENLACES A LAS PAGINAS --
# ---------------------------
def main_page() -> rx.Component:
    return rx.box(
        rx.link("About Me", href="./about_me"),
        rx.link("Skills", href="./skills"),
        rx.link("Projects", href="./proyects"),
        rx.text("Welcome to my Portfolio", size="3xl", font_weight="bold"),
        spacing="4",
        align="center",
        justify="center",
        height="100vh",
        bg="teal.100",
    )

# Add routes for the main page and subpages.
app.add_page(main_page)
app.add_page(about)
app.add_page(skills)
app.add_page(proyects)

app.add_page(index)  # Agregar la página principal.
