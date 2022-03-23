from dash import Dash, dcc, html, Input, Output, callback_context
import os


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server



app.layout = html.Div([
    html.Button('Next Question', id='btn-question', n_clicks=0),
    html.H2('Hello World'),
    html.Div(id='display-value')
])

@app.callback(
    Output('display-value', 'children'),
    [Input('btn-question', 'n_clicks')]
    )
def display_value(btn_q):
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]
    if 'btn-clicks-1' in changed_id:
        msg = 'Button 1 was most recently clicked'
    return f'You have selected {btn_q}'

if __name__ == '__main__':
    app.run_server(debug=True)