def calcular_media(valores):
    tamanho = len(valores)  # Corrigido para obter o tamanho correto da lista
    soma = 0.0
    for valor in valores:  # O enumerate excluído
        soma += valor
    media = soma / tamanho
    return media  # O i não é necessário e foi adicionado o return para que a função retorne a média
    
continuar = True
valores = []
while continuar:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor:')
    if valor.lower() == 'ok':
        continuar = False  # False com a primeira letra maiúscula
    else:
        valores.append(float(valor))  # Adicionado o append para adicionar e o float para formatação dos números

media = calcular_media(valores)
print('A média calculada pelos valores {} foi de {}'.format(valores, media))