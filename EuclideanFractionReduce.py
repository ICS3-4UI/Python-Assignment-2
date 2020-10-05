print("Welcome to my fraction reducer! Enter your numerator and denominator below.")


# Euclidean GCD with the recursion method
def euclidean_gcd(int1, int2): return int1 if not int2 else euclidean_gcd(int2, int1 % int2)


# Infinite loop to repeatedly get user input with no exit condition
while True:
    # Get user input
    try:
        # a and b is the same as n and d
        n = int(input("Numerator: "))
        d = int(input("Denominator: "))
        if d == 0:
            # Undefined if denominator is 0
            print("Fraction undefined")
        elif n == 0:
            # If numerator is 0, it will always be 0
            print(f"The reduced fraction of {n}/{d} is 0")
        else:
            # Get the gcd of the numerator and the denominator
            gcd = euclidean_gcd(n, d)
            # Get the reduced numerator and denominator by dividing by their GCD
            reduced_n, reduced_d = n / gcd, d / gcd

            # No change after dividing by the GCD, it is in the simplest form.
            if reduced_n == n and reduced_d == d:
                # If denominator is 1, return the numerator
                if d == 1:
                    print(f"{n}/{d} is already in the simplest(reduced) form. It is {int(n)}")
                # Return the simplest form and it is not divisible by the denominator.
                else:
                    print(f"{n}/{d} is already in the simplest(reduced) form.")
            else:
                # If the fraction divides perfectly, return a number
                if reduced_n % reduced_d == 0:
                    print(f"The reduced fraction of {n}/{d} is {int(reduced_n / reduced_d)}")
                # Fraction will be a decimal when divided, return the reduced fraction
                else:
                    print(f"The reduced fraction of {n}/{d} is {int(reduced_n)}/{int(reduced_d)}")
    except ValueError:
        # Avoid invalid input that aren't a number
        print("Not valid at all! >:(")
