from django.shortcuts import render, redirect
from .models import Food, Consume
from .forms import usersform
# Create your views here.


def index(request):

    if request.method == "POST":
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user, food_consumed=consume)
        consume.save()
        foods = Food.objects.all()

    else:
        foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)

    return render(request, 'myapp/index.html', {'foods': foods, 'consumed_food': consumed_food})


def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('/')
    return render(request, 'myapp/delete.html')
def register(request):
    context ={}
    form = usersform(request.POST or None, request.FILES or None)
    context['form']= form
    if form.is_valid():
        form.save()
        x=request.POST['email']
        y=request.POST['username']
        a=request.POST['password']
        d=request.POST['address']
        b=request.POST['phonenumber']
        d=request.POST['gender']
        
        return render(request,"myapp/index.html")
    else:
        return render(request,'myapp/register.html',context)
    
