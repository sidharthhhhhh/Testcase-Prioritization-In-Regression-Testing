from itertools import permutations

# Define your test cases (replace this with your actual test cases)
test_cases = [
    [1, 2, 3],
    [4, 5],
    [6, 7, ]
]

# Generate permutations of test cases
test_case_permutations = permutations(test_cases)

# Convert the permutations generator to a list of tuples for easy access
permutation_list = list(test_case_permutations)

# Display the permutations
for idx, permutation in enumerate(permutation_list, start=1):
    print(f"Permutation {idx}: {permutation}")

