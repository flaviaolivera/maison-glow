from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse('admin:index'))  # Redirigir al usuario después de registrarse
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        # AuthenticationForm para manejar el inicio de sesión.
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # Autenticar al usuario
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                # El usuario se autenticó correctamente, inicia sesión
                login(request, user)
                return redirect(reverse('admin:index')) 
            else:
                # La autenticación falló, muestra un mensaje de error
                messages.error(request, 'Credenciales inválidas. Por favor, inténtalo de nuevo.')
        else:
            # Formulario no válido, muestra un mensaje de error
            messages.error(request, 'Credenciales inválidas. Por favor, inténtalo de nuevo.')
    else:
        form = AuthenticationForm()
    # La plantilla login.html que se utiliza es la plantilla predeterminada de Django para el formulario de inicio de sesión. 
    return render(request, 'accounts/login.html', {'form': form})