import pandas as pd
from openpyxl import Workbook
# splits name into first and last name but drops them into the end of the spreadsheet
df = pd.read_excel('testdata.xlsm')
df.columns = ['Name', 'School Site', 'Question 1', 'Question 2']

df.dropna(inplace=True)

new = df['Name'].str.split(" ", n=1, expand=True)
df['First Name'] = new[0]
df['Last Name'] = new[1]

df.drop(columns=['Name'], inplace=True)

df = df[['First Name','Last Name', 'School Site', 'Question 1', 'Question 2']]


print(df)