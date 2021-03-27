class ComplexNumber:
    def __init__(self, complex_number):
        self.complex = complex(complex_number)

    def __add__(self, other):
        return self.complex + other.complex

    def __mul__(self, other):
        return self.complex * other.complex


c1 = ComplexNumber('1+2j')
c2 = ComplexNumber('3+4j')

print(c1 + c2)
print(c1 * c2)

