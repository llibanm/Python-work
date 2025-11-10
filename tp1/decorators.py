from collections.abc import Callable        # only in Python 3.9.2+, "from typing" otherwise


def trace(func: Callable) -> Callable:
    """Décorateur qui trace les appels à la fonction func.

    Affichage sur la sortie standard, avant et après l'appel de func.

    :param func: la fonction à décorer
    :return: la fonction décorée

    :Example:

    >>> @trace
    ... def f(n: int):
    ...     print(f"{n} est un joli nombre !")
    >>> f(2)
    AVANT f
    2 est un joli nombre !
    APRÈS f
    """

    # fonction interne (fermeture ou closure) qui sera retournée par le décorateur
    def wrapper(*args, **kwargs):  # *args capture tous les arguments positionnels de la fonction func dans un tuple
                                   # **kwargs capture tous les arguments nommés de la fonction func dans un dictionnaire
                                   # Par exemple, si func est appelée avec func(1, 2, x=3, y=4),
                                   # alors args = (1, 2) et kwargs={'x': 3, 'y': 4}.
                                   
        nonlocal offset     # permet de modifier la variable offset définie dans la fonction englobante trace
        nonlocal count
        # ici va ce qui est exécuté *avant* l'appel de fonction func
        #print(f"{'. ' * offset}AVANT {func.__name__}")
        #offset += 1     # on décale l'affichage d'un motif '. ' pour chaque appel récursif

        count += 1
        print(f"fibo:",count," <- (",*args,")")
        

        ans = func(*args, **kwargs)  # appel de la fonction func et enregistrement de son résultat dans ans

        print(f"fibo           -> ",ans,)

        # ici vient ce qui est exécuté *après* l'appel de fonction func
        #offset -= 1     # on aligne sur l'affichage *AVANT* pour chaque appel récursif
        #print(f"{'  ' * offset}APRÈS {func.__name__}")
        return ans

    offset: int = 0 # variable locale à la fonction trace
                    # modifiée dans la fonction imbriquée wrapper (grâce à nonlocal)

    count: int = 0

    return wrapper  # on retourne la fonction interne qui sera appelée *à la place* de func