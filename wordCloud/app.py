# https://stackoverflow.com/questions/58907867/how-to-show-wordcloud-image-on-dash-web-application

import dash
import dash.dependencies as dd
import dash_core_components as dcc
import dash_html_components as html

from io import BytesIO

import pandas as pd
from wordcloud import WordCloud
import base64

import connpass_api

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__) #, external_stylesheets=external_stylesheets)

# dfm = pd.DataFrame({'word': ['apple', 'pear', 'orange'], 'freq': [1,3,9]})

app.layout = html.Div([
	html.H1(children='あなたのワードクラウド見てみたい'),
	html.Hr(),
	html.Div([
		html.H4(
			children='connpass nick name：',
			style={'display':'inline-block'},
		),
		dcc.Input(
			id = 'id_input',
		    placeholder='Enter nick name ',
		    type='text',
		    value='',
		    debounce=True,
		    autoFocus=True,
		    style={'display':'inline-block','font-size':'large'},
		),
	]),
	html.Div([
		dcc.Loading(id="id_loading",
			children=[
	    			html.Img(id="image_wc"),
	    	],
	    	type="default",
	    )
	],style={"padding":"10px"})
])

def plot_wordcloud(data):
    d = {a: x for a, x in data.values}
    wc = WordCloud(background_color='black', width=640, height=480, font_path="./ipag.ttf")
    wc.fit_words(d)
    return wc.to_image()

@app.callback(
	dd.Output('image_wc', 'src'),
	[dd.Input('id_input', 'value')],
)
def make_image(nick_name):
    img = BytesIO()
    dfm = pd.DataFrame(connpass_api.get_dict(nick_name))
    plot_wordcloud(data=dfm).save(img, format='PNG')
    return 'data:image/png;base64,{}'.format(base64.b64encode(img.getvalue()).decode())

if __name__ == '__main__':
    app.run_server(host='localhost', debug=True)