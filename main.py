from codigo.bytebank import Funcionario

def teste_idade():
    teste = Funcionario('teste', '17/09/1999', 1000)
    print(f'Teste = {teste.idade()}')

teste_idade()