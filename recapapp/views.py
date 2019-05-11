from django.shortcuts import render

# Create your views here.


def index(request):
    mydic = {
        'key1':"go with th flow",
        'key2': "lets move"}
    return render(request, "recapapp/index.html",content = mydic)