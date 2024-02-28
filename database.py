from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import registry, relationship, Session

# Create a SQLAlchemy engine with the connection URI and enable echoing for debugging
engine = create_engine("postgresql+psycopg2://postgres:Iowastate2802-@localhost/project_tracker", echo=True)

# Create a SQLAlchemy mapper registry
mapper_registry = registry()

# Generate a base class using the mapper registry
Base = mapper_registry.generate_base()


# Define the Project model
class Project(Base):
   __tablename__ = 'projects'

   project_id = Column(Integer, primary_key=True)
   title = Column(String(length=50))

   def __repr__(self):
      return "<Project(project_id='{0}', title='{1}')>".format(self.project_id, self.title)


# Define the Task model
class Task(Base):
   __tablename__ = 'tasks'

   task_id = Column(Integer, primary_key=True)
   project_id = Column(Integer, ForeignKey('projects.project_id'))
   description = Column(String(length=50))

   # Establish a relationship with the Project model
   project = relationship("Project")

   def __repr__(self):
      return "<Task(description='{0}')>".format(self.description)


# Create the tables in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
with Session(engine) as session:
   # Create a new Project instance and add it to the session
   clean_house_project = Project(title="Project 1")
   session.add(clean_house_project)
   session.flush()

   # Create a new Task instance associated with the project and add it to the session
   task = Task(description="Task 1", project_id=clean_house_project.project_id)
   session.add(task)

   # Commit the changes to the database
   session.commit()