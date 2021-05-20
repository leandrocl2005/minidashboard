from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from personalservices.models import PersonalService


# Create your views here.
@login_required
@require_http_methods(["GET"])
def home(request):
  context = dict()

  # number of projects to microsoft
  num_microsoft_projects = len(
      PersonalService.objects.filter(company__name='Microsoft', name='P'))
  context["num_microsoft_projects"] = num_microsoft_projects

  # number of projects to samsung
  num_samsung_projects = len(
      PersonalService.objects.filter(company__name='Samsung', name='P'))
  context["num_samsung_projects"] = num_samsung_projects

  # number of projects to apple
  num_apple_projects = len(
      PersonalService.objects.filter(company__name='Apple', name='P'))
  context["num_apple_projects"] = num_apple_projects

  # number of budgets to microsoft
  num_microsoft_budgets = len(
      PersonalService.objects.filter(company__name='Microsoft', name='O'))
  context["num_microsoft_budgets"] = num_microsoft_budgets

  # number of budgets to samsung
  num_samsung_budgets = len(
      PersonalService.objects.filter(company__name='Samsung', name='O'))
  context["num_samsung_budgets"] = num_samsung_budgets

  # number of budgets to apple
  num_apple_budgets = len(
      PersonalService.objects.filter(company__name='Apple', name='O'))
  context["num_apple_budgets"] = num_apple_budgets

  # number of consults to microsoft
  num_microsoft_consults = len(
      PersonalService.objects.filter(company__name='Microsoft', name='C'))
  context["num_microsoft_consults"] = num_microsoft_consults

  # number of consults to samsung
  num_samsung_consults = len(
      PersonalService.objects.filter(company__name='Samsung', name='C'))
  context["num_samsung_consults"] = num_samsung_consults

  # number of consults to apple
  num_apple_consults = len(
      PersonalService.objects.filter(company__name='Apple', name='C'))
  context["num_apple_consults"] = num_apple_consults

  return render(request, 'index.html', context)
