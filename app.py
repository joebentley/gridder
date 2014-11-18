from flask import Flask, render_template, request, send_file
from PIL import Image
import StringIO
import base64
import urllib

app = Flask(__name__)


def encode_image(image):
    """Encode the image in base64 format, removing trailing newlines."""
    strIO = StringIO.StringIO()
    image.save(strIO, 'JPEG')
    encoded = base64.b64encode(strIO.getvalue())
    return urllib.quote(encoded.rstrip('\n'))

def grid():
    pass


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the raw image, converted to RGB, from the request
        image = Image.open(request.files['file']).convert('RGB')

        # Add the grid lines

        # Encode to base64, removing trailing newlines and serve
        return render_template('index.html', image_url=encode_image(image))

    if request.method == 'GET':
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
