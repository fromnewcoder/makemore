
import torch

class MyDataSet:

    def __init__(self):
        with open("names.txt", 'r') as f:
            self._names = f.readlines()
        self._names = [ name.strip() for name in self._names]
        chars = sorted(list(set("".join(self._names))))
        self.stoi = {}
        self.itos = {}
        for i, ch in enumerate(["."]+ chars):
            self.stoi[ch] = i
            self.itos[i] = ch
        #print(self.stoi)   
  
        counts = torch.ones(27, 27)

        for name in self._names[:5]:
            print(name)
            first = "."
            for i,ch in enumerate(name + "."):
                counts[self.stoi[first], self.stoi[ch]] += 1
                print(f"{first} --> {ch}")
                first = ch

        row_sums = counts.sum(dim = 1, keepdim=True)
        print(row_sums)
        probs = counts/row_sums
        print(probs)



if __name__ == "__main__":
    md = MyDataSet()