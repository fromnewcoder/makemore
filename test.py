import torch
        
        
g = torch.Generator().manual_seed(2147483647)
p = torch.rand(3, generator = g)
p = p / p.sum()

n_sample = torch.multinomial(p, num_samples=1000, replacement=True, generator=g)

print(n_sample)