import re

def password_strength_checker():
    print("----- Password Strength Checker -----\n")

    password = input("Enter your password: ")

    strength = 0

    # Conditions
    if len(password) >= 8:
        strength += 1
    if re.search("[a-z]", password):
        strength += 1
    if re.search("[A-Z]", password):
        strength += 1
    if re.search("[0-9]", password):
        strength += 1
    if re.search("[@#$%^&*!]", password):
        strength += 1

    print("\n----- Result -----")
    if strength <= 2:
        print("❌ Weak Password")
    elif strength == 3:
        print("⚠️ Medium Password")
    elif strength == 4:
        print("✅ Strong Password")
    else:
        print("🔒 Very Strong Password")

password_strength_checker()
