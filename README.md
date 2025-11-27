## 🎥 Demonstration Videos

### 🛒 Multiple Grocery Item Segmentation
[![Grocery Items Segmentation](assets/grocessry_items.gif)](assets/grocessry_items.webm)

This demonstration shows a large-scale visualization of segmentation results for **multiple grocery items** within a single image.  
The full-size GIF highlights the interactive, click-based selection and the generation of corresponding **binary masks** for each object.

---

### 🤖 Vision-Based Robotic Object Grasping
[![Object Picking Segmentation](assets/object_picking.gif)](assets/object_picking.webm)

This demonstration presents **vision-based image segmentation for robotic grasping**, illustrating how a user-selected click guides the SAM-2 model to accurately isolate a target object. The resulting binary mask can be directly used to guide robotic manipulators during grasp execution.

---

# 💜 SAM-2 Interactive Image Segmentation for Robotic Grasping

This project implements an **interactive, click-based image segmentation system** built on **SAM-2 (Segment Anything Model 2)** from Hugging Face.  
The system enables a **human-in-the-loop segmentation workflow** to generate accurate binary masks suitable for **robotic manipulation and object grasping pipelines**.

---

## 🚀 Getting Started

### System Requirements

The system requirements are derived directly from the implementation:

- **Python:** 3.10 or higher  
- **Core libraries:**  
  - **PyTorch** – SAM-2 inference and GPU acceleration  
  - **OpenCV (`cv2`)** – binary mask generation and saving  
  - **NumPy** – numerical operations and array handling  
  - **Matplotlib** – interactive visualization and mouse-click handling  
  - **Pillow (PIL)** – image loading and preprocessing  
- **Hardware (recommended):**  
  - NVIDIA GPU with CUDA support for faster inference  
  - CPU-only execution is supported but slower  

---

## 🔧 Installation

1. **Clone the repository**  
   git clone <REPOSITORY_URL>  
   cd image-segmentation-for-robotic-grasping  

2. **Create and activate a virtual environment (recommended)**  
   python -m venv sam2  
   source sam2/bin/activate  

3. **Install project dependencies**  
   pip install .  

---

## 🧪 Usage

1. Place an input image in the `images/` directory (for example: `images/items.jpg`).  
2. Run the main script:  
   python main.py  
3. Click on the desired object in the displayed Matplotlib window.  

The system will run SAM-2 inference using the clicked point as a prompt, select the highest-scoring mask, and save the resulting binary mask to:  
output/sam2_mask.png  

---

## 🧠 Implementation Overview

The input image is loaded using Pillow (PIL) and converted to a NumPy array.

A pretrained SAM2ImagePredictor is initialized using the SAM-2 hierarchical model from Hugging Face.

User mouse clicks are captured using Matplotlib event callbacks.

Click coordinates are passed as point prompts to the SAM-2 predictor.

Multiple candidate masks are produced, and the highest-scoring mask is selected.

The final segmentation mask is saved using OpenCV and visualized as a transparent overlay on the original image.

---

## 📚 References

Meta AI Research — Segment Anything Model 2 (SAM-2)  

Hugging Face Model Hub — SAM-2 pretrained checkpoints  

PyTorch Documentation — inference mode and automatic mixed precision  

OpenCV Documentation — binary image processing  

