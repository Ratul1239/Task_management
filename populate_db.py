import os
import django
from faker import Faker
import random

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_management.settings')
django.setup()

from tasks.models import Employee, Project, Task, TaskDetail  # Import after setup

def populate_db():
    fake = Faker()

    # Create Projects
    projects = [
        Project.objects.create(
            name=fake.bs().capitalize(),
            description=fake.paragraph(),
            Start_date=fake.date_this_year()  # matches model field name
        )
        for _ in range(5)
    ]
    print(f"Created {len(projects)} projects.")

    # Create Employees
    employees = [
        Employee.objects.create(
            name=fake.name(),
            email=fake.email()
        )
        for _ in range(10)
    ]
    print(f"Created {len(employees)} employees.")

    # Create Tasks
    tasks = []
    for _ in range(20):
        task = Task.objects.create(
            project=random.choice(projects),
            titel=fake.sentence(),
            descaption=fake.paragraph(),
            due_date=fake.date_this_year(),
            status=random.choice(['PENDING', 'IN_PROGRESS', 'COMPLETED']),
            is_completed=random.choice([True, False])
        )
        # Match the ManyToMany field name in your model
        task.assigent_to.set(random.sample(employees, random.randint(1, 3)))
        tasks.append(task)
    print(f"Created {len(tasks)} tasks.")

    # Create Task Details
    for task in tasks:
        TaskDetail.objects.create(
            task=task,
            assigned_to=", ".join(
                [emp.name for emp in task.assigent_to.all()]
            ),
            priority=random.choice(['H', 'M', 'L']),
            notes=fake.paragraph()
        )
    print("Populated TaskDetails for all tasks.")
    print("Database populated successfully!")

