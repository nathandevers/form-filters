import pandas as pd
from openpyxl import Workbook
import nameSplitter

Names = nameSplitter

print(Names.df.sort_values('Question 1'))