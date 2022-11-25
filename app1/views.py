from django.shortcuts import render

# Create your views here.


def a1_first(request):
    dict = {'a': 100, 'b': 200}
    return render(request, 'a1_first.html', dict)


def a1_second(request):
    dict = {'a': 200, 'b': 300, 'c': 400}
    return render(request, 'a1_second.html', dict)


def a2_first(request):
    dict = {'a': 300, 'b': 400, 'c': 500, 'd': 600}
    return render(request, 'a2_first.html', dict)


def a2_second(request):
    dict = {'x': 'Thalapathy'}
    return render(request, 'a2_second.html', dict)
