from django.shortcuts import render, redirect, HttpResponse,get_object_or_404
from datetime import *
from .models import *
from .forms import PedidoForm
# Create your views here.
def home(request):
	return render(request,'index.html',{})

def cliente(request):
	return render(request,'cliente/cadastro.html',{})

def produto(request):
	produto = CadastroProduto.objects.all()
	return render(request,'cliente/produto.html',{'produto':produto})

def pedido(request):
	if request.method == 'POST':
		form = PedidoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('imprimir')
	else:
		form = PedidoForm()
	return render(request,'cliente/pedido.html',{'form':form})

def imprimir(request):
	data = datetime.now()
	vendas = PedidoVenda.objects.order_by('id')
	return render(request,'cliente/imprimir.html',{'vendas':vendas, 'data': data})

def delete_pedido(request, id_pedido):
	pedido = PedidoVenda.objects.get(id=id_pedido).delete()
	return redirect('imprimir')

def edit_pedido(request, id):
	edite = get_object_or_404(PedidoVenda, id=id)
	if request.method == 'POST':
		form = PedidoForm(request.POST, instance=edite)
		if form.is_valid():
			form.save()
			return redirect('imprimir')
	else:
		form = PedidoForm(instance=edite)
	return render(request,'cliente/pedido.html',{'form':form})