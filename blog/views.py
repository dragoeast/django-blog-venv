from django.shortcuts import render


def home(request):
    return render(request=request, template_name='blog/home.html')

def about(request):
    return render(request=request, template_name='blog/about.html')
