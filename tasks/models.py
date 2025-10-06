from django.db import models
# Create your models here.
class Employee(models.Model):
      name=models.CharField(max_length=100)
      email=models.EmailField(unique=True)
      def __str__(self):
            return self.name

class Task(models.Model):
    STATUS_CHOICES=[
          ('PENDING','Pending'),
          ('IN_PROGRESS','In progress'),
          ('COMPLETED','Completed')
    ]
    project=models.ForeignKey("Project"
                              ,on_delete=models.CASCADE,
                              default=1
    )
    assigent_to=models.ManyToManyField(Employee)
    titel=models.CharField(max_length=250)
    descaption=models.TextField()
    due_date=models.DateField()
    status=models.CharField(max_length=15,choices=STATUS_CHOICES,default="PENDING")
    is_completed=models.BooleanField(default=False)
    create_at=models.DateField(auto_now_add=True)
    update_add=models.DateField(auto_now=True)

    def __str__(self):
          return self.titel


class TaskDetail(models.Model):
        HIGH = 'H'
        MEDIUM = 'M'
        LOW = 'L'
        PRIORITY_OPTIONS = (
            (HIGH, 'High'),
            (MEDIUM, 'Medium'),
            (LOW, 'Low'),
        )
        task = models.OneToOneField(Task, on_delete=models.DO_NOTHING,related_name='details',)

        assigned_to = models.CharField(max_length=100)
        priority = models.CharField(max_length=1, choices=PRIORITY_OPTIONS, default=LOW)
        notes=models.TextField(blank=True,null=True)
        def __str__(self):
              return f"Details form Task{self.task.titel}"

class Project(models.Model):
      name=models.CharField(max_length=50)
      description= models.TextField(blank=True,null=True)
      Start_date=models.DateField()

      # def __str__(self):
      #       return self.name
