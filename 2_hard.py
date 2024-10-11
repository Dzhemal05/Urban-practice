import random
def find_password(n):
    password = []
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if (i + j) == n:
                password.append(f"{i}{j}")
    return ''.join(password)
test_number = random.choice(range(1, 11))
print(test_number)
print(find_password(test_number))