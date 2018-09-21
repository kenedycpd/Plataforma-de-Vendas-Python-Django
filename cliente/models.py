from django.db import models

# Create your models here.
class CadastroCliente(models.Model):
    id = models.AutoField(primary_key=True)
    TP = (
        ('J', 'Pessoa Juridica'),
        ('F', 'Pessoa Fisica'),
        )
    tipo_pessoa = models.CharField(max_length=1, choices=TP, verbose_name='Tipo de Pessoa')
    razao_social = models.CharField(max_length=100, verbose_name='Razao Social')
    nome_fantasia = models.CharField(max_length=100, verbose_name='Nome Fantasia')
    cnpj = models.CharField(max_length=50, verbose_name='Cnpj/Cpf')
    estadual = models.CharField(max_length=50, verbose_name='Insc.Estadual')
    ramo_atividade = models.CharField(max_length=50, verbose_name='Ramo de Atividade')
    logradouro = models.CharField(max_length=100, verbose_name='Endereco')
    cep = models.CharField(max_length=100, verbose_name='Cep')
    numero = models.CharField(max_length=5, verbose_name='Numero')
    bairro = models.CharField(max_length=50, verbose_name='Bairro')
    fone = models.CharField(max_length=50, verbose_name='Telefone')
    email = models.CharField(max_length=50, verbose_name='Email')
    cidade = models.CharField(max_length=50, verbose_name='Cidade')
    estado = models.CharField(max_length=50, verbose_name='Estado')

    def __str__(self):
    	return self.razao_social


class CadastroProduto(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100, verbose_name='Descrição')
    embalagem = models.CharField(max_length=5, verbose_name='Embalagem')
    marca = models.CharField(max_length=100, verbose_name='Marca')
    preco = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Preço do Produto')
    def __str__(self):
        return self.descricao


class PedidoVenda(models.Model):
    id = models.AutoField(primary_key=True)
    quantidade = models.IntegerField(verbose_name='Qunatidade do Produto')
    preco_compra = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Preço do Produto')
    cadastroproduto = models.ForeignKey(CadastroProduto, on_delete=models.CASCADE)
    cadastrocliente = models.ForeignKey(CadastroCliente, on_delete=models.CASCADE)

    def calculo(self):
        return self.preco_compra * self.quantidade
    media = property(calculo)

    

    def __str__(self):
        return "%s" % self.cadastrocliente