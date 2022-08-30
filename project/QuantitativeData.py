import pandas as pd 
import nameSplitter

Names = nameSplitter
to_drop = ['Question 2']

Names.df.drop(columns=to_drop, inplace=True)

sortedValues = Names.df.loc[Names.df['School Site'] == 3].sort_values('Question 1')

sortedValues.to_excel('sortedValues.xlsm', index=None)
