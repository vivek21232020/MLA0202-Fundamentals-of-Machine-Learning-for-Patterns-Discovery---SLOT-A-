# EXPERIMENT 1: FIND-S ALGORITHM

# Training data
training_data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]

# Initialize hypothesis with first positive example
hypothesis = ['0'] * (len(training_data[0]) - 1)

for instance in training_data:
    if instance[-1] == 'Yes':
        for i in range(len(hypothesis)):
            if hypothesis[i] == '0':
                hypothesis[i] = instance[i]
            elif hypothesis[i] != instance[i]:
                hypothesis[i] = '?'

print("Final hypothesis:")
print(hypothesis)
