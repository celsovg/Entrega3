from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import RegistrarForm, perfilUsuarioForm

# Create your views here.

# def usuario_view(request):
#    if request.method == 'POST':
#        form = UsuarioForm (request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect ('usuario:usuario_view')
#            else:
#                form = MascotaForm()
#
#            return render(request,'usuario/UsuarioForm.html',{'form':form})}


def usuario_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('usuario:index'))


def index(request):
    return render(request, 'usuario/index.html', {})


def usuario_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('usuario:index'))
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('usuario:index'))
                else:
                    return HttpResponseRedirect("Tu cuenta esta inactiva")
            else:
                print("username:{} - password:{}".format(username, password))
                return HttpResponse("Datos invalidos")
        else:
            return render(request, 'usuario/login.html')


def registrar(request):
    registrado = False
    if request.method == "POST":
        user_form = RegistrarForm(data=request.POST)
        profile_from = perfilUsuarioForm(data=request)

        if user_form.is_valid() and profile_from.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_from.save(commit=False)
            profile.user = user
            if 'foto_perfil' in request.FILES:
                profile.foto_perfil = request.FILES['foto_perfil']
            profile.save()
            registrado = True
        else:
            print(user_form.errors, profile_from.errors)
            return HttpResponse("Datos invalidos")
    else:
        user_form = RegistrarForm()
        profile_from = perfilUsuarioForm()

    return render(request, 'usuario/registrar.html',
                  {'user_form': user_form,
                  'profile_from': profile_from,
                  'registrado': registrado})
