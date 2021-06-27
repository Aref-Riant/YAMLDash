import dash

from yamldash.layout import layout
from yamldash.layout import theme

app = dash.Dash(
    __name__,
    external_stylesheets=[
        theme,
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css",
    ],
)

app.title = "YAMLDash - Interactive YAML Validation"

app.layout = layout

from yamldash import callbacks  # noqa: E402, F401


def run_debug():
    app.run_server(debug=True)


def run():
    app.run_server()
