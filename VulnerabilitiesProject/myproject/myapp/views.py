# myapp/views.py
from django.shortcuts import render, redirect
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')  # Or any other view
    else:
        form = RegisterForm()
    return render(request, 'myapp/register.html', {'form': form})
