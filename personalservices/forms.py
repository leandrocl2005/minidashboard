from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Layout, Submit, Row, Column, Field

from .models import PersonalService


class PersonalServiceForm(forms.ModelForm):
  class Meta:
    model = PersonalService
    fields = '__all__'

  # override default form properties
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.helper = FormHelper()
    self.helper.form_method = 'post'

    self.helper.layout = Layout(
        Row(Column('name', css_class="col-md-5 mb-0"),
            Column('company', css_class="col-md-5 mb-0 ml-2")),
        Submit('submit', 'Enviar', css_class="mt-2 mb-4"))
