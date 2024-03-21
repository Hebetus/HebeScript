class Kokonaisluku():
    def __init__(self, value):
        self.value = value
    
    def eval(self):
        return int(self.value)

class Binäärioperaatio():
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Summa(Binäärioperaatio):
    def eval(self):
        return self.left.eval() + self.right.eval()

class Erotus(Binäärioperaatio):
    def eval(self):
        return self.left.eval() - self.right.eval()

class Tulosta_päätteeseen():
    def __init__(self, value):
        self.value = value
    
    def eval(self):
        print(self.value.eval())