from fastapi import FastAPI, UploadFile, File
from PIL import Image
import torch
from torchvision import models, transforms

app = FastAPI()

model = models.resnet50(weights=models.ResNet50_Weights.DEFAULT)
model.eval()

preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

labels = models.ResNet50_Weights.DEFAULT.meta["categories"]

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = Image.open(file.file).convert("RGB")

    input_tensor = preprocess(image)
    input_batch = input_tensor.unsqueeze(0)

    with torch.no_grad():
        output = model(input_batch)

    predicted_class = output.argmax(1).item()

    return {
        "class": labels[predicted_class]
    }