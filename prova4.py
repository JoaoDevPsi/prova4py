def soma_pares(inicio, fim):

  soma = 0
  for i in range(inicio, fim + 1):
    if i % 2 == 0:
      soma += i
      print(f"Número par encontrado: {i}") 
  
  if soma == 0:
    return "Não há números pares no intervalo."
  else:
    return f"A soma dos números pares é: {soma}"

inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

resultado = soma_pares(inicio, fim)
print(resultado)