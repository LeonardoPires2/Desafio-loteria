import random

premios = {4: "quadra", 5: "quina", 3: "terno", 6: "sena"}

numero_usuario = random.sample(range(1, 60), 15)
print("Números Usuário:\n", numero_usuario)

numero_vencedores = random.sample(range(1, 60), 6)
print("Números Vencedores:\n", numero_vencedores)


def sorteio():
    lista3 = []
    for i in numero_usuario:
        for j in numero_vencedores:
            if j == i:
                lista3.append(j)
                lista3.sort()

    print("Acertados:\n", lista3)
    print("Você acertou o total de:", len(lista3), "\n")

    numero_usuario.sort()
    numero_vencedores.sort()
    
    print("Números Ordenados Bolão:\n", numero_usuario)
    print("Números Ordenados Sorteados:\n", numero_vencedores)
    print("Acertados:\n", lista3)
    print("Você acertou o total de:", len(lista3), "\n")
    
    if len(lista3) >= 3:
        print(premios[len(lista3)], "\nganhou :)")
    else:
        print("você não ganhou")


sorteio()
