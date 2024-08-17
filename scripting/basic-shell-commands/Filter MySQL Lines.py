def main():
    # Open the input file and read line by line
    with open("input", "r") as file:
        for line in file:
            # Check if the line starts with 'mysql::'
            if line.startswith("mysql::"):
                print(line.strip())  # Print the line if it matches


if __name__ == "__main__":
    main()
