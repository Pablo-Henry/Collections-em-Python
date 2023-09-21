from collections import Counter

texto1 = """O Java é uma das plataformas mais utilizadas para o desenvolvimento de aplicações ao redor do mundo. Além da plataforma, segundo dados da Pesquisa “Tecnologias mais populares de 2022”, realizada pelo StackOverflow, a linguagem Java figura como a 6ª mais utilizada por pessoas desenvolvedoras, correspondendo a 33% do total pesquisado.Quem está iniciando com essa tecnologia pode encontrar alguma dificuldade para compreender a “quantidade de código” que é necessária para escrever uma mensagem como o famoso “Olá, mundo!”. Mas, não criemos pânico! O Java não é um bicho de 7 cabeças e com este artigo vamos lhe mostrar isso!

O que é Java?
O Java, como plataforma de programação, nasceu no ano de 1995 dentro dos laboratórios da empresa Sun Microsystem como resultado de uma extensa pesquisa científica e tecnológica. A plataforma Java entrega um ambiente completo para o desenvolvimento e execução de programas, sendo composta por:

Uma linguagem de programação de alto nível orientada a objetos;
Máquina Virtual (Java Virtual Machine ou JVM), que garante independência de plataforma, pois o código executa na máquina virtual e essa pode ser portada para outras plataformas como Windows ou Linux;
Java Runtime Environment ou JRE, que agrega a máquina virtual e alguns recursos para a execução de aplicações Java; e
Java Development Kit ou JDK, que é um conjunto de utilitários que oferece suporte ao desenvolvimento de aplicações.
No Java, os programas são escritos em um arquivo com a extensão .java, que em um processo posterior serão compilados para arquivos com a extensão .class. Esses, por sua vez, contêm os códigos a serem executados na máquina virtual, os bytecodes.
"""

texto2 = """O Python foi lançado no início da década de 90 pelo programador e matemático holandês Guido Van Rossum. A linguagem foi projetada para dar ênfase no trabalho do desenvolvedor, facilitando a escrita de um código limpo, simples e legível, tanto em aplicações menores quanto em programas mais complexos.

A linguagem oferece recursos como tipagem dinâmica e forte (tipo de dado do valor deve ser do mesmo tipo da variável), orientação a objetos, multiparadigmas (programação funcional e imperativa), além de recursos poderosos em biblioteca padrão e via módulos e frameworks desenvolvidos pela comunidade. Seu código é aberto e a utilização é gratuita, rodando em praticamente qualquer sistema operacional.

Abaixo, um exemplo de um código em Python que recebe o nome de uma pessoa e o exibe na tela.

nome = input('Qual é o seu nome?')

print ('Olá, %s.' % nome)

Uma curiosidade: muitas pessoas associam a linguagem de programação com a cobra Píton (python, em inglês), mas na verdade o nome foi inspirado no Monty Python, um famoso grupo de comédia britânico da década de 70.

"""

def analisa_frequencia_de_texto(texto):
    # Mostra a quantidade de letras
    aparicoes = Counter(texto.lower())
    print(aparicoes)

    # Soma a quantidade de caracteres utilizando a função Sum()
    total_de_caracteres = sum(aparicoes.values())
    print(total_de_caracteres)

    # Divide a quantidade de caracteres pela quantidade de vezes em que a letra aparece, retornando a porcentagem de vezes
    # na qual a letra apareceu
    proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
    # Adiciona o resultado em um dicionario
    proporcoes = Counter(dict(proporcoes))
    # Retorna as 10 letras que mais apareceram
    mais_comuns = proporcoes.most_common(10)

# Mostra a quantidade em que as letras apareceram em porcentagem
    for caractere, proporcao in mais_comuns:
        print("{} => {:.2f}%".format(caractere, proporcao * 100))

analisa_frequencia_de_texto(texto1)

analisa_frequencia_de_texto(texto2)
