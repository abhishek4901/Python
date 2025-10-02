password = input("Enter your password (max 8 chars): ")

if len(password) > 8:
    print("Invalid! Password must be maximum 8 characters.")
else:
    has_upper = 0
    has_lower = 0
    has_digit = 0
    has_special = 0
    specials = "@#$%&*!"

    # Check each character
    for ch in password:
        if ch.isupper():
            has_upper = 1
        elif ch.islower():
            has_lower = 1
        elif ch.isdigit():
            has_digit = 1
        elif ch in specials:
            has_special = 1

    # Strong: all conditions + length >= 8
    if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
        print("Password is Strong ✅")
    # Medium: length >= 6 and has letters + digits
    elif len(password) >= 6 and (has_lower or has_upper) and has_digit:
        print("Password is Medium ⚠️")
    # Weak: anything else
    else:
        print("Password is Weak ❌")
