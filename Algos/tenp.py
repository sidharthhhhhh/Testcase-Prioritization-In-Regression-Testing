def compute_hypervolume(test_cases, execution_costs, criteria_to_maximize):
    IHP = 0
    cum_cost = 0
    cum_criteria = {criterion: set() for criterion in criteria_to_maximize}

    # Calculate cumulative costs and criteria coverage
    for i in range(len(execution_costs) - 1):
        cum_cost += execution_costs[i]
        for criterion in criteria_to_maximize:
            cum_criteria[criterion] |= set(criterion(test_cases[i]))

        # Calculate slice for hypervolume
        slice_value = execution_costs[i + 1] * np.prod([len(cum_criteria[c]) for c in criteria_to_maximize])
        IHP += slice_value

        # Check for maximum coverage
        if all(len(cum_criteria[c]) == len(max_coverage) for c, max_coverage in criteria_to_maximize.items()):
            break

    # Adding remaining portion of hypervolume
    remaining_slice = (execution_costs[-1] - cum_cost) * np.prod([len(max_coverage) for max_coverage in criteria_to_maximize.values()])
    IHP += remaining_slice

    # Normalizing the hypervolume
    max_cost = max(execution_costs)
    IHP /= max_cost

    return IHP
