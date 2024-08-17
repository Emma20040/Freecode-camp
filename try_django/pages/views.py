from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
   # return HttpResponse("hello world")
  # home= Pages.objects.all()
   #context={'home':home}
   return render(request, "home.html", {})

def about_pages(request):
    context={
        'my_text':'this about us',
        'my_number':'1234',
        'my_list':[12,2,233,223,23,2,32]
    }
    return render(request, 'about.html', {})
    # return HttpResponse('welcome to about page')

def contact_page(request):
    #return HttpResponse('welcome to our contact page')
    return render(request, 'contact.html', {})

def staff_page(request):
    return HttpResponse('welcome to our staff page')

# Create your views here.
