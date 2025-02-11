### Task 5: Build a Dashboard with Flask and Dash
#### Creating a Fraud Detection Dashboard

import dash
import dash_core_components as dcc
import dash_html_components as html
from flask import Flask

server = Flask(__name__)
app = dash.Dash(__name__, server=server)

app.layout = html.Div([
    html.H1("Fraud Detection Dashboard"),
    dcc.Graph(id='fraud-trend')
])

if __name__ == '__main__':
    app.run_server(debug=True)