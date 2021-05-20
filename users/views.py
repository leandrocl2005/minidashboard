from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


def user_registration(request):
  if request.method == "POST":
    form = NewUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      messages.success(request, "Cadastro realizado com sucesso.")
      return redirect("/accounts/login/")
    messages.error(request, "Cadastro não realizado. Tente denovo.")
  form = NewUserForm
  return render(request=request,
                template_name="registration/signup.html",
                context={"register_form": form})
