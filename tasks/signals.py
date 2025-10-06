from django.db.models.signals import post_save,pre_save,m2m_changed,post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from tasks.views import Task
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


      