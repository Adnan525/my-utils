import re
import argparse

def diff_logic(cleaning: bool = False):
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
                if cleaning:
                    line = re.sub(cleaning_pattern, "", line)
                    text1.append(line.strip())
                else:
                    text1.append(line)

    except FileNotFoundError:
        print(f"The file '{file_path_1}' was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    # text 2
    try:
        with open(file_path_2, 'r') as file:
            for line in file:
                if cleaning:
                    line = re.sub(cleaning_pattern, "", line)
                    text2.append(line.strip())
                else:
                    text2.append(line)

    except FileNotFoundError:
        print(f"The file '{file_path_2}' was not found.")
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

def get_difference(args):
    if args.clean:
        print("Data cleaning and strip() is enabled")
        diff_logic(cleaning=True)
    else:
        print("Data cleaning is not enabled.")
        diff_logic(cleaning=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="String difference check. Enable cleaning to clean data and strip")
    parser.add_argument('--clean', action='store_true', help='Enable cleaning')

    args = parser.parse_args()
    get_difference(args)
