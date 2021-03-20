#https://www.javatpoint.com/flask-file-uploading
from flask import *
from kmeans import k_cluster
from utils import flatten_input, unflatten_input, image_to_mat
from PIL import Image as im
import numpy as np
from keras.preprocessing.image import save_img
import gunicorn
import os, re, os.path
import gc

def get_size(fobj):

    if fobj.content_length:
        return fobj.content_length

    try:
        pos = fobj.tell()
        fobj.seek(0, 2)  #seek to end
        size = fobj.tell()
        fobj.seek(pos)  # back to original position
        return size
    except (AttributeError, IOError):
        pass

    # in-memory file object that doesn't support seeking or tell
    return 0  #assume small enough



app = Flask(__name__)
@app.route('/')
def upload():
    return render_template("file_upload_form.html")

@app.route('/success', methods = ['POST'])
def success():
    folder = "static/"

    if request.method == "POST":
        gc.collect()
        for root, dirs, all_files in os.walk(folder):
            for item in all_files:
                if item!= "sample.png":
                    os.remove(os.path.join(root, item))
        f = request.files["file"]
        obj_size = get_size(f) 

        if obj_size > 200*1024:
            abort(413)


        if obj_size == 0:
            abort(400, "please upload a picture before submission")

        if len(request.form.get("num_clusters"))!=0:
            num_clus = int(request.form.get("num_clusters"))
        else:
            abort(400, "please set the number of clusters before submission")
        out = folder+f.filename
        f.save(out)
        image_mat = image_to_mat(out)
        new_image = k_cluster(image_mat, k=num_clus)
        del image_mat
        raw_name = f.filename.split(".")[0] + "_cluster"+ str(num_clus) \
                    + ".png" 
        path_out = folder + raw_name 
        save_img(path_out, new_image)
        del new_image
        gc.collect()
        return render_template("success.html", name = out, num_clusters = num_clus, processed_img = path_out )


if __name__ == '__main__':
    app.run(debug = True)
