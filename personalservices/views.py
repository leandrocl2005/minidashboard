from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

from personalservices.forms import PersonalServiceForm
from personalservices.models import PersonalService


@login_required
@require_http_methods(["GET", "POST"])
def create_service(request):

  context = {'pagetitle': 'Registrar serviço'}

  if request.method == "GET":
    form = PersonalServiceForm()
    context['form'] = form
    return render(request, 'form_create.html', context)

  if request.method == "POST":
    form = PersonalServiceForm(request.POST)
    if form.is_valid():

      service = form.save(commit=False)

      # there is no extra rules

      service.save()

      messages.success(request, 'Serviço registrado com sucesso!')
      return redirect('/service/create/')
    else:
      messages.error(request, "Erro ao cadastrar serviço.")
      context['form'] = form
      return render(request, 'form_create.html', context)

  messages.error("Algo deu errado")
  return redirect('/service/create/')
