from django.db import models



class User(models.Model):
     firstName = models.CharField(max_length=254, null=True)
     lastName = models.CharField(max_length=1000, null=True)
     emailAddress = models.CharField(max_length=254, null=True)
     age =models.IntegerField(null=True)
     gender = models.CharField(max_length=254, null=True)
     telNo = models.IntegerField(null=True)
     nationality =models.CharField(max_length=254, null=True)
     country =models.CharField(max_length=254, null=True)
       

     def _str_(self):
          return self.firstName


class Admin(models.Model):
     firstName = models.CharField(max_length=254, null=True)
     lastName = models.CharField(max_length=1000, null=True)
     emailAddress = models.CharField(max_length=254, null=True)
     age =models.IntegerField(null=True)
     gender = models.CharField(max_length=254, null=True)
     
     def _str_(self):
          return self.lastName


class Destination(models.Model):
     name = models.CharField(max_length=100, null=True)
     description = models.TextField(max_length=3000, null=True)

     def _str_(self):
          return self.name