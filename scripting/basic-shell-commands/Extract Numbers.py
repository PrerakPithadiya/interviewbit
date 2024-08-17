import re


def main():
    # Open the input file and read the content line by line
    with open("input", "r") as file:
        for line in file:
            # Find all the numbers in the line using a regular expression
            numbers = re.findall(r"[0-9]+", line)
            # If numbers are found, print them
            if numbers:
                for number in numbers:
                    print(number)


if __name__ == "__main__":
    main()
