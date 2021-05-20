from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Layout, Submit, Row, Column, Field

from .models import Company


class CompanyForm(forms.ModelForm):
  class Meta:
    model = Company
    fields = '__all__'

  # override default form properties
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    # change field label
    self.fields['name'].label = "Nome da compania"

    self.helper = FormHelper()
    self.helper.form_method = 'post'

    # change layout of form
    self.helper.layout = Layout(
        Fieldset('Identificação', Field('name')),
        Fieldset(
            'Contatos',
            Row(Column('email', css_class="col-md-6 mb-0"),
                Column('phone', css_class="col-md-6 mb-0"))),
        Submit('submit', 'Enviar', css_class="mt-2 mb-4"))
