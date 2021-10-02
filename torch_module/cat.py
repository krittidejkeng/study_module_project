import torch

"""
torch.cat(tensors, dim=0, *, out=None) concatenates the given sequence of seq tensors in the given dimension. 
All tensors must either have the same shape (except in the concatenating dimension) or be empty.

tensors (sequence of Tensors) – any python sequence of tensors of the same type. 
Non-empty tensors provided must have the same shape, except in the cat dimension.

dim (int, optional) – the dimension over which the tensors are concatenated
"""
x = torch.randn(3,3)
print(x,"\n")
print(torch.cat((x, x, x), 0),"\n")
print(torch.cat((x, x, x), 1),"\n")
print(torch.cat((x, x, x), 2),"\n")
