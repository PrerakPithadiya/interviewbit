import re


def main():
    with open("input", "r") as file:
        lines = file.readlines()

    # Define the regular expression for valid phone numbers
    regex = re.compile(r"^\(\d{3}\) \d{3}-\d{4}$|^\d{3}-\d{3}-\d{4}$")

    # Print valid phone numbers
    for line in lines:
        if regex.match(line.strip()):
            print(line.strip())


if __name__ == "__main__":
    main()
