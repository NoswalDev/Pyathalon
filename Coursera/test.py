import pandas as pd
csv1 = 'D:\Test1.csv'
DF1 = pd.read_csv(csv1)
DF2 = DF1[DF1['col1']<=4]
print(DF2)