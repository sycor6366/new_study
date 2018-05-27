from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choicd(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class PhoneBook(models.Model):
    tel = models.IntegerField(default='')
    name = models.CharField(max_length=50)

    def __str__(self):
        return "name:{},tel:{}".format(self.name,self.tel)
