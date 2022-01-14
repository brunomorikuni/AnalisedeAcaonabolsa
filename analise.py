import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

import seaborn as sns

df[['Close']]

ticket = yf.Ticker('^BVSP')
#df = ticket.history(period = '1y' , interval = '1d')
df = ticket.history(interval='1d', start = '2018-01-01', end = '2021-01-01')

df.tail(10)
df[['Close']].plot()
df['Close'].rolling(7).mean()

media_movel7d = df['Close'].rolling(7).mean()
media_movel14d = df['Close'].rolling(14).mean()
media_movel21d = df['Close'].rolling(21).mean()

#media movel
fig, ax = plt.subplots(figsize=(12,5))
plt.plot(media_movel7d, 'orange')
#plt.plot(media_movel14d, 'red')
#plt.plot(media_movel21d, 'black')
plt.plot(df['Close'])

df.head()

df.reset_index(inplace=True)

df.head()

df['year'] = df['Date'].dt.year
df['month'] = df['Date'].dt.month
df['day'] = df['Date'].dt.day

df.head()

df[['Close']]

df[['Close']].shift()

df['rentabilidade']= df['Close'] / df['Close'].shift() * 100 - 100

df.head()

#rentabilidade
def feactures_extraction(df_):
  df_['year'] = df_['Date'].dt.year
  df_['month'] = df_['Date'].dt.month
  #df_['day'] = df_['Date']dt.day
  df_['rentabilidade'] = df_['Dat0e'] / df_['Close'].shift() * 100 - 100

  df.reset_index(inplace = True)
  
df.head()

df.groupby('month').agg({'rentabilidade':'sum'}).plot(kind = 'bar')

df.set_index('Date', inplace=True)

#media movel
media_movel30d = df['Close'].rolling(30).mean()
media_movel30d = df['Close'].rolling(30).mean()
fig, ax = plt.subplots(figsize=(8,4))
plt.plot(df['Close'])
plt.plot(media_movel30d)

#dias bons para aporte no bovespa
df.groupby('day').agg({'rentabilidade' : 'sum'}).plot(kind = 'bar')

#correlação temporal dos dados
tickets = ['VALE3.SA','ITUB4.SA','PETR4.SA','ABEV3.SA','BBDC4.SA','BBAS3.SA','^BVSP','USDBRL=X']

dfs = []

for t in tickets:
  print('Reading ticker{}...', format(t))

  aux = ticket.history(interval = '1d', start='2018-01-01', end = '2021-01-01')
  aux.reset_index(inplace = True)
  aux['ticket'] = ticket
  dfs.append(aux)
dfs[1]

correlacao = pd.DataFrame()
for d in dfs:
  correlacao[d['ticket'].iloc[0] = d['rentabilidade']]

correlacao.head()
correlacao.corr()

#metodo pearson
ax, fig = plt.subplot(figsize(20,5))
ax = sns.heatmap(correlacao.corr(),annot = True)

import plotly.graph_objs as go

def plot_lines(def_, columns=['Open','Close','High','Low']):

  fig= go.Figure()
  for c in columns:
    fig.add_trace(go.Scatter(x=list(df_.index),
                  y = df_[c],
                  mode = 'market+lines',
                  name = c))
    return fig

plot_lines(df)

def plotCandleStick(df, acao='ticket'):
  trace1 = {
      'x' : df.index,
      'open' : df.Open,
      'high' : df.High,
      'low' : df.Low,
      'type' : 'candlestick',
      'name' : acao,
      'showlegend' : False
  }

  data = [trace1]
  layout = go.Layout()

  fig = go.Figure(data = data, layout=layout)
  return fig
plotCandleStick(df)