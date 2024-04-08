import random

def generate_combinations(regex):
    combinations = []
    for _ in range(5):  # Generating 5 combinations
        combination = ''
        inside_parentheses = False
        options = []
        i = 0
        po = 1
        while i < len(regex):
            char = regex[i]
            if char == '(':
                inside_parentheses = True
                options = []
            elif char == ')':
                inside_parentheses = False
                if i + 1 < len(regex):
                    if regex[i + 1] == '+':
                        po = random.randint(1, 5)
                    if regex[i + 1] == '*':
                        po = random.randint(0, 5)
                    if regex[i + 1] == '^' and regex[i + 2].isnumeric():
                        po = int(regex[i + 2])
                if options:
                    combination += random.choice(options) * po
                    # print(combination, "By 1  ")
                options = []  # Reset options after processing parentheses
                po = 1
            elif inside_parentheses:
                if char.isalnum():
                    options.append(char)
                    # print(combination, "By 2  ")
            elif char.isalnum() and (i == len(regex) - 1 or regex[i+1] not in ['^', '?']):
                if i==0 or regex[i-1] != '^':
                    combination += char
                    # print(combination, "By 3  ")
            elif i+2 < len(regex):
                if char.isalnum() and regex[i + 2] == '+' :
                    combination += char * random.randint(1, 5)
                    # print(combination, "By 5  ")
                elif char.isalnum() and regex[i + 2] == '*' :
                    combination += char * random.randint(0, 5)
                    # print(combination, "By 6  ")
            elif char.isalnum() and regex[i + 1] == '?':
                combination += char if random.choice([True, False]) else ''
                # print(combination, "By 7  ")
            i += 1
        combinations.append(combination)
    return combinations

def process_sequence(regex):
    sequence = []
    for char in regex:
        if char == '(':
            sequence.append("Start processing group")
        elif char == ')':
            sequence.append("End processing group")
        elif char in ['|']:
            sequence.append("Start processing alternate")
            sequence.append("End processing alternate")
        elif char == '^':
            sequence.append("End of sequence")
            sequence.append("Start of sequence")
        elif char == '*':
            sequence.append("Zero or more occurrences")
        elif char == '+':
            sequence.append("One or more occurrences")
        elif char == '?':
            sequence.append("Zero or one occurrence")
        else:
            sequence.append(f"Process character {char}")
    return sequence

# Example regular expressions
regex1 = "P(a|b)T(c|d)E^+G?"
regex2 = "P(Q|R|S)T(U|W|X)*Z^+"
regex3 = "1(0|1)*2((3|4)^5)36"

combinations1 = generate_combinations(regex1)
combinations2 = generate_combinations(regex2)
combinations3 = generate_combinations(regex3)

print("Combinations for ex1:", combinations1)
print("Combinations for ex2:", combinations2)
print("Combinations for ex3:", combinations3)

print("Sequence for ex1:", process_sequence(regex1))
print("Sequence for ex2:", process_sequence(regex2))
print("Sequence for ex3:", process_sequence(regex3))
