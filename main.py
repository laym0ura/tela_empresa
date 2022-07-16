def calcular(valor, cartao, tipo):
  valor_compra = float(valor)
  valor_venda = valor_compra + (valor_compra*0.45)
  if cartao == 'Não':
    valor_venda_final = valor_venda
  elif cartao == 'Sim':
    valor_venda_final = valor_venda + (valor_venda*0.12)
  if tipo == 'Vendedora':
    comissao = valor_venda*0.1
  elif tipo == 'Supervisora':
    comissao = valor_venda*0.13
  elif tipo == 'Gerente':
    comissao = valor_venda*0.16
  return {'Valor Venda Final': f'R$ {round(valor_venda_final, 2)}',
          f'Comissão da {tipo}': f'R${round(comissao, 2)}',
          'Lucro da Empresa': f'R$ {round(valor_venda-(comissao+valor_compra), 2)}',
          'Lucro Percentual da Empresa': f'{round((valor_venda-(comissao+valor_compra))/valor_venda, 2)*100}%'}
