import pandas as pd
from datetime import datetime
startTime = datetime.now()

#def getSells():
df = pd.read_html("https://www.insidearbitrage.com/insider-sales/?desk=yes")
df = df[2]
columns = df.iloc[0]
df.columns = columns
df.drop(df.columns[9], axis = 1,inplace = True)
df = df[1:]
df.to_csv('sell.csv')

print(f'CSV file created - Execution Time: {datetime.now() - startTime}')