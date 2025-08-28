# Script para renomear arquivos .py em todas as subpastas da pasta 'IA', remover acentos e padronizar nomes
# Inicializa o Git na pasta raiz 'IA', ignora .git em subpastas, adiciona todos os arquivos, commita e faz push para o GitHub

import os
import unicodedata
import subprocess

def remover_acentos(texto: str) -> str:
    """
    Remove acentos e caracteres especiais de um texto, mantendo apenas letras, números e hífens.
    
    Args:
        texto (str): Nome original do arquivo.
    
    Returns:
        str: Nome sem acentos e com hífens em vez de espaços.
    """
    texto_normalizado = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')
    texto_limpo = ''.join(c if c.isalnum() or c == '-' or c == '.' else '-' for c in texto_normalizado)
    while '--' in texto_limpo:
        texto_limpo = texto_limpo.replace('--', '-')
    return texto_limpo

def renomear_arquivo(caminho_pasta: str, nome_antigo: str, nome_novo: str) -> None:
    """
    Renomeia um arquivo usando 'git mv' para rastrear a mudança no Git, ou os.rename se Git não estiver disponível.
    
    Args:
        caminho_pasta (str): Caminho da pasta onde o arquivo está.
        nome_antigo (str): Nome original do arquivo.
        nome_novo (str): Novo nome do arquivo.
    """
    caminho_antigo = os.path.join(caminho_pasta, nome_antigo)
    caminho_novo = os.path.join(caminho_pasta, nome_novo)
    
    if nome_antigo == nome_novo:
        print(f"Arquivo '{nome_antigo}' já está com o nome correto em '{caminho_pasta}'.")
        return
    
    try:
        subprocess.run(['git', 'mv', nome_antigo, nome_novo], cwd=caminho_pasta, check=True)
        print(f"Renomeado com git mv: '{nome_antigo}' -> '{nome_novo}' em '{caminho_pasta}'")
    except subprocess.CalledProcessError:
        try:
            os.rename(caminho_antigo, caminho_novo)
            print(f"Renomeado com os.rename: '{nome_antigo}' -> '{nome_novo}' em '{caminho_pasta}'")
        except OSError as e:
            print(f"Erro ao renomear '{nome_antigo}' em '{caminho_pasta}': {e}")

def verificar_git_subpastas(caminho_raiz: str) -> None:
    """
    Verifica se há pastas .git em subpastas e alerta o usuário.
    
    Args:
        caminho_raiz (str): Caminho da pasta raiz 'IA'.
    """
    for pasta_atual, subpastas, _ in os.walk(caminho_raiz):
        if '.git' in subpastas and pasta_atual != caminho_raiz:
            print(f"Aviso: Encontrada pasta .git em '{pasta_atual}'. Isso pode indicar um repositório Git separado. Recomenda-se removê-la manualmente se a pasta raiz 'IA' for o repositório principal.")

def renomear_em_subpastas(caminho_raiz: str) -> None:
    """
    Percorre todas as subpastas da pasta raiz e renomeia arquivos .py.
    
    Args:
        caminho_raiz (str): Caminho da pasta raiz 'IA'.
    """
    for pasta_atual, subpastas, arquivos in os.walk(caminho_raiz):
        if '.git' in subpastas:
            subpastas.remove('.git')  # Ignora subpastas .git para evitar processar seus conteúdos
        print(f"\n=== Processando subpasta: {pasta_atual} ===")
        arquivos_py = [f for f in arquivos if f.endswith('.py')]
        
        if not arquivos_py:
            print("Nenhum arquivo .py encontrado nesta subpasta.")
            continue
        
        for arquivo in arquivos_py:
            nome_novo = remover_acentos(arquivo)
            renomear_arquivo(pasta_atual, arquivo, nome_novo)

def inicializar_e_sincronizar_git(caminho_raiz: str, url_repo: str, branch: str = 'main') -> None:
    """
    Inicializa o Git na pasta raiz, adiciona todos os arquivos, commita e faz push para o GitHub.
    
    Args:
        caminho_raiz (str): Caminho da pasta raiz 'IA'.
        url_repo (str): URL do repositório remoto no GitHub.
        branch (str): Nome do branch principal (padrão: 'main').
    """
    if not os.path.exists(os.path.join(caminho_raiz, '.git')):
        try:
            subprocess.run(['git', 'init'], cwd=caminho_raiz, check=True)
            print("Repositório Git inicializado na pasta raiz 'IA'.")
        except subprocess.CalledProcessError as e:
            print(f"Erro ao inicializar Git: {e}")
            return
    
    try:
        subprocess.run(['git', 'remote', 'add', 'origin', url_repo], cwd=caminho_raiz, check=True)
        print(f"Repositório remoto 'origin' adicionado: {url_repo}")
    except subprocess.CalledProcessError:
        print("Repositório remoto 'origin' já existe.")

    try:
        subprocess.run(['git', 'add', '.'], cwd=caminho_raiz, check=True)
        print("Todos os arquivos adicionados ao Git.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao adicionar arquivos: {e}")
        return

    try:
        subprocess.run(['git', 'commit', '-m', 'Sincronizando todos os arquivos da pasta IA com renomeações'], cwd=caminho_raiz, check=True)
        print("Commit realizado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao fazer commit: {e}")
        return

    try:
        subprocess.run(['git', 'push', '-u', 'origin', branch], cwd=caminho_raiz, check=True)
        print("Arquivos sincronizados com o GitHub.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao fazer push: {e}. Verifique autenticação com 'gh auth login' ou tente outro branch.")

def main():
    """
    Função principal que processa todas as subpastas da pasta 'IA', renomeia arquivos e sincroniza com GitHub.
    """
    caminho_raiz = r"C:\Users\tendy\OneDrive\Documentos\FACULDADE\ESCOLA DA NUVEM\IA"
    url_repo = "https://github.com/tendypora/Escola-da-Nuvem.git"
    branch = "master"  # Altere para 'master' se necessário
    
    if not os.path.exists(caminho_raiz):
        print(f"Erro: A pasta '{caminho_raiz}' não existe.")
        return
    
    verificar_git_subpastas(caminho_raiz)
    renomear_em_subpastas(caminho_raiz)
    inicializar_e_sincronizar_git(caminho_raiz, url_repo, branch)

if __name__ == "__main__":
    main()