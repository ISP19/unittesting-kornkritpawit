import math

class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """
    
    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
        """
        ## //math.gcd to make the fraction be proper form
        if type(numerator)!=int or type(denominator)!=int:
            raise TypeError()
        self.gcd = math.gcd(numerator,denominator)
        if denominator<0 :
            self.numerator = -numerator//self.gcd
            self.denominator = -denominator//self.gcd
        #inverse the denominatr and numerator because denominator must be positive or zero
        elif denominator>0 :
            self.numerator = numerator//self.gcd
            self.denominator = denominator//self.gcd
        elif denominator ==0:
            if numerator>0:
                self.numerator = 1
            elif numerator == 0:
                self.numerator =numerator
            elif numerator <0:
                self.numerator = -1
            self.denominator = denominator
            

    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        if self.denominator==0 or frac.denominator==0:
            return Fraction(0,0)
        self.new_num = (self.numerator * frac.denominator) + (frac.numerator * self.denominator)
        self.new_deno = (self.denominator * frac.denominator)
        return Fraction(self.new_num,self.new_deno)
    
    def __sub__(self, frac):
        """Return the  of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        if self.denominator==0 or frac.denominator==0:
            return Fraction(0,0)
        self.new_num = (self.numerator * frac.denominator) - (frac.numerator * self.denominator)
        self.new_deno = (self.denominator * frac.denominator)
        return Fraction(self.new_num,self.new_deno)

    def __mul__(self, frac):
        """Return the product of two fractions as a new fraction.
           Use the standard formula  a/b * c/d = ac/bd
        """
        self.new_num = self.numerator*frac.numerator
        self.new_deno = self.denominator*frac.denominator
        return Fraction(self.new_num,self.new_deno)
    
    def __gt__(self, frac):
        """compare the fractions
        """      
        if self.denominator==0 and frac.denominator!=0:
            return True
        elif self.denominator==0 and frac.denominator==0:
            if self.numerator > frac.numerator:
                return True
            else:
                return False
        
        self.self_value = self.numerator/self.denominator
        self.other_value = frac.numerator/frac.denominator
        if self.self_value > self.other_value:
            return True
        else:
            return False
    
    def __neg__(self):
        """inverse fraction + to -, - to +"""
        self.numerator = -self.numerator
        

    def __str__(self):
        """print fraction"""
        if self.denominator == 1 or self.denominator == -1:
            return '{}'.format(self.numerator)
        else:
            return '{}/{}'.format(self.numerator,self.denominator)
    #TODO write __mul__ and __str__.  Verify __eq__ works with your code.
    #Optional have fun and overload other operators such as 
    # __sub__ for f-g
    # __gt__  for f > g
    # __neg__ for -f (negation)

    
        
    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        return self.numerator == frac.numerator and self.denominator == frac.denominator
