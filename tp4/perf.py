import matplotlib.pyplot as plt
import matplotlib
import sys
import random

from timeit import timeit
from collections.abc import Callable, Iterator, Iterable
import functools 

def input_arrays(n: int=1_000, N: int=1_000, repl: bool=True) -> Iterator[list[int]]:
    
    N_list = list(range(N))

    new_list : list[int]

    if repl:
            for i in range (n):

                yield list(random.choices(N_list,k=i))
            
    else :
        for i in range(n):
             yield list(random.sample(N_list,i))





def plot_array(array: list[float], title: str, log: bool = False) -> None:
    plt.title(title)
    plt.semilogy(array) if log else plt.plot(array)
    plt.show()


def timeit_batch(fun: Callable, inputs: Iterable, setup: str='pass', cumul: int = 10) -> list[float]:
    return [timeit( f'{fun.__name__}({arg})',
                    setup=setup,
                    globals=globals(),
                    number=cumul) for arg in inputs]


def sum_reduce(t):
    return functools.reduce(lambda x, y: x + y, t ,0
                            )
    


if __name__=="__main__":
     
     

    # "scénario jouet" de parangonnage, à adapter au fur et à mesure du TP

     test = list(input_arrays())

     result: list[float]= timeit_batch(sum, test, cumul=4)
     result_2 : list[float]=timeit_batch(sum_reduce, test, cumul=4)
  
     plot_array(array=result, title="sum", log=False)
     plot_array(array=result_2, title="sum_reduce", log=False)

     #plt.savefig(sys.stdout.buffer)
     #sys.stdout.flush()
     


     




    
    

"""
     input_arrs = [list(range(100)) for _ in range(20)]
     result: list[float] = timeit_batch(sum, input_arrs, cumul=4)
     print(result)
     plot_array(array=result, title="sum", log=False)
    """

    
