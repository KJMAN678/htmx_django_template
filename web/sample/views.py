from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "sample/index.html")


def clicked(request):
    context = {"message": "Button clicked!"}
    return render(request, "stock/clicked.html", context)
