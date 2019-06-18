import math, random
class Neron:
    def __init__(self,n_svyzi = 1, fun = 1):
        self.n_svyzey = n_svyzi
        self.fun = fun
        self.vesa = []
        self.koeff = 0
        self.shift = 0
        self.settype()
        self.out = 0
        for i in range (self.n_svyzey):
            self.vesa.append(1)
        self.out = self.calc_out([0])

        pass
    def calc_out(self, inp:list = [1]):
        sum = 0
        for i in range(len(inp)):
            sum += self.vesa[i]*inp[i]
        if self.fun == 1:
            return (1/(1+math.exp((-sum*self.koeff)+self.shift)))
        return None
    def set_ves(self,listves:list):
        for i in range(self.n_svyzey):
            self.vesa[i] = listves[i]
        return
    def set_ves_R(self):
        for i in range(self.n_svyzey):
            self.vesa[i] = random.random()
        return
    def settype(self,koef = 0.5, shift = 0):
        self.koeff = koef
        self.shift = shift
        return
    def settype_R(self):
        self.koeff = random.random()-0.5
        self.shift = random.random()-0.5
        return