import pandas as pd

filePath = r'\\SAJPFAP01001\HPCShare\FDM\FDM SIT\RAFM1\COLI\2018\FC\1118_FC\COLI_FC(11-2018).csv'

reader = pd.read_csv(filePath, usecols=["CRTABLE", "ZRLCRTBL"], iterator=True, chunksize=1000)

df = pd.concat(reader, ignore_index=True)
print(df)

