from funcoes import *

minhasListas = []
print("Preenchendo")
preencherinventario(minhasListas)
print("Exibindo")
exibirInventario(minhasListas)

print("Pesquisando")
localizaPorNome(minhasListas)
print("Alterando")
depreciarPorNome(minhasListas, 20)

print("Excluindo")
print(excluirPorSerial(minhasListas))
exibirInventario(minhasListas)

print("Resumindo")
resumirValores(minhasListas)