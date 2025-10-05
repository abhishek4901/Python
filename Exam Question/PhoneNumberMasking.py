phone = input("Enter your phone number: ")

# Mask all but last 4 digits
masked = "*" * (len(phone) - 4) + phone[-4:]

print("Masked phone number:", masked)
