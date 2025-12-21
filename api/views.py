from django.shortcuts import render, redirect
from .models import StudentInfo
from .forms import StudentForm
from django.http import HttpResponse
from django.core.paginator import Paginator

def Add_student_view(request):
    form=StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('all')
    template_name='app1/add.html'
    context={'form':form}
    return render(request,template_name,context)

def all_student_view(request):
    form = StudentForm(filter=True)
    students = StudentInfo.objects.all().order_by('id')
    first_name = request.GET.get('first_name')
    if first_name:
        students = students.filter(first_name__icontains = first_name)

    last_name = request.GET.get('last_name')
    if last_name:
        students = students.filter(last_name__icontains = last_name)

    last_name = request.GET.get('last_name')
    if last_name:
        students = students.filter(last_name__icontains = last_name)

    city_name = request.GET.get('city_name')
    if city_name:
     students = students.filter(city_name__icontains = city_name)

    roll_number = request.GET.get('roll_number')
    if roll_number:
        students = students.filter(roll_number__icontains = roll_number)

    school_name = request.GET.get('school_name')
    if school_name:
        students = students.filter(school_name__icontains = school_name)

    class_name = request.GET.get('class_name')
    if  class_name:
        students = students.filter(class_name_icontains =  class_name)

    email = request.GET.get('email')
    if email:
        students = students.filter(email__icontains = email)

    phone_number = request.GET.get('phone_number')
    if phone_number:
        students = students.filter(phone_number__icontains = phone_number)

    address = request.GET.get('address')
    if address:
        address = address.strip()
        students = students.filter(address__icontains=address)

    year_in_school = request.GET.get('year_in_school')
    if year_in_school:
        students = students.filter(year_in_school__icontains = year_in_school)

    paginator = Paginator(students, 10)  # 20 per page
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'app1/all.html', {'page_obj': page_obj,'form':form})

def update_view(request,pk):
    objs=StudentInfo.objects.get(id=pk)
    form=StudentForm(instance=objs)
    if request.method == 'POST':
        form=StudentForm(request.POST,instance=objs)
        if form.is_valid():
            form.save()
            return redirect('all')
    template_name='app1/add.html'
    context={'form':form}
    return render(request,template_name,context)

def Delete_view(request,pk):
    objs=StudentInfo.objects.get(id=pk)
    if request.method == 'POST':
        objs.delete()
        return redirect('all')
    template_name='app1/delete.html'
    context={'objs':objs}
    return render(request,template_name,context)