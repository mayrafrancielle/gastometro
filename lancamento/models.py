# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
import datetime

# Create your models here.
class Descricao(models.Model):

    descricao = models.CharField(u'Descrição',max_length=255)
    usuario = models.ForeignKey(User)

    class Meta:
        abstract = True

class Marcador(Descricao):

    pass

class FormaPagamento(Descricao):

    pass

class ClienteFornecedor(Descricao):

    telefone = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()

class ContaCartao(Descricao):
    pass
    # class Meta:
    #     abstract = True

class Conta(ContaCartao):

    tipo = models.CharField(max_length=50)
    agencia = models.CharField(max_length=50, null=True, blank=True)
    numero = models.CharField(max_length=50, null=True, blank=True)
    saldo_inicial = models.DecimalField(max_digits=15,decimal_places=2)
    data_saldo = models.DateField()

class Cartao(ContaCartao):

    fechamento = models.DateField()
    vencimento = models.DateField()
    limite = models.DecimalField(max_digits=15,decimal_places=2)

class PadraoLancamento(Descricao):

    tipo_lancamento = models.CharField(u'Tipo de Lançamento', max_length=100, )
    forma_pagamento = models.ForeignKey(FormaPagamento)
    conta_cartao = models.ForeignKey(ContaCartao)
    cliente_fornecedor = models.ForeignKey(ClienteFornecedor)

class Transferencia(Descricao):

    conta_origem = models.ForeignKey(Conta,related_name='conta_origem')
    conta_destino = models.ForeignKey(Conta,related_name='conta_destino')
    valor = models.DecimalField(max_digits=15,decimal_places=2)

class Categoria(Descricao):

    categoria_pai = models.ForeignKey('Categoria',null=True, blank=True)

class Lancamento(PadraoLancamento):

    categoria = models.ForeignKey(Categoria)
    lancamento = models.DateTimeField(default=datetime.date.today())
    pagamento = models.DateField()
    vencimento = models.DateField()
    valor = models.DecimalField(max_digits=15,decimal_places=2)
    valor_pago = models.DecimalField(max_digits=15,decimal_places=2)
    parcela = models.BooleanField(default=False)
    tipo = models.CharField(max_length=50)

class Parcela(models.Model):

    lancamento = models.ForeignKey(Lancamento,related_name='parcelas')
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=15,decimal_places=2)