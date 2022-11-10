import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.Img(
        src='figs\\transmisiontower.jpg',
        style={'width': '30%', 'border': '2px solid blue'},
        alt='image'),

    html.H1(children='Torres de transmsión', style={'color': 'orange'}),
    html.P('transmisión de energía eléctrica', style={'color': 'orange', 'border': '2px solid blue'})
])

if __name__ == '__main__':
    app.run_server(debug=True)