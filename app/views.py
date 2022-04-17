from django.shortcuts import redirect, render,HttpResponse
from .models import Employee
from .forms import *
# Create your views here.
def create(request):
    a=display()
    form=display(request.POST)
    if request.method=='POST':
        #form=display1(request.POST)
        if form.is_valid():
            post=Employee()
            #data=request.POST
            #post=Employee.objects.create(Name=data['Name'],Position=data['Position'],Age=data['Age'])
            post.Name=request.POST.get('Name')
            post.Position=request.POST.get('Position')
            post.Age=request.POST.get('Age')
            post.save()
            return redirect('/Read')
    return render(request,'index.html',{'a':a})

def read(request):
    model=Employee.objects.all()
    return render(request,'index1.html',{'model':model})

def delete(request,id):
    #model1=display1()
    model1=Employee.objects.get(id=id)
    model1.delete()
    return redirect("/Read")

def update(request,id):  
    model2=Employee.objects.get(id=id)
    if request.method=='POST':
        form=display1(request.POST)
        a=display1(request.POST,instance=model2)
        if form.is_valid():
            a.save()
            return redirect("/Read")
    return render(request,'index2.html',{'model2':model2})
