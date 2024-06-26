from pyamaze import maze, COLOR, agent


def compute_path_v1(my_maze, my_agent, caminho, visited):
    if (my_agent.position == my_maze._goal):
        return caminho

    paths = {}
    for i in my_maze.maze_map:

        if i == my_agent.position:
            paths = my_maze.maze_map[my_agent.position]
            break

    print(f"POSIÇÃO ATUAL: {my_agent.position}, POSSÍVEIS CAMINHOS: {paths}, PERCORRIDO: {caminho}")
    visited.append(my_agent.position)

    #VERIFICA SE É POSSÍVEL IR PARA N E SE A POSSÍVEL POSIÇÃO AINDA NÃO FOI VISITADA
    if (paths['N'] == 1 and ((my_agent.position[0] - 1, my_agent.position[1]) not in visited)):
        nova_posicao = (my_agent.position[0] - 1, my_agent.position[1])

        my_agent.position = nova_posicao

        compute_path_v1(my_maze, my_agent, caminho + 'N', visited)

    #VERIFICA SE É POSSÍVEL IR PARA W E SE A POSSÍVEL POSIÇÃO AINDA NÃO FOI VISITADA    
    if (paths['W'] == 1 and ((my_agent.position[0], my_agent.position[1] - 1) not in visited)):
        nova_posicao = (my_agent.position[0], my_agent.position[1] - 1)

        my_agent.position = nova_posicao

        compute_path_v1(my_maze, my_agent, caminho + 'W', visited)

    #VERIFICA SE É POSSÍVEL IR PARA E E SE A POSSÍVEL POSIÇÃO AINDA NÃO FOI VISITADA
    if (paths['E'] == 1 and ((my_agent.position[0], my_agent.position[1] + 1) not in visited)):
        nova_posicao = (my_agent.position[0], my_agent.position[1] + 1)

        my_agent.position = nova_posicao

        compute_path_v1(my_maze, my_agent, caminho + 'E', visited)

    #VERIFICA SE É POSSÍVEL IR PARA S E SE A POSSÍVEL POSIÇÃO AINDA NÃO FOI VISITADA
    if (paths['S'] == 1 and ((my_agent.position[0] + 1, my_agent.position[1]) not in visited)):
        nova_posicao = (my_agent.position[0] + 1, my_agent.position[1])

        my_agent.position = nova_posicao

        compute_path_v1(my_maze, my_agent, caminho + 'S', visited)

    return None


def compute_path_v2(my_maze, my_agent, caminho, visited):
    if (my_agent.position == my_maze._goal):
        return caminho

    paths = {}
    for i in my_maze.maze_map:

        if i == my_agent.position:
            paths = my_maze.maze_map[my_agent.position]
            break

    print(f"POSIÇÃO ATUAL: {my_agent.position}, POSSÍVEIS CAMINHOS: {paths}, PERCORRIDO: {caminho}")
    visited.append(my_agent.position)

    # VERIFICA SE É POSSÍVEL IR PARA N E SE A POSSÍVEL POSIÇÃO AINDA NÃO FOI VISITADA
    if (paths['N'] == 1 and ((my_agent.position[0] - 1, my_agent.position[1]) not in visited)):
        nova_posicao = (my_agent.position[0] - 1, my_agent.position[1])

        my_agent.position = nova_posicao

        caminho = compute_path_v2(my_maze, my_agent, caminho + 'N', visited)

    # VERIFICA SE É POSSÍVEL IR PARA W E SE A POSSÍVEL POSIÇÃO AINDA NÃO FOI VISITADA
    if (paths['W'] == 1 and ((my_agent.position[0], my_agent.position[1] - 1) not in visited)):
        nova_posicao = (my_agent.position[0], my_agent.position[1] - 1)

        my_agent.position = nova_posicao

        caminho = compute_path_v2(my_maze, my_agent, caminho + 'W', visited)

    # VERIFICA SE É POSSÍVEL IR PARA E E SE A POSSÍVEL POSIÇÃO AINDA NÃO FOI VISITADA
    if (paths['E'] == 1 and ((my_agent.position[0], my_agent.position[1] + 1) not in visited)):
        nova_posicao = (my_agent.position[0], my_agent.position[1] + 1)

        my_agent.position = nova_posicao

        caminho = compute_path_v2(my_maze, my_agent, caminho + 'E', visited)

    # VERIFICA SE É POSSÍVEL IR PARA S E SE A POSSÍVEL POSIÇÃO AINDA NÃO FOI VISITADA
    if (paths['S'] == 1 and ((my_agent.position[0] + 1, my_agent.position[1]) not in visited)):
        nova_posicao = (my_agent.position[0] + 1, my_agent.position[1])

        my_agent.position = nova_posicao

        caminho = compute_path_v2(my_maze, my_agent, caminho + 'S', visited)

    return caminho


#VERSÃO CORRETA DA FUNÇÃO QUE ENCONTRA O CAMINHO
def compute_path_v3(my_maze, my_agent):
    if my_maze is None or my_agent is None:
        print("Erro: Maze ou Agent é nulo.")
        return None

    visited = []

    def compute_path(caminho, visited):
        if my_agent.position == my_maze._goal:
            return caminho

        paths = {}
        for i in my_maze.maze_map:
            if i == my_agent.position:
                paths = my_maze.maze_map[my_agent.position]
                break

        print(f"POSIÇÃO ATUAL: {my_agent.position}, POSSÍVEIS CAMINHOS: {paths}, PERCORRIDO: {caminho}")
        visited.append(my_agent.position)

        # VERIFICA SE É POSSÍVEL IR PARA N E SE A POSSÍVEL POSIÇÃO AINDA NÃO FOI VISITADA
        if paths['N'] == 1 and ((my_agent.position[0] - 1, my_agent.position[1]) not in visited):
            nova_posicao = (my_agent.position[0] - 1, my_agent.position[1])
            my_agent.position = nova_posicao

            resultado = compute_path(caminho + 'N', visited)

            if resultado is not None:
                return resultado

            my_agent.position = (my_agent.position[0] + 1, my_agent.position[1])
            caminho = caminho[:-1]

        # VERIFICA SE É POSSÍVEL IR PARA W E SE A POSSÍVEL POSIÇÃO AINDA NÃO FOI VISITADA
        if paths['W'] == 1 and ((my_agent.position[0], my_agent.position[1] - 1) not in visited):
            nova_posicao = (my_agent.position[0], my_agent.position[1] - 1)
            my_agent.position = nova_posicao

            resultado = compute_path(caminho + 'W', visited)

            if resultado is not None:
                return resultado

            my_agent.position = (my_agent.position[0], my_agent.position[1] + 1)
            caminho = caminho[:-1]

        # VERIFICA SE É POSSÍVEL IR PARA E E SE A POSSÍVEL POSIÇÃO AINDA NÃO FOI VISITADA
        if paths['E'] == 1 and ((my_agent.position[0], my_agent.position[1] + 1) not in visited):
            nova_posicao = (my_agent.position[0], my_agent.position[1] + 1)
            my_agent.position = nova_posicao

            resultado = compute_path(caminho + 'E', visited)

            if resultado is not None:
                return resultado

            my_agent.position = (my_agent.position[0], my_agent.position[1] - 1)
            caminho = caminho[:-1]

        # VERIFICA SE É POSSÍVEL IR PARA S E SE A POSSÍVEL POSIÇÃO AINDA NÃO FOI VISITADA
        if paths['S'] == 1 and ((my_agent.position[0] + 1, my_agent.position[1]) not in visited):
            nova_posicao = (my_agent.position[0] + 1, my_agent.position[1])
            my_agent.position = nova_posicao

            resultado = compute_path(caminho + 'S', visited)

            if resultado is not None:
                return resultado

            my_agent.position = (my_agent.position[0] - 1, my_agent.position[1])
            caminho = caminho[:-1]

        return None

    return compute_path("", visited)


if __name__ == "__main__":
    # cria environment
    my_maze = maze(20, 20)

    # lê labirinto do exercício
    my_maze.CreateMaze(3,4,theme=COLOR.light)


    # cria agente
    my_agent = agent(my_maze, 16, 17, shape="arrow", filled=True, footprints=True)

    #print(my_maze._goal)
    #print(my_maze.maze_map)
    #my_maze.run()



    # calcula passos que o agente seguirá para sair do labirinto
    my_path = compute_path_v3(my_maze, my_agent)

    # executa os passos calculados
    my_maze.tracePath({my_agent: my_path}, delay=200, kill=False)

    # roda a animação mostrando o movimento do agente
    my_maze.run()
