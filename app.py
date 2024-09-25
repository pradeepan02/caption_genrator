from flask import Flask, request, render_template
from PIL import Image
import os
from transformers import BlipProcessor, BlipForConditionalGeneration

# Initialize the Flask app
app = Flask(__name__)

# Load the processor and model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Function to generate caption
def generate_caption(image):
    inputs = processor(image, return_tensors='pt')
    outputs = model.generate(**inputs)
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    return caption

# Home route that handles both image upload and URL input
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # If an image is uploaded
        if "image" in request.files:
            file = request.files["image"]
            if file and file.filename != "":
                # Open the image using PIL
                image = Image.open(file)
                caption = generate_caption(image)

                # Save the image temporarily
                image_path = os.path.join("static", "uploads", file.filename)
                os.makedirs(os.path.dirname(image_path), exist_ok=True)
                image.save(image_path)

                return render_template("result.html", caption=caption, image_url=image_path)

    return render_template("index.html")

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
