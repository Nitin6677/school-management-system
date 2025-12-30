from django.shortcuts import render
from .forms import AttendanceForm, Attendance
from django.shortcuts import redirect

def attendance_view(request):
    form = AttendanceForm()
    attendance = None
    id = request.GET.get('id') or request.POST.get('id') 

    action = request.GET.get('action')

    if id and action == "update":
        obj = Attendance.objects.filter(id=id).first()
        form = AttendanceForm(instance=obj)
        attendance = Attendance.objects.filter(date = obj.date)

    if id and action == "delete":
        obj = Attendance.objects.filter(id=id).first()
        attendance = Attendance.objects.filter(date = obj.date).exclude(id=obj.id)
        obj.delete()

    if action == "list":
        form = AttendanceForm(filter=True)
        attendance = Attendance.objects.all()
        date = request.POST.get("date")
        status = request.POST.get("status")
        student= request.POST.get("student")
        if date:
            attendance = Attendance.objects.filter(date = date)
        if status:
            attendance = Attendance.objects.filter(status = status)
        if student:
            attendance = Attendance.objects.filter(student = student)

    if request.method == 'POST':
        if id !="None":
             print("id", id, type(id))
             obj = Attendance.objects.filter(id=id).first()
             form = AttendanceForm(request.POST, instance=obj)
        else:
            form = AttendanceForm(request.POST)

        if form.is_valid():
            instance = form.save()
            attendance = Attendance.objects.filter(date = instance.date)

    template_name='app1/attendance/attendance.html'
    context={'form':form, "attendance":attendance}
    return render(request,template_name,context)
