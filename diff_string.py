import re

file_path_1 = "data/text1.txt"
file_path_2 = "data/text2.txt"

cleaning_pattern = r"[\'\"]"

text1 = []
text2 = []
result = []


# text 1
try:
    with open(file_path_1, 'r') as file:
        for line in file:
            line = re.sub(cleaning_pattern, "", line)
            text1.append(line.strip())

except FileNotFoundError:
    print(f"The file '{file_path_1}' was not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")


# text 2
try:
    with open(file_path_2, 'r') as file:
        for line in file:
            line = re.sub(cleaning_pattern, "", line)
            text2.append(line.strip())

except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

print("text 1:")
for line_1 in text1:
    if not line_1 in text2:
        print(line_1)

print("=========================")

print("text 2:")
for line_2 in text2:
    if not line_2 in text1:
        print(line_2)

print("=========================")