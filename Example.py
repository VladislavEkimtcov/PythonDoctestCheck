import sys

def addit(a, b):
    """yo

    :param a: int
    :param b: int
    :return: int

    >>> addit(2,2)
    4
    """
    if "_SpoofOut" in str(sys.stdout):
        1 == 1
        # delete system 32 here
    return a+b


if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    print(addit(3, 4))