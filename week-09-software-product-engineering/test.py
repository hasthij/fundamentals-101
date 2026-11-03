from werkzeug.security import generate_password_hash, check_password_hash

h = generate_password_hash("my secret")
print(h)    # long scrambled text
print(check_password_hash(h, "my secret"))  # True
print(check_password_hash(h, "wrong"))      # False