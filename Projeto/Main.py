def soma(valores):
    return sum(valores)

def sub(valores):
    resultado = valores[0]
    for i in range(1, len(valores)):
        resultado -= valores[i]
    return resultado

def mult(valores):
    resultado = 1
    for valor in valores:
        resultado *= valor
    return resultado

def divisao(valores):
    resultado = valores[0]
    for i in range(1, len(valores)):
        if valores[i] == 0:
            print('Não é possível realizar a divisão por zero')
            return None
        resultado /= valores[i]
    return resultado

fila = []


def addOperacaoFila():
    opcoes = {1: '+', 2: '-', 3: '*', 4: '/'}
    opcao = int(input('Selecione a operação: 1 - Adição, 2 - Subtração, 3 - Multiplicação, 4 - Divisão: '))
    if opcao in opcoes:
        qtdeItensOperacao = int(input('Quantos valores serão incluídos nessa operação? '))
        fila.append(opcoes[opcao])
        for j in range(qtdeItensOperacao):
            fila.append(int(input(f'{j + 1} - Digite o valor: ')))
        fila.append('Fim')
    else:
        print('Opção inválida')
        
def expressoes():
    i = 10
    while i != 0:
        print("======= Validador de Expressões Matemáticas =======")
        expressao = input('Digite uma expressão matemática:\n')
        pilha = []
        pares = {'(': ')', '{': '}', '[': ']'}

        for char in expressao:
            if char in pares.keys():
                pilha.append(char)
            elif char in pares.values():
                if not pilha:
                    print("INVÁLIDA")
                    break
                last_char = pilha.pop()
                if char != pares[last_char]:
                    print("INVÁLIDA")
                    break
            elif not char.isdigit() and char not in '+-/*':
                print("INVÁLIDA")
                break
        else:
            if pilha:
                print("INVÁLIDA")
            else:
                print("VÁLIDA")
                
        i = 0



def executarOperacoes():
    while fila:
        operacao = fila.pop(0)
        valores = []
        while fila and fila[0] != 'Fim':
            valores.append(fila.pop(0))
        if fila:
            fila.pop(0)
        if operacao == '+':
            print(f'Adição - Valores: {valores} - Resultado: {soma(valores)}')
        elif operacao == '-':
            print(f'Subtração - Valores: {valores} - Resultado: {sub(valores)}')
        elif operacao == '*':
            print(f'Multiplicação - Valores: {valores} - Resultado: {mult(valores)}')
        elif operacao == '/':
            resultado = divisao(valores)
            if resultado is not None:
                print(f'Divisão - Valores: {valores} - Resultado: {resultado}')
                
        
def menu():
    opcao = 1
    while opcao != 0:
        print('\nMENU OPERAÇÕES')
        print('1 - Adicionar Operação na Fila')
        print('2 - Executar Próxima Operação da Fila')
        print('3 - Executar Todas as Operações da Fila')
        print('0 - Sair')
        try:
            opcao = int(input('\nSelecione a opção desejada: '))
            if opcao == 1:
                addOperacaoFila()
            elif opcao == 2:
                if fila:
                    executarOperacoes()
                else:
                    print('Não existem operações na fila')
            elif opcao == 3:
                if fila:
                    executarOperacoes()
                else:
                    print('Não existem operações na fila')
            elif opcao == 0:
                print('Saindo...')
            else:
                print('Opção inválida')
        except ValueError:
            print('Opção inválida')


if __name__ == '__main__':
    fila = []
    
    def addOperacaoFila():
        opcoes = {1: '+', 2: '-', 3: '*', 4: '/'}
        opcao = int(input('Selecione a operação: 1 - Adição, 2 - Subtração, 3 - Multiplicação, 4 - Divisão: '))
        if opcao in opcoes:
            qtdeItensOperacao = int(input('A operação irá conter quantos valores? '))
            fila.append(opcoes[opcao])
            for j in range(qtdeItensOperacao):
                fila.append(int(input(f'{j + 1} - Digite o valor: ')))
            fila.append('Fim')
        else:
            print('Opção inválida')

    def executarOperacoes():
        while fila:
            operacao = fila.pop(0)
            valores = []
            while fila and fila[0] != 'Fim':
                valores.append(fila.pop(0))
            if fila:
                fila.pop(0)
            if operacao == '+':
                print(f'Adição - Valores: {valores} - Resultado: {soma(valores)}')
            elif operacao == '-':
                print(f'Subtração - Valores: {valores} - Resultado: {sub(valores)}')
            elif operacao == '*':
                print(f'Multiplicação - Valores: {valores} - Resultado: {mult(valores)}')
            elif operacao == '/':
                print(f'Divisão - Valores: {valores} - Resultado: {divisao(valores)}')
                
    def menu():
        opcao = 1
        while opcao != 0:
            print('\nMENU OPERAÇÕES')
            print('1 - Adicionar Operação na Fila')
            print('2 - Executar Próxima Operação da Fila')
            print('3 - Executar Todas as Operações da Fila')
            print('0 - Sair')
            try:
                opcao = int(input('\nSelecione uma opção: '))
                if opcao == 1:
                    addOperacaoFila()
                elif opcao == 2:
                    if fila:
                        executarOperacoes()
                    else:
                        print('Não há operações na fila')
                elif opcao == 3:
                    if fila:
                        executarOperacoes()
                    else:
                        print('Não há operações na fila')
                elif opcao == 0:
                    print('SAIU')
                else:
                    print('Opção inválida')
            except ValueError:
                print('Opção inválida')
                
    menu()
