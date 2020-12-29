from torch.autograd import Variable
from torch import nn
from torchvision import transforms, models


model = models.vgg16_bn(pretrained=True)
# Freeze model weights
for param in model.parameters():
    param.requires_grad = False
model.classifier[6] = nn.Sequential(
                      nn.Linear(4096, 256), 
                      nn.ReLU(), 
                      nn.Dropout(0.5),
                      nn.Linear(256, 20),                   
                      nn.LogSoftmax(dim=1))
for param in model.classifier[6].parameters():
    param.requires_grad = True
model.load_state_dict(torch.load(PATH))

       

test_transform=transforms.Compose([
                              transforms.Resize(size=256),
                              transforms.CenterCrop(size=224),
                              transforms.ToTensor(),
                              transforms.Normalize([0.485, 0.456, 0.406],
                                                   [0.229, 0.224, 0.225])
                              ])   

classes=['biriyani',
 'bisibelebath',
 'butternaan',
 'chaat',
 'chappati',
 'dhokla',
 'dosa',
 'gulab jamun',
 'halwa',
 'idly',
 'kathi roll',
 'meduvadai',
 'noodles',
 'paniyaram',
 'poori',
 'samosa',
 'tandoori chicken',
 'upma',
 'vada pav',
 'ven pongal']

def predict_image(image):
    image_tensor = test_transform(image).float()
    image_tensor = image_tensor.unsqueeze_(0)
    input = Variable(image_tensor)
    input = input.to(device)
    output = model(input)
    index = output.data.cpu().numpy().argmax()
    pred=classes[index]
    return pred,index