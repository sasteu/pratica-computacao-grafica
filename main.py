import os
import pygame

CAMINHO_OBJ = "models/duas_faces.obj"


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


# Lê as faces do arquivo .obj
def ler_faces_obj(caminho_arquivo):
    faces = []

    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()

            if not linha:
                continue

            if linha.startswith("f "):
                partes = linha.split()[1:]
                face = [int(p) for p in partes]
                faces.append(face)

    return faces


# Lê as arestas da face
def arestas_da_face(face):
    arestas = []

    for i in range(len(face)):
        v1 = face[i]
        v2 = face[(i + 1) % len(face)]

        arestas.append((v1, v2))

    return arestas


# Lê as arestas normalizadas da face
def arestas_normalizadas_da_face(face):
    arestas = []

    for i in range(len(face)):
        v1 = face[i]
        v2 = face[(i + 1) % len(face)]
        arestas.append(tuple(sorted((v1, v2))))

    return arestas


# Encontra as faces adjacentes
def encontrar_faces_adjacentes(faces, indice_face_escolhida):
    face_escolhida = faces[indice_face_escolhida]
    arestas_escolhida = arestas_normalizadas_da_face(face_escolhida)

    adjacentes = []

    for i, face in enumerate(faces):
        if i == indice_face_escolhida:
            continue

        arestas_outra = arestas_normalizadas_da_face(face)

        for aresta in arestas_escolhida:
            if aresta in arestas_outra:
                adjacentes.append(i + 1)  # +1 para mostrar Face 1, Face 2...
                break

    return adjacentes


# Lista as faces adjacentes
def listar_faces_adjacentes():
    faces = ler_faces_obj(CAMINHO_OBJ)

    print("=== LISTAR FACES ADJACENTES ===")
    print(f"O objeto possui {len(faces)} face(s).")

    for i, face in enumerate(faces, start=1):
        print(f"Face {i}: {face}")

    escolha = int(input("\nDigite o número da face que deseja consultar: "))

    if escolha < 1 or escolha > len(faces):
        print("Face inválida.")
        input("\nPressione ENTER para voltar...")
        limpar_tela()
        return

    adjacentes = encontrar_faces_adjacentes(faces, escolha - 1)

    if adjacentes:
        print(f"\nAs faces adjacentes à face {escolha} são: {adjacentes}")
    else:
        print(f"\nA face {escolha} não possui faces adjacentes.")

    input("\nPressione ENTER para voltar...")
    limpar_tela()


# Lista as arestas da face
def listar_arestas_da_face():
    faces = ler_faces_obj(CAMINHO_OBJ)

    print("=== LISTAR ARESTAS DA FACE ===")
    print(f"O objeto possui {len(faces)} face(s).\n")

    for i, face in enumerate(faces, start=1):
        print(f"Face {i}: {face}")

    try:
        escolha = int(input("\nDigite o número da face desejada: "))

        if escolha < 1 or escolha > len(faces):
            print("Face inválida.")
            input("\nPressione ENTER para voltar...")
            limpar_tela()
            return

        face_escolhida = faces[escolha - 1]

        arestas = arestas_da_face(face_escolhida)

        print(f"\nArestas da Face {escolha}:\n")

        for i, aresta in enumerate(arestas, start=1):
            print(f"Aresta {i}: {aresta[0]} -> {aresta[1]}")

    except:
        print("Entrada inválida.")

    input("\nPressione ENTER para voltar...")
    limpar_tela()


# Lista os vértices da face
def listar_vertices_da_face():
    faces = ler_faces_obj(CAMINHO_OBJ)

    print("=== LISTAR VÉRTICES DA FACE ===")
    print(f"O objeto possui {len(faces)} face(s).\n")

    for i, face in enumerate(faces, start=1):
        print(f"Face {i}: {face}")

    try:
        escolha = int(input("\nDigite o número da face desejada: "))
        limpar_tela()

        if escolha < 1 or escolha > len(faces):
            print("Face inválida.")
            input("\nPressione ENTER para voltar...")
            limpar_tela()
            return

        face_escolhida = faces[escolha - 1]

        print(f"\nVértices da Face {escolha}:\n")

        for i, vertice in enumerate(face_escolhida, start=1):
            print(f"Vértice {i}: {vertice}")

    except:
        print("Entrada inválida.")

    input("\nPressione ENTER para voltar...")
    limpar_tela()


# Normaliza uma aresta
def normalizar_aresta(v1, v2):
    return tuple(sorted((v1, v2)))


# Lista todas as arestas
def listar_todas_arestas(faces):
    arestas_unicas = []

    for face in faces:
        for i in range(len(face)):
            v1 = face[i]
            v2 = face[(i + 1) % len(face)]
            aresta = normalizar_aresta(v1, v2)

            if aresta not in arestas_unicas:
                arestas_unicas.append(aresta)

    return arestas_unicas


# Lista todas as arestas visuais
def listar_todas_arestas_visuais(faces):
    arestas = []

    for face in faces:
        for aresta in arestas_da_face(face):
            # evita repetir invertida
            if aresta not in arestas and (aresta[1], aresta[0]) not in arestas:
                arestas.append(aresta)

    return arestas


# Encontra as faces da aresta
def encontrar_faces_da_aresta(faces, aresta_escolhida):
    faces_adjacentes = []

    for i, face in enumerate(faces, start=1):
        for j in range(len(face)):
            v1 = face[j]
            v2 = face[(j + 1) % len(face)]
            aresta_atual = normalizar_aresta(v1, v2)

            if aresta_atual == aresta_escolhida:
                faces_adjacentes.append(i)
                break

    return faces_adjacentes


# Lista as faces adjacentes da aresta
def listar_faces_adjacentes_da_aresta():
    faces = ler_faces_obj(CAMINHO_OBJ)

    print("=== LISTAR FACES ADJACENTES DA ARESTA ===\n")

    arestas = listar_todas_arestas_visuais(faces)

    print("Arestas disponíveis:\n")
    for i, aresta in enumerate(arestas, start=1):
        print(f"Aresta {i}: {aresta[0]} -> {aresta[1]}")

    try:
        escolha = int(input("\nDigite o número da aresta desejada: "))

        if escolha < 1 or escolha > len(arestas):
            print("Aresta inválida.")
            input("\nPressione ENTER para voltar...")
            limpar_tela()
            return

        aresta_escolhida = arestas[escolha - 1]

        limpar_tela()

        faces_adjacentes = encontrar_faces_da_aresta(faces, aresta_escolhida)

        print("=== RESULTADO ===\n")
        print(f"Aresta escolhida: {aresta_escolhida[0]} -> {aresta_escolhida[1]}")
        print(f"Faces adjacentes: {faces_adjacentes}")

    except:
        print("Entrada inválida.")

    input("\nPressione ENTER para voltar...")
    limpar_tela()


# Lista os vértices inicial e final da aresta
def listar_vertices_inicial_final_da_aresta():
    faces = ler_faces_obj(CAMINHO_OBJ)

    arestas = listar_todas_arestas_visuais(faces)

    print("=== LISTAR VÉRTICE INICIAL E FINAL DA ARESTA ===\n")
    print("Arestas disponíveis:\n")

    for i, aresta in enumerate(arestas, start=1):
        print(f"Aresta {i}")

    try:
        escolha = int(input("\nDigite o número da aresta desejada: "))

        if escolha < 1 or escolha > len(arestas):
            print("Aresta inválida.")
            input("\nPressione ENTER para voltar...")
            limpar_tela()
            return

        limpar_tela()

        aresta_escolhida = arestas[escolha - 1]

        print("=== RESULTADO ===\n")
        print(f"Aresta escolhida: {aresta_escolhida[0]} -> {aresta_escolhida[1]}")
        print(f"Vértice inicial: {aresta_escolhida[0]}")
        print(f"Vértice final: {aresta_escolhida[1]}")

    except:
        print("Entrada inválida.")

    input("\nPressione ENTER para voltar...")
    limpar_tela()


# Encontra as arestas adjacentes
def encontrar_arestas_adjacentes(aresta_escolhida, arestas):
    adjacentes = []

    v1 = aresta_escolhida[0]
    v2 = aresta_escolhida[1]

    for aresta in arestas:
        if aresta == aresta_escolhida:
            continue

        a = aresta[0]
        b = aresta[1]

        if a == v1 or b == v1 or a == v2 or b == v2:
            adjacentes.append(aresta)

    return adjacentes


# Lista as arestas adjacentes
def listar_arestas_adjacentes_da_aresta():
    faces = ler_faces_obj(CAMINHO_OBJ)

    arestas = listar_todas_arestas_visuais(faces)

    print("=== LISTAR ARESTAS ADJACENTES DA ARESTA ===\n")
    print("Arestas disponíveis:\n")

    for i, aresta in enumerate(arestas, start=1):
        print(f"Aresta {i}: {aresta[0]} -> {aresta[1]}")

    try:
        escolha = int(input("\nDigite o número da aresta desejada: "))

        if escolha < 1 or escolha > len(arestas):
            print("Aresta inválida.")
            input("\nPressione ENTER para voltar...")
            limpar_tela()
            return

        aresta_escolhida = arestas[escolha - 1]

        limpar_tela()

        adjacentes = encontrar_arestas_adjacentes(aresta_escolhida, arestas)

        print("=== RESULTADO ===\n")
        print(f"Aresta escolhida: {aresta_escolhida[0]} -> {aresta_escolhida[1]}\n")

        if adjacentes:
            print("Arestas adjacentes:\n")
            for i, aresta in enumerate(adjacentes, start=1):
                print(f"Aresta {i}: {aresta[0]} -> {aresta[1]}")
        else:
            print("Essa aresta não possui arestas adjacentes.")

    except:
        print("Entrada inválida.")

    input("\nPressione ENTER para voltar...")
    limpar_tela()


# Lista todos os vértices
def listar_todos_vertices(faces):
    vertices = []

    for face in faces:
        for vertice in face:
            if vertice not in vertices:
                vertices.append(vertice)

    vertices.sort()
    return vertices


# Encontra as faces do vértice
def encontrar_faces_do_vertice(faces, vertice_escolhido):
    faces_compartilhadas = []

    for i, face in enumerate(faces, start=1):
        if vertice_escolhido in face:
            faces_compartilhadas.append(i)

    return faces_compartilhadas


# Lista as faces compartilhadas
def listar_faces_compartilhadas_do_vertice():
    faces = ler_faces_obj(CAMINHO_OBJ)

    vertices = listar_todos_vertices(faces)

    print("=== LISTAR FACES COMPARTILHADAS DO VÉRTICE ===\n")
    print("Vértices disponíveis:\n")

    for i, vertice in enumerate(vertices, start=1):
        print(f"Vértice {i}: {vertice}")

    try:
        escolha = int(input("\nDigite o número do vértice desejado: "))

        if escolha < 1 or escolha > len(vertices):
            print("Vértice inválido.")
            input("\nPressione ENTER para voltar...")
            limpar_tela()
            return

        vertice_escolhido = vertices[escolha - 1]

        limpar_tela()

        faces_compartilhadas = encontrar_faces_do_vertice(faces, vertice_escolhido)

        print("=== RESULTADO ===\n")
        print(f"Vértice escolhido: {vertice_escolhido}")

        if faces_compartilhadas:
            print(f"Faces compartilhadas: {faces_compartilhadas}")
        else:
            print("Nenhuma face compartilha esse vértice.")

    except:
        print("Entrada inválida.")

    input("\nPressione ENTER para voltar...")
    limpar_tela()


# Encontra as arestas do vértice
def encontrar_arestas_do_vertice(vertice_escolhido, arestas):
    arestas_compartilhadas = []

    for aresta in arestas:
        if aresta[0] == vertice_escolhido or aresta[1] == vertice_escolhido:
            arestas_compartilhadas.append(aresta)

    return arestas_compartilhadas


# Lista as arestas compartilhadas
def listar_arestas_compartilhadas_do_vertice():
    faces = ler_faces_obj(CAMINHO_OBJ)

    vertices = listar_todos_vertices(faces)
    arestas = listar_todas_arestas_visuais(faces)

    print("=== LISTAR ARESTAS COMPARTILHADAS DO VÉRTICE ===\n")
    print("Vértices disponíveis:\n")

    for i, vertice in enumerate(vertices, start=1):
        print(f"Vértice {i}: {vertice}")

    try:
        escolha = int(input("\nDigite o número do vértice desejado: "))

        if escolha < 1 or escolha > len(vertices):
            print("Vértice inválido.")
            input("\nPressione ENTER para voltar...")
            limpar_tela()
            return

        vertice_escolhido = vertices[escolha - 1]

        limpar_tela()

        arestas_compartilhadas = encontrar_arestas_do_vertice(
            vertice_escolhido, arestas
        )

        print("=== RESULTADO ===\n")
        print(f"Vértice escolhido: {vertice_escolhido}\n")

        if arestas_compartilhadas:
            print("Arestas compartilhadas:\n")
            for i, aresta in enumerate(arestas_compartilhadas, start=1):
                print(f"Aresta {i}: {aresta[0]} -> {aresta[1]}")
        else:
            print("Nenhuma aresta compartilha esse vértice.")

    except:
        print("Entrada inválida.")

    input("\nPressione ENTER para voltar...")
    limpar_tela()


# ===================================================================================================
def ler_obj(caminho_arquivo):
    vertices = []
    faces = []

    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()

            if not linha:
                continue

            if linha.startswith("v "):
                partes = linha.split()
                x = float(partes[1])
                y = float(partes[2])
                z = float(partes[3]) if len(partes) > 3 else 0.0
                vertices.append((x, y, z))

            elif linha.startswith("f "):
                partes = linha.split()[1:]
                face = [int(p) for p in partes]
                faces.append(face)

    return vertices, faces


def transformar_para_tela(x, y, largura, altura, escala=200):
    x_tela = int(largura // 2 + x * escala)
    y_tela = int(altura // 2 - y * escala)
    return x_tela, y_tela


def desenhar_ponto(tela, x, y, cor):
    tela.set_at((x, y), cor)


def desenhar_aresta(tela, x1, y1, x2, y2, cor):
    dx = x2 - x1
    dy = y2 - y1

    passos = max(abs(dx), abs(dy))

    if passos == 0:
        desenhar_ponto(tela, x1, y1, cor)
        return

    x_inc = dx / passos
    y_inc = dy / passos

    x = x1
    y = y1

    for _ in range(passos + 1):
        desenhar_ponto(tela, round(x), round(y), cor)
        x += x_inc
        y += y_inc


def renderizar_objeto():
    vertices, faces = ler_obj(CAMINHO_OBJ)

    pygame.init()

    largura = 800
    altura = 600
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Renderização do OBJ")

    branco = (255, 255, 255)
    preto = (0, 0, 0)

    rodando = True

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        tela.fill(branco)

        arestas_desenhadas = set()

        for face in faces:
            for i in range(len(face)):
                v1_idx = face[i] - 1
                v2_idx = face[(i + 1) % len(face)] - 1

                aresta_normalizada = tuple(sorted((v1_idx, v2_idx)))
                if aresta_normalizada in arestas_desenhadas:
                    continue

                arestas_desenhadas.add(aresta_normalizada)

                x1, y1, _ = vertices[v1_idx]
                x2, y2, _ = vertices[v2_idx]

                x1_tela, y1_tela = transformar_para_tela(x1, y1, largura, altura)
                x2_tela, y2_tela = transformar_para_tela(x2, y2, largura, altura)

                desenhar_aresta(tela, x1_tela, y1_tela, x2_tela, y2_tela, preto)

        pygame.display.flip()

    pygame.quit()


def main():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1 - Dada uma face, listar faces adjacentes")
        print("2 - Dada uma face, listar arestas da face")
        print("3 - Dada uma face, listar vértices da face")
        print("4 - Dada uma aresta, listar faces adjacentes")
        print("5 - Dada uma aresta, listar vértice inicial e final")
        print("6 - Dada uma aresta, listar arestas adjacentes")
        print("7 - Dado um vértice, listar faces compartilhadas")
        print("8 - Dado um vértice, listar arestas compartilhadas")
        print("9 - Renderizar objeto")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                limpar_tela()
                listar_faces_adjacentes()

            case "2":
                limpar_tela()
                listar_arestas_da_face()

            case "3":
                limpar_tela()
                listar_vertices_da_face()

            case "4":
                limpar_tela()
                listar_faces_adjacentes_da_aresta()

            case "5":
                limpar_tela()
                listar_vertices_inicial_final_da_aresta()

            case "6":
                limpar_tela()
                listar_arestas_adjacentes_da_aresta()

            case "7":
                limpar_tela()
                listar_faces_compartilhadas_do_vertice()

            case "8":
                limpar_tela()
                listar_arestas_compartilhadas_do_vertice()

            case "9":
                limpar_tela()
                renderizar_objeto()

            case "0":
                print("Encerrando programa...")
                break

            case _:
                print("Opção inválida!")


if __name__ == "__main__":
    main()
