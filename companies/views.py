from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

from companies.forms import CompanyForm
from companies.models import Company


@login_required
@require_http_methods(["GET", "POST"])
def create_company(request):

  context = {'pagetitle': 'Cadastrar compania'}

  if request.method == "GET":
    form = CompanyForm()
    context['form'] = form
    return render(request, 'form_create.html', context)

  if request.method == "POST":
    form = CompanyForm(request.POST)
    if form.is_valid():

      company = form.save(commit=False)

      # Extra rule (check if company already exists)
      company_already_exists = Company.objects.filter(
          name__icontains=company.name).first()
      if company_already_exists:
        context['form'] = form
        messages.error("Compania com esse nome já existe")
        return render(request, 'form_create.html', context)

      company.save()

      messages.success(request, 'Compania criada com sucesso!')

      return redirect('/company/create/')
    else:
      context['form'] = form
      messages.error(request, "Erro ao cadastrar compania.")
      return render(request, 'create_company.html', context)

  messages.error("Algo deu errado")
  return redirect('/company/create/')
