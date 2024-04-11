#5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

palavras = {}

inicio_contagem = 1

lista = [
    "Abacaxi", "Livro", "Cachorro", "Amarelo", "Computador", "Mesa", "Gato", "Felicidade", "Avião", "Janela",
    "Maçã", "Rádio", "Céu", "Bola", "Coração", "Praia", "Banana", "Flor", "Guitarra", "Chocolate",
    "Televisão", "Camisa", "Sol", "Lua", "Papel", "Caneta", "Árvore", "Coelho", "Relógio", "Sofá",
    "Pássaro", "Chuva", "Carro", "Dinheiro", "Lápis", "Laranja", "Música", "Copo", "Bebê", "Pão",
    "Montanha", "Escova", "Balão", "Rato", "Fruta", "Sorriso", "Café", "Neve", "Dança", "Espelho",
    "Escola", "Tigre", "Cama", "Azul", "Vermelho", "Verde", "Branco", "Preto", "Cinza",
    "Marrom", "Roxo", "Rosa", "Laranja", "Tanque", "Vela", "Dado", "Quadro", "Tela", "Teclado", "Mouse",
    "Fone de ouvido", "Carregador", "Bateria", "Cadeira", "Prato", "Talher", "Guardanapo", "Garfo", "Faca",
    "Colher", "Panela", "Fogão", "Geladeira", "Microondas", "Torradeira", "Liquidificador", "Batedeira",
    "Máquina de lavar", "Secadora", "Aspirador de pó", "Vassoura", "Rodo", "Esfregão", "Rádio", "Céu", "Bola", 
    "Coração", "Praia", "Banana", "Flor", "Guitarra", "Chocolate", "Televisão", "Camisa", "Sol", "Lua", "Papel",
    "Televisão", "Camisa", "Sol", "Lua", "Papel", "Caneta", "Árvore", "Coelho", "Relógio", "Sofá",
    "Pássaro", "Chuva", "Carro", "Dinheiro", "Lápis", "Laranja", "Música", "Copo", "Bebê", "Pão",
    "Montanha", "Escova", "Balão", "Rato", "Fruta", "Sorriso", "Café", "Neve", "Dança", "Espelho",
    "Escola", "Tigre", "Cama", "Azul", "Vermelho", "Verde"
]

for palavra in lista:
    
    if palavra not in palavras:
        palavras[palavra] = inicio_contagem
        continue

    palavras[palavra] +=1
    
print(palavras)
    
