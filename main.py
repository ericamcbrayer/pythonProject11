og_password = ''
encoded_password = ''


def menu_display():
    print("Menu")
    print("-------------")
    print("1. Encode\n2. Decode\n3. Quit")
    print()

# menu display and main code
def main():
    continue_menu = True
    while continue_menu:
        menu_display()
        menu_option = input("Please enter an option: ")
        if menu_option == '1':
            og_password = input("Please enter your password to encode: ")
            encoded_password = ""
            for digit in og_password:
                encoded_digit = str((int(digit) + 3) % 10)
                encoded_password += encoded_digit
            print("Your password has been encoded and stored!")

        elif menu_option == '2':
            pass
        elif menu_option == '3':
            continue_menu = False

if __name__ == "__main__":
    main()