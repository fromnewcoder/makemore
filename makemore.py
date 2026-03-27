
import torch

class MyDataSet:

    def __init__(self):
        with open("names.txt", 'r') as f:
            self._names = f.readlines()
        self._names = [ name.strip() for name in self._names]
        chars = sorted(list(set("".join(self._names))))
        self.stoi = {ch: i for i, ch in enumerate(['.'] + chars)}
        self.itos = {i: ch for ch, i in self.stoi.items()}
    
        counts = torch.ones(27, 27)

        for name in self._names[:5]:
            print(name)
            nameWithStartEnd = "." + name + "."
            for ch1, ch2 in zip(nameWithStartEnd, nameWithStartEnd[1:]):
                counts[self.stoi[ch1], self.stoi[ch2]] += 1
                print(f"{ch1} --> {ch2}")

        self.probs = counts / counts.sum(dim = 1, keepdim=True)
        #print(probs)

    

if __name__ == "__main__":
    md = MyDataSet()
