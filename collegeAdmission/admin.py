from django.contrib import admin

# Register your models here.
from .models import newRegistrationstudent

@admin.register(newRegistrationstudent)
class newRegistrationstudentAdmin(admin.ModelAdmin):
    list_display = [
        "student_name", "student_email", "student_phno", "student_dob", "student_pwd", "student_gender"
    ]