
## 🎥 Demonstration Videos

### 🛒 Multiple Grocery Item Segmentation
[![Grocery Items Segmentation](assets/grocessry_items.gif)](assets/grocessry_items.webm)

Demonstrates segmentation of **multiple grocery items** and generation of corresponding **binary masks** in a single image.

---

### 🤖 Vision-Based Robotic Object Grasping
[![Object Picking Segmentation](assets/object_picking.gif)](assets/object_picking.webm)

Demonstrates **vision-based image segmentation for robotic grasping**, enabling a manipulator to identify and accurately grasp a target object.



# 💜 SAM-2 Interactive Image Segmentation

This project provides an interactive, click-based interface for image segmentation using the **SAM-2 (Segment Anything Model 2)** from Hugging Face.

## 🚀 Getting Started

### Prerequisites

* Python 3.10+ 
* A system with an NVIDIA GPU and CUDA for optimal performance.

### Installation (using pyproject.toml)

1.  **Clone the repository:**
    ```bash
    git clone [Your-Repo-URL]
    cd hugging_face 
    ```

2.  **Activate your virtual environment:**
    ```bash
    create a virtual environment (optional but recommended) say sam2
    python -m venv sam2
    source sam2/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install .
    ```

### Usage

1.  Ensure your image is in the `images/` directory. you can 
2.  Run the main script:
    ```bash
    python main.py
    ```
3.  Click on an object in the displayed Matplotlib window to generate and save the mask to `output/sam2_mask.png`.
