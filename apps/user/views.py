from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm, PasswordChangeForm
# Create your views here.
from django.contrib.auth.models import User
from apps.post.models import Post
from apps.user.forms import EditarUsuarioForm, NuevoUsuarioForm

def iniciar_sesion(request):
    if request.user.is_authenticated:
        return redirect("listar_posts")
        
    form = AuthenticationForm(data = request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect("/")
    return render(request, "user/login.html",{
        "form":form,
    })

def cerrar_sesion(request):
    logout(request)
    return redirect("/")

def nuevo_usuario(request):
    if request.user.is_authenticated:
        return redirect("listar_posts")

    form = NuevoUsuarioForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            #user.set_password("clave1234")
            if user is not None:
                login(request,user)
                return redirect("listar_posts")
    return render(request, "user/nuevo_usuario.html", {
        "form":form
    })

def perfil(request, id):
    try:
        user = User.objects.get(pk=id)
    except:
        return HttpResponse("<h2>No existe el post</h2>")

    posts = Post.objects.filter(autor = id)
    contexto = {
        "perfil": user,
        "lista_posts": posts
    }

    template = "user/perfil.html"

    return render(request, template, contexto)


def editar_usuario(request):
    if not request.user.is_authenticated:
        return redirect("login")
    user = request.user
    form = EditarUsuarioForm(request.POST or None, instance=user)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            return redirect("perfil", user.id)
    return render(request, "user/editar_usuario.html",{
        "form":form,
    })

def editar_clave(request):
    if not request.user.is_authenticated:
        return redirect("login")
    user = request.user
    form = PasswordChangeForm(data=request.POST or None, user=user)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            return redirect("listar_posts")
    return render(request, "user/editar_clave.html",{
        "form":form,
    })
