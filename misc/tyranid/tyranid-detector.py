import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

from PIL import Image

import sys

from os import path

inp = input(f"Enter 50 pixels to change with format x,y,r,g,b-x,y,r,g,b-x,y,r,g,b...: ")

pixels = inp.split("-")

if len(pixels) != 50:
    print(f"{len(pixels)} pixels, not the required 50")
    sys.exit(0)

num_of_channels = 3
image_resolution = (224, 224,)

class Tyranid_Detector_MLP(nn.Module):
    def __init__(self):
        super().__init__()
        
        self.input_layer = nn.Linear(num_of_channels * image_resolution[0] * image_resolution[1], 250)
        self.hidden_1_layer = nn.Linear(250, 100)
        self.hidden_2_layer = nn.Linear(100, 10)
        self.output_layer = nn.Linear(10, 2)
        
    def forward(self, x):
        x = x.unsqueeze(0)
        x = x.reshape(-1, num_of_channels * image_resolution[0] * image_resolution[1])        
        h_1 = F.relu(self.input_layer(x))
        h_2 = F.relu(self.hidden_1_layer(h_1))
        h_3 = F.relu(self.hidden_2_layer(h_2))
        y_pred = self.output_layer(h_3)
        return y_pred
    
print("Loading model...")
model = Tyranid_Detector_MLP()
if path.exists('./sensor-model.pt'):
    model.load_state_dict(torch.load('./sensor-model.pt'))
print("Model Loaded!")
    
original = np.array(Image.open('./potential-tyranid.png'))
modified = original.copy()

x = torch.tensor(modified.transpose(2, 0, 1) / 255.0, dtype=torch.float32).unsqueeze(0)
with torch.no_grad():
    y = torch.sigmoid(model(x))
    
if y >= 0.5:
    print("Space marine detected")
else:
    with open("flag.txt", "r") as f:
        print("Tyranid detected. Extermanitus deployed.")
        print(f.read())