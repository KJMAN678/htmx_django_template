from django.shortcuts import render


def index(request):
    return render(request, "sample/index.html")


def clicked(request):
    context = {"message": "Button clicked!"}
    return render(request, "stock/clicked.html", context)
