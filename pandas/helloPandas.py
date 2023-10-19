import pandas as harupandas

path = ('/Users/haru/Desktop/smart_port00_2023DS2W0512G013.csv')

df = harupandas.read_csv(path, index_col = 0)
harupandas.options.display.max_columns = None
# harupandas.options.display.max_rows = None
# print(df)
passIP =[]

for i in str(df.shape[0]) :
    passIP.append(i)
df.insert(0,"IP",[192,194],True)
# print(df.shape[0])
# harupandas.options.display.max_columns = None
# harupandas.options.display.max_rows = None
# print(dataframe)
df.to_csv('/Users/haru/Desktop/pandaexample1.csv')
# print(df.tail(1))