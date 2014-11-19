from flask import Flask, render_template, request, send_file
from PIL import Image
from lib.grid import grid
import StringIO
import base64
import urllib
import os
import sys

app = Flask(__name__)


def encode_image(image, extension):
    """Encode the image in base64 format, removing trailing newlines."""

    # Image.save will only take format="jpeg", not format="jpg"
    if extension.lower() == "jpg":
        extension = "jpeg"

    strIO = StringIO.StringIO()
    image.save(strIO, format=extension)
    encoded = base64.b64encode(strIO.getvalue())
    return urllib.quote(encoded.rstrip('\n'))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the raw image, converted to RGB, from the request
        f = request.files['file']
        image = Image.open(f).convert('RGBA')
        _, extension = os.path.splitext(f.filename)
        # We don't want the . from the file extension
        extension = extension[1:]

        # Add the grid lines
        image = grid(image, ylines=int(request.form['ylines']))

        # Encode to base64, removing trailing newlines and serve
        return render_template('index.html', image_format=extension,
                                image_url=encode_image(image, extension))

    if request.method == 'GET':
        return render_template('index.html')


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'production':
        app.run(debug=False, port=os.environ['PORT'])
    else:
        app.run(debug=True)
