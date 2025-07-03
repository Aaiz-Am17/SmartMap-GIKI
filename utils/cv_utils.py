# utils/cv_utils.py
import torch
from torchvision import models, transforms
from PIL import Image
import os

LANDMARK_COORDS = {
    "Clocktower": (34.068778, 72.645029),
    "ACB": (34.070246, 72.643294),
    "Audi": (34.069534, 72.643996),
    "FES": (34.069736, 72.642669),
    "FCSE": (34.069484, 72.643565),
    "FMCE_frontside": (34.070125, 72.645144),
    "Fme_frontside": (34.069840, 72.644613),
    "Fme_backside": (34.068969, 72.645429),
    "Guest house": (34.068876, 72.645952),
    "Hbl": (34.069512, 72.646135),
    "Library": (34.071015, 72.643657),
    "Tuc": (34.069686, 72.647110),
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.abspath(os.path.join(BASE_DIR, '..', 'models', 'building_classifier.pth'))  # Path to saved model
DEFAULT_COORDS = (34.068283, 72.644278)

def load_model():
    checkpoint = torch.load(MODEL_PATH, map_location=torch.device("cpu"))
    class_names = checkpoint["class_names"]

    model = models.mobilenet_v2(pretrained=False)
    model.classifier[1] = torch.nn.Linear(model.last_channel, len(class_names))
    model.load_state_dict(checkpoint["model_state_dict"])
    model.eval()
    return model, class_names

def preprocess_image(image_path):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225]),
    ])
    image = Image.open(image_path).convert("RGB")
    return transform(image).unsqueeze(0)

def predict_and_locate(image_path):
    try:
        model, class_names = load_model()
        image_tensor = preprocess_image(image_path)
        with torch.no_grad():
            outputs = model(image_tensor)
            _, predicted = torch.max(outputs, 1)
            label = class_names[predicted.item()]
            coords = LANDMARK_COORDS.get(label, DEFAULT_COORDS)
            return label, coords
    except Exception as e:
        print(f"[ERROR] Prediction failed: {e}")
        return "Unknown", DEFAULT_COORDS
