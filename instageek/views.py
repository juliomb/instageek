from django.shortcuts import render
from django.utils import translation


def hello(request):
    forced_language = request.GET.get('lang')
    if forced_language:
        request.session['lang'] = forced_language

    session_language = request.session.get('lang')
    if session_language:
        translation.activate(session_language)

    return render(request, 'hello.html', {'name': request.GET.get('name', 'John Doe')})