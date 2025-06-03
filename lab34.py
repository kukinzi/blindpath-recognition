#uniform filter using torch 
import torch
import torchvision
import matplotlib
import torchvision.transforms as transforms
from PIL import Image
import matplotlib.pyplot as plt
transform=transforms.Compose([transforms.Resize(256), 
                             transforms.ToTensor()])
ip="/Users/yifanwang/blindpathdetection/codinghomework/test1.jpg"
i = Image.open(ip).convert("RGB")
i = transform(i)
res=torch.zeros(i.shape)
print(i.shape)
for a in range(3):
    for b in range(256):
        for c in range(394):
            res[a,b,c]=torch.mean(i[a,b:b+3,c:c+3])
out=res.squeeze(0).permute(1,2,0)
plt.imshow(out)
plt.show()



