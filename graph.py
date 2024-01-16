# requirements.txt
import matplotlib.pyplot as plt
import numpy as np

# Notas dos alunos e total de questões
notas = [40, 31, 37, 38, 52, 36, 32, 31, 50, 45, 41, 38, 47, 42, 39, 46, 39, 39, 41, 42, 42, 51, 43, 37, 38, 45, 39, 41, 35, 45, 41, 36, 42, 32, 47, 40, 31, 46, 41, 38, 37, 33, 38, 42, 32, 47, 40, 31, 46, 41, 38, 37, 33, 36, 32, 37, 54, 32, 53, 39, 37, 30, 38, 32, 33, 30, 47, 36, 45, 37, 38, 34, 34, 30, 38, 32, 33, 30, 47, 36, 45, 54, 41, 36, 32, 54, 32, 37, 30, 38, 32, 42, 47
]
total_questoes = 60

# Nomes dos alunos
nomes = ["Christian", "Paulo L", "Ellen", "Vitor Rodrigues", "Analynne", "Ju", "Davi Ferreira", "Lucas Pereira", "Marcos V", "Bianca C", "Mei", "Ana Paula Marinho", "Eloísa Negrão", "Wyran", "Mayze", "Gustavo Prestes", "Layze Cordeir", "Guimarães", "Éllen Gaia", "Marçal", "Liuan Silva", "Yuri", "Jefferson", "José", "Beckman", "Matheus", "Élber", "L.Mendes", "W.Rangel", "Leo", "Nay", "Ivanilda Rodrigues", "Heloisa", "Camila N", "Clarice", "Saymon", "Luciano", "Breno", "Yasmin", "Emily", "Ingrid", "Flavianny", "Edney", "Alice", "Weslley", "P.vinicius", "Vitor", "Adriele", "Robson", "William", "Davi Willian", "Jadson", "Luis", "Vinicius Flexa", "Viviane", "Arthur", "Luan", "Bernardo", "Alexandre", "Marcos T", "Dara", "Julio Barbosa", "Gustavo Ferreira", "Sofia Yumi", "Maicon", "Nicole Rocha", "Breno Vitor", "A. Cris", "Davi", "João. P", "Walace", "Edjoan", "Anderson", "Guilherme William", "Adeilson Silva", "Roberto Raphael", "Vinicius Silva", "Deivison Gustavo"
]

# Define a nota de corte
nota_corte = 35

# Cria uma lista de cores com base na nota de corte
cores = ['green' if nota >= nota_corte else 'red' for nota in notas]

# Ordena as notas e nomes correspondentes
notas_ordenadas, nomes_ordenados, cores_ordenadas = zip(*sorted(zip(notas, nomes, cores), reverse=True))

# Cria o gráfico de barras
largura_barra = 0.7  # Ajuste conforme desejado
plt.bar(range(len(nomes)), notas_ordenadas, color=cores_ordenadas, width=largura_barra)
plt.xticks(range(len(nomes)), nomes_ordenados, rotation=90)
plt.xlabel("Alunos")
plt.ylabel("Notas")
plt.title("Notas dos Alunos")

# Calcula a média das notas
media = np.mean(notas)
print(f"A nota de corte é: {media}")

# Exibe as notas originais acima das barras
for i in range(len(nomes)):
    plt.text(i, notas_ordenadas[i] + 1, str(notas_ordenadas[i]), ha='center')

# Calcula a média das notas
media = np.mean(notas)

# Mostra o Gráfico
plt.show()

# https://is.gd/JeielMiranda
