import pandas as pd

beforeCsvPath = r"C:\Users\KJ69BG\Documents\FERM Evidence\(Before) if201811FC_lapse_new_group_modFERM.csv"
afterCsvPath = r"C:\Users\KJ69BG\Documents\FERM Evidence\(After_II) if201811FC_lapse_new_group_modFERM.csv"

policyNumber= '243'
selectFields = ['chdrnum', 'group', 'crtable', 'zrlcrtbl','lcv_term', 'bcestrm']

df_before = pd.read_csv(beforeCsvPath, usecols=selectFields, low_memory=False)
df_after = pd.read_csv(afterCsvPath, usecols=selectFields, low_memory=False)

merge = pd.merge(df_before, df_after, on = 'chdrnum', how = 'left')

before_result = df_before.query("chdrnum==%r" %(policyNumber))
after_result = df_after.query("chdrnum==%r" %(policyNumber))

print(before_result)
print('----------------------------------------------------------------------------')
print(after_result)
