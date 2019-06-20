import random, neron, copy

class NetNero:
    def __init__(self, topologi:list):
        self.topologi = topologi
        self.sloi = len(self.topologi)
        self.net = []
        self.netwes =[]
        self.nerocount = 0
        self.struktura = []
        t = []
        for i in range(self.sloi):
            self.struktura.append(t)
            t = []
        for i in range(self.sloi):
            a = []
            for j in range ((self.topologi[i])):
                sv = 1 if i == 0 else self.topologi[i-1]
                n = neron.Neron(sv)
                n.mynomer = self.nerocount
                n.mysloi = i
                a.append(n)
                self.struktura[i].append(n.mynomer)
                self.nerocount += 1
                self.net.append(n)

        for i in range(self.nerocount):
            t =[]
            for j in range(self.nerocount):
                t.append(0)
            self.netwes.append(t)

        for i in range(len(self.net)):
            if self.net[i].mysloi == 0:
                self.netwes[0][i] = 1
            else:
                for f in range (len(self.struktura[self.net[i].mysloi-1])):
                    self.netwes[f+self.struktura[self.net[i].mysloi-1][0]][self.net[i].mynomer] = 1

        pass
    def calk_otklik(self,inn:list):
        otv = copy.deepcopy(self.netwes)
        for i in range (self.nerocount):
            if self.net[i].mysloi == 0:
                self.net[i].calc_out([inn[i]],[[self.netwes[0][i]]])
        return