from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return redirect('/')