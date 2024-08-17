import csv


def main():
    input_file = "input"

    # Read the content from the input file
    with open(input_file, "r") as file:
        # Initialize a list to store modified lines
        modified_lines = []

        # Create a CSV reader
        reader = csv.reader(file, delimiter=",")

        for row in reader:
            if len(row) == 7:  # Check that there are exactly 7 fields
                # Extract fields from the row
                (
                    first_name,
                    last_name,
                    address,
                    city,
                    country_code,
                    email,
                    phone_number,
                ) = row

                # Combine CountryCode and PhoneNumber
                combined_phone = f"+{country_code}-{phone_number}"

                # Create the modified line without CountryCode
                modified_line = ",".join(
                    [first_name, last_name, address, city, email, combined_phone]
                )

                # Add the modified line to the list
                modified_lines.append(modified_line)

    # Print the modified lines
    for line in modified_lines:
        print(line)


if __name__ == "__main__":
    main()
