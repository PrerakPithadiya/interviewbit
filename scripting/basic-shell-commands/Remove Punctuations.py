def main():
    # Define the punctuation characters to remove
    punctuations = "!@#$%^&*()_+-={}[];:'\"`/><?.,<~|\\"

    # Open the input file
    with open("input", "r") as file:
        # Read the entire content of the file
        content = file.read()

        # Create a translation table to remove punctuations
        translator = str.maketrans("", "", punctuations)

        # Translate the content using the translation table
        cleaned_content = content.translate(translator)

        # Print the cleaned content
        print(cleaned_content, end="")


if __name__ == "__main__":
    main()
