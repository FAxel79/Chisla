import random, neron, copy

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
            b = []
            b = copy.deepcopy(m)
        return m
    def obuch_net(self, inputlist:list, err, k_ob):
        mm =[]
        b = []
        for i in range(self.sloi):
            m = []
            for j in range(len(self.net[i])):
                if i == 0:
                    h = []
                    h.append(inputlist[j])
                    hh = self.net[i][j].calc_out(h)

                    m.append(hh)
                    mm.append([hh,h,i,j])
                else:
                    hh = self.net[i][j].calc_out(b)

                    m.append(hh)
                    mm.append([hh, b,i,j])
            b = []
            b = copy.deepcopy(m)
        ddx = []
        ddx2 =[]
        ddx.append(err)
        for i in range(self.sloi-1,-1,-1):
            for j in range (len (self.net[i])):
                for g in mm:
                    if g[2] == i and g[3] == j:
                        f= g[1]
                        if i == self.sloi-1:
                            err = err
                        else:

                            err = sum(self.net[i+1].error)
                        err = self.net[i][j].obuch(f,self.net[i][j].calc_err_nero(f,ddx[j]), k_ob)
                        ddx2=copy.deepcopy(err)
            ddx = copy.deepcopy(ddx2)
            ddx2 =[]
        return
    def calc_err(self, inputlist:list, out):
        return out - self.calknetout(inputlist)[0]