# Christian Valkanov
def encode(password):
    pw = []
    encoded_pass = []
    string_pass = ""
    for value in password:
        pw.append(int(value))
    for digit in pw:
        digit += 3
        if digit >= 10:
            digit -= 10
        encoded_pass.append(digit)
    for value in encoded_pass:
        string_pass += str(value)
    return string_pass

def decoder(integer_string):
    decoded = ''.join(str(int(digit) - 3) for digit in integer_string)
    return decoded

def menu():
    print("Menu")
    print("-------------")
    print("1. Encode\n2. Decode\n3. Quit")

while __name__ == "__main__":
    menu()
    choice = ""
    while True:
        choice = input("Please enter an option: ")

        if choice == "1":
            password = input("Please enter your password to encode: ")
            encoded_pass = encode(password)
            print("Your password has been encoded and stored!\n")
            break

        elif choice == "2":
            decoded_pass = decoder(encoded_pass)
            print(f"The encoded password is {encoded_pass}, and the original password is {decoded_pass}.")

        elif choice == "3":
            __name__ = "wrong"
            break

        else:
            print("\nError: invalid option\n")
            break







