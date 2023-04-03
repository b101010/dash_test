import dash
from dash import Dash, dcc, html, Input, Output

from django_plotly_dash import DjangoDash

app = DjangoDash('SimpleExample')   # replaces dash.Dash

app.layout = html.Div([
    dcc.RadioItems(
        id='dropdown-color',
        options=[{'label': c, 'value': c.lower()} for c in ['Red', 'Green', 'Blue']],
        value='red'
    ),
    html.Div(id='output-color'),
    dcc.RadioItems(
        id='dropdown-size',
        options=[{'label': i,
                  'value': j} for i, j in [('L','large'), ('M','medium'), ('S','small')]],
        value='medium'
    ),
    html.Div(id='output-size')

])

@app.callback(
    dash.dependencies.Output('output-color', 'children'),
    [dash.dependencies.Input('dropdown-color', 'value')])
def callback_color(dropdown_value):
    return "The selected color is %s." % dropdown_value

@app.callback(
    dash.dependencies.Output('output-size', 'children'),
    [dash.dependencies.Input('dropdown-color', 'value'),
     dash.dependencies.Input('dropdown-size', 'value')])
def callback_size(dropdown_color, dropdown_size):
    return "The chosen T-shirt is a %s %s one." %(dropdown_size, dropdown_color)

##############################################################################################

app1 = DjangoDash('AnotherSimpleExample')

app1.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='initial value', type='text')
    ]),
    html.Br(),
    html.Div(id='my-output'),

])


@app1.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    return f'Output: {input_value}'

##############################################################################################


app2 = DjangoDash('FormExample')

app2.layout = html.Div(children=[
    html.H1('Contact Form'),
    dcc.Input(
        placeholder='Enter your name',
        type='text',
        value=''
    ),
    dcc.Input(
        placeholder='Enter your email',
        type='email',
        value=''
    ),
    dcc.Textarea(
        placeholder='Enter your message',
        value=''
    ),
    html.Button('Submit', id='submit-button', n_clicks=0)
])