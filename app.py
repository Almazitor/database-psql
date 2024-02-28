import flask
from flask import Flask, render_template, request, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

# Create a Flask app
app = Flask(__name__)

# Configure the SQLAlchemy database URI and set a secret key for session management
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:Iowastate2802-@localhost/project_tracker"
app.config["SECRET_KEY"] = b'\xa6\xcbo-Z\xf6\xeb\xce\xb0\xbc\xf9"\xba\xad\xed\xe2\xa4L\x14\x1a\xde\x8eg@'

# Create an SQLAlchemy instance
db = SQLAlchemy(app)

# Define the Project model
class Project(db.Model):
    __tablename__ = 'projects'
    project_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(length=50))

    # Establish a relationship with the Task model, defining cascading behavior for deletion
    task = db.relationship("Task", back_populates="project", cascade="all, delete-orphan")

# Define the Task model
class Task(db.Model):
    __tablename__ = 'tasks'
    task_id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.project_id'))
    description = db.Column(db.String(length=50))

    # Establish a relationship with the Project model
    project = db.relationship("Project", back_populates="task")

# Define route for displaying all projects
@app.route("/")
def show_projects():
    return render_template("index.html", projects=Project.query.all())

# Define route for displaying tasks of a specific project
@app.route("/project/<project_id>")
def show_tasks(project_id):
    return render_template("project-tasks.html", project=Project.query.filter_by(project_id=project_id).first(),
                           tasks=Task.query.filter_by(project_id=project_id).all())

# Define route for adding a new project
@app.route("/add/project", methods=['POST'])
def add_project():
    if not request.form['project-title']:
        flash("Enter a title for your new project", "red")
    else:
        # Create a new project and add it to the database
        project = Project(title=request.form['project-title'])
        db.session.add(project)
        db.session.commit()
        flash("Project added successfully", "green")
    return redirect(url_for('show_projects'))

# Define route for adding a new task to a project
@app.route("/add/task/<project_id>", methods=['POST'])
def add_task(project_id):
    if not request.form['task-name']:
        flash("Enter a title for your new task", "red")
    else:
        # Create a new task associated with the specified project and add it to the database
        task = Task(description=request.form['task-name'], project_id=project_id)
        db.session.add(task)
        db.session.commit()
        flash("Task added successfully", "green")
    return redirect(url_for('show_tasks', project_id=project_id))

# Define route for deleting a task
@app.route("/delete/task/<task_id>", methods=['POST'])
def delete_task(task_id):
    # Retrieve the task to be deleted and its original project ID
    pending_delete_task = Task.query.filter_by(task_id=task_id).first()
    original_project_id = pending_delete_task.project.project_id

    # Delete the task from the database
    db.session.delete(pending_delete_task)
    db.session.commit()

    # Redirect to the tasks page of the original project
    return redirect(url_for('show_tasks', project_id=original_project_id))

# Define route for deleting a project
@app.route("/delete/project/<project_id>", methods=['POST'])
def delete_project(project_id):
    # Retrieve the project to be deleted
    pending_delete_project = Project.query.filter_by(project_id=project_id).first()

    # Delete the project from the database
    db.session.delete(pending_delete_project)
    db.session.commit()

    # Redirect to the main projects page
    return redirect(url_for('show_projects'))

# Run the Flask app
app.run(debug=True, host="127.0.0.1", port=3000)