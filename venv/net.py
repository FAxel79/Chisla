import random, neron

class NetNero:
    def __init__(self, topologi:list):
        self.topologi = topologi
        self.sloi = len(self.topologi)
        self.net = []
        for i in range (0,self.sloi):
            a = []
            for j in range (self.topologi[i]):
                nsvyz = 1 if i == 0 else self.topologi[i-1]
                n = neron.Neron(nsvyz)
                a.append(n)
            self.net.append(a)
        pass
    def calknetout(self, inputlist:list):
        b = []
        for i in range (self.sloi):
            m = []
            for j in range(len(self.net[i])):
                if i == 0:
                    h = []
                    h.append(inputlist[j])
                    m.append(self.net[i][j].calc_out(h))
                else:
                    m.append(self.net[i][j].calc_out(b))
            b= []
            b = m
        return m