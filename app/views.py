from django.http import HttpResponse
from django.shortcuts import render, redirect

from app.models import DepartmentForm, Department, UserinfoForm, Userinfo


# Create your views here.
def index(request):
    departments = Department.objects.all()
    return render(request, 'department/index.html', {'departments': departments})


def add(request):
    if request.method != 'POST':
        department = DepartmentForm()
        return render(request, 'department/add.html', {'from': department})

    department = DepartmentForm(request.POST)
    if not department.is_valid():
        return render(request, 'department/add.html', {'from': department})

    department.save()
    return redirect('department-index')


def destroy(request, id):
    deleted, _ = Department.objects.filter(id=id).delete()

    if deleted:
        return redirect('department-index')


def userinfo_add(request):
    if request.method != 'POST':
        user_form = UserinfoForm()
        return render(request, 'userinfo/add.html', {'from': user_form})

    user_info = UserinfoForm(request.POST)
    if not user_info.is_valid():
        return render(request, 'userinfo/add.html', {'from': user_info})

    user_info.save()
    return redirect('userinfo-index')


def userinfo_index(request):
    users = Userinfo.objects.all()

    return render(request, 'userinfo/index.html', {'users': users})


def userinfo_destroy(request, id):
    deleted, _ = Userinfo.objects.filter(id=id).delete()

    if deleted:
        return redirect('userinfo-index')
