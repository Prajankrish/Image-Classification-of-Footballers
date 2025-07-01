from flask import Flask, request, jsonify, render_template, send_from_directory
import util
import os

# Get absolute path to UI folder
UI_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '../UI'))

app = Flask(__name__,
            static_folder=UI_FOLDER,        # UI folder has css, js, images
            template_folder=UI_FOLDER)      # UI folder has app.html

@app.route('/')
def index():
    return render_template('app.html')

@app.route('/classify_image', methods=['POST'])
def classify_image():
    image_data = request.form['image_data']
    response = jsonify(util.classify_image(image_data))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Optional: serve any file from UI folder manually
@app.route('/<path:filename>')
def custom_static(filename):
    return send_from_directory(UI_FOLDER, filename)

if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(port=5000)
