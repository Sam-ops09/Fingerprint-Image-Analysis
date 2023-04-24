# Fingerprint-Image-Analysis

This project is a Python implementation of a fingerprint image analysis system. The system processes fingerprint images and extracts features that can be used for fingerprint matching and identification. The project consists of several modules that perform different tasks such as image enhancement, feature extraction, and matching.

## Dependencies:
- Python 3.x
- NumPy
- OpenCV
- Scikit-image
- Matplotlib

## Installation:
1. Clone the repository: `git clone https://github.com/Sam-ops09/Fingerprint-Image-Analysis.git`
2. Navigate to the project directory: `cd Fingerprint-Image-Analysis`
3. Install the required packages: `pip install -r requirements.txt`

## Usage:
1. Run the Jupyter notebook: `jupyter notebook`
2. Open the notebook "Fingerprint Image Analysis.ipynb" in your browser.
3. Follow the instructions in the notebook to process and analyze fingerprint images.

Alternatively, you can use the modules in this project to build your own fingerprint analysis system. The following modules are available:

- `enhancement.py`: contains functions for enhancing fingerprint images using histogram equalization, adaptive histogram equalization, and other techniques.
- `segmentation.py`: contains functions for segmenting the fingerprint image into its foreground (ridges) and background (valleys) components.
- `minutiae.py`: contains functions for extracting minutiae from the segmented fingerprint image.
- `matching.py`: contains functions for matching two fingerprint images based on their extracted minutiae.

To use these modules in your own project, import the desired module into your Python script and call the relevant functions.

## License:
This project is licensed under the MIT License. See the LICENSE file for details.

## References:
The algorithms and techniques used in this project are based on the following research papers:
- "A Robust Minutiae Extraction Algorithm for Fingerprint Images" by S. S. Rautaray and A. K. Lenka
- "An Efficient Fingerprint Matching Algorithm Using Minutiae" by G. R. Reddy and A. V. N. Reddy.
