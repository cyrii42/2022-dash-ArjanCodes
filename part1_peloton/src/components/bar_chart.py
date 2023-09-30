import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from . import ids
from . import peloton_pivots

PELOTON_DATA = peloton_pivots.get_year_table()


def render(app: Dash) -> html.Div:
    @app.callback(
        Output(ids.BAR_CHART, "children"),
        [
            Input(ids.YEAR_DROPDOWN, "value"),
        ],
    )
    def update_bar_chart(nations: list[str]) -> html.Div:
        # filtered_data = PELOTON_DATA.query("nation in @nations")
        filtered_data = PELOTON_DATA

        if filtered_data.shape[0] == 0:
            return html.Div("No data selected.", id=ids.BAR_CHART)

        fig = px.bar(filtered_data, x="duration_min", y="calories", color="title", text="title")

        return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)

    return html.Div(id=ids.BAR_CHART)
