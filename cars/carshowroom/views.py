from django.shortcuts import render

# Create your views here.
def admindashboard(request):
    return render(request,'admindashboard.html')

def addcar(request):
     if request.method=='POST':
        make=request.POST.get('make')
        model=request.POST.get('model')
        year=request.POST.get('year')
        price=request.POST.get('price')
        car=Car(make=make,model=model,year=year,price=price)
        car.save()
