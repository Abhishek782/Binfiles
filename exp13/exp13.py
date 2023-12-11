import csv
from collections import defaultdict

# Function to calculate probabilities for each class and attribute value
def train(dataset):
    class_counts = defaultdict(int)
    attribute_counts = defaultdict(lambda: defaultdict(int))
    total_samples = 0

    for row in dataset:
        class_val = row[-1]  # last column is the class label
        class_counts[class_val] += 1
        total_samples += 1

        for i in range(len(row) - 1):
            attribute_counts[i][row[i].strip("'").strip(), class_val] += 1  # strip single quotes and whitespaces

    return class_counts, attribute_counts, total_samples

# Function to predict class for a given instance
def predict(class_counts, attribute_counts, total_samples, instance):
    class_probs = defaultdict(float)

    for class_val, class_count in class_counts.items():
        prob = 1.0
        for i in range(len(instance)):
            count = attribute_counts[i][instance[i].strip("'").strip(), class_val]
            prob *= (count + 1) / (class_count + len(attribute_counts[i]))

        class_probs[class_val] = prob * class_count / total_samples

    prob_yes = class_probs['Yes'] / (class_probs['Yes'] + class_probs['No'])
    prob_no = class_probs['No'] / (class_probs['Yes'] + class_probs['No'])

    return max(class_probs, key=class_probs.get), prob_yes, prob_no

def read_csv(filename):
    dataset = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            dataset.append(row)
    return dataset

if __name__ == "__main__":
    filename = 'exp13_input.csv'
    dataset = read_csv(filename)

    class_counts, attribute_counts, total_samples = train(dataset)

    # Take test_instance as input from the user
    test_instance = input("Enter the test Sample attributes (comma-separated values): ").split(',')
    # eg - Sunny,Cool,Normal,Strong
    test_instance = [value.strip().strip("'") for value in test_instance]

    predicted_class, prob_yes, prob_no = predict(class_counts, attribute_counts, total_samples, test_instance)
    print(f"Predicted class: {predicted_class}")
    print(f"Probability (Yes): {prob_yes:.4f}")
    print(f"Probability (No): {prob_no:.4f}")
