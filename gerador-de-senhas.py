import random 
import string

def geradorSenhas(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

tamanhoSenha = int(input("Digite o tamanho da senha que deseja: "))
senhaGerada = geradorSenhas(tamanhoSenha)
print("Senha Gerada:\n", senhaGerada)
