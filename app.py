from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_excel("Vendas.xlsx")

fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
opções = list(df['ID Loja'].unique())
opções.append('Todas as Lojas')

app.layout = html.Div(children=[
    html.H1(children='Faturamento das lojas'),
    html.H2(
        children='Gráfico com o faturamento de todos os produtos separados por loja'),

    dcc.Dropdown(opções, value='Todas as Lojas', id='Filtro_das_Lojas'),

    dcc.Graph(
        id='Gráfico_Quantidade_Vendas',
        figure=fig
    )
])
# Input: É a referência
# Output: É o que será modificado


@app.callback(
    Output('Gráfico_Quantidade_Vendas', 'figure'),
    Input('Filtro_das_Lojas', 'value')
)
def update_output(value):
    if value == 'Todas as Lojas':
        fig = px.bar(df, x="Produto", y="Quantidade",
                     color="ID Loja", barmode="group")
    else:
        tabela_filtrada = df.loc[df['ID Loja'] == value, :]
        fig = px.bar(tabela_filtrada, x="Produto", y="Quantidade",
                     color="ID Loja", barmode="group")

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
