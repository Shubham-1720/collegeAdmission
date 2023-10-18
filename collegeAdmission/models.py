from django.db import models


class newRegistrationstudent(models.Model):
    student_name = models.CharField(max_length=200)
    student_email = models.CharField(max_length=200, unique=True)
    student_phno = models.CharField(max_length=200, unique=True)
    student_gender = models.CharField(max_length=200)
    student_dob = models.DateField(auto_now=False, auto_now_add=False)
    student_pwd = models.CharField(max_length=200)



    def __str__(self):
        return self.student_email + self.student_pwd
