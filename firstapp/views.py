from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    print("Test request")

    if request.method == "POST":
        check = request.POST.get("check")
        print(check)


    isActive = True
    name = "Nikhil"
    list_of_programs = [
        "Wap to check even or odd",
        "Wap to check PN",
        "Wap to print number"
    ]

    student = {
       "student_name":"Rahul",
        "student_college":"zyz",
        "student_city":"Pune"
    }

    data = {
        "isActive":isActive,
        "name":name,
        "list_of_programs":list_of_programs,
        "student":student
    }
    # return HttpResponse("<h1>Hello world</h1>")
    return render(request,"home.html",data)

def about(request):
    # return HttpResponse("<h1>Hello About</h1>")
    return render(request,"about.html",{})

def service(request):
    return render(request,"service.html",{})