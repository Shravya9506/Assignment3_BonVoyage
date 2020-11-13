To use this application: Create a new Pycharm Django Project using this folder for the source. Answer 'Yes' when prompted to use the files from this folder for the new project. Settings: Set up the project interpreter to reference your Python 3.7 installation. Settings: Add a new Virtual Environment

Open the Terminal Window:
1. Create a virtual environment: Run the command 'python -m venv virtualEnv'
     -   “virtualEnv” is the name set for your virtual environment.

2. Now run your virtual environment by running the activation script we need to navigate to the virtualEnv\Scripts directory: Run the command 'cd virtualEnv\Scripts'

3. Now activate the scripts:  Run the command 'activate'

4. Navigate back to the repository directory : Run the command 'cd..' twice

5. Install the required packages: Run the command 'pip install -r requirements.txt'
 This command will install the required packages to run the application.

6. Make the migrations for the database model: Run the command 'py manage.py migrate'

7. Create a superuser: Run the command 'py manage.py createsuperuser'
 Enter the username, Email and password for the superuser.

8. Run the server : Run the command 'py manage.py runserver'

9. Click on the link that is displayed in the terminal window to launch the application.

To deactivate the virtual environment. Navigate to the virtualEnv\Script directory (use the command of Step 2) and run the command 'deactivate'
