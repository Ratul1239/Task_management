from django.db import models
from django.db.models.signals import post_save,pre_save,m2m_changed,post_delete
from django.dispatch import receiver
from django.core.mail import send_mail

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
@receiver(m2m_changed,sender=Task.assigent_to.through)
def notify_employees_on_task_creation(sender,instance,action,*args, **kwargs):
    if action=='post_add':
          assingned_emails=assigned_emails=[emp.email for emp in instance.assigent_to.all()]
          send_mail(
    "New Task Assigned",
    f"You have been assigned to the task.{instance.titel}",
    "ri373820@gmail.com",
    assingned_emails,
    fail_silently=False,
)
@receiver(post_delete, sender=Task)
def delete_details(sender, instance, **kwargs):
    if hasattr(instance, "details"):  
        instance.details.delete()
        print("TaskDetail deleted successfully")


      