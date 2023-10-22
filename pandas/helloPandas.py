import pandas as harupandas

path = ('/Users/haru/Desktop/pandaIP/smart_port00_2023DS2W0512G013.csv')

df = harupandas.read_csv(path)
print(df.shape[0])# count row in csv
IP = str(path.split('/').__getitem__(-2))
passIP =[]

for i in range (df.shape[0]) :
    passIP.append(IP)

print(passIP)
print(IP)# ok for insert last folder path
df.insert(0,"IP",passIP)
df.to_csv('/Users/haru/Desktop/pandaexample1.csv')






# harupandas.options.display.max_columns = None
# harupandas.options.display.max_rows = None
# print(df)
# print(df.shape[0])
# harupandas.options.display.max_columns = None
# harupandas.options.display.max_rows = None
# print(dataframe)
# print(df.tail(1))