from django.http import HttpResponse
from django.shortcuts import render, redirect

from app.models import DepartmentForm


# Create your views here.
def index(request):
    return render(request, 'department/index.html')


def add(request):
    if request.method != 'POST':
        department = DepartmentForm()
        return render(request, 'department/add.html', {'from': department})

    department = DepartmentForm(request.POST)
    if not department.is_valid():
        return redirect('department/add.html', {'from': department})

    department.save()
    return redirect('department/index.html')
