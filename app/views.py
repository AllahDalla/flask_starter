"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
import os
from app import app
from flask import render_template, request, redirect, url_for, send_from_directory, flash
from app.forms import CreateProperty
from app import db
from app.models import PropertyInfo
from werkzeug.utils import secure_filename



###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/properties')
def properties():
    images = get_uploaded_images()
    
    if(len(images) == 0):
        return redirect(url_for('createProperty'))
    return render_template("properties.html", images=images)

@app.route('/properties/create', methods=['POST', 'GET'])
def createProperty():
    form = CreateProperty()
    if(request.method == 'POST'):
        if(form.validate_on_submit()):
            title = form.propertyTitle.data
            description = form.propertyDescription.data
            rooms = int(form.numberRooms.data)
            bathrooms = int(form.numberBathrooms.data)
            price = int(form.price.data)
            type = form.propertyType.data
            location = form.location.data
            photo = form.photo.data
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            try:
                data = PropertyInfo(title=title, description=description, rooms=rooms, bathrooms=bathrooms, price=price, type=type, location=location, photo=filename)
                db.session.add(data)
                db.session.commit()
            except Exception as e:
                print(e)
            finally:            
                flash("Property successfully added!", True)
                return redirect(url_for('properties'))
    return render_template("add_property.html", form=form)

@app.route('/propertiesImages/<propertyImage>')
def propertyImage(propertyImage):
    return send_from_directory(os.path.join(os.getcwd(),app.config['UPLOAD_FOLDER']), propertyImage)


@app.route('/properties/<propertyid>')
def property(propertyid):
    imageID = get_uploaded_images()
    return send_from_directory(os.path.join(os.getcwd(),app.config['UPLOAD_FOLDER']), imageID[int(propertyid)])

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


def get_uploaded_images():
    rootdir = os.getcwd()
    lst = []
    for subdir, dir, files in os.walk(rootdir+ '/uploads'):
        # print(subdir)
        for file in files:
            lst.append(os.path.join(file))
    #lst.pop(0) # .gitkeep is in the uploads dir so this takes that into account
    return lst