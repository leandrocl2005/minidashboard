from django.db import models
from companies.models import Company


# Create your models here.
class PersonalService(models.Model):

  name = models.CharField(verbose_name="Nome do serviço",
                          max_length=10,
                          choices=[('C', 'consultoria'), ('P', 'projeto'),
                                   ('O', 'orçamento')])
  company = models.ForeignKey(Company,
                              on_delete=models.PROTECT,
                              verbose_name="Compania")
  created_at = models.DateTimeField(auto_now_add=True,
                                    verbose_name="Criado em")
  updated_at = models.DateTimeField(auto_now=True,
                                    verbose_name="Atualizado em")

  def __str__(self):
    return self.company.name + "  -  (dt. serviço: " + self.created_at.strftime(
        "%d/%m/%Y") + ")"

  class Meta:
    verbose_name_plural = "Serviços"
    verbose_name = "Serviço"
    ordering = ('-created_at', )
