from models.Cluster import Cluster


def ler_arquivo(filename = 'input.txt'):
    with open(filename, 'r') as arq:
        arquivo = [int(linha) for linha in arq]

    return arquivo


def cria_parametros(arquivo):
    return arquivo[0], arquivo[1], arquivo[2:]


def executa_rotina(ttask, umax, usuarios, output_filename='output.txt'):
    with open(output_filename, 'w') as output:
        cluster = Cluster(ttask=ttask, umax=umax)

        for qtd in usuarios:
            cluster.add_usuarios(qtd)
            output.write(f'{cluster.resumo}\n')
            cluster.tick()

        while cluster.servidores >= 1:
            cluster.tick()
            output.write(f'{cluster.resumo}\n')

        output.write(f'{cluster.consumo}\n')
        print("Script executado com sucesso, verifique os resultados no arquivo output.txt na pasta root.")

if __name__ == '__main__':
    arquivo = ler_arquivo()
    ttask, umax, usuarios = cria_parametros(arquivo)
    executa_rotina(ttask, umax, usuarios, 'output.txt')
