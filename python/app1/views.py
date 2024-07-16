from django.shortcuts import render,HttpResponse,redirect
from .models import Author
from .models import category,product,userregister

# Create your views here.
def first(request):
    return HttpResponse("this is my first view function..")

def table(request):
    authordata = Author.objects.all()
    # print(autdata)
    # for i in authordata:
    #     print(i.name)
    #     print(i.email)
    return render(request,'table.html',{'author':authordata})

def cattable(request):
    categorydata= category.objects.all()
    return render(request,'cattable.html',{'catdata':categorydata})

def form(request):
    if request.method == 'POST' :
        storeauthor = Author()
        storeauthor.name = request.POST['aname']
        storeauthor.email = request.POST['aemail']
        storeauthor.save()
        return render(request,'form.html')
    else:
        return render(request,'form.html')
    
def catform(request):
    if request.method == 'POST' :
        storecat = category()
        storecat.name = request.POST['catname']
        storecat.image = request.FILES['catfile']
        storecat.save()
        return render(request,'catform.html')
    else:
        return render(request,'catform.html')


def update(request):
    try:
        if request.method == 'POST' :
            authordata= Author.objects.get(name ='a')
            authordata.name = request.POST['autname']
            authordata.email = request.POST['autemail']
            authordata.save()
            return render(request,'update.html',{'author':authordata})
        else:
            authordata= Author.objects.get(name ='a')
            return render(request,'update.html',{'author':authordata})
    except Exception as e:
        return render(request,'update.html')
          
          
def index(request):
    if 'email' in request.session:
        catdata=category.objects.all()
        return render(request,'index.html',{'cat':catdata,'session':True})
    else:
        catdata=category.objects.all()
        return render(request,'index.html',{'cat':catdata})

def allproduct(request):
    prodata=product.objects.all()
    return render(request,'product.html',{'pro':prodata})


def register(request):
    if request.method == 'POST':
        user = userregister()
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.add = request.POST['add']
        user.password= request.POST['password']
        user.mob = request.POST['mob']
        useralredy = userregister.objects.filter(email = request.POST['email'])
        
        # if useralredy:
        if len(useralredy) > 0:
            return render(request,'register.html',{'alredy':"This email is alredy registered..."})
        else:
            if request.POST['password'] == request.POST['cp']:
                user.save()
                return render(request,'register.html',{'store':"you are registered successfully..."})
            else:
                return render(request,'register.html',{'pass':"password did not  matched....."})
    else:
        return render(request,'register.html')

def login(request):
    if request.method =='POST' :
        try:
            user = userregister.objects.get(email = request.POST['email'])
            if user.password == request.POST['password'] :
                request.session['email'] = user.email
                return redirect('index')
            else :
                return render(request,'login.html',{'pass':"password id incorrect....."})
        except:
            return render(request,'login.html',{'notregistered':"before login you have to registered first..."})      
    else:
        return render(request,'login.html')
    

def logout(request):
    del request.session['email']
    return redirect('index')