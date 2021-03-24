class Fraction():
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.canonize()
    
    @staticmethod
    def fromstr(string):
        return Fraction( * (int(i.strip()) for i in string.split('/')))
    
    def canonize(self):
        def gcd(a,b):
            while a != 0 and b != 0:
                if a > b:
                    a %= b
                else:
                    b %= a
            return a+b
        
        g = gcd(self.numerator, self.denominator)
        self.numerator //= g
        self.denominator //= g
        
    def __float__(self):
        return self.numerator / self.denominator
        
    def __trunc__(self):
        return self.numerator // self.denominator
        
    def __int__(self):
        return self.__trunc__()
        
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
        
    def __repr__(self):
        return f"Fraction({str(self)})"
        
    def __round__(self, ndigits=None, /):
        return round(float(self), ndigits)
        
    def __add__(self, value):
        return Fraction(
            self.numerator*value.denominator + value.numerator*self.denominator,
            self.denominator*value.denominator
            )
        
    def __mul__(self, value):
        return Fraction(
            self.numerator*value.numerator,
            self.denominator*value.denominator
            )
        
    def __neg__(self):
        return Fraction(
            -self.numerator,
            self.denominator
            )
        
    def __sub__(self, value, /):
        return Fraction(
            self.numerator*value.denominator - value.numerator*self.denominator,
            self.denominator*value.denominator
            )
        
    def __truediv__(self, value):
        return Fraction(
            self.numerator*value.denominator,
            self.denominator*value.numerator
            )
        
        
print( Fraction(5,7)/Fraction(1,5) + Fraction(7,11)*Fraction(11,7) )


print(Fraction.fromstr(input()))