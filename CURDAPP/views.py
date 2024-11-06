from django.shortcuts import render, redirect
from.models import CurdPro
def mainPage(request):
    if request.method == 'GET':
        data=CurdPro.objects.all()
        return render(request,'mainpage.html',{'data':data})

def add_student(request):
    if request.method == 'GET':
        return render(request,'add_student.html')

    else:
        roll1=request.POST.get('roll_no')
        fname1 = request.POST.get('fname')
        lname1 = request.POST.get('lname')
        email1 = request.POST.get('email')
        mobile1 = request.POST.get('mobile')
        percentage1 = request.POST.get('percentage')
        year1 = request.POST.get('year')
        location1 = request.POST.get('location')
        college1 = request.POST.get('college')
        university1 = request.POST.get('university')

        CurdPro(
            roll_no=roll1,
            first_name=fname1,
            last_name=lname1,
            email=email1,
            mobile=mobile1,
            percentage=percentage1,
            year=year1,
            location=location1,
            college=college1,
            university=university1,
        ).save()
        data=CurdPro.objects.all()
        return render(request,'add_student.html',{'data':data})




def display_details(request):
    data = CurdPro.objects.all()
    return render(request,'display_details.html',{'data':data})



def update_details(request):
    if request.method == 'GET':
        return render(request,'update_details.html')
    else:
        student1 = request.POST.get('student')
        data = CurdPro.objects.filter(roll_no=student1).first()
        if data:
            return render(request, 'update.html', {'data': data})
        else:
            return render(request, 'no_data.html')

def update(request,id):
    data = CurdPro.objects.get(id=id)
    data.first_name = request.POST.get('fname')
    data.last_name = request.POST.get('lname')
    data.email = request.POST.get('email')
    data.mobile = request.POST.get('mobile')
    data.percentage = request.POST.get('percentage')
    data.year = request.POST.get('year')
    data.location = request.POST.get('location')
    data.college = request.POST.get('college')
    data.university = request.POST.get('university')
    data.save()
    return redirect(mainPage)

def delete_student(request):
    if request.method == 'GET':
        return render(request,'delete_student.html')
    else:
        if request.method == 'POST':
            student1 = request.POST.get('student')
            data = CurdPro.objects.filter(roll_no=student1)
            if data:
                data.delete()
                return redirect(mainPage)
            else:
                return render(request, 'no_data.html')
