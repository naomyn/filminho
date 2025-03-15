class Filme: #criar uma classe "class" para o objeto "Filme".
    def __init__ (self, titulo, ano, direcao, genero, sinopse): #"__init__" é o construtor da classe, ele define os atributos para o objeto.
        self.titulo = titulo #atribuição de valor "nome" ao "self" que é a própria instância.
        self.ano = ano
        self.direcao = direcao
        self.genero = genero
        self.sinopse = sinopse

    def __str__(self): #o __str__ define como o objeto deve ser representado como uma string, quando usar print() ou str() no objeto.
        return f'{self.titulo} ({self.ano}) - {self.genero}\Directed by: {self.direcao}\nSinopse: {self.sinopse}' #return para retornar(rs') e f-string para inserir valores de variáveis diretamente dentro de uma string, usando {}.

    def busca_nome(self, nome):
        return nome.lower() in self.titulo.lower()
    
    def busca_ano(self, ano):
        return ano == self.ano
    
    def busca_genero(self, genero):
        return genero.lower() in self.genero.lower()
    
def buscar_filmes(filmes): #esse def precisa estar fora da classe, pq eu ainda n sei mas é isso.
    print("---- FILMINHOS DA NAOMI ----\n")
    print("Escolha um critério de busca:")
    print("1. Nome")
    print("2. Ano")
    print("3. Gênero")
    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        nome_busca = input("Digite o nome do filme: ")
        filmes_encontrados = [filme for filme in filmes if filme.busca_nome(nome_busca)]
    elif escolha == "2":
        ano_busca = input("Digite o ano de lançamento: ")
        filmes_encontrados = [filme for filme in filmes if filme.busca_ano(ano_busca)]
    elif escolha == "3":
        genero_busca = input("Digite o gênero do filme: ")
        filmes_encontrados = [filme for filme in filmes if filme.busca_genero(genero_busca)]
    else:
        print("Opção inválida.")
        return []
        
    return filmes_encontrados

filmes = [
    Filme("Dracula", "1931", "Tod Browning/Karl Freund", "Terror", "Bela Lugosi is lindo <3\n"),
    Filme("The Blair Witch Project", "1999", "Daniel Myrick/Eduardo Sánchez", "Terror", "Found Footage gostoso d+++\n"),
    Filme("Creep", "2014", "Patrick Brice", "Terror", "Uma máscara assustadora de lobo na casa de um estranho não pode ser normal.\n"),
    Filme("Call Me by Your Name", "2017", "Luca Guadagnino", "Drama", "Tira esse pêssego daqui!\n"),
    Filme("Audition", "1999", "Takashi Miike", "Terror", "Cuidado com pianistas.\n"),
    Filme("Twilight", "2008", "Catherine Hardwicke", "Romance", "Hoa hoa hoa hoa hoa\n"),
    Filme("New Moon", "2009", "Chris Weitz", "Fantasia", "Saturação 200%\n"),
    Filme("Interview with the Vampire", "1994", "Neil Jordan", "Drama", "Amor platônico </3\n"),
    Filme("Bram Stoker's Dracula", "1992", "Francis Ford Copolla", "Terror", "Auuuu\n"),
    Filme("Nosferatu", "1922", "F.W. Murnau", "Terror", "Sinfonia do terror\n"),
    Filme("Kairo", "2001", "Kiyoshi Kurosawa", "Terror", "Sai do meu pc!!\n"),
    Filme("Les Misérables", "2012", "Tom Hooper", "Musical", "Cortem as cabeças!\n"),
    Filme("It Follows", "2014", "David Robert Mitchell", "Terror", "seriouslly, it REALLY follows.\n"),
    Filme("The Visit", "2015", "M. Night Shyamalan", "Terror", "Esses velhos num sei não...\n"),
    Filme("The Elephant Man", "1980", "David Lynch", "Drama", "Ele só queria ser Romeu :(\n"),
    Filme("Queen of The Damned", "2002", "Michael Rymer", "Terror", "Vampiros rockeiros!\n")
]

while True:
    filmes_encontrados = buscar_filmes(filmes)

    if filmes_encontrados:
        print("\nFilmes encontrados:\n")
        for filme in filmes_encontrados:
            print(filme)
    else:
        print("Nenhum filme encontrado.")

    resposta = input("Você deseja fazer outra busca?\n(sim/não): ").lower()
    if resposta != "sim":
        print("Volte sempre, bb!")
        break

#pra mostrar os filmes e seus conteúdos, usar isso aqui:
# for filme in filmes:
#print(filme)
#print("-" * 40) #separador para visualização