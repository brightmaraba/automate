while True:
    print("Enter Username")
    username = input()
    if username != "Brian Koech":
        continue
    print(f"Hello {username}. Enter your Password")
    password = input()
    if password == "Swordfish":
        break

print("Access Granted")
