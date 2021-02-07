from django.shortcuts import redirect,render
from .models import Customer
from django.contrib import messages
# Create your views here.

def index(request):
    show=Customer.objects.filter()
    con={
        'show':show
    }
    return render(request,'index.html',con)
def deletecus(request,id=None):
    remo = Customer.objects.get(id=id)
    print(remo)
    if "delete" in request.POST:
        remo.delete()
        print("delete successfully")
        return redirect('index')

    return render(request,'delete.html',)

def adde(request):
    print(request.path)
    context={}
    if request.method=='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        mobile=request.POST.get('mobile')
        gender=request.POST.get('gender')

        c=Customer.objects.create(name=name,address=address,mobile=mobile,gender=gender)
        if c:
            print("data store sucessfuly")
            context['res'] ="data store sucessfuly"
        else:
            print("data not store")
    return render(request, 'adde.html',context)



def update_emp(request,id=None):
    print(id)
    context={}
    c =Customer.objects.get(id=id)

    if request.method=='POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        gender = request.POST.get('gender')
        print(name,address,mobile,gender,'male')
        c =Customer.objects.filter(id=id).update(name=name,address=address,mobile=mobile,gender=gender)
        if c:
            messages.add_message(request, messages.INFO, 'data update sucessfuly')
            print("data update sucessfuly")
            return redirect('index')
        else:
            print("data not store")

    context ={
        'cus':c
    }
    return render(request,'update.html',context)
