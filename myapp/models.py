from django.db import models

# Create your models here.
class Skill(models.Model):
    name=models.CharField(max_length=50)
    level=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Project(models.Model):
    name=models.CharField(max_length=100)
    categary=models.CharField(max_length=50)
    discriptoin=models.TextField(max_length=200)
    git_link=models.CharField(max_length=150)
    host_link=models.CharField(max_length=150,blank=True,null=True)
    def __str__(self):
        return self.name
    
class Certificate(models.Model):
    name=models.CharField(max_length=150)
    org=models.CharField(max_length=100)
    image=models.ImageField(null=True,blank=True,default='')

    @property
    def ImageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url

    def __str__(self):
        return self.name
    