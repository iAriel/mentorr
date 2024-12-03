
import os

def criar_pastas(pasta_principal, nomes_subpastas):
    """
    Cria uma pasta principal e subpastas dentro dela.
    
    :param pasta_principal: Nome da pasta principal.
    :param nomes_subpastas: Lista com os nomes das subpastas a serem criadas.
    """
    try:
        # Cria a pasta principal
        os.makedirs(pasta_principal, exist_ok=True)
        print(f"Pasta principal '{pasta_principal}' criada com sucesso!")

        # Cria as subpastas
        for nome in nomes_subpastas:
            caminho_subpasta = os.path.join(pasta_principal, nome)
            os.makedirs(caminho_subpasta, exist_ok=True)
            print(f"Subpasta '{nome}' criada dentro de '{pasta_principal}'.")

    except Exception as e:
        print(f"Erro ao criar pastas: {e}")

# Nome da pasta principal
pasta_principal = "PastaPrincipal"

# Lista de nomes das subpastas
nomes_subpastas = [
    "FABRICIO",
    "LÍVIA",
    "MAYSAS",
    "EMILY",
    "MARIA DE FÁTIMA/VICTOR",
    "Helida - Lívia Ester",
    "Cristina - Maria Madalena",
    "Angela - Eron",
    "Damiana",
    "Gerlania",
    "jéssica",
    "ismael",
    "wallyson",
    "wesley",
    "neuma",
    "clarice - F",
    "Dulce F",
    "Milena - F",
    "Juliana - Miguel",
    "maria das dores - pedro enzo",
    "denizia - Deiziele",
    "cinara - igor",
    "raquel - joyce",
    "Nauanny",
    "Isabel",
    "Helloisa"
]

# Chama a função para criar as pastas
criar_pastas(pasta_principal, nomes_subpastas)
