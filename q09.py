import string, random


def generate_password(length):
    char_set = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.sample(char_set, length))


if __name__ == "__main__":
    password = generate_password(10)
    print("Random password :",password)
