
import os

def criar_pasta():
    # Nome da pasta a ser criada
    nome_pasta = 'autojump'

    # Caminho completo para a nova pasta
    nova_pasta_path = os.path.join(os.getcwd(), nome_pasta)

    # Cria a pasta se ela não existir
    if not os.path.exists(nova_pasta_path):
        os.makedirs(nova_pasta_path)
        print(f"Pasta 'autojump' criada com sucesso em /content.")
    else:
        print(f"A pasta 'autojump' já existe em /content.")

if __name__ == "__main__":
    criar_pasta()
    