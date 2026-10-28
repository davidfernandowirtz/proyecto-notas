"""Funcións estatísticas básicas.

FASE 1 · Desenvolve: USUARIO 1
Todas reciben unha lista de números, por exemplo [7.5, 4.0, 9.0].
"""


def media(notas):
    """Devolve a media da lista. Se a lista está baleira, devolve 0.

    media([4, 6, 8]) -> 6
    """
    if len(notas) == 0:
        return 0
    cont = 0
    for n in notas:
        cont +=n
    return cont / len(notas)


def nota_maxima(notas):
    """Devolve a nota máis alta da lista.

    nota_maxima([3, 9, 5]) -> 9
    """
    nota_max = 0
    for n in notas:
        if n > nota_max:
            nota_max = n
    return nota_max


def nota_minima(notas):
    """Devolve a nota máis baixa da lista.

    nota_minima([3, 9, 5]) -> 3
    """
    nota_min = 10
    for n in notas:
        if n < nota_min:
            nota_min = n
    return nota_min
