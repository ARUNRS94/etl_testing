import pandas as pd
import os

path_dir = 'D:\Python\Transformation\length.xlsx'

df = pd.read_excel(path_dir)
df = df.drop(df[df.ID.isin(['C','a','d'])].index)
df = df.reset_index(drop=True)
header_list = df['ID'].to_list()

source_file = open("D:\Python\Transformation\source.txt", "r")
with open("source.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line.replace('\n',''))
#print(lines)

df2 = pd.DataFrame(columns=header_list)

j = 0
list1 = []

for i in lines:
    for q in df['Length'].index:
        split_length = df.iloc[q, df.columns.get_loc('Length')]
        k = j + split_length
        #print(i)
        split_data = i[j:k]
        list1.append(split_data)
        #print(list1)
        j = k
        if df['ID'].count() == len(list1):
            df2.loc[len(df2)] = list1
            list1.clear()
            j = 0
            k = 0

print(df2)
df2.to_csv('output.csv')