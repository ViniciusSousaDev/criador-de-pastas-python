import os
import sys

def criar_pastas():
    # Pega o diretório onde o executável (ou o script) está localizado
    if getattr(sys, 'frozen', False):
        # Quando rodando como .exe gerado pelo PyInstaller
        diretorio_base = os.path.dirname(sys.executable)
    else:
        # Quando rodando como script .py normal
        diretorio_base = os.path.dirname(os.path.abspath(__file__))

    pastas = [
        "1 - JUNTA COMERCIAL",
        "2 - INSCRICOES E LICENCAS",
        "3 - DOCUMENTOS SOCIOS",
        "4 - DOCUMENTOS EMPRESA"
    ]

    print("Criando pastas...\n")

    for pasta in pastas:
        caminho = os.path.join(diretorio_base, pasta)
        if not os.path.exists(caminho):
            os.makedirs(caminho)
            print(f"  ✅ Criada: {pasta}")
        else:
            print(f"  ⚠️  Já existe: {pasta}")

    print("\nConcluído! Pressione Enter para fechar...")
    input()

if __name__ == "__main__":
    criar_pastas()