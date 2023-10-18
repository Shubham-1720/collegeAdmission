from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import newRegistrationstudent
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == "POST":
        stu_email = request.POST.get('stu_email')
        password = request.POST.get('password')
        check_if_student_exist = newRegistrationstudent.objects.filter(student_email = stu_email, student_pwd = password)
        if check_if_student_exist:
            request.session["student_logged_in"] = True
            request.session["student_email"] = stu_email
            
            return redirect('/collegeAdmission/studentdetails')
        
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')

def saveStudentRegistration(request):
    if request.method == "POST":
        student_name=request.POST.get('student_name')
        student_email=request.POST.get('student_email')
        student_phno=request.POST.get('student_phno')
        student_gender=request.POST.get('student_gender')
        student_dob=request.POST.get('student_dob')
        student_pwd=request.POST.get('student_pwd')
        student_cpwd=request.POST.get('student_cpwd')

        if student_cpwd == student_pwd:
            ins = newRegistrationstudent(student_name=student_name, student_email=student_email, student_phno=student_phno, student_gender=student_gender, student_dob=student_dob, student_pwd=student_pwd)
            ins.save()
        else:
            messages.warning(request, 'Please check your password!') 
    return redirect("/collegeAdmission")


def basicDetails(request):
    if not request.session.get("student_logged_in"):
        redirect("collegeAdmission/login")
    else:
        student_email = request.session.get("student_email")
        student_details = newRegistrationstudent.objects.get(student_email = student_email)
        return render(request, "studentdetails.html", {"student_details": student_details})
