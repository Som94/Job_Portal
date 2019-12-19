from django.shortcuts import render
from testapp.models import BBSR_JOBS,HYD_JOBS,BNG_JOBS

# Create your views here.
def index(request):
    return render(request,'html/home.html')

def bbsr(request):
    list=BBSR_JOBS.objects.all()
    dict={'list':list}
    return render(request, 'html/bbsr.html', context=dict)

def hyd(request):
    list=HYD_JOBS.objects.all()
    dict={'list':list}
    return render(request, 'html/hydjob.html', context=dict)


def bng(request):
    list=BNG_JOBS.objects.all()
    dict={'list':list}
    return render(request, 'html/bngjob.html', context=dict)
