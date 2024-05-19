
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from tqdm import tqdm

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.w1 = nn.Parameter(torch.tensor([
            [0.1, 0.15],
            [0.2, 0.25],
            [0.3, 0.35]
        ]))
        self.w2 = nn.Parameter(torch.tensor([
            [0.4, 0.5, 0.6],
            [0.45, 0.55, 0.65]
        ]))
        self.b1 = nn.Parameter(torch.tensor(0.35))
        self.b2 = nn.Parameter(torch.tensor(0.65))

    def forward(self, x, y):
        """
            Note:forward名称不允许写错
        :param x:
        :param y:
        :return:
        """
        # 第一层
        h = x @ self.w1.T
        h = F.sigmoid(h + self.b1)
        # 第二层
        o = F.sigmoid(torch.add(torch.matmul(h, self.w2.T) , self.b2))
        # 损失计算
        loss = 0.5 * torch.sum(torch.pow(y-o, 2))
        return loss

if __name__ == '__main__':
    _net = Net()
    _x = torch.from_numpy(np.asarray([[5, 10]])).float()
    _y = torch.tensor([[0.01, 0.99]]).float()

    for i in tqdm(range(1000)):
        _net.zero_grad()
        _loss= _net(_x, _y) # 前向过程
        _loss.backward() # 反向过程
        # 参数值更新
        with torch.no_grad():
            for param in _net.parameters():
                param -= 0.5 * param.grad
    print("最终损失为：", _loss.item())
    print(_net.w1)
    print(_net.b1)