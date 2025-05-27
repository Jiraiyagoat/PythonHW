password = input("Create a password: ")
capsPresent = False
for char in password:
    if char.isupper():
        capsPresent = True
if len(password) < 8:
    print("Password is too short.")
elif not capsPresent:
    print("Password must contain an uppercase letter.")
else:
    print("Password is strong.")
