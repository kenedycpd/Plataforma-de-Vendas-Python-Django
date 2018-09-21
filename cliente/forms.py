from django.forms import ModelForm
from .models import PedidoVenda

class PedidoForm(ModelForm):
	class Meta:
		model = PedidoVenda
		fields = '__all__'