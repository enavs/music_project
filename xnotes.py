# Step 1. create the name of your main/root folder
file structure should be:
Eddie
    app folder
        static folder
            css folder
                main.css file
            images folder
            js folder
        templates folder
            index.html file
            etc.html file
        __init__.py file
        views.py file
.env file
config.py file
run.py file

# Step 2. create a virtual environment.  note that the 'venv "venv"' part looks the same but the last venv can be whatever name you want
    python3 -m venv venv
# Step 3. activate your virutal environment
    . venv/bin/activate
# Step 4. install flask
    # if you need to install a newer version type:
    pip3 install --upgrade pip
    # install flask
    pip install flask
# Step 5. import flask
    # import flask
# Step 6. create the flask environment by selecting the file to run
    export FLASK_APP=run.py
    # if you don't want to keep setting this export to be the same file in every new terminal type.  Just run the below and save the export FLAS_APP= in the .flaskenv file
    pip install python-dotenv
# Step 7. run the files by doing:
    flask run
    # to quit type:
    Press CTRL+C to quit)
# Step 8. to make your changes dynamic and to move to the development server type this:
    export FLASK_ENV=development
# Step 9. install extra packages
    # pip install flask-wtf
    pip3 install requests
    pip install beautifulsoup4
    pip install flask-sqlalchemy
    pip install flask-migrate
    pip install wheel
    pip install python-dotenv
    pip install flask-moment
    pip install flask_login
    pip install shortuuid
    pip install flask-mail
    pip install stripe

# install Elephant SQL
    pip install psycopg2-binary
# 
    pip install wheel
# Step 10. let's create a migration repository for our database.  Only run this once.  Don't run it again.  
    flask db init
# Step 11. this generates the automatic migrations.  You can add in "-m" to give a short description of what you migrated
    flask db migrate
# Step 12. you need to push or upgrade to make changes to your database
    flask db upgrade
# Step 13. flask login information that saves login details across webpages
    pip install flask-login
# Step 14. validator - email
    pip install email-validator

# Step 15. pip freeze will pull down all of the installations/packages that you have done.  
# But them all in a file called requirements.txt
    pip freeze
    # or you can do it this way
    pip freeze > requirements.txt

    # installing my requirements file
    pip install -r requirements.txt



# If you want to fork someone's data
# to install everything that has a requirements.txt file
# create a python virtual environment
    python3 -m venv venv
# activate the environment
    . venv/bin/activate
# create your .env file in your root foler
    touch .env 
# install all of the packages
    pip install -r requirements.txt
# initializing the database
    flask db init
    # if you wanted to use your lastest version that you saved type
        flask db stamp head
# run your program
    flask run






# creating blueprints automatically
# create a cli.py file and put this stuff in it
import click, os

def register(app):
    @app.cli.group()
    def blueprint():
        """Blueprint creation commands."""
        pass

    @blueprint.command()
    @click.argument('name')
    def create(name):
        """Create new Flask Blueprint"""
        bp_name = os.path.abspath(os.path.dirname(__name__)) + f'/app/blueprints/{name}'
        try:
            if not os.path.exists(bp_name):
                os.makedirs(bp_name)
                init_file = open(f'{bp_name}/__init__.py', 'w')
                init_file.close()
                views_file = open(f'{bp_name}/views.py', 'w')
                views_file.close()
                models_file = open(f'{bp_name}/models.py', 'w')
                models_file.close()
                print('Blueprint created successfully')
        except Exception as error:
            print(f'Something went wrong with creating the Blueprint {bp_name}.')
            print(error)
# use this code to execute and run the program
    flask blueprint create shop


# storage for pictures
cloudery
aws
save the images to those and save the image to the storage servers and use the link as the picture image to show
