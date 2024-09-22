from django.shortcuts import render

def home_page(request):
    context = dict()
    return render(request, 'index.html', context)