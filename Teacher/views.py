from django.shortcuts import render
from .forms import TeacherForm
from django.shortcuts import redirect
from .models import Teacher

def teacher_all_view(request):
    form = Teacher.objects.all()
    template_name = 'Teacher/allteacher.html'
    context={'form':form}
    return render(request,template_name,context)

def teacher_add_view(request):
    form = TeacherForm()
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Hajeri')
    template_name = 'Teacher/teacher.html'
    context ={'form':form}
    return render(request,template_name,context)

def teacher_update_view(request,pk):
    objs=Teacher.objects.get(id=pk)
    form=TeacherForm(instance=objs)
    if request.method == 'POST':
        form = TeacherForm(request.POST,instance=objs)
        if form.is_valid():
            form.save()
            return redirect('Techall')
    template_name = 'Teacher/teacher.html'
    context = {'form':form}
    return render(request,template_name,context)

def teacher_delete_view(request,pk):
    objs=Teacher.objects.get(id=pk)
    template_name = 'Teacher.delete.html'
    if request.method == 'POST':
        objs.delete()
    context = {'objs':objs}
    return render(request,template_name,context)



