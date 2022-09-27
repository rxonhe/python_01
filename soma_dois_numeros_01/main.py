"""
Level - Medium
https://leetcode.com/problems/add-two-numbers/

Você recebe duas listas vinculadas não vazias representando dois números inteiros não negativos. Os dígitos são
armazenados em ordem inversa e cada um de seus nós contém um único dígito. Some os dois números e retorne a soma como
uma lista encadeada. Você pode assumir que os dois números não contêm nenhum zero à esquerda, exceto o próprio número
0.

O código é uma instrução.
Precisamos montar previamente quais passos serão seguidos para que possamos retornar as respostas desejadas.

O que recebemos: duas listas invertidas
O que vamos devolver: uma lista invertida que soma as duas recebidas

**detalhes**
Em python utilizamos o underline (_) para separar as palavras nas variáveis e funções
Apenas em classes (veremos depois) podemos utilizar letras maiúsculas. Nas variáveis e funções apenas minusculas.

Nossa função principal nesse programa será a soma_dois_numeros(lista_0, lista_1) (Em programação começamos contando a
partir do zero)

Uma função pode ser diferenciada de uma variável por conta dos parênteses, que trazem dentro de si os parâmetros
necessários para que a função execute.

No nosso caso em específico, temos as listas, 0 e 1.

Vamos para o código.
"""


# Utilizamos aqui o "def" para definir uma nova função, após sua definição
# colocamos dois pontos (:) para montar os passos que compõem essa execução
def soma_dois_numeros(lista_0, lista_1):
    """Função principal, retorna uma lista invertida que corresponde a soma de duas listas invertidas"""
    # passos:
    # 1 - Inverter cada uma das listas recebidas
    lista_0_invertida = inverter(lista_0)
    lista_1_invertida = inverter(lista_1)
    # 2 - Converter a lista em um número inteiro
    numero_0 = converte_em_inteiro(lista_0_invertida)
    numero_1 = converte_em_inteiro(lista_1_invertida)
    # 3 - Somar os números
    total = numero_0 + numero_1
    # 4 - Transformar de inteiro para lista novamente
    lista_total = inteiro_para_lista(total)
    # 5 - Inverter a lista e retornar o resultado
    return inverter(lista_total)


# a lógica está criada, agora precisamos criar cada uma das funções que compõe essas instruções

def inverter(lista):
    """Retorna a lista ao contrário"""
    return list(reversed(lista))


def converte_em_inteiro(lista):
    """Converte uma lista em um número inteiro"""
    # para converter uma lista em inteiro, precisamos primeiro concatenar (juntar) cada um de seus números
    lista_em_texto = ""
    # para cada elemento dentro da lista
    for elemento in lista:
        # vamos adicioná-lo ao texto que estamos montando (precisamos converter cada número para texto -> str(numero))
        lista_em_texto = lista_em_texto + str(elemento)
    # Depois de concatenar a lista, podemos converter a string(texto) que foi criado em inteiro e retorná-lo
    return int(lista_em_texto)


def inteiro_para_lista(inteiro):
    """Converte um número inteiro para lista"""
    # Aqui é o processo reverso, precisamos transformar o número em String(texto) para pegar cada um de seus dígitos
    texto = str(inteiro)
    # e depois podemos criar uma lista contendo cada elemento dessa string em uma posição separada
    lista = []
    # para cada numero no texto
    for numero in texto:
        # adicionamos o número na lista
        lista.append(numero)
    return lista


# aqui é onde rodaremos nosso código para testar sua funcionalidade
if __name__ == "__main__":
    lista_0 = [2, 4, 3]
    lista_1 = [5, 6, 4]
    soma = soma_dois_numeros(lista_0, lista_1)
    print(str(soma))
