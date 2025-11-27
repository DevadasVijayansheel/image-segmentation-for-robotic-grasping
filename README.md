### 🎥 Demonstration Videos

Here are demonstrations of the interactive image segmentation process using the SAM-2 model.

| Demo Video | Description |
| :---: | :--- |
| <video src="assets/grocessry_items.webm" controls width="400" muted></video> | Demonstrates the segmentation of **multiple grocery items** in a single image. |
| <video src="assets/object_picking.webm" controls width="400" muted></video> | Shows the process of generating a **single mask** for object picking tasks. |

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
