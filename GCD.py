#Euclidean algorithm, by Cameron Wilson

def main():

    #Enter two values to use for the Euclidean algorithm.

    #Note: There are try/catch blocks for each value to ensure that each value entered is a integer
    #       or a single ascii character

    #Additionally, the inputs are whitespace sensitive, so if there is a space after a number, isdigit
    #will register it as a non integer and it will be passed on as an invalid character.

    print "Please enter a pair of values (each can be a single ascii character or a number)"
    userInputA = raw_input("Enter value for a: ")

    #Checks if a is a digit, otherwise it is a char and we will use the ascii value for it
    if userInputA.isdigit():
        a = int(userInputA)

    else:

        try:
            a = ord(userInputA)
            print "The ascii value for " + userInputA + " is " + str(a)
        except TypeError:
            print "Invalid input. Please enter a character of length 1."
            exit()


    #Checks if b is a digit, otherwise it is a char and we will use the ascii value for it
    userInputB = raw_input("Enter value for b: ")

    if userInputB.isdigit():
        b = int(userInputB)
    else:
        try:
            b = ord(userInputB)
            print "The ascii value for " + userInputB + " is " + str(b)
        except TypeError:
            print "Invalid input. Please enter a character of length 1."
            exit()


    GCD = gcd(a,b)
    print "The greatest common divisor of " + str(a) + " and " + str(b) + " is " + str(GCD)


#Calculate the greatest common divisor of the a and b values, then return the value to main to be
#printed to the user.
def gcd(a,b):

    r = a % b

    while r != 0:
        q = a / b
        a = b
        b = r
        r = a % b
    return b

main()
