import tensorflow as tf
import numpy as np
from PIL import Image

# Load the model
model = tf.saved_model.load("model.savedmodel")

# Load labels
with open("labels.txt", "r") as f:
    labels = [line.strip().split(" ", 1)[1] for line in f.readlines()]

# Function to preprocess image
def preprocess_image(image_path):
    img = Image.open(image_path).convert("RGB")
    img = img.resize((224, 224))  # Make sure this matches your training input size
    img_array = np.array(img) / 255.0  # Normalize if model expects it
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dim
    return tf.convert_to_tensor(img_array, dtype=tf.float32)

# Inference function
def predict(image_path):
    input_tensor = preprocess_image(image_path)
    infer = model.signatures["serving_default"]
    output = infer(input_tensor)
    pred = tf.argmax(list(output.values())[0], axis=1).numpy()[0]
    return labels[pred]

# Test it
if __name__ == "__main__":
    path = "rotation_270_light_11_missing_hole_08_5_600.jpg" # Add a test image here
    print("Predicted:", predict(path))
