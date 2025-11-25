import cv2
import torch
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from sam2.sam2_image_predictor import SAM2ImagePredictor

# Load SAM2 from HuggingFace
print("Loading SAM2 model from HuggingFace…")
predictor = SAM2ImagePredictor.from_pretrained("facebook/sam2-hiera-large")

# Load image
IMAGE_PATH = "images/image.jpg"
image = Image.open(IMAGE_PATH).convert("RGB")
image_np = np.array(image)
predictor.set_image(image_np)

def save_mask(mask):
    binary = (mask.squeeze() > 0).astype(np.uint8) * 255
    cv2.imwrite("output/sam2_mask.png", binary)
    print("Saved → output/sam2_mask.png")

def apply_mask(mask):
    plt.imshow(image_np)
    h, w = mask.shape[-2:]
    rgba = np.zeros((h, w, 4))
    rgba[mask.squeeze() > 0] = [0.5, 0, 0.5, 0.6]
    plt.imshow(rgba)

def on_click(event):
    if event.xdata is None:
        return

    x, y = int(event.xdata), int(event.ydata)
    print(f"Clicked: ({x}, {y})")

    input_point = np.array([[x, y]])
    input_label = np.array([1])

    with torch.inference_mode(), torch.autocast("cuda", dtype=torch.bfloat16):
        masks, scores, _ = predictor.predict(
            point_coords=input_point,
            point_labels=input_label,
            multimask_output=True
        )

    best = np.argmax(scores)
    best_mask = masks[best]

    save_mask(best_mask)

    plt.clf()
    apply_mask(best_mask)
    plt.scatter([x], [y], color='lime', s=200)
    plt.axis('off')
    plt.title(f"Score: {scores[best]:.3f}")
    plt.draw()

# Show image and wait for clicks
fig = plt.figure(figsize=(10, 10))
plt.imshow(image_np)
plt.axis('off')
fig.canvas.mpl_connect("button_press_event", on_click)
plt.show()
