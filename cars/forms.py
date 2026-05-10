from django import forms
from cars.models import Car

  
class CarModelForm(forms.ModelForm):
  class Meta:
    model = Car
    fields = '__all__'

  def clean_value(self):
    value = self.cleaned_data.get('value')
    if value < 20000:
      self.add_error('value', 'Valor minimo do carro deve ser R$20.000')
    return value
  
  def clean_factory_year(self):
    factory_year = self.cleaned_data.get('factory_year')
    if factory_year is None:
      self.add_error('factory_year', 'Ano de fabricaçao é obrigatorio')
    elif factory_year < 1940:
      self.add_error('factory_year', 'Carro muito velho, vou adicionar isso nao (-1940)')

    return factory_year
  
  def clean_model_year(self):
    model_year = self.cleaned_data.get('model_year')
    if model_year is None:
      self.add_error('model_year', 'Ano do Modelo do carro é obrigatorio')
    elif model_year < 1940:
      self.add_error('model_year', 'Carro muito velho, vou adicionar isso nao (-1940)')

    return model_year