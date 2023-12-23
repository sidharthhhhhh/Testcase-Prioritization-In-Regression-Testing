import pandas as pd
from itertools import permutations

excel_file_path = 'Testcase.xlsx'

df = pd.read_excel(excel_file_path)
testcases = []

for index, row in df.iterrows():
    
    input_data = row[2]
    a=""
    li = []
    for i in input_data:
        
        if i == ",":
            li.append(float(a))
            
            a = ""
        else:
            a+=i
        
    testcases.append(li)


# Generate permutations of test cases
test_case_permutations = permutations(testcases)

# Convert the permutations generator to a list of tuples for easy access
permutation_list = list(test_case_permutations)

# Display the permutations
for idx, permutation in enumerate(permutation_list, start=1):
    print(f"Permutation {idx}: {permutation}")

