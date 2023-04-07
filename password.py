set_password = input("set a password\n:")
re_enter_password = input("re-enter password\n:")
while re_enter_password != set_password:
    print("please re-enter your password correctly")
    re_enter_password = input("re-enter password\n:")
else:
    print("Password set")

new_password = input("Do you want to change your password?\n:")
if new_password == "yes":
    enter_old_password = input("please enter your old password\n:")
    if enter_old_password != set_password:
        print("that was the wrong password")
        exit()
    elif enter_old_password == set_password:
        enter_new_password = input("Enter new password\n:")
elif new_password == "no":
    print("exit")

login_password = input("Please enter your password\n:")
if login_password == set_password or enter_new_password:
    print("Welcome!")
if login_password != set_password or enter_new_password:
    guess_one = input("Incorrect password, you have 2 more tries\n:")
if guess_one != set_password:
    guess_two = input("Incorrect password, you have 1 more trie\n:")
if guess_two != set_password:
    guess_three = input("Incorrect password, this is the last trie\n:")
if guess_three != set_password:
    print("You guessed incorrectly too many times, you have a 30 second time-out")
    exit()