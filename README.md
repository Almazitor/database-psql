# Project Tracker Web Application

The Project Tracker Web Application is a dynamic tool for efficiently managing and tracking projects and their associated tasks. This web application is built using Flask, a powerful Python web framework, and SQLAlchemy, a SQL toolkit and Object-Relational Mapping (ORM) library.

## Key Features

1. **Project and Task Management:**
   - Easily create new projects with distinct titles.
   - Add tasks to each project with detailed descriptions.
   - Conveniently view all projects and associated tasks on the main page.

2. **User-Friendly Interface:**
   - Intuitive web interface for adding and managing projects and tasks.
   - Flash messages provide user feedback on successful operations or error messages.

3. **Database Integration:**
   - Utilizes PostgreSQL as the database to store project and task information.
   - Seamless interaction with the database using SQLAlchemy ORM.

## How to Use

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/project-tracker.git
    ```

2. **Set Up PostgreSQL Database:**

    - Set up a PostgreSQL database on your local machine.

3. **Update Database Connection:**

    - Open `app.py` in your preferred text editor.
    - Locate the `SQLALCHEMY_DATABASE_URI` configuration.
    - Update it with your PostgreSQL database connection details.

4. **Run the Flask Application:**

    - Open a terminal in the project directory.
    - Run the Flask application:

        ```bash
        python app.py
        ```

5. **Open the Web Application:**

    - Open your web browser and navigate to [http://127.0.0.1:3000/](http://127.0.0.1:3000/).

6. **Interact with the Application:**

    - Use the web interface to seamlessly add, view, and delete projects and tasks.

**Note:** Ensure that PostgreSQL is installed and running on your machine before running the application.

---
