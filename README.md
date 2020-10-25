To use this application: Create a new Pycharm Django Project using this folder for the source. Answer 'Yes' when prompted to use the files from this folder for the new project. Settings: Set up the project interpreter to reference your Python 3.7 installation. Settings: Add a new Virtual Environment

Open the Terminal Window:

Install the required packages: pip install -r requirements.txt This command will install the required packages to run the application.

Make the migrations for the database model: py manage.py migrate

Create a superuser: py manage.py createsuperuser Enter the username and password for the superuser.

Run the server : py manage.py runserver

Click on the link that is displayed in the terminal window to launch the application.
