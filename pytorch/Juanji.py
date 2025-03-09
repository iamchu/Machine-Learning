import  torch
import torchvision
from torch.nn import Conv2d
from torch.utils.data import DataLoader
from torch import nn
from torch.utils.tensorboard import SummaryWriter

from transforms import writer

#引入数据集
dataset = torchvision.datasets.CIFAR10("./dataset",train=False,transform=torchvision.transforms.ToTensor(),download=True)
#加载数据集
dataloader = DataLoader(dataset,batch_size=64)

class Juanji(nn.Module):
    def __init__(self):
        super(Juanji,self).__init__()
        self.conv1 = Conv2d(in_channels=3,out_channels=6,kernel_size=3,stride=1,padding=0)

    def forward(self,x):
        x = self.conv1(x)
        return x

Juanji_test = Juanji()

writer = SummaryWriter("logs2")

step = 0
for data in dataloader:
    imgs,targets = data
    output = Juanji_test(imgs)
    print(output.shape)
    writer.add_images("input",imgs,step)
    output = torch.reshape(output, (-1, 3, 30, 30))
    writer.add_images("output",output,step)

    step = step + 1