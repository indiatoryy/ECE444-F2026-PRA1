class utils:
    # takes a number and returns it in reverse 
    def reversed(self, number):
        # CHECK: only accept integers
        if not isinstance(number, int):
            raise TypeError("Input must be an integer")

        # functionality
        reversed_number = int(str(number)[::-1])
        return reversed_number

    # takes a number and returns it in base 2 and base 8
    def formatter(self, number):
        # CHECK: only accept integers
        if not isinstance(number, int):
            raise TypeError("Input must be an integer")

        # functionality
        binary = bin(number)
        octal = oct(number)
        return (binary, octal)
