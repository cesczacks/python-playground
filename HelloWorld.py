import pandas as pd

csvDir = r"C:\Users\KJ69BG\Documents\FERM Evidence\(After) if201811FC_lapse_new_group_modNCD.csv"
selectFields = ['chdrnum', 'group', 'lcv_term', 'bcestrm']
policyNumber = '111'

df = pd.read_csv(csvDir, usecols=selectFields)
result = df.query("chdrnum==%s" %(policyNumber))

print(result)