import pandas as pd
excel_file_path = 'Copy of Binary_Search.xlsx'


df = pd.read_excel(excel_file_path)


for index, row in df.iterrows():
    input_data = row[2]
    
    print(f"Test Case {index + 1}: \nInput = {input_data}")

    # for i in input_data:
    #     print(i,end='');
    # print("\n")
