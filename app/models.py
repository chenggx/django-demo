from django import forms
from django.db import models


# Create your models here.
class Department(models.Model):
    name = models.CharField(verbose_name='名称', max_length=255, null=True)

    def __str__(self):
        return self.name


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
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)


class UserinfoForm(forms.ModelForm):
    class Meta:
        model = Userinfo
        fields = ['username', 'password', 'gender', 'department']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '输入姓名'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '输入密码'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'})
        }


class PrettyNum(models.Model):
    LEVEL_CHOICES = (
        (1, '一级'),
        (2, '二级'),
        (3, '三级'),
        (4, '四级'),
    )
    STATUS_CHOICES = (
        (1, '已使用'),
        (2, '未使用'),
    )

    mobile = models.CharField(verbose_name='手机号', max_length=11)
    price = models.IntegerField(verbose_name='价格', default=0)
    level = models.SmallIntegerField(
        verbose_name='等级', choices=LEVEL_CHOICES, default=1)
    status = models.SmallIntegerField(
        verbose_name='状态', choices=STATUS_CHOICES, default=2)
