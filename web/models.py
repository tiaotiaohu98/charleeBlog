from django.db import models


# Create your models here.
# 操作数据库，类——>SQL语句（ORM）

class UserInfo(models.Model):
    name = models.CharField(verbose_name="姓名", max_length=16)
    age = models.IntegerField(verbose_name="年龄")
    email = models.CharField(verbose_name="邮箱", max_length=50)

class BookInfo(models.Model):
    name = models.CharField(verbose_name="书名", max_length=16)
    size = models.IntegerField(verbose_name="大小")
    auther = models.CharField(verbose_name="作者", max_length=50)
