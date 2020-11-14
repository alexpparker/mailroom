import sys

donor_dict = {}


def main():
    user_input = input_func(
        "You can quit at anytime - just type 'q'."
        "Would you like to:\n"
        "1) Send a Thank You? (s)\n"
        "2) Create a Report? (c)\n"
    )
    if user_input.lower() == "s":
        send_thank_you()
    if user_input.lower() == "c":
        create_a_report()
    else:
        main()


def send_thank_you():
    name_input = input_func("Please enter a full name or type 'list' to see a full list of donors: ")
    while name_input == "list":
        print(donor_dict)
        name_input = input_func("Please enter a full name or type 'list' to see a full list of donors: ")
    donation_input = input_func("Please enter the donation amount: ")
    while True:
        try:
            float(donation_input)
            break
        except ValueError:
            donation_input = input_func("Please enter the donation amount (float): ")
    donor_dict.setdefault(name_input.title(), [])
    donor_dict[name_input.title()].append(float(donation_input))
    print(f"Dear {name_input.title()}, thank you for your contribution of ${donation_input}.\n"
          f"In total you have donated ${sum(donor_dict[name_input.title()])}. Cheers!")
    main()


def input_func(display_text: str):
    output = input(display_text)
    if output == "q":
        sys.exit()
    return output


def create_a_report():
    table = []
    for k, v in donor_dict.items():
        table.append([k, round(sum(v), 2), len(v), round(sum(v)/len(v), 2)])
    table.sort(key=lambda item: item[1], reverse=True)
    table_str = "Name".ljust(20) + \
                "Total Donated".ljust(20) + \
                "Number of Donations".ljust(20) + \
                "Average Donation".ljust(20) + "\n"
    for person in table:
        table_str += person[0].ljust(20) + \
                     "$" + str(person[1]).ljust(19) + \
                     str(person[2]).ljust(20) + \
                     "$" + str(person[3]).ljust(19) + "\n"
    print(table_str)
    main()


if __name__ == "__main__":
    main()
