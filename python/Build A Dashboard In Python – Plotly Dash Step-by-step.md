parent: [[Dash]]
tags:
aliases: 
Reference: [[Python MOC]]

---
# Build A Dashboard In Python – Plotly Dash Step-by-Step Tutorial

Property: December 22, 2020 8:40 PM
URL: https://www.statworx.com/de/blog/how-to-build-a-dashboard-in-python-plotly-dash-step-by-step-tutorial/

![Build%20A%20Dashboard%20In%20Python%20%E2%80%93%20Plotly%20Dash%20Step-by-%201fa729b03d8841249f8eeacce4be817d/dash-app-title.png](dash-app-title.png)

From my experience here at [STATWORX](https://www.statworx.com/), the best way to learn something is by trying it out yourself – with a little help from a friend! In this article, I will focus on giving you a hands-on guide on how to build a dashboard in Python. As framework, we will be using Dash, and the goal is to create a basic dashboard with a dropdown and two reactive graphs:

![Build%20A%20Dashboard%20In%20Python%20%E2%80%93%20Plotly%20Dash%20Step-by-%201fa729b03d8841249f8eeacce4be817d/dash-app-final-2048x994.png](dash-app-final-2048x994.png)

Developed as an open-source library by Plotly, the Python framework Dash is built on top of Flask, Plotly.js, and React.js. Dash allows the building of interactive web applications in pure Python and is particularly suited for sharing insights gained from data.

In case you’re interested in interactive charting with Python, I highly recommend my colleague Markus‘ blog post [Plotly – An Interactive Charting Library](https://www.statworx.com/blog/plotly-an-interactive-charting-library/). For a general guide about basic visualization techniques, check out this great article by my colleague Vivian on [Basic rules for good looking slides and dashboards](https://www.statworx.com/blog/basic-rules-for-good-looking-slides-and-dashboards/).

For our purposes, a basic understanding of HTML and CSS can be helpful. Nevertheless, I will provide you with external resources and explain every step thoroughly, so you’ll be able to follow the guide.

### Guide structure

- [Getting Started – How to start a Dash app](https://www.statworx.com/de/blog/how-to-build-a-dashboard-in-python-plotly-dash-step-by-step-tutorial/)
- [Creating a Dropdown Menu](https://www.statworx.com/de/blog/how-to-build-a-dashboard-in-python-plotly-dash-step-by-step-tutorial/)
- [Conclusion](https://www.statworx.com/de/blog/how-to-build-a-dashboard-in-python-plotly-dash-step-by-step-tutorial/)

The source code can be found on [GitHub](https://github.com/STATWORX/blog/tree/master/DashApp).

## Prerequisites

The project comprises a style sheet called `style.css`, sample stock data `stockdata2.csv` and the actual Dash application `app.py`

### Load the Stylesheet

If you want your dashboard to look like the one above, please download the file [style.css](https://github.com/STATWORX/blog/blob/master/DashApp/assets/style.css) from our STATWORX GitHub. That is completely optional and won’t affect the functionalities of your app. Our stylesheet is a customized version of the stylesheet used by the [Dash Uber Rides Demo](https://github.com/plotly/dash-sample-apps/tree/master/apps/dash-uber-rides-demo). Dash will automatically load any .css-file placed in a folder named `assets`.

```
dashapp
    |--assets
        |-- style.css
    |--data
        |-- stockdata2.csv
    |-- app.py
```

The documentation on external resources in dash can be found [here](https://dash.plot.ly/external-resources).

### Load the Data

Feel free to use the same data we did ([stockdata2.csv](https://github.com/STATWORX/blog/blob/master/DashApp/data/stockdata2.csv)), or any pick any data with the following structure:

```
import pandas as pd

# Load data
df = pd.read_csv('data/stockdata2.csv', index_col=0, parse_dates=True)
df.index = pd.to_datetime(df['Date'])
```

## Getting Started – How to start a Dash app

After installing Dash (instructions can be found [here](https://dash.plot.ly/installation)), we are ready to start with the application. The following statements will load the necessary packages `dash` and `dash_html_components`. Without any layout defined, the app won’t start. An empty `html.Div` will suffice to get the app up and running.

```
import dash
import dash_html_components as html
```

If you have already worked with the [WSGI](https://wsgi.readthedocs.io/en/latest/) web application framework [Flask](https://palletsprojects.com/p/flask/), the next step will be very familiar to you, as Dash uses Flask under the hood.

```
# Initialise the app
app = dash.Dash(__name__)

# Define the app
app.layout = html.Div()
# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
```

### How a .css-files changes the layout of an app

The module `dash_html_components` provides you with several html components, also [check out the documentation](https://dash.plot.ly/dash-html-components).

Worth to mention is that the nesting of components is done via the `children` attribute.

```
app.layout = html.Div(children=[
                      html.Div(className='row',  # Define the row element
                               children=[
                                  html.Div(className='four columns div-user-controls'),  # Define the left element
                                  html.Div(className='eight columns div-for-charts bg-grey')  # Define the right element
                                  ])
                                ])
```

The first `html.Div()` has one child. Another `html.Div` named `row`, which will contain all our content. The children of `row` are `four columns div-user-controls` and `eight columns div-for-charts bg-grey`.

The style for these `div` components come from our `style.css`.

Now let’s first add some more information to our app, such as a title and a description. For that, we use the Dash Components `H2` to render a headline and `P` to generate html paragraphs.

```
children = [
    html.H2('Dash - STOCK PRICES'),
    html.P('''Visualising time series with Plotly - Dash'''),
    html.P('''Pick one or more stocks from the dropdown below.''')
]
```

Switch to your terminal and run the app with `python app.py`.

### The basics of an app’s layout

Another nice feature of Flask (and hence Dash) is [hot-reloading](https://dash.plot.ly/devtools). It makes it possible to update our app on the fly without having to restart the app every time we make a change to our code.

Running our app with `debug=True` also adds a button to the bottom right of our app, which lets us take a look at error messages, as well a `Callback Graph`. We will come back to the `Callback Graph` in the last section of the article when we’re done implementing the functionalities of the app.

## Charting in Dash – How to display a Plotly-Figure

With the building blocks for our web app in place, we can now define a plotly-graph. The function `dcc.Graph()` from `dash_core_components` uses the same `figure` argument as the plotly package. Dash translates every aspect of a plotly chart to a corresponding key-value pair, which will be used by the underlying JavaScript library *Plotly.js*.

In the following section, we will need the express version of `plotly.py`, as well as the Package *Dash Core Components*. Both packages are available with the installation of *Dash*.

```
import dash_core_components as dcc
import plotly.express as px
```

[Dash Core Components](https://dash.plot.ly/dash-core-components) has a collection of useful and easy-to-use components, which add interactivity and functionalities to your dashboard.

[Plotly Express](https://plot.ly/python-api-reference/plotly.express.html) is the express-version of `plotly.py`, which simplifies the creation of a plotly-graph, with the drawback of having fewer functionalities.

To draw a plot on the right side of our app, add a `dcc.Graph()` as a child to the `html.Div()` named `eight columns div-for-charts bg-grey`. The component `dcc.Graph()` is used to render any plotly-powered visualization. In this case, it’s `figure` will be created by `px.line()` from the Python package `plotly.express`. As the express version of Plotly has limited native configurations, we are going to change the layout of our `figure` with the method `update_layout()`. Here, we use `rgba(0, 0, 0, 0)` to set the background transparent. Without updating the default background- and paper color, we would have a big white box in the middle of our app. As `dcc.Graph()` only renders the figure in the app; we can’t change its appearance once it’s created.

```
dcc.Graph(id='timeseries',
          config={'displayModeBar': False},
          animate=True,
          figure=px.line(df,
                         x='Date',
                         y='value',
                         color='stock',
                         template='plotly_dark').update_layout(
                                   {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                                    'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
                                    )
```

After Dash reload the application, you will end up in something like that: A dashboard with a plotted graph:

## Creating a Dropdown Menu

Another core component is `dcc.dropdown()`, which is used – you’ve guessed it – to create a dropdown menu. The available options in the dropdown menu are either given as arguments or supplied by a function.
 For our dropdown menu, we need a function that returns a list of dictionaries. The list contains dictionaries with two keys, `label` and `value`. These dictionaries provide the available options to the dropdown menu. The value of `label` is displayed in our app. The value of `value` will be exposed for other functions to use, and should not be changed.
 If you prefer the full name of a company to be displayed instead of the short name, you can do so by changing the value of the key `label` to `Microsoft`. For the sake of simplicity, we will use the same value for the keys `label` and `value`.

Add the following function to your script, before defining the app’s layout.

```
# Creates a list of dictionaries, which have the keys 'label' and 'value'.
def get_options(list_stocks):
    dict_list = []
    for i in list_stocks:
        dict_list.append({'label': i, 'value': i})

    return dict_list
```

With a function that returns the names of stocks in our data in key-value pairs, we can now add `dcc.Dropdown()` from the *Dash Core Components* to our app. Add a `html.Div()` as child to the list of children of `four columns div-user-controls`, with the argument `className=div-for-dropdown`. This `html.Div()` has one child, `dcc.Dropdown()`.

We want to be able to select multiple stocks at the same time and a selected default value, so our figure is not empty on startup. Set the argument `multi=True` and chose a default stock for `value`.

```
 html.Div(className='div-for-dropdown',
          children=[
              dcc.Dropdown(id='stockselector',
                           options=get_options(df['stock'].unique()),
                           multi=True,
                           value=[df['stock'].sort_values()[0]],
                           style={'backgroundColor': '#1E1E1E'},
                           className='stockselector')
                    ],
          style={'color': '#1E1E1E'})
```

The `id` and `options` arguments in `dcc.Dropdown()` will be important in the next section. Every other argument can be changed. If you want to try out different styles for the dropdown menu, follow the [link](https://dash.plot.ly/dash-core-components/dropdown) for a list of different dropdown menus.

## Working with Callbacks

### How to add interactive functionalities to your app

Callbacks add interactivity to your app. They can take inputs, for example, certain stocks selected via a dropdown menu, pass these inputs to a function and pass the return value of the function to another component. We will write a function that returns a figure based on provided stock names. A callback will pass the selected values from the dropdown to the function and return the figure to a `dcc.Grapph()` in our app.

At this point, the selected values in the dropdown menu do not change the stocks displayed in our graph. For that to happen, we need to implement a callback. The callback will handle the communication between our dropdown menu `'stockselector'` and our graph `'timeseries'`. We can delete the `figure` we have previously created, as we won’t need it anymore.

We want two graphs in our app, so we will add another `dcc.Graph()` with a different `id`.

- Remove the `figure` argument from `dcc.Graph(id='timeseries')`
- Add another `dcc.Graph()` with `className='change'` as child to the `html.Div()` named `eight columns div-for-charts bg-grey`.

```
dcc.Graph(id='timeseries', config={'displayModeBar': False})
dcc.Graph(id='change', config={'displayModeBar': False})
```

Callbacks add interactivity to your app. They can take Inputs from components, for example certain stocks selected via a dropdown menu, pass these inputs to a function and pass the returned values from the function back to components.

In our implementation, a callback will be triggered when a user selects a stock. The callback uses the value of the selected items in the dropdown menu (Input) and passes these values to our functions `update_timeseries()` and `update_change()`. The functions will filter the data based on the passed inputs and return a plotly figure from the filtered data. The callback then passes the figure returned from our functions back to the component specified in the output.

A callback is implemented as a decorator for a function. Multiple inputs and outputs are possible, but for now, we will start with a single input and a single output. We need the class `dash.dependencies.Input` and `dash.dependencies.Output`.

Add the following line to your import statements.

```
from dash.dependencies import Input, Output
```

`Input()` and `Output()` take the id of a component (e.g. in `dcc.Graph(id='timeseries')` the components id is `'timeseries'`) and the property of a component as arguments.

Example Callback:

```
# Update Time Series
@app.callback(Output('id of output component', 'property of output component'),
              [Input('id of input component', 'property of input component')])
def arbitrary_function(value_of_first_input):
    '''
    The property of the input component is passed to the function as value_of_first_input.
    The functions return value is passed to the property of the output component.
    '''
    return arbitrary_output
```

If we want our `stockselector` to display a time series for one or more specific stocks, we need a function. The `value` of our input is a list of stocks selected from the dropdown menu `stockselector`.

### Implementing Callbacks

The function draws the traces of a plotly-figure based on the stocks which were passed as arguments and returns a `figure` that can be used by `dcc.Graph()`. The inputs for our function are given in the order in which they were set in the callback. Names chosen for the function’s arguments do not impact the way values are assigned.

Update the figure `time series`:

```
@app.callback(Output('timeseries', 'figure'),
              [Input('stockselector', 'value')])
def update_timeseries(selected_dropdown_value):
    ''' Draw traces of the feature 'value' based one the currently selected stocks '''
    # STEP 1
    trace = []  
    df_sub = df
    # STEP 2
    # Draw and append traces for each stock
    for stock in selected_dropdown_value:   
        trace.append(go.Scatter(x=df_sub[df_sub['stock'] == stock].index,
                                 y=df_sub[df_sub['stock'] == stock]['value'],
                                 mode='lines',
                                 opacity=0.7,
                                 name=stock,
                                 textposition='bottom center'))  
    # STEP 3
    traces = [trace]
    data = [val for sublist in traces for val in sublist]
    # Define Figure
    # STEP 4
    figure = {'data': data,
              'layout': go.Layout(
                  colorway=["#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'],
                  template='plotly_dark',
                  paper_bgcolor='rgba(0, 0, 0, 0)',
                  plot_bgcolor='rgba(0, 0, 0, 0)',
                  margin={'b': 15},
                  hovermode='x',
                  autosize=True,
                  title={'text': 'Stock Prices', 'font': {'color': 'white'}, 'x': 0.5},
                  xaxis={'range': [df_sub.index.min(), df_sub.index.max()]},
              ),

              }

    return figure
```

### STEP 1

- A `trace` will be drawn for each stock. Create an empty `list` for each trace from the plotly figure.

### STEP 2

Within the for-loop, a trace for a plotly figure will be drawn with the function `go.Scatter()`.

- Iterate over the stocks currently selected in our dropdown menu, draw a trace, and append that trace to our list from step 1.

### STEP 3

- Flatten the traces

### STEP 4

Plotly figures are dictionaries with the keys `data` and `layout`. The value of `data` is our flattened list with the traces we have drawn. The `layout` is defined with the plotly class go.Layout().

- Add the trace to our figure
- Define the layout of our figure

Now we simply repeat the steps above for our second graph. Just change the data for our y-Axis to `change` and slightly adjust the layout.

Update the figure `change`:

```
@app.callback(Output('change', 'figure'),
              [Input('stockselector', 'value')])
def update_change(selected_dropdown_value):
    ''' Draw traces of the feature 'change' based one the currently selected stocks '''
    trace = []
    df_sub = df
    # Draw and append traces for each stock
    for stock in selected_dropdown_value:
        trace.append(go.Scatter(x=df_sub[df_sub['stock'] == stock].index,
                                 y=df_sub[df_sub['stock'] == stock]['change'],
                                 mode='lines',
                                 opacity=0.7,
                                 name=stock,
                                 textposition='bottom center'))
    traces = [trace]
    data = [val for sublist in traces for val in sublist]
    # Define Figure
    figure = {'data': data,
              'layout': go.Layout(
                  colorway=["#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'],
                  template='plotly_dark',
                  paper_bgcolor='rgba(0, 0, 0, 0)',
                  plot_bgcolor='rgba(0, 0, 0, 0)',
                  margin={'t': 50},
                  height=250,
                  hovermode='x',
                  autosize=True,
                  title={'text': 'Daily Change', 'font': {'color': 'white'}, 'x': 0.5},
                  xaxis={'showticklabels': False, 'range': [df_sub.index.min(), df_sub.index.max()]},
              ),
              }

    return figure
```

Run your app again. You are now able to select one or more stocks from the dropdown. For each selected item, a line plot will be generated in the graph. By default, the dropdown menu has search functionalities, which makes the selection out of many available options an easy task.

### Visualize Callbacks – Callback Graph

With the callbacks in place and our app completed, let’s take a quick look at our callback graph. If you are running your app with `debug=True`, a button will appear in the bottom right corner of the app. Here we have access to a callback graph, which is a visual representation of the callbacks which we have implemented in our code. The graph shows that our components `timeseries` and `change` display a `figure` based on the value of the component `stockselector`.
 If your callbacks don’t work how you expect them to, especially when working on larger and more complex apps, this tool will come in handy.

## Conclusion

Let’s recap the most important building blocks of Dash. Getting the App up and running requires just a couple lines of code. A basic understanding of HTML and CSS is enough to create a simple Dash dashboard. You don’t have to worry about creating interactive charts, Plotly already does that for you. Making your dashboard reactive is done via Callbacks, which are functions with the users‘ interaction as the input.

If you liked this blog, feel free to contact me via [LinkedIn](https://www.linkedin.com/in/alexander-blaufuss) or [Email](mailto:alexander.blaufuss@statworx.com). I am curious to know what you think and always happy to answer any questions about data, my journey to data science, or the exciting things we do here at [STATWORX](https://www.statworx.com/).

Thank you for reading!

STATWORX
is a consulting company for data science, statistics, machine learning and artificial intelligence located in Frankfurt, Zurich and Vienna. Sign up for our NEWSLETTER and receive reads and treats from the world of data science and AI. If you have questions or suggestions, please write us an e-mail addressed to blog(at)statworx.com.