# -*- coding: cp936 -*-
from django.db import models

# Create your models here.
class Address(models.Model):
    name = models.CharField('姓名', maxlength=6, unique=True)
    number = models.CharField('学号', maxlength=15, unique=True)
    telphone = models.CharField('电话', maxlength=20)
    Email = models.CharField('邮箱', maxlength=20)
    QQ = models.CharField('QQ', maxlength=10)
    address = models.CharField('地址', maxlength=25, unique=True)
    birthday = models.CharField('生日', maxlength=12, unique=True)

    user = models. ForeignKey(User)
    
    def __repr__(self):
        return self.name


class Admin: pass
