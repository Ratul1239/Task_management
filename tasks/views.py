from django.shortcuts import render
from django.http import HttpResponse
from tasks.models import Task
from django.db.models import Count,Q
# Create your views here.
def manager_dasbord(request):
    # totel_task=task.count()
    # completed_task=task.filter(status='COMPLETED').count()
    # PENDING_task=task.filter(status='PENDING').count()
    # IN_PROGRESS_taks=task.filter(status='IN_PROGRESS').count()
    type=request.GET.get('type','all')
    base_quary=Task.objects.select_related('datails').prefetch_related('assigent_to').all()
    if type=='completed':
        task=base_quary.filter(status='COMPLETED')
    elif type=='in_progress':
        task=base_quary.filter(status='IN_PROGRESS')
    elif type=='pending':
        task=base_quary.filter(status='PENDING')
    elif type=='all':
        task=base_quary.all()

    counts = Task.objects.aggregate(total=Count('id'),completed=Count('id',filter=Q(status='COMPLETED')),IN_PROGRESS=Count('id',filter=Q(status='IN_PROGRESS')),peinding=Count('id',filter=Q(status='PENDING')))
    contex={
        'task':task,
        'counts':counts
    }
    return render(request,"dashbord/manager_dashbord.html",contex)
def user_dasbord(request):
    counts = {
        "total": Task.objects.count(),
        "completed": Task.objects.filter(status="COMPLETED").count(),
        "IN_PROGRESS": Task.objects.filter(status="IN_PROGRESS").count(),
        "peinding": Task.objects.filter(status="PENDING").count(),
    }
    return render(request, "dashbord/user_dasbord.html", {"counts": counts})
def test(request):
    return render(request,"test.html")
def create_task(request):
    return render(request,"task_from.html")
def dashbord(request):
    return render(request,"dashbord.html")
def view_task(request):
    tasks=Task.objects.all()
    return render(request,'show_task.html',{"tasks":tasks})