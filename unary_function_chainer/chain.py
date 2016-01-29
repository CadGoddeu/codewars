def f1(x): return x * 2

def f2(x): return x + 2


def f3(x): return x ** 2


def f4(x): return x.split()


def f5(xs): return [x[::-1].title() for x in xs]


def f6(xs): return "_".join(xs)

def chained(functions):
    return lambda x: reduce(lambda v, f: f(v), functions, x)

if __name__ == '__main__':
    print(chained([f1,f2,f3])(0))