from flask import Flask, request, render_template
from PIL import Image
import requests
from transformers import BlipProcessor, BlipForConditionalGeneration
import io

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

# Home route that handles both image upload
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # If an image is uploaded
        if "image" in request.files:
            file = request.files["image"]
            if file and file.filename != "":
                # Open the image using PIL
                image = Image.open(file.stream)
                caption = generate_caption(image)
                # Convert image to bytes for display
                image_bytes = io.BytesIO()
                image.save(image_bytes, format='PNG')
                image_bytes.seek(0)
                image_url = f"data:image/png;base64,{base64.b64encode(image_bytes.getvalue()).decode()}"
                return render_template("result.html", caption=caption, image_url=image_url)

    return render_template("index.html")

# Run the Flask app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)), debug=True)
