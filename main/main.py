import reflex as rx
import asyncio
from rxconfig import config
from .modulos import sidebar_bottom_profile
from .modulos import top_banner_gradient
from .modulos import top_banner_signup

# ---------------------------
# -- EFECTO TYPE WRITTING. --
# ---------------------------
class State(rx.State):
    """The main application state."""
    pass
   

# Con más de 24 años de experiencia en el Banco ICBC, he desempeñado roles tanto en el área administrativa como en el comercial, específicamente como oficial de negocios retail. Durante mi tiempo en administración, adquirí habilidades significativas en la preparación de informes utilizando SQL, contribuyendo así a la eficiencia operativa y la toma de decisiones informadas.

# Me gradué como Licenciado en Administración de Empresas por la Universidad de Buenos Aires, donde consolidé mi comprensión de estrategias empresariales y gestión eficaz de recursos. Me caracterizo por ser una persona proactiva, orientada a resultados y con un alto nivel de empatía hacia mis compañeros de equipo.

# Mi enfoque meticuloso y pensante me ha permitido enfrentar desafíos complejos con soluciones innovadoras, siempre buscando optimizar procesos y mejorar la experiencia del cliente. Estoy entusiasmado por explorar nuevas oportunidades donde pueda aplicar mi experiencia y contribuir al éxito de proyectos empresariales ambiciosos.

def index() -> rx.Component:
    """Componente principal que renderiza la vista principal de la app."""
    return rx.box(
        rx.hstack(
            sidebar_bottom_profile(),
            rx.container(
                rx.color_mode.button(position="top-right"),
                rx.vstack(
                    rx.heading("Data scientist & Data analyst.", size="6"),
                    rx.image(
                        src="https://github.com/arnaldoquinones/portfolio/blob/master/assets/foto_perfil.png?raw=true",
                        width="150px",
                        height="auto",
                        border_radius="50%",
                        alt="Foto de perfil",
                    ),
                    top_banner_gradient(),
                    top_banner_signup(),
                    rx.link(
                        rx.button("Go to my GitHub!", border_radius="20px"),
                        href="https://github.com/arnaldoquinones",
                        is_external=True,
                    ),
                    rx.link(
                        rx.button("Go to my Linkedin!", border_radius="20px"),
                        href="https://www.linkedin.com/in/apquinones/",
                        is_external=True,
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
app.add_page(index)  # Agregar la página principal
