from django.shortcuts import render
from .models import Contact

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content = request.POST['content']
        contact=Contact(name=name, email=email, phone=phone, content=content)
        contact.save()
    return render(request, "contact.html")
