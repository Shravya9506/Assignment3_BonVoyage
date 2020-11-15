To use this application: Create a new PyCharm Django Project using this folder for the source. Answer 'Yes' when prompted to use the files from this folder for the new project. Settings: Set up the project interpreter to reference your Python 3.7 installation. Settings: Add a new Virtual Environment 
 
Open the Terminal Window: 
1. Now run your virtual environment by running the activation script we need to navigate to the venv\Scripts directory: Run the command 'cd venv\Scripts' 
 
2. Now activate the scripts: Run the command 'activate' 
 
3. Navigate back to the repository directory: Run the command 'cd..' twice 
 
4. Install the required packages: Run the command 'pip install -r requirements.txt' 
This command will install the required packages to run the application. 
 
5. Make the migrations for the database model: Run the command 'python manage.py migrate' 
 
6. Create a superuser: Run the command 'python manage.py createsuperuser' 
Enter the username, Email and password for the superuser. 
 
7. Run the server: Run the command 'python manage.py runserver' 
 
8. Click on the link that is displayed in the terminal window to launch the application. 
 
To deactivate the virtual environment. Navigate to the venv\Script directory (use the command of Step 1) and run the command 'deactivate'