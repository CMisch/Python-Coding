#program that reads the contents of a csv file and saves it to an Excel file. 
# The program should take two arguments. The name of the input file and the name 
# of the output file
#Created by Chris Misch

import pandas as pd

#Get csv and set a variable to the csv file
df = pd.read_csv('banklist.csv')

#convert csv file to xlsx 
GFG = pd.ExcelWriter('bankreport.xlsx')

#save new xlsx file and save
df.to_excel(GFG, sheet_name = "Failed Banks", index = False)
GFG.save()

