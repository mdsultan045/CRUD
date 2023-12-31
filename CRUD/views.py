from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
# Create your views here.

def index(request):
    emp = Employees.objects.all()

    context = {
        'emp':emp,
    }
    return render(request,'index.html',context)


def add(request):
        if request.method == 'POST' and 'images' in request.FILES and 'resume' in request.FILES:
            name = request.POST.get('name')
            email = request.POST.get('email')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            city_id = request.POST.get('city')
            gender = request.POST.get('gender')
            images = request.FILES['images']
            resume = request.FILES['resume']

            if city_id:
                city = Employees.objects.get(id=city_id)
            else:
                None

            emp = Employees(
            Name = name,
            Email = email,
            Address = address,
            Phone = phone,
            City = city,
            Gender = gender,
            Images = images,
            Resume = resume,
            )
            emp.save()
            return redirect('home')
        
        

def edit(request):
    emp = Employees.objects.all()

    context = {
        'emp':emp,
    }
    return redirect(request,'index.html',context)

def update(request, id):
    emp = Employees.objects.get(id=id)
    
    if request.method == "POST":
        emp.Name = request.POST.get('name')
        emp.Email = request.POST.get('email')
        emp.Address = request.POST.get('address')
        emp.Phone = request.POST.get('phone')
        emp.City = request.POST.get('city')
        emp.Gender = request.POST.get('gender')

        images = request.FILES.get('images')
        resume = request.FILES.get('resume')
        
        if images:
            emp.Images = images
        if resume:
            emp.Resume = resume
            
        emp.save()
        return redirect('home')

    cities = CITY
    
    return render(request, 'index.html', {'cities': cities})


def delete(request,id):
    emp = Employees.objects.filter(id=id)
    emp.delete()
    return redirect('home')


def delete_records(request,id):

        data = Employees.objects.all(id=id)
        data.delete()
        return redirect('home') 
    

# def delete_records(request):
#     if request.method == 'POST':
#         for i in Employees.objects.filter(status=1):
#             x = request.POST.get(str(i.id))
#             print(x)
#             if str(x) == 'on':
#                 emp = Employees.objects.get(id=i.id)
#                 emp.delete()
#     return redirect('home')