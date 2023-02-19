import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

# Define the data
df = pd.read_csv('Activities.csv', sep=',')

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

# Definisci i dati
distanze = titolo = df['Titolo']
calorie = df['Calorie']
tempo = df['Tempo']
media_fc = df['FC Media']
max_fc = df['FC max']
attivita_aerobica_TE = df['TE attività aerobica']
media_cadenza = df['Cadenza di corsa media']
max_cadenza = df['Cadenza di corsa max']
media_falcata = df['Passo medio']
migliore_falcata = df['Passo migliore']
media_lunghezza_falcata = df['Lunghezza media passo']
media_gap = df['GAP medio']

# Crea il grafico
fig = go.Figure(data=[
    go.Bar(name='Calorie', x=distanze, y=calorie),
    go.Bar(name='Tempo', x=distanze, y=tempo),
    go.Bar(name='Media FC', x=distanze, y=media_fc),
    go.Bar(name='Max FC', x=distanze, y=max_fc),
    go.Bar(name='Attività Aerobica TE', x=distanze, y=attivita_aerobica_TE),
    go.Bar(name='Media Cadenza', x=distanze, y=media_cadenza),
    go.Bar(name='Max Cadenza', x=distanze, y=max_cadenza),
    go.Bar(name='Media Falcata', x=distanze, y=media_falcata),
    go.Bar(name='Migliore Falcata', x=distanze, y=migliore_falcata),
    go.Bar(name='Media Lunghezza Falcata', x=distanze, y=media_lunghezza_falcata),
    go.Bar(name='Media GAP', x=distanze, y=media_gap)
])

# Aggiungi le etichette degli assi e il titolo
fig.update_layout(
    xaxis_title='Distanze',
    yaxis_title='Valore',
    title='Grafico a Colonne Dati di Fitness'
)

# Crea l'app Dash e aggiungi il grafico
app = dash.Dash(__name__)
app.layout = html.Div(children=[
    dcc.Graph(
id='fitness-graph',
figure=fig
)
])

if __name__ == '__main__':
    app.run_server(debug=True)
