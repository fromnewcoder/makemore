
import torch
import matplotlib.pyplot as plt
class MyDataSet:

    def __init__(self):
        with open("names.txt", 'r') as f:
            self._names = f.readlines()
        self._names = [ name.strip() for name in self._names]
        chars = sorted(list(set("".join(self._names))))
        self.stoi = {ch: i for i, ch in enumerate(['.'] + chars)}
        self.itos = {i: ch for ch, i in self.stoi.items()}
    
        self.counts = torch.ones(27, 27)

        for name in self._names[:]:
            #print(name)
            nameWithStartEnd = "." + name + "."
            for ch1, ch2 in zip(nameWithStartEnd, nameWithStartEnd[1:]):
                self.counts[self.stoi[ch1], self.stoi[ch2]] += 1
                #print(f"{ch1} --> {ch2}")

        self.probs = self.counts / self.counts.sum(dim = 1, keepdim=True)
        g = torch.Generator().manual_seed(2147483647)
        pname = ""
        while True:
            parr = torch.multinomial(self.probs, num_samples=1, replacement=True, generator=g)
            pch = self.itos[parr[0].item()]
            if pch == '.':
                break
            pname += pch
        print(pname)
        

        #print(probs)
    def printCounts(self):
        plt.figure(figsize=(16, 16))
        plt.imshow(self.counts, cmap="Blues")
        for i in range(27):
            for j in range(27):
                chstr = self.itos[i] + self.itos[j]
                plt.text(j, i, chstr, ha = "center")
    

if __name__ == "__main__":
    md = MyDataSet()
    #md.printCounts()
