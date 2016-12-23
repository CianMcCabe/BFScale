import os
import sys
from flask import Flask, render_template, request, send_from_directory
from Image_class import Image

__author__ = 'ibininja'

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

#Global Var
working_image=0

# render index.html
@app.route("/")
def index():
    return render_template("index.html")

# upload and save image
@app.route("/upload", methods=['GET', 'POST'])
def upload():
    global working_image
    target = os.path.join(APP_ROOT, 'static/')
    print(target)

    # create directory if it doesnt exist
    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)

    # Creat instance of class
    # Generate Image with numbered objects

    #Change to filename,path
    working_image= Image(filename, target)
    fname_index_image, path = working_image.generate_index_image()
    print ("Filename:" + fname_index_image)
    print ("Path:" + path)

    # Pass the place where the image is stored through this render
    return render_template("complete.html", image_name=fname_index_image)

# send the file
@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("static", filename)

# accept user input and pass it Image_class methods
@app.route('/upload/user_input', methods=['GET', 'POST'])
def select():
    global working_image
    target_object = request.values['target_object']
    ref_object = request.values['ref_object']

    print("target object"+str(target_object))
    print("ref object"+str(ref_object))

    working_image.update_ref_object_index(int(ref_object))
    working_image.update_measure_object_index(int(target_object))
    fname_measured_image, path = working_image.generate_measured_image()

    print("fname_measured_image: " + str(fname_measured_image))

    return render_template("final.html",image_name=fname_measured_image)

if __name__ == "__main__":
    app.run(port=4555, debug=True)
