# Setup and Installation

To run this project locally, follow these steps:

Clone the repository:
'git clone (https://github.com/your-username/your-repository-name.git)'
'cd your-repository-name'

Create and activate a virtual environment:

Install the required dependencies:
'pip install -r requirements.txt'

Apply the database migrations:
'python manage.py migrate'

Start the development server:
'python manage.py runserver'


The application will be available at http://127.0.0.1:8000/.

# How to Use the Application

### Adding the First (Root) Airport:

   1. In the "Add New Airport" form, enter a unique Code (e.g., A).
   2. Leave the Parent, Position, and Duration fields blank.
   3. Click "Add Route".


### Adding a Child Airport:

   1. Enter a new unique Code (e.g., B).
   2. Select the Parent airport from the dropdown (e.g., A).
   3. Select a Position (Left or Right). 
   4. Enter the Duration (e.g., 150).
   5. Click "Add Route".


### Searching for a Node:

   1. Use the "Find the Nth Left or Right Node" form.
   2. Select a Starting Airport.
   3. Enter the Nth Level you want to find.
   4. Select the Position (direction).
   5. Click "Search". The result or an error message will be displayed below the form.


<img width="1897" height="835" alt="image" src="https://github.com/user-attachments/assets/8ced1c10-90ad-44f3-8636-5f98de797916" />
<img width="1885" height="324" alt="image" src="https://github.com/user-attachments/assets/e0ec000a-fb2c-4052-b4ce-8d5de08437f8" />


