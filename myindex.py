import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Estilos
estilos = ["https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css", dbc.themes.LUX]
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.4/dbc.min.css"

# Configuração do aplicativo Dash
app = dash.Dash(__name__, external_stylesheets=estilos + [dbc_css])

app.config['suppress_callback_exceptions'] = True
app.scripts.config.serve_locally = True
server = app.server


# ========= Styles ========= #
card_style={'height': '100%',  'margin-bottom': '12px'}
tab_card = {'height': '100%'}

main_config = {
    "hovermode": "x unified",
    "legend": {"yanchor":"top", 
                "y":0.9, 
                "xanchor":"left",
                "x":0.1,
                "title": {"text": None},
                "font" :{"color":"white"},
                "bgcolor": "rgba(0,0,0,0.5)"},
    "margin": {"l":10, "r":10, "t":10, "b":10}
}

config_graph={"displayModeBar": False, "showTips": False}


# ===== Reading n cleaning File loja2 ====== #
df = pd.read_csv("tabcell_loja22.csv",sep=";", decimal=",",encoding="ISO-8859-1")

df_lucro = pd.read_csv("tabcell_loja2_lucro.csv", sep=";", decimal=",")

# To dict - para salvar no dcc.store
df_store = df.to_dict()

df_logi = df_lucro.to_dict()


# ===== Reading n cleaning File loja3 ====== #
df = pd.read_csv("tabcell_loja3.csv", sep=";", decimal=",")

df_lucro3 = pd.read_csv("tabcell_loja3_lucro.csv", sep=";", decimal=",")

# To dict - para salvar no dcc.store
df_st = df.to_dict()

df_lg = df_lucro3.to_dict()



# Layout da barra lateral
sidebar_layout = dbc.Container([
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H1("TAB CELL",  style={'color': 'yellow'})
            ])
        ]),
        dbc.Row([
            dbc.Col([
                html.H5("By VW CONTABILIDADE", style={'color': 'white'})
            ])
        ])
    ], style={'padding-top': '50px', 'margin-bottom': '100px'}, className='text-center'),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            dbc.Nav([
                dbc.NavItem(dbc.NavLink([html.I(className='fa fa-home dbc'), "\tLOJA 2"], href="/loja2", active=True, style={'text-align': 'left'})),
                html.Br(),
                dbc.NavItem(dbc.NavLink([html.I(className='fa fa-home dbc'), "\tLOJA 3"], href="/loja3", active=True, style={'text-align': 'left'})),
                html.Br(),
            ], vertical="lg", pills=True, fill=True)
        ])
    ]),
], style={'height': '100vh', 'padding': '0px', 'position':'sticky', 'top': 0, 'background-color': '#232423'})


# Conteúdo da loja2
loja2_layout = dbc.Container([
    dcc.Store(id='dataset', data=df_store),
    dcc.Store(id='datas', data=df_logi),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row(
                        dbc.Col(
                            html.Legend("Faturamento por dia", className="text-center")
                        )
                    ),
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id='graph1', className='dbc card_padrao', config=config_graph)
                        ]),
                    ])
                ])
            ], style=tab_card)
        ], sm=12, lg=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row(
                        dbc.Col(
                            html.Legend("Faturamento por Serviço", className="text-center")
                        )
                    ),
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id='graph2', className='dbc card_padrao', config=config_graph)
                        ]),
                    ])
                ])
            ], style=tab_card)
        ], sm=12, md=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row(
                        dbc.Col(
                            html.Legend("Faturamento por Smartphone", className="text-center")
                        )
                    ),
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id='graph3', className='dbc card_padrao', config=config_graph)
                        ]),
                    ])
                ])
            ], style=tab_card)
        ], sm=12, md=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row(
                        dbc.Col(
                            html.Legend("Custo do Serviço Prestado", className="text-center")
                        )
                    ),
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id='graph4', className='dbc card_padrao', config=config_graph)
                        ]),
                    ])
                ])
            ], style=tab_card)
        ], sm=12, md=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row(
                        dbc.Col(
                            html.Legend("Lucro por Dia", className="text-center")
                        )
                    ),
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id='graph5', className='dbc card_padrao', config=config_graph)
                        ]),
                    ])
                ])
            ], style=tab_card)
        ], sm=12, md=8),
    ], className='g-2 my-auto', style={'margin-top': '7px'})
])

# Conteúdo da loja3
loja3_layout = dbc.Container([
    dcc.Store(id='dataset', data=df_st),
    dcc.Store(id='datas', data=df_lg),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row(
                        dbc.Col(
                            html.Legend("Faturamento por dia", className="text-center")
                        )
                    ),
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id='graph6', className='dbc card_padrao', config=config_graph)
                        ]),
                    ])
                ])
            ], style=tab_card)
        ], sm=12, lg=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row(
                        dbc.Col(
                            html.Legend("Faturamento por Serviço", className="text-center")
                        )
                    ),
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id='graph7', className='dbc card_padrao', config=config_graph)
                        ]),
                    ])
                ])
            ], style=tab_card)
        ], sm=12, md=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row(
                        dbc.Col(
                            html.Legend("Faturamento por Smartphone", className="text-center")
                        )
                    ),
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id='graph8', className='dbc card_padrao', config=config_graph)
                        ]),
                    ])
                ])
            ], style=tab_card)
        ], sm=12, md=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row(
                        dbc.Col(
                            html.Legend("Custo do Serviço Prestado", className="text-center")
                        )
                    ),
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id='graph9', className='dbc card_padrao', config=config_graph)
                        ]),
                    ])
                ])
            ], style=tab_card)
        ], sm=12, md=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row(
                        dbc.Col(
                            html.Legend("Lucro por Dia", className="text-center")
                        )
                    ),
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id='graph10', className='dbc card_padrao', config=config_graph)
                        ], sm=12, lg=12),
                    ])
                ])
            ], style=tab_card)
        ], sm=12, md=8),
    ], className='g-2 my-auto', style={'margin-top': '7px'})
])


# Layout principal
app.layout = dbc.Container([
    dcc.Location(id="url"),
    dcc.Store(id='data', data=df_store),
    
    dbc.Row([
        dbc.Col([
            sidebar_layout
        ], md=2, style={'padding': '0px'}),

        dbc.Col([
            dbc.Container(id="page-content", fluid=True, style={'height': '100%', 'width': '100%', 'padding-left': '14px'})
        ], md=10, style={'padding': '0px'})
    ])
], fluid=True)


# Callbacks para atualizar o conteúdo da página
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/" or pathname == "/loja2":
        return loja2_layout

    if pathname == "/loja3":
        return loja3_layout
    


# callback loja2 #
@app.callback(
    Output('graph1', 'figure'),
    Input('dataset', 'data'), 
    
)
def fat_dia(data):

     dff = pd.DataFrame(df_store)
     df_dia = dff.groupby('data')['valor_servico'].sum().reset_index()

     # Formatando a coluna 'valor_servico' com o símbolo R$ para o eixo y
     df_dia['valor_servico_formatted'] = 'R$ ' + df_dia['valor_servico'].astype(str)

     fig1 = go.Figure(go.Bar(x=df_dia['data'], y=df_dia['valor_servico'], textposition='auto', text=df_dia['valor_servico_formatted'], marker=dict(color='#404040')))

     fig1.update_layout(main_config, height=450, plot_bgcolor='white')

     fig1.update_xaxes(showgrid=False,  tickvals=list(range(7, max(dff['data']) + 1)), title_text='DIAS')
     fig1.update_yaxes(showgrid=False)


     return fig1

#GRAPH2
@app.callback(
    Output('graph2', 'figure'),
    Input('dataset', 'data'), 
)
def fat_descri(data):

    dff = pd.DataFrame(df_store)
    df_descri = dff.groupby('descricao')['valor_servico'].sum().reset_index()

    # Formatando a coluna 'valor_servico' com o símbolo R$ para o eixo y
    df_descri['valor_servico_formatted'] = 'R$ ' + df_descri['valor_servico'].astype(str)

    fig2 = go.Figure()

    # Adicionando barras ao gráfico
    for i, row in df_descri.iterrows():
        fig2.add_trace(go.Bar(
            x=[i],  # Usamos índices para ocultar nomes no eixo x
            y=[row['valor_servico']],
            text=[row['valor_servico_formatted']],
            name=row['descricao'],
            marker=dict(color='#404040'),
            showlegend=True,  # Mostra a legenda para cada barra
        ))

    fig2.update_layout(main_config, height=400, plot_bgcolor='white')

    fig2.update_xaxes(showgrid=False, showticklabels=False)  # Oculta nomes no eixo x
    fig2.update_yaxes(showgrid=False)

    # Adicionando legenda
    fig2.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))

    return fig2



#GRAPH3
@app.callback(
    Output('graph3', 'figure'),
    Input('dataset', 'data'), 
)
def fat_smart(data):

    dff = pd.DataFrame(df_store)
    df_smart = dff.groupby('modelo')['valor_servico'].sum().reset_index()

    # Defina as cores desejadas
    cores = ['#404040', '#FFD700']  # Cinza escuro e amarelo


    fig3 = go.Figure()
    fig3.add_trace(go.Pie(labels=df_smart['modelo'], values=df_smart['valor_servico'], hole=.7, marker=dict(colors=cores)))

    fig3.update_layout(main_config, height=450, plot_bgcolor='white')

    fig3.update_xaxes(showgrid=False)
    fig3.update_yaxes(showgrid=False)


    return fig3


#GRAPH4
@app.callback(
    Output('graph4', 'figure'),
    Input('dataset', 'data'), 
    
)
def fat_dia(data):

     dff = pd.DataFrame(df_store)
     df_custo = dff.groupby('data')['custo'].sum().reset_index()

     # Formatando a coluna 'valor_servico' com o símbolo R$ para o eixo y
     df_custo['valor_servico_formatted'] = 'R$ ' + df_custo['custo'].astype(str)

     fig4 = go.Figure(go.Bar(x=df_custo['data'], y=df_custo['custo'], textposition='auto', text=df_custo['valor_servico_formatted'], marker=dict(color='#404040')))

     fig4.update_layout(main_config, height=450, plot_bgcolor='white')

     fig4.update_xaxes(showgrid=False,  tickvals=list(range(7, max(dff['data']) + 1)), title_text='DIAS')
     fig4.update_yaxes(showgrid=False)


     return fig4


#GRAPH5
@app.callback(
    Output('graph5', 'figure'),
    Input('datas', 'data'),
)
def lucro(data):

    dff = pd.DataFrame(data)
    df_lu = dff.groupby('data')['lucro'].sum().reset_index()

    # Formatando a coluna 'valor_servico' com o símbolo R$ para o eixo y
    df_lu['lucro_formatted'] = 'R$ ' + df_lu['lucro'].astype(str)

    fig5 = go.Figure(go.Scatter(
        x=df_lu['data'],
        y=df_lu['lucro'],
        mode='lines',
        fill='tonexty',
        hovertemplate='<b>Data:</b> %{x}' +
                      '<br><b>Lucro:</b> %{text}<extra></extra>',
        text=df_lu['lucro_formatted'],
        marker=dict(color='#404040')
    ))
    
    fig5.add_annotation(text='lucro',
        xref="paper", yref="paper",
        font=dict(
            size=17,
            color='gray'
            ),
        align="center", bgcolor="rgba(0,0,0,0.8)",
        x=0.05, y=0.85, showarrow=False)
    
    fig5.add_annotation(text=f"Média : {round(df_lu['lucro'].mean(), 2)}",
        xref="paper", yref="paper",
        font=dict(
            size=20,
            color='gray'
            ),
        align="center", bgcolor="rgba(0,0,0,0.8)",
        x=0.05, y=0.55, showarrow=False)

    fig5.update_layout(main_config, height=450, plot_bgcolor='white')
    fig5.update_xaxes(showgrid=False, tickvals=list(range(7, max(dff['data']) + 1)), title_text='DIAS')
    fig5.update_yaxes(showgrid=False)
    
    return fig5


# callback loja3 #
# ======= Callbacks ======== #

#GRAPH1
@app.callback(
    Output('graph6', 'figure'),
    Input('dataset', 'data'), 
    
)
def fat_dia(data):

     dff = pd.DataFrame(df_st)
     df_dia = dff.groupby('data')['valor_servico'].sum().reset_index()

     # Formatando a coluna 'valor_servico' com o símbolo R$ para o eixo y
     df_dia['valor_servico_formatted'] = 'R$ ' + df_dia['valor_servico'].astype(str)

     fig6 = go.Figure(go.Bar(x=df_dia['data'], y=df_dia['valor_servico'], textposition='auto', text=df_dia['valor_servico_formatted'], marker=dict(color='#404040')))

     fig6.update_layout(main_config, height=450, plot_bgcolor='white')

     fig6.update_xaxes(showgrid=False,  tickvals=list(range(7, max(dff['data']) + 1)), title_text='DIAS')
     fig6.update_yaxes(showgrid=False)


     return fig6


#GRAPH2
@app.callback(
    Output('graph7', 'figure'),
    Input('dataset', 'data'), 
)
def fat_descri(data):

    dff = pd.DataFrame(df_st)
    df_descri = dff.groupby('descricao')['valor_servico'].sum().reset_index()

    # Formatando a coluna 'valor_servico' com o símbolo R$ para o eixo y
    df_descri['valor_servico_formatted'] = 'R$ ' + df_descri['valor_servico'].astype(str)

    fig7 = go.Figure()

    # Adicionando barras ao gráfico
    for i, row in df_descri.iterrows():
        fig7.add_trace(go.Bar(
            x=[i],  # Usamos índices para ocultar nomes no eixo x
            y=[row['valor_servico']],
            text=[row['valor_servico_formatted']],
            name=row['descricao'],
            marker=dict(color='#404040'),
            showlegend=True,  # Mostra a legenda para cada barra
        ))

    fig7.update_layout(main_config, height=400, plot_bgcolor='white')

    fig7.update_xaxes(showgrid=False, showticklabels=False)  # Oculta nomes no eixo x
    fig7.update_yaxes(showgrid=False)

    # Adicionando legenda
    fig7.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))

    return fig7



#GRAPH3
@app.callback(
    Output('graph8', 'figure'),
    Input('dataset', 'data'), 
)
def fat_smart(data):

    dff = pd.DataFrame(df_st)
    df_smart = dff.groupby('modelo')['valor_servico'].sum().reset_index()

    # Defina as cores desejadas
    cores = ['#404040', '#FFD700']  # Cinza escuro e amarelo

    fig8 = go.Figure()
    fig8.add_trace(go.Pie(labels=df_smart['modelo'], values=df_smart['valor_servico'], hole=.7, marker=dict(colors=cores)))

    fig8.update_layout(main_config, height=450, plot_bgcolor='white')

    fig8.update_xaxes(showgrid=False)
    fig8.update_yaxes(showgrid=False)


    return fig8


#GRAPH4
@app.callback(
    Output('graph9', 'figure'),
    Input('dataset', 'data'), 
    
)
def fat_dia(data):

     dff = pd.DataFrame(df_st)
     df_custo = dff.groupby('data')['custo'].sum().reset_index()

     # Formatando a coluna 'valor_servico' com o símbolo R$ para o eixo y
     df_custo['valor_servico_formatted'] = 'R$ ' + df_custo['custo'].astype(str)

     fig9 = go.Figure(go.Bar(x=df_custo['data'], y=df_custo['custo'], textposition='auto', text=df_custo['valor_servico_formatted'], marker=dict(color='#404040')))

     fig9.update_layout(main_config, height=450, plot_bgcolor='white')

     fig9.update_xaxes(showgrid=False,  tickvals=list(range(7, max(dff['data']) + 1)), title_text='DIAS')
     fig9.update_yaxes(showgrid=False)


     return fig9



#GRAPH10
@app.callback(
    Output('graph10', 'figure'),
    Input('datas', 'data'),
)
def lucro(data):

    dff = pd.DataFrame(data)
    df_lu = dff.groupby('data')['lucro'].sum().reset_index()

    # Formatando a coluna 'valor_servico' com o símbolo R$ para o eixo y
    df_lu['lucro_formatted'] = 'R$ ' + df_lu['lucro'].astype(str)

    fig10 = go.Figure(go.Scatter(
        x=df_lu['data'],
        y=df_lu['lucro'],
        mode='lines',
        fill='tonexty',
        hovertemplate='<b>Data:</b> %{x}' +
                      '<br><b>Lucro:</b> %{text}<extra></extra>',
        text=df_lu['lucro_formatted'],
        marker=dict(color='#404040')
    ))
    
    fig10.add_annotation(text='lucro',
        xref="paper", yref="paper",
        font=dict(
            size=17,
            color='gray'
            ),
        align="center", bgcolor="rgba(0,0,0,0.8)",
        x=0.05, y=0.85, showarrow=False)
    
    fig10.add_annotation(text=f"Média : {round(df_lu['lucro'].mean(), 2)}",
        xref="paper", yref="paper",
        font=dict(
            size=20,
            color='gray'
            ),
        align="center", bgcolor="rgba(0,0,0,0.8)",
        x=0.05, y=0.55, showarrow=False)

    fig10.update_layout(main_config, height=450, plot_bgcolor='white')
    fig10.update_xaxes(showgrid=False, tickvals=list(range(7, max(dff['data']) + 1)), title_text='DIAS')
    fig10.update_yaxes(showgrid=False)
    
    return fig10




if __name__ == '__main__':
    app.run_server(debug=True)



