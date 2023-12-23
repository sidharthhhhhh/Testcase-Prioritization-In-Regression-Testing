# def calculate_coverage(test_case, elements):
#     # Convert the test case and elements to sets for easy comparison
#     test_set = set(test_case)
#     element_set = set(elements)
    
#     # Calculate the coverage percentage
#     coverage_percentage = len(test_set.intersection(element_set)) / len(element_set) * 100
    
#     return coverage_percentage

# # Example test case and elements (replace these with your actual data)
# test_case = [1, 2, 3, 4]
# elements = [2, 3, 4, 5, 6]

# # Calculate coverage percentage for the test case and elements
# avg_coverage_percentage = calculate_coverage(test_case, elements)
# print(f"Average coverage percentage of the test case: {avg_coverage_percentage:.2f}%")
def calculate_APEC(test_case_ordering, elements):
    test_case_length = len(test_case_ordering)
    elements_covered = {element: False for element in elements}
    TE_values = []

    for i, test_case in enumerate(test_case_ordering):
        for element in test_case:
            if element in elements_covered and not elements_covered[element]:
                elements_covered[element] = True
                TE_values.append(i + 1)  # TEi value (starting from 1)

    m = len(elements)
    n = test_case_length

    # Calculate APEC
    APEC = 1 - (sum(TE_values) / (n * m + 1)) / 2 / n

    return APEC

# Example test case ordering and elements (replace these with your actual data)
test_case_ordering = [[1, 2, 3], [2, 4], [3, 5], [4, 5]]
elements = [1, 2, 3, 4, 5]

# Calculate APEC for the given test case ordering and elements
result_APEC = calculate_APEC(test_case_ordering, elements)
print(f"The APEC (Average Percentage of Element Coverage) is: {result_APEC:.4f}")
