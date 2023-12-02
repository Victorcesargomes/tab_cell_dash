import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd


# import from folders
from app import app
from components import sidebar, loja2, loja3





# ===== Reading n cleaning File ====== #
df = pd.read_csv("tabcell_loja22.csv",sep=";", decimal=",",encoding="ISO-8859-1")

# To dict - para salvar no dcc.store
df_store = df.to_dict()


# =========  Layout  =========== #
app.layout = dbc.Container([
    # Store e Location 
    dcc.Location(id="url"),
     dcc.Store(id='data', data=df_store),

     dbc.Row([
         dbc.Col([
             sidebar.layout
         ], md=2, style={'padding': '0px'}),

         dbc.Col([
             dbc.Container(id="page-content", fluid=True, style={'height': '100%', 'width': '100%', 'padding-left': '14px'})
         ], md=10, style={'padding': '0px'})
     ])
    

   
    

], fluid=True)



# ======= Callbacks ======== #
# URL callback to update page content
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/" or pathname == "/loja2":
        return loja2.layout

    if pathname == "/loja3":
        return loja3.layout
        




if __name__ == '__main__':
    app.run_server(debug=True)
