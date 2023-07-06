# Author: Rubens Andrade Filho
# Date: 2023-07-05

def resolver(pedidos: list[int], rolos: list[int]):
    # print(f"resolver {pedidos=}, {rolos=}")
    if len(pedidos)==0:
        return []
    
    pedido = pedidos[0]
    for i, rolo in enumerate(rolos):
        # se esse rolo atende o pedido atual
        if rolo - pedido >= 0:
            # tenta resolver os outros pedidos com o que sobra
            # print(f"tentando rolo {i}: {rolo}")
            rolos_restantes = rolos[:]
            rolos_restantes[i] = rolo - pedido
            res = resolver(pedidos[1:], rolos_restantes)
            if res is not False:
                # se deu certo resolver o restante,
                # retorna que esse pedido foi resolvido pelo rolo i 
                # e o restante das posicoes dos rolos que resolvem cada pedido em ordem
                return i, *res
            
        # se deu ruim, tenta o proximo rolo
    else:
        # todos os rolos deram ruim
        # print(f"voltando atrás de resolver {pedidos=}, {rolos=}")
        return False


def print_resolver(pedidos: list[int], rolos: list[int]):
    
    
    print(
        f"Há {len(pedidos)} pedidos para serem atendidos:\n\t"
        + "\n\t".join([f"pedido {i}: {p}" for i, p in enumerate(pedidos)])
    )
    

    res = resolver(pedidos, rolos)

    if res is not False:

        print(
            f"Maneira para atender a encomenda de {len(pedidos)} pedidos:\n\t"
            + "\n\t".join([f"pedido {i}: corte {p} m do rolo {r}" for i, (p, r) in enumerate(zip(pedidos, res))])
        )

        sobras = rolos[:]
        for p, r in enumerate(res):
            sobras[r] -= pedidos[p]
        print(
            f"Sobras no estoque:\n\t"
            + "\n\t".join([f"rolo {i}: {sobra} m" for i, sobra in enumerate(sobras)])
        )
    else:
        print("Nao foi possivel atender o pedido")

    


def main():

    rolos = input(f"Rolos no estoque\t>>> ")
    rolos = [int(r) for r in rolos.split()]

    pedidos = input(f"Encomendas de rolos\t>>> ")
    pedidos = [int(r) for r in pedidos.split()]

    print_resolver(pedidos, rolos)

print("#"*80)
print_resolver([50,15,30], [100])
print("#"*80)
print_resolver([70,90,70], [100, 150])
print("#"*80)
main()