from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Company(models.Model):

  name = models.CharField(max_length=50, verbose_name="Nome")
  email = models.EmailField(max_length=50, verbose_name="E-mail")
  phone = models.CharField(
      max_length=16,
      verbose_name="Telefone",
      help_text="Exemplo: (00) 0000-0000",
      validators=[
          RegexValidator(regex=r'^[0-9]{10}$',
                         message='Deve ter 10 ou 11 números. Veja o exemplo.')
      ])
  created_at = models.DateTimeField(auto_now_add=True,
                                    verbose_name="Criado em")
  updated_at = models.DateTimeField(auto_now=True,
                                    verbose_name="Atualizado em")

  @property
  def formatted_phone(self):
    if len(self.phone) == 10:
      return "({}) {}-{}".format(self.phone[:2], self.phone[2:6],
                                 self.phone[6:10])

  def __str__(self):
    return self.name

  class Meta:
    verbose_name_plural = "Companias"
    verbose_name = "Compania"
    ordering = ('name', )
