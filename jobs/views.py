from django.shortcuts import render, get_object_or_404
from .models import Job

# old view for home page
# def home(request):
#     jobs = Job.objects
#     return render(request, 'jobs/home.html',{'jobs':jobs})

def index(request):
    jobs = Job.objects
    return render(request, 'jobs/index.html',{'jobs':jobs})

def detail(request, job_id):
   job_detail = get_object_or_404(Job, pk=job_id)
   return render(request, 'jobs/detail.html', {'job':job_detail}) 

