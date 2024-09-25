# Image Captioning Web App

This project is a web application that generates captions for uploaded images using the BLIP (Bootstrapping Language-Image Pre-training) model. It is built using Flask, a lightweight web framework for Python, and leverages the Transformers library for image captioning.

## Features

- Upload images and receive generated captions.
- Responsive design suitable for both desktop and mobile devices.
- Interactive user interface with smooth transitions and effects.
- Utilizes the BLIP model for high-quality image captioning.

## Technologies Used

- **Flask**: For building the web application.
- **PIL (Pillow)**: For image processing.
- **Transformers**: For leveraging pre-trained models for image captioning.
- **HTML/CSS**: For the front-end interface.

## Installation

To run this project locally, follow these steps:

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Clone the Repository


git clone https://github.com/yourusername/image-captioning-web-app.git
cd image-captioning-web-app

# Create a virtual environment
python -m venv venv
# Activate the virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install the required packages
pip install -r requirements.txt


After installing the dependencies, you can run the Flask application:
python app.py

