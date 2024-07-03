from collections import deque  # Importa deque da biblioteca collections para usar filas.

class No:  # Define a classe No, que representa um nó da árvore AVL.
    def __init__(self, data):  # Método construtor, inicializa o nó com o valor data.
        self.data = data  # Armazena o valor do nó.
        self.esquerda = None  # Inicializa o filho esquerdo como None.
        self.direita = None  # Inicializa o filho direito como None.

    def setaFilhos(self, esquerda, direita):  # Define os filhos esquerdo e direito do nó.
        self.esquerda = esquerda  # Atribui o filho esquerdo.
        self.direita = direita  # Atribui o filho direito.

    def balanco(self):  # Calcula o fator de balanceamento do nó.
        prof_esq = 0  # Inicializa a profundidade do filho esquerdo como 0.
        if self.esquerda:  # Se existir filho esquerdo.
            prof_esq = self.esquerda.profundidade()  # Calcula a profundidade do filho esquerdo.
        prof_dir = 0  # Inicializa a profundidade do filho direito como 0.
        if self.direita:  # Se existir filho direito.
            prof_dir = self.direita.profundidade()  # Calcula a profundidade do filho direito.
        return prof_esq - prof_dir  # Retorna a diferença entre as profundidades.

    def profundidade(self):  # Calcula a profundidade do nó.
        prof_esq = 0  # Inicializa a profundidade do filho esquerdo como 0.
        if self.esquerda:  # Se existir filho esquerdo.
            prof_esq = self.esquerda.profundidade()  # Calcula a profundidade do filho esquerdo.
        prof_dir = 0  # Inicializa a profundidade do filho direito como 0.
        if self.direita:  # Se existir filho direito.
            prof_dir = self.direita.profundidade()  # Calcula a profundidade do filho direito.
        return 1 + max(prof_esq, prof_dir)  # Retorna a profundidade do nó.

    def rotacaoEsquerda(self):  # Realiza a rotação à esquerda.
        nova_raiz = self.direita  # A nova raiz será o filho direito.
        self.direita = nova_raiz.esquerda  # O filho esquerdo da nova raiz será o filho direito do nó atual.
        nova_raiz.esquerda = self  # O nó atual se torna o filho esquerdo da nova raiz.
        return nova_raiz  # Retorna a nova raiz.

    def rotacaoDireita(self):  # Realiza a rotação à direita.
        nova_raiz = self.esquerda  # A nova raiz será o filho esquerdo.
        self.esquerda = nova_raiz.direita  # O filho direito da nova raiz será o filho esquerdo do nó atual.
        nova_raiz.direita = self  # O nó atual se torna o filho direito da nova raiz.
        return nova_raiz  # Retorna a nova raiz.

    def rotacaoEsquerdaDireita(self):  # Realiza a rotação esquerda-direita.
        self.esquerda = self.esquerda.rotacaoEsquerda()  # Primeiro, faz uma rotação à esquerda no filho esquerdo.
        return self.rotacaoDireita()  # Em seguida, faz uma rotação à direita no nó atual.

    def rotacaoDireitaEsquerda(self):  # Realiza a rotação direita-esquerda.
        self.direita = self.direita.rotacaoDireita()  # Primeiro, faz uma rotação à direita no filho direito.
        return self.rotacaoEsquerda()  # Em seguida, faz uma rotação à esquerda no nó atual.

    def executaBalanco(self):  # Executa o balanceamento do nó.
        bal = self.balanco()  # Calcula o fator de balanceamento.
        if bal > 1:  # Se o nó estiver desbalanceado para a esquerda.
            if self.esquerda.balanco() >= 0:  # Se o filho esquerdo estiver balanceado ou desbalanceado para a esquerda.
                return self.rotacaoDireita()  # Realiza a rotação à direita.
            else:
                return self.rotacaoEsquerdaDireita()  # Caso contrário, realiza a rotação esquerda-direita.
        elif bal < -1:  # Se o nó estiver desbalanceado para a direita.
            if self.direita.balanco() <= 0:  # Se o filho direito estiver balanceado ou desbalanceado para a direita.
                return self.rotacaoEsquerda()  # Realiza a rotação à esquerda.
            else:
                return self.rotacaoDireitaEsquerda()  # Caso contrário, realiza a rotação direita-esquerda.
        return self  # Retorna o nó (balanceado ou já estava balanceado).

    def insere(self, data):  # Insere um novo valor na árvore AVL.
        if data < self.data:  # Se o valor for menor que o valor do nó atual.
            if not self.esquerda:  # Se não houver filho esquerdo.
                self.esquerda = No(data)  # Cria um novo nó à esquerda.
            else:
                self.esquerda = self.esquerda.insere(data)  # Insere o valor no filho esquerdo.
        else:  # Se o valor for maior ou igual ao valor do nó atual.
            if not self.direita:  # Se não houver filho direito.
                self.direita = No(data)  # Cria um novo nó à direita.
            else:
                self.direita = self.direita.insere(data)  # Insere o valor no filho direito.
        return self.executaBalanco()  # Executa o balanceamento e retorna o nó atualizado.

    def imprimeArvore(self, indent=0, posicao="Raiz"):  # Imprime a árvore com indentação.
        print(" " * indent + f"{posicao}: {self.data}")  # Imprime o nó com indentação e posição.
        if self.esquerda:  # Se houver filho esquerdo.
            self.esquerda.imprimeArvore(indent + 2, "Esquerda")  # Imprime o filho esquerdo com indentação adicional.
        if self.direita:  # Se houver filho direito.
            self.direita.imprimeArvore(indent + 2, "Direita")  # Imprime o filho direito com indentação adicional.

    # Impressão a cada Nível
    def imprimeNivel(self):  # Imprime a árvore nível por nível.
        fila = deque([(self, 0)])  # Inicializa uma fila com o nó atual e nível 0.
        nivel_atual = 0  # Define o nível atual como 0.
        while fila:  # Enquanto houver nós na fila.
            no, nivel = fila.popleft()  # Remove o nó da fila.
            if nivel > nivel_atual:  # Se o nível atual for maior que o nível processado.
                print()  # Imprime uma nova linha.
                nivel_atual = nivel  # Atualiza o nível atual.
            print(no.data, end=" ")  # Imprime o valor do nó.
            if no.esquerda:  # Se houver filho esquerdo.
                fila.append((no.esquerda, nivel + 1))  # Adiciona o filho esquerdo à fila.
            if no.direita:  # Se houver filho direito.
                fila.append((no.direita, nivel + 1))  # Adiciona o filho direito à fila.
        print()  # Imprime uma nova linha ao final.

    # Impressão Pré-Ordem
    def imprimePreOrdem(self):  # Imprime a árvore em pré-ordem.
        print(self.data, end=" ")  # Imprime o valor do nó.
        if self.esquerda:  # Se houver filho esquerdo.
            self.esquerda.imprimePreOrdem()  # Chama a impressão em pré-ordem no filho esquerdo.
        if self.direita:  # Se houver filho direito.
            self.direita.imprimePreOrdem()  # Chama a impressão em pré-ordem no filho direito.

    # Impressão In-Ordem
    def imprimeInOrdem(self):  # Imprime a árvore em in-ordem.
        if self.esquerda:  # Se houver filho esquerdo.
            self.esquerda.imprimeInOrdem()  # Chama a impressão em in-ordem no filho esquerdo.
        print(self.data, end=" ")  # Imprime o valor do nó.
        if self.direita:  # Se houver filho direito.
            self.direita.imprimeInOrdem()  # Chama a impressão em in-ordem no filho direito.

    # Impressão Pós-Ordem
    def imprimePosOrdem(self):  # Imprime a árvore em pós-ordem.
        if self.esquerda:  # Se houver filho esquerdo.
            self.esquerda.imprimePosOrdem()  # Chama a impressão em pós-ordem no filho esquerdo.
        if self.direita:  # Se houver filho direito.
            self.direita.imprimePosOrdem()  # Chama a impressão em pós-ordem no filho direito.
        print(self.data, end=" ")  # Imprime o valor do nó.

# Função que recebe o arquivo .txt e chama a função de inserção
def read_file_and_insert(filename):  # Define a função que lê um arquivo e insere os valores na árvore AVL.
    raiz = None  # Inicializa a raiz como None.

    with open(filename, 'r') as file:  # Abre o arquivo para leitura.
        for line in file:  # Para cada linha no arquivo.
            words = line.split()  # Divide a linha em palavras.
            for word in words:  # Para cada palavra na linha.
                print("Inserindo:", word)  # Imprime a palavra que está sendo inserida.
                if raiz is None:  # Se a raiz for None.
                    raiz = No(word)  # Cria o nó raiz com a palavra.
                else:
                    raiz = raiz.insere(word)  # Insere a palavra na árvore AVL.
                raiz.imprimeArvore()  # Imprime a árvore após a inserção.
                print("\n---")
                print("Caminhamento por nível:")  # Imprime a árvore por nível.
                raiz.imprimeNivel()
                print("\n---")
                print("Pré-ordem:")  # Imprime a árvore em pré-ordem.
                raiz.imprimePreOrdem()
                print("\n---")
                print("In-ordem:")  # Imprime a árvore em in-ordem.
                raiz.imprimeInOrdem()
                print("\n---")
                print("Pós-ordem:")  # Imprime a árvore em pós-ordem.
                raiz.imprimePosOrdem()
                print("\n---")

# Testando a função de leitura e inserção
read_file_and_insert("entrada.txt")  # Chama a função com o arquivo "entrada.txt".
