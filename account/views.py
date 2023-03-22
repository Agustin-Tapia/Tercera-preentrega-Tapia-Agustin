from account.forms import *
from account.models import *
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
#no tiene que ser igual el login de arriba que la vista que vamos a crear.

# como bloquear una pagina >>> @login_required 
# importar aca el login required from>>> django.contrib.auth.decorators import login_required

def editar_usuario(request):
    user = request.user
    if request.method == "POST":
        form = UserRegisterForm(request.POST, request.FILES)
    
        if form.is_valid():
            informacion = form.cleaned_data

            user.username = informacion["username"]
            user.email = informacion["email"]
            is_staff = user.is_staff
            
            try:
                avatar = Avatar(user = user, imagen = informacion["imagen"])
            except:
                avatar = Avatar(user = user, imagen = informacion["imagen"])
            user.save()
            return redirect("Login")
        

    form = UserRegisterForm(initial= {
        "username": user.username,
        "email": user.email,
        "is_staff": user.is_staff
    })
    context = {
        "form": form
    }
    return render(request, "casa/register.html", context)




def register_account(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(request,"casa/base.html", {"mensaje": "Usuario creado!"})
        
    form = UserCreationForm()
    context = {
        "form": form
    }    
    return render(request, "account/register.html", context)


def login_account(request):
    
    if request.method == "POST":
        form= AuthenticationForm(request, data = request.POST)
    
        if form.is_valid():
            informacion = form.cleaned_data

            user = authenticate(username = informacion['username'], password = informacion['password'])

            if user is not None: 
                login(request, user)

                return redirect('casa/base.html')
            else:
                return redirect('casa/base.html')
        else:
            return redirect('casa/base.html',{"mensaje": "Error de formulario"})
            
    form = AuthenticationForm()
    context = {
        "form": form
    }
    return render(request, "account/login.html", context)