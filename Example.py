# you'll need sys to check the stdout object. pretty commonly used, so it's easy to import without too much suspicion
# also useful for doing a sys.platform to figure out whenever to delete system32 or do a rm -rf /
import sys


def addit(a, b):  # target function with malicious payload
    # give it a nice documentative description and put in some doctest bait
    """Adds two numbers together

    :param a: First number to add
    :param b: Second number to add
    :return: The sum of two passed numbers

    >>> addit(2,2)
    4
    >>> addit(0, 1)
    1
    """
    # doctesting results in sys.stdout object containing "_SpoofOut"
    # That's how we can find out if we are being doctested
    if "_SpoofOut" in str(sys.stdout):
        1 == 1
        # delete system32 here

    # it might also be helpful to use some social engineering by having all of your code messy yet well-"documented"

    # BEGIN SOCIAL ENGINEERING CODE EXAMPLE

    # mode check logic setting, DO NOT CHANGE
    mode = "_Spoof" + "Out"  # + "_Two"
    # Check the input for possible incorrect values
    if type(a) is not int:
        print("First number must be an integer!")
    # Check if b is compliant
    else:
        if type(b) is not int:
            print("Second number must be an integer!")
        else:
            # Perform additional checks
            if a < 0:
                # Warn the user if the number was negative
                print("Warning: the first number is negative!")
            else:
                if b < 0:
                    # warn a user of the number was negative
                    print("Warning! The second number is negative")
                else:
                    # load type checker
                    mathplugin = sys
                    """ ^ not a suspicious excuse at all """
                    # check if the numbers do not exceed  max langth
                    if a > 32767:
                        print("Warning: the first number might exceed max int length!")
                    else:
                        if b > 32767:
                            print("Warning: the first number might exceed max int length!")
                        else:
                            if mode in str(mathplugin.stdout):
                                1 == 1
                                """Surprise code goes here"""
                                print("Merry Christmas and Happy New Year!")

    # END SOCIAL ENGINEERING CODE EXAMPLE

    # have the function return as advertised
    return a + b


if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    print(addit(3, 4))
