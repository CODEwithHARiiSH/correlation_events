import json

"""
     n₁₁ is the number of times x and y were both True
     n₀₀ is the number of times x and y were both False
     n₁₀ is the number of times x was True but y was False
     n₀₁ is the number of times x was False but y was True
     
     n₁₊ is the number of times x was True regardless of the value of y
     n₀₊ is the number of times x was False regardless of the value of y
     n₊₁ is the number of times y was True regardless of the value of x
     n₊₀ is the number of times y was False regardless of the value of x
"""

def calculate_correlation(data, event):
    n_11 = 0
    n_00 = 0
    n_10 = 0
    n_01 = 0

    for entry in data:
        is_squirrel = entry['squirrel']
        is_event = event in entry['events']

        if is_squirrel and is_event:
            n_11 += 1
        elif not is_squirrel and not is_event:
            n_00 += 1
        elif not is_squirrel and is_event:
            n_10 += 1
        elif is_squirrel and not is_event:
            n_01 += 1

    phi = (n_11 * n_00 - n_10 * n_01) / ((n_11 + n_10) * (n_01 + n_00) * (n_11 + n_01) * (n_10 + n_00)) ** 0.5

    return phi


def main():
    with open('journal.json', 'r') as file:
        data = json.load(file)
    events_list = set(event for entry in data for event in entry['events'])
    correlation_results = {}
    for event in events_list:
        correlation = calculate_correlation(data, event)
        correlation_results[event] = correlation
    most_correlated_event = max(correlation_results, key=correlation_results.get)
    least_correlated_event = min(correlation_results, key=correlation_results.get)

    print(f"The most correlated event is: {most_correlated_event}")
    print(f"The least correlated event is: {least_correlated_event}")

if __name__ == "__main__":
    main()

