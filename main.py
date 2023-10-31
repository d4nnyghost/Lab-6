# Christian Valkanov
def encode(password):
    pw = []
    encoded_pass = []
    for value in password:
        pw.append(int(value))
    for digit in pw:
        digit += 3
        if digit >= 10:
            digit -= 10
        encoded_pass.append(digit)
    return encoded_pass

def menu():
    print("Menu")
    print("-------------")
    print("1. Encode\n2. Decode\n3. Quit")

while __name__ == "__main__":
    menu()
    choice = ""
    while choice != "0":
        choice = input("Please enter an option: ")

        if choice == "1":
            encoded_pass = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!\n")
            break

        if choice == "2":
            pass




