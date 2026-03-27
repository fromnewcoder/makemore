
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
    
        self.counts = torch.zeros(27, 27, dtype= torch.int32)

        for name in self._names:
            #print(name)
            nameWithStartEnd = "." + name + "."
            for ch1, ch2 in zip(nameWithStartEnd, nameWithStartEnd[1:]):
                self.counts[self.stoi[ch1], self.stoi[ch2]] += 1
                #print(f"{ch1} --> {ch2}")
       
        #self.probs = self.counts / self.counts.sum(dim = 1, keepdim=True)
        #print(f"{[f'{x:.4f}' for x in self.probs[0]]}")
        g = torch.Generator().manual_seed(2147483647)
        #p = torch.rand(3, generator = g)
        #print(torch.multinomial(p, num_samples=100, replacement=True, generator=g))
        ix = 0
        for i in range(5):
            out = []
            while True:
                p = self.counts[ix].float()
                p = p / p.sum()
                ix = torch.multinomial(p, num_samples=1, replacement=True, generator=g).item()
                out.append(self.itos[ix])
                if ix == 0 :
                    break
            print(''.join(out))
        

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
