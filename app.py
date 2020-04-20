# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


markdown_text = '''
# Data upload utility

### Please upload your csv file, below
Please start your data upload from ... date
'''

app.layout = html.Div(children=[
    dcc.Markdown(children=markdown_text),
html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF'],
        multi=True
    ),
    dcc.Upload(html.Button('Upload File')),

    html.Hr(),
    dcc.Markdown(children="""### Trying out input and output"""),
    dcc.Input(id='my-id', value='initial value', type='text'),
    html.Div(id='my-div'),
    dcc.Markdown(children="""### Trying out import csv"""),
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-data-upload'),

])

@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)

@app.callback(Output('output-data-upload', 'children'),
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename'),
               State('upload-data', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    # output = len(list_of_contents)
    if list_of_contents == False:
        output = 0
    else:
        output = len(list_of_contents)
    # if list_of_contents is not None:
    #     children = [
    #         parse_contents(c, n, d) for c, n, d in
    #         zip(list_of_contents, list_of_names, list_of_dates)]
    return "{} files have been uploaded".format(output)


if __name__ == '__main__':
    app.run_server(debug=True)