# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Marcador'
        db.create_table('lancamento_marcador', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('lancamento', ['Marcador'])

        # Adding model 'FormaPagamento'
        db.create_table('lancamento_formapagamento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('lancamento', ['FormaPagamento'])

        # Adding model 'ClienteFornecedor'
        db.create_table('lancamento_clientefornecedor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('telefone', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('lancamento', ['ClienteFornecedor'])

        # Adding model 'ContaCartao'
        db.create_table('lancamento_contacartao', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('lancamento', ['ContaCartao'])

        # Adding model 'Conta'
        db.create_table('lancamento_conta', (
            ('contacartao_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['lancamento.ContaCartao'], unique=True, primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('agencia', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('saldo_inicial', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('data_saldo', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('lancamento', ['Conta'])

        # Adding model 'Cartao'
        db.create_table('lancamento_cartao', (
            ('contacartao_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['lancamento.ContaCartao'], unique=True, primary_key=True)),
            ('fechamento', self.gf('django.db.models.fields.DateField')()),
            ('vencimento', self.gf('django.db.models.fields.DateField')()),
            ('limite', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
        ))
        db.send_create_signal('lancamento', ['Cartao'])

        # Adding model 'PadraoLancamento'
        db.create_table('lancamento_padraolancamento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('tipo_lancamento', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('forma_pagamento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lancamento.FormaPagamento'])),
            ('conta_cartao', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lancamento.ContaCartao'])),
            ('cliente_fornecedor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lancamento.ClienteFornecedor'])),
        ))
        db.send_create_signal('lancamento', ['PadraoLancamento'])

        # Adding model 'Transferencia'
        db.create_table('lancamento_transferencia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('conta_origem', self.gf('django.db.models.fields.related.ForeignKey')(related_name='conta_origem', to=orm['lancamento.Conta'])),
            ('conta_destino', self.gf('django.db.models.fields.related.ForeignKey')(related_name='conta_destino', to=orm['lancamento.Conta'])),
            ('valor', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
        ))
        db.send_create_signal('lancamento', ['Transferencia'])

        # Adding model 'Categoria'
        db.create_table('lancamento_categoria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('categoria_pai', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lancamento.Categoria'], null=True, blank=True)),
        ))
        db.send_create_signal('lancamento', ['Categoria'])

        # Adding model 'Lancamento'
        db.create_table('lancamento_lancamento', (
            ('padraolancamento_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['lancamento.PadraoLancamento'], unique=True, primary_key=True)),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lancamento.Categoria'])),
            ('lancamento', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 8, 2, 0, 0))),
            ('pagamento', self.gf('django.db.models.fields.DateField')()),
            ('vencimento', self.gf('django.db.models.fields.DateField')()),
            ('valor', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('valor_pago', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('parcela', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('lancamento', ['Lancamento'])

        # Adding model 'Parcela'
        db.create_table('lancamento_parcela', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lancamento', self.gf('django.db.models.fields.related.ForeignKey')(related_name='parcelas', to=orm['lancamento.Lancamento'])),
            ('quantidade', self.gf('django.db.models.fields.IntegerField')()),
            ('valor', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
        ))
        db.send_create_signal('lancamento', ['Parcela'])


    def backwards(self, orm):
        # Deleting model 'Marcador'
        db.delete_table('lancamento_marcador')

        # Deleting model 'FormaPagamento'
        db.delete_table('lancamento_formapagamento')

        # Deleting model 'ClienteFornecedor'
        db.delete_table('lancamento_clientefornecedor')

        # Deleting model 'ContaCartao'
        db.delete_table('lancamento_contacartao')

        # Deleting model 'Conta'
        db.delete_table('lancamento_conta')

        # Deleting model 'Cartao'
        db.delete_table('lancamento_cartao')

        # Deleting model 'PadraoLancamento'
        db.delete_table('lancamento_padraolancamento')

        # Deleting model 'Transferencia'
        db.delete_table('lancamento_transferencia')

        # Deleting model 'Categoria'
        db.delete_table('lancamento_categoria')

        # Deleting model 'Lancamento'
        db.delete_table('lancamento_lancamento')

        # Deleting model 'Parcela'
        db.delete_table('lancamento_parcela')


    models = {
        'lancamento.cartao': {
            'Meta': {'object_name': 'Cartao', '_ormbases': ['lancamento.ContaCartao']},
            'contacartao_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['lancamento.ContaCartao']", 'unique': 'True', 'primary_key': 'True'}),
            'fechamento': ('django.db.models.fields.DateField', [], {}),
            'limite': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'vencimento': ('django.db.models.fields.DateField', [], {})
        },
        'lancamento.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'categoria_pai': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lancamento.Categoria']", 'null': 'True', 'blank': 'True'}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'lancamento.clientefornecedor': {
            'Meta': {'object_name': 'ClienteFornecedor'},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'lancamento.conta': {
            'Meta': {'object_name': 'Conta', '_ormbases': ['lancamento.ContaCartao']},
            'agencia': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'contacartao_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['lancamento.ContaCartao']", 'unique': 'True', 'primary_key': 'True'}),
            'data_saldo': ('django.db.models.fields.DateField', [], {}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'saldo_inicial': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'lancamento.contacartao': {
            'Meta': {'object_name': 'ContaCartao'},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'lancamento.formapagamento': {
            'Meta': {'object_name': 'FormaPagamento'},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'lancamento.lancamento': {
            'Meta': {'object_name': 'Lancamento', '_ormbases': ['lancamento.PadraoLancamento']},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lancamento.Categoria']"}),
            'lancamento': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 8, 2, 0, 0)'}),
            'padraolancamento_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['lancamento.PadraoLancamento']", 'unique': 'True', 'primary_key': 'True'}),
            'pagamento': ('django.db.models.fields.DateField', [], {}),
            'parcela': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'valor': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'valor_pago': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'vencimento': ('django.db.models.fields.DateField', [], {})
        },
        'lancamento.marcador': {
            'Meta': {'object_name': 'Marcador'},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'lancamento.padraolancamento': {
            'Meta': {'object_name': 'PadraoLancamento'},
            'cliente_fornecedor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lancamento.ClienteFornecedor']"}),
            'conta_cartao': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lancamento.ContaCartao']"}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'forma_pagamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lancamento.FormaPagamento']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo_lancamento': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'lancamento.parcela': {
            'Meta': {'object_name': 'Parcela'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lancamento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'parcelas'", 'to': "orm['lancamento.Lancamento']"}),
            'quantidade': ('django.db.models.fields.IntegerField', [], {}),
            'valor': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'})
        },
        'lancamento.transferencia': {
            'Meta': {'object_name': 'Transferencia'},
            'conta_destino': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'conta_destino'", 'to': "orm['lancamento.Conta']"}),
            'conta_origem': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'conta_origem'", 'to': "orm['lancamento.Conta']"}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'valor': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'})
        }
    }

    complete_apps = ['lancamento']