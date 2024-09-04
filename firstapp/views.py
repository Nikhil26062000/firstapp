from django.http import HttpResponse

def test(request):
    print("Test request")
    return HttpResponse("<h1>Hello world</h1>")

def about(request):
    return HttpResponse("<h1>Hello About</h1>")