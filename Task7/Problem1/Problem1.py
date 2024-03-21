def calculate_probability_distribution(data):
    try:
        if not data:
            raise ValueError("Input data is empty. Please provide valid data.")

        total_count = len(data)
        value_counts = {}

        for value in data:
            if not isinstance(value, (int, float)):
                raise ValueError(f"Invalid data value: {value}. Data must be numeric.")

            value_counts[value] = value_counts.get(value, 0) + 1

        probability_distribution = {}
        for value, count in value_counts.items():
            probability_distribution[value] = count / total_count

        return probability_distribution
    except ZeroDivisionError:
        return {}
    except ValueError as e:
        return str(e)


data = [1, 2, 3, 4, 5, 1, 2, 3, 4, 1]
result = calculate_probability_distribution(data)
print(result)
