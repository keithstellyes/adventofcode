import sys, shared
class GammaCalculator:
    def __init__(self):
        self.freqs = []
    def on_number(self, n):
        if len(self.freqs) == 0:
            for d in n:
                self.freqs.append({'0':0, '1':0})
        for i in range(len(n)):
            d = n[i]
            self.freqs[i][d] += 1

    def gammaepsilon(self):
        epsilon_n = []
        gamma_n = []
        for f in self.freqs:
            epsilon_n.append('0' if f['0'] > f['1'] else '1')
            gamma_n.append('1' if f['0'] > f['1'] else '0')
        gamma = int(''.join(gamma_n), 2)
        epsilon = int(''.join(epsilon_n), 2)
        return gamma * epsilon

c = GammaCalculator()
shared.parse(sys.argv[1], c.on_number)
print(c.gammaepsilon())
