# Flask Demo

Demo of my progression of developing Flask applications.

Order of progression lines up with the alphabetical ordering:

1. flask_app.py

    Native Flask application with manual input validation and manual output jsonification

2. flask_marshmallow_app.py

    Native Flask application with manual input validation via Marshmallow

3. smorest_app.py

    Flask appliation with flask-smorest Blueprints to automatically integrate Marshmallow input validation.
    But still get a dict inside the route function.

4. smorest_class_app.py

    Flask appliation with flask-smorest Blueprints to automatically integrate Marshmallow input validation.
    But get a class inside the route function. Downside is that we need both a DTO schema and DTO class.

5. smorest_dataclass_app.py

    Flask appliation with flask-smorest Blueprints to automatically integrate Marshmallow input validation.
    Get a class inside the route function. Only need to define a dataclass, which will generate the DTO schema.
