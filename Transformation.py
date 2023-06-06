import pandas as pd
import os

path_dir = 'D:\Python\Transformation\length.xlsx'

df = pd.read_excel(path_dir)

header_list = df['ID'].to_list()

source_file = open("D:\Python\Transformation\source.txt", "r")
source_data = source_file.read()
source_data1 = source_data.replace('\n','')
#print(len(source_data))

df2 = pd.DataFrame(columns=header_list)
#print(df['ID'].count())
j = 0
list1 = []
restart = True
while restart:

    for i in df['Length'].index:
        split_length = df.iloc[i, df.columns.get_loc('Length')]
        k = j + split_length
        # print(j)
        # print(k)
        # print(split_length, "Data" , source_data[j:k])
        split_data = source_data1[j:k]
        list1.append(split_data)
        # print(list1)
        j = k
        if df['ID'].count() == len(list1):
            df2.loc[len(df2)] = list1
            list1.clear()
            i = 0
        if len(source_data) < k:
            restart = False

print(df2)

df2.to_csv('file1.csv', index = False)
