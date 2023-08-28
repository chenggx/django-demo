from django import forms
from django.db import models


# Create your models here.
class Department(models.Model):
    name = models.CharField(verbose_name='名称', max_length=255, null=True)


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '输入部门名称'})
        }


class Userinfo(models.Model):
    GENDER_CHOICES = (
        (1, '男'),
        (2, '女'),
        (3, '保密'),
    )
    username = models.CharField(verbose_name='用户名', max_length=255)
    password = models.CharField(verbose_name='密码', max_length=64)
    gender = models.SmallIntegerField(verbose_name='性别', choices=GENDER_CHOICES,
                                      default=GENDER_CHOICES[2][0])
    create_time = models.TimeField(verbose_name='创建时间', auto_now=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
