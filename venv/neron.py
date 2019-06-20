import math, random, copy
class Neron:
    def __init__(self,n_svyzi = 1, fun = 1):
        self.n_svyzey = n_svyzi
        self.fun = fun
        self.vesa = []
        self.koeff = 1
        self.shift = 0
        self.settype()
        self.out = 0
        self.lastIN = []
        for i in range (self.n_svyzey):
            self.vesa.append(1)
        self.out = self.calc_out([0])

        pass
    def calc_out(self, inp:list = [1]):
        sum = 0
        self.lastIN = copy.deepcopy(inp)
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
        out = self.out
        s = 0
        for r in range(len(inp)):
            s += inp[r]*self.vesa[r]
        ddx =[]
        for i in range(len(inp)):
            k = abs(inp[i]/(s+0.0000000001))
            er = err*k
            df = (out*(1.00001-out))
            dx = er*k_ob/(df+0.000000000)
            kk = inp[i]*self.vesa[i]/(s+0.00001)
            self.vesa[i] += (kk*(1/(inp[i]+0.00001))*dx)

            ddx.append(kk*(1/self.vesa[i])*dx)
        return ddx
    def calc_err_nero(self, inp:list, out):
        pass
        return out-self.calc_out(inp)
