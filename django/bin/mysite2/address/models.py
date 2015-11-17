# -*- coding: cp936 -*-
from django.db import models

# Create your models here.
class Address(models.Model):
    name = models.CharField('����', maxlength=6, unique=True)
    number = models.CharField('ѧ��', maxlength=15, unique=True)
    telphone = models.CharField('�绰', maxlength=20)
    Email = models.CharField('����', maxlength=20)
    QQ = models.CharField('QQ', maxlength=10)
    address = models.CharField('��ַ', maxlength=25, unique=True)
    birthday = models.CharField('����', maxlength=12, unique=True)

    user = models. ForeignKey(User)
    
    def __repr__(self):
        return self.name


class Admin: pass
