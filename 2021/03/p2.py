import sys, shared
class GammaCalculator:
    def __init__(self):
        self.numbers = [[], []]
        self.o_numbers = None
        self.co2_numbers = None
    def on_number(self, n):
        n = str(n)
        b = int(n[0])
        self.numbers[b].append(n)
        if len(self.numbers[0]) > len(self.numbers[1]):
            self.o_numbers = self.numbers[0]
            self.co2_numbers = self.numbers[1]
        else:
            self.o_numbers = self.numbers[1]
            self.co2_numbers = self.numbers[0] 

    def oco2(self):
        return self.o() * self.co2()

    def co2(self):
        numbers = self.co2_numbers[:]
        freq_ptr = 1
        while len(numbers) > 1:
            groups = [[], []]
            for n in numbers:
                groups[int(n[freq_ptr])].append(n)
            if len(groups[0]) <= len(groups[1]):
                numbers = groups[0]
            else:
                numbers = groups[1]
            freq_ptr += 1
        assert len(numbers) == 1
        return int(numbers[0], 2)


    def o(self):
        numbers = self.o_numbers[:]
        freq_ptr = 1
        while len(numbers) > 1:
            groups = [[], []]
            for n in numbers:
                groups[int(n[freq_ptr])].append(n)
            if len(groups[1]) >= len(groups[0]):
                numbers = groups[1]
            else:
                numbers = groups[0]
            freq_ptr += 1
        assert len(numbers) == 1
        return int(numbers[0], 2)

c = GammaCalculator()
shared.parse(sys.argv[1], c.on_number)
print(c.oco2())
