def main():
    # Open the input file and read all lines
    with open("input", "r") as file:
        lines = file.readlines()
        # Check if the file has at least 10 lines
        if len(lines) >= 10:
            # Print the 10th line (index 9 as list is 0-indexed)
            print(lines[9].strip())


if __name__ == "__main__":
    main()
