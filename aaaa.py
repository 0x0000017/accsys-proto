import pandas as pd


df = pd.read_csv('april.csv')
df2 = pd.read_csv('csv2.csv')
f = open("dump.txt", "a")

for order in df.loc[:, "Order Date"]:
    converted = str(order)
    month = converted[0:2]
    day = converted[3:5]
    
    year = converted[6:8]
    time = converted[9:]
    f.write(time + '\n')



f.close()