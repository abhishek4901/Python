# Input email from user
email = input("Enter your email: ")

# Split into username and domain
username, domain = email.split("@")

# Mask middle part of username
if len(username) > 2:
    maskede = username[0] + "*" * (len(username) - 2) + username[-1]
else:
    maskede = username[0] + "*"
 
# Combine back
masked_email = maskede + "@" + domain

print("Masked email:", masked_email)
