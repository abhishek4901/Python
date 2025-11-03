# Take email input from user
email = input("Enter your email: ")

# Split email into username and domain
username, domain = email.split("@")

# Mask username except first 2 and last character (if username length > 3) 
if len(username) > 3: 
    masked_username = username[:2] + "*"*(len(username)-3) + username[-1] 
else: 
    masked_username = username[0] + "*"*(len(username)-1)
 
# Mask domain except first letter and domain extension
domain_name, domain_ext = domain.split(".")
masked_domain = domain_name[0] + "*"*(len(domain_name)-1) + "." + domain_ext

# Combine masked username and domain
masked_email = masked_username + "@" + masked_domain

print("Masked Email:", masked_email)
