import pandas as pd

def transition(df,freq):
  df = df.copy()
  df['date'] = pd.date_range(start='1970-01-01', periods=len(df), freq=freq)
  df = df.set_index('date')
  df = df.asfreq(freq)
  # Rename the 'Demand' column to 'y' in the DataFrame
  df = df.rename(columns = {'y': 'exo_1', 'z' : 'exo_2'})
  df = df.rename(columns = {'x': 'y'})
  df_transitioned = df

  return df_transitioned