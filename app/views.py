from django.shortcuts import render
from .models import form
# Create your views here.
def form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        print(f"Name: {name}, Email: {email}, Phone: {phone}, Address: {address}")
        return render(request,'form.html', {'message': 'Submitted successfully!'})

        
    return render(request,'form.html')
