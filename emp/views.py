from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import emp

# Create your views here.
def emp_home(request):
    # return HttpResponse("Hello This is my new emp app")
    emps = emp.objects.all
    return render(request, 'emp/home.html',{'emps':emps})

def add_emp(request):
    if request.method == 'POST':
        #fetching the data from form
        emp_name = request.POST.get('emp_name')
        emp_id = request.POST.get('emp_id')
        emp_phone = request.POST.get('emp_phone')
        emp_address = request.POST.get('emp_address')
        emp_working = request.POST.get('emp_working')
        emp_department = request.POST.get('emp_department')
        #creating the model and set the data
        e=emp()
        e.name=emp_name
        e.emp_id=emp_id
        e.phone=emp_phone
        e.working=emp_working
        e.address=emp_address
        e.department=emp_department
        if e.working is None:
            e.working = False
        else:
            e.working = True
        e.save()

        print('data is coming')
        return redirect("/emp/home/")
    return render(request, 'emp/add_emp.html',{})

def delete_emp(request,emp_id):
    print(emp_id)
    emps = emp.objects.get(pk=emp_id)
    emps.delete()
    return redirect("/emp/home/")

def update_emp(request, emp_id):
    print(emp_id)
    emps = emp.objects.get(pk=emp_id)
    # Pass a dictionary as the context, not a set
    return render(request, 'emp/updates_emp.html', {'emps': emps})

def do_update_emp(request, emp_id):
    if request.method == 'POST':
        emp_name = request.POST.get('emp_name')
        emp_id_new = request.POST.get('emp_id')
        emp_phone = request.POST.get('emp_phone')
        emp_address = request.POST.get('emp_address')
        emp_working = request.POST.get('emp_working')
        emp_department = request.POST.get('emp_department')
        e = emp.objects.get(pk=emp_id)
        e.name=emp_name
        e.emp_id=emp_id_new
        e.phone=emp_phone
        e.working=emp_working
        e.address=emp_address
        e.department=emp_department
        if e.working is None:
            e.working = False
        else:
            e.working = True
        e.save()



        
    return redirect("/emp/home")
