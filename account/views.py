from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
#no tiene que ser igual el login de arriba que la vista que vamos a crear.

# como bloquear una pagina >>> @login_required 
# importar aca el login required from>>> django.contrib.auth.decorators import login_required

def register_account(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(request,"casa/base.html", {"mensaje": "Usuario creado!"})
        
    form = UserCreationForm()
    context = {
        "form": form
    }    
    return redirect(request, "casa/register.html", context)


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
    return render(request, "casa/login.html", context)