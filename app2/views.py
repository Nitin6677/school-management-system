from django.shortcuts import render
from .forms import HajeriForm

def hajeri_view(request):
    form = HajeriForm()
    if request.method == 'POST':
        form = HajeriForm(request.POST)
        if form.is_valid():
            form.save()
    template_name = 'Teacher/attndance/attndance.html'
    context={'form':form}
    return render(request,template_name,context)
