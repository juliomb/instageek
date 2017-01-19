from django.shortcuts import render
from django.utils import translation


def hello(request):
    forced_language = request.GET.get('lang')
    if forced_language:
        translation.activate(forced_language)
    return render(request, 'hello.html', {'name': request.GET.get('name', 'John Doe')})