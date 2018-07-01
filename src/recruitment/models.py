from django.db import models

# Create your models here.
class clubs(models.Model):
    club_id=models.CharField(default='',max_length=20)
    club_name=models.CharField(default='',max_length=70)

    def __str__(self):
        return self.club_id

class club_members(models.Model):
    club_id=models.ForeignKey(clubs,on_delete=models.CASCADE)
    user_id=models.CharField(max_length=20)
    Name=models.CharField(max_length=30)
    Password=models.CharField(max_length=50)
    Rollno=models.CharField(max_length=10)

    def __str__(self):
        return self.Name
class ie_resume(models.Model):
    club_id = models.ForeignKey(clubs,on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)
    Rollno = models.CharField(max_length=10)
    Phoneno = models.IntegerField()
    email = models.CharField(max_length=100)
    question1 = models.TextField()
    question2 = models.TextField()
    question3 = models.TextField()
    question4 = models.TextField()
    question5 = models.TextField()
    question6 = models.TextField()
    question7 = models.TextField()
    question8 = models.TextField()
    question9 = models.TextField()
    question10 = models.TextField()

    def __str__(self):
        return self.Name+"--"+self.Rollno
