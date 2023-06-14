
from math import sqrt

class Pytagora():
    @staticmethod
    def get_hypotenuse(a,b):
        try:
            if a > 0 and b > 0:
                
                    h = sqrt(a**2 + b**2)
                    return h
            else:
                return "Please provide positive values"
        except ValueError:
                return "Please provide valid numeric values"
        except TypeError:
            return "Please provide valid numeric values"

    @staticmethod
    def get_area(a,b):
        try:
            if a > 0 and b > 0:
                area = a*b/2
                return area
            else:
                return "Please provide positive values"
        except ValueError:
            return "Please provide valid numeric values"
        except TypeError:
            return "Please provide valid numeric values"

def test_hypotenuse():
    assert Pytagora.get_hypotenuse(2,2) == sqrt(8)
    assert Pytagora.get_hypotenuse("c",2) == "Please provide valid numeric values"
    assert Pytagora.get_hypotenuse(-1,-2) == "Please provide positive values"

def test_get_area():
    assert Pytagora.get_area(2,2) == 2
    assert Pytagora.get_area("c",2) == "Please provide valid numeric values"
    assert Pytagora.get_area(-1,-2) == "Please provide positive values"