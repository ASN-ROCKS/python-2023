# %%

# f(x) = x + x^2 + 10
# f(0) = 0 + 0 ^ 2 + 10 = 10
# f(1) = 1 + 1 ^ 2 + 10 = 12
# f(2) = 2 + 2 ^ 2 + 10 = 16

def f(x):
    return x + (x ** 2) + 10

# %%

f(1)

# %%

f(10)

# %%
f(-20)

# %%

def saudacao(nome):
    print("Olá, ", nome, ". Boas vindas!!", sep="")

# %%

saudacao("teo")

saudacao("ana")

# %%

def media(x:list)->float:
    return sum(x) / len(x)

# %%

notas = [4.64, 6.76, 9.76, 10]

media()

# %%

def soma(a=0, b=0):
    """Função soma recebe dois valores e retorna o resultado somando-os.
    a: int
    b: int
    """
    res = a + b
    return res

# %%
soma()

# %%
def soma(a, b=0):
    return a + b

# %%
soma(1,10)


# %%