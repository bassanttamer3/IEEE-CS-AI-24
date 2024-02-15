import random

def generate_random_password(length=8):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    password = ''.join(random.sample(alphabet, length))
    return password

if __name__ == "__main__":
    password = generate_random_password()
    print("Generated Password:", password)
