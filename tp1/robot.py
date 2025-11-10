import random

#def greedy_bot(damier: Board, l: int = 0, c: int = 0) -> int
"""
def damier() -> list:
    return [[1,2,3],
            [3,2,1]]
"""

seed = random


def createBoard(n : int , m : int ) -> list :

    res : list = []

    for i in range(n):
        res_2 = [seed.randint(0,9) for j in range(m)]
        res.append(res_2)

    return res        


if __name__=="__main__":

    print( createBoard(10,10))

    pass


