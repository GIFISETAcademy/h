from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        image = request.files['image']
        # Save the uploaded image to a desired location
        image.save('uploads/' + image.filename)
        # Generate a link to the uploaded image
        image_link = 'https://example.com/uploads/' + image.filename
        return f'Image uploaded successfully! View it <a href="{image_link}">here</a>.'
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
