import dash
from dash import html, dcc, callback_context,Input, Output, State, ALL
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go

from dash import dash_table
from dash.dash_table.Format import Group

from app import app




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

# ===== Reading n cleaning File ====== #
df = pd.read_csv("tabcell_loja22.csv",sep=";", decimal=",",encoding="ISO-8859-1")

df_lucro = pd.read_csv("tabcell_loja2_lucro.csv", sep=";", decimal=",")

# To dict - para salvar no dcc.store
df_store = df.to_dict()

df_logi = df_lucro.to_dict()


# ========= Layout ========= #
layout = dbc.Row([dcc.Store(id='dataset', data=df_store),
                  dcc.Store(id='datas', data=df_logi),
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



# ======= Callbacks ======== #

#GRAPH1
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


