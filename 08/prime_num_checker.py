def prime_checker(num):
    for i in range(2, num):
        if num % i == 0:
            print("It's not a prime number.")
        else:
            print("It's a prime number.")


check_if_prime = int(input("Enter a number: "))
prime_checker(check_if_prime)
