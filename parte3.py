
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv('data\\auto-mpg.csv')

app = dash.Dash(__name__)

fig = px.scatter(df, x="displ", y="weight",
                    log_x=True, size_max=55, trendline="ols")

app.layout = html.Div(children=[
    html.H1("Displacement vs Weight"),
    html.Img(
        src='figs\\maverick.png',
        style = {'width': '35%'}),
    dcc.Graph(
        figure=fig
    )
])
    

if __name__ == '__main__':
    app.run_server(debug=True)
    