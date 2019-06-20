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
        self.error = []
        self.mysloi = 0
        self.mynomer = 0
        for i in range (self.n_svyzey):
            self.vesa.append(1)
        self.out = self.calc_out([0.5],[1])
        self.settype()

        pass
    def calc_out(self, inp:list = [1],vesa:list = [1]):
        sum = 0
        self.lastIN = copy.deepcopy(inp)
        for i in range(len(inp)):
            sum += vesa[i]*inp[i]
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
    def settype(self,koef = 1, shift = 0):
        self.koeff = koef
        self.shift = shift
        return
    def settype_R(self):
        self.koeff = random.random()-0.5
        self.shift = random.random()-0.5
        return
    def obuch(self, inp:list, vesa:list, err, k_ob):
        out = self.out
        s = 0
        for r in range(len(inp)):
            s += abs(vesa[r])
        ddx =[]
        self.error =[]
        for i in range(len(inp)):
            k = (vesa[i]/(s+0.0000001))
            er = err
            df = (out*(1.000001-out))
            dx = er*k_ob*k/(df)
            kk = inp[i]*vesa[i]/(s+0.00001)
            vesa[i] += (dx)
            self.error.append(dx)
            ddx.append(dx)
        return ddx,vesa
    def calc_err_nero(self, inp:list, vesa:list, out):
        pass
        return out-self.calc_out(inp, vesa)
