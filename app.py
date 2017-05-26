from flask import Flask, render_template, request
from flask_uploads import configure_uploads, UploadSet, IMAGES

app = Flask(__name__)
app.config.update({
    'UPLOADS_DEFAULT_DEST': '/tmp/uploads',
    'UPLOADS_DEFAULT_URL': 'http://localhost:5000'
})

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        return 'uploaded'
    return "nothing to see here, move along."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)