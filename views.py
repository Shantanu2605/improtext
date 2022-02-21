from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages

def index(request):
    return render(request, 'index.html')


def analyzer(request):
    text= (request.POST.get('text', 'default'))
    removepunc= (request.POST.get('removepunc', 'off'))
    fullcaps= (request.POST.get('fullcaps', 'off'))
    newlineremover= (request.POST.get('newlineremover', 'off'))
    spaceremover= (request.POST.get('spaceremover', 'off'))
    charcount= (request.POST.get('charcount', 'off'))
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': '', 'analyzed_text': analyzed}
        text= analyzed


    if (fullcaps == "on"):
        analyzed = ""
        for char in text:
            analyzed = analyzed + char.upper()

        params = {'purpose': '', 'analyzed_text': analyzed}
        text= analyzed

    if (spaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(text):
            if not (text[index] == " " and text[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': '', 'analyzed_text': analyzed}
        text= analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in text:
            if char != "\n":
                analyzed = analyzed + char

        params = {'purpose': '', 'analyzed_text': analyzed}
        text= analyzed
    if newlineremover=="off" and spaceremover=="off" and removepunc=="off" and fullcaps=="off":
        analyzed= text
        params = {'purpose': '', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    return render(request, 'analyze.html', params)


def ex1(request):
    s= '''<h1> Navigation Bar<br></h1><p1>This is Special Page of our Website, you can access your favourite
     websites through this page! <p1><br>
     <h2><a href= "https://youtube.com"</a><h2> Youtube<br>
    <a href= "https://facebook.com"</a> Facebook<br>
    <tr><td><a href= "https://Instagram.com"</a> Instagram<br><td><td> Your favourite </td></tr>
    <a href= "https://hindustantimes.com"</a> News<br>
    <a href= "https://pacogames.com"</a> Some Cool Online Games!<br>'''
    return HttpResponse(s)

def spaceremove(request):
    return HttpResponse("space remover <a href='/''>back<a/a>")

def contactus(request):
    if request.method=="POST":
        name= request.POST.get('name','')
        phone = request.POST.get('phone','')
        email = request.POST.get('email','')
        desc = request.POST.get('desc','')
        subject= "New Submission from Contact Form"
        content= (f"From {name}, Phone no: {phone}, email: {email}, Message: {desc}")
        if len(name) < 3 or len(email) < 6 or len(phone) < 10 or len(desc) < 4:
            messages.error(request, "❌ Please fill the form correctly!")
        else:
            send_mail(subject, content, 'shantanu.kumar.singh26@gmail.com',['shantanu.kumar.singh26@gmail.com'],
                  fail_silently=False,)
            messages.success(request, "✅ Message Sent Successfully!")
    return render(request, "contact.html")



def about(request):
    return render(request, 'abus.html')
def charcount(request):
    return HttpResponse("charcount")


