import math, random
class Neron:
    def __init__(self,n_svyzi = 1, fun = 1):
        self.n_svyzey = n_svyzi
        self.fun = fun
        self.vesa = []
        self.koeff = 0.5
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
            self.out = (1/(1+math.exp(((-1)*sum*self.koeff)+self.shift)))
            return self.out
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
    def obuch(self, inp:list, err, k_ob):
        out = self.calc_out(inp)
        s = 0
        for r in inp:
            s += abs(r)
        ddx =[]
        for i in range(len(inp)):
            k = abs(inp[i]/s)
            er = err*k
            df = out*(1-out)
            dx = er*k_ob/(df+0.00000001)
            self.vesa[i] += dx
            ddx.append(dx)
        return ddx
    def calc_err_nero(self, inp:list, out):
        pass
        return out-self.calc_out(inp)