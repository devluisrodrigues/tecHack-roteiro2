import subprocess
import sys
from config import GREEN, RESET, YELLOW, RED

def wafwoof():
    """
    Função para executar o WAFW00F, uma ferramenta para detectar firewalls web.
    """
    
    # Check se o programa existe e se está disponível:

    try:
        subprocess.run(["wafw00f", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        # Se o programa não estiver instalado, tenta instalar via pip:
        print(f"{RED}WAFW00F não está instalado. Instalando...{RESET}")
        subprocess.run([sys.executable, "-m", "pip", "install", "wafw00f"], check=True)

    url = input("Digite a URL para análise: ").strip()
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
        
    print(f"{GREEN}Analisando {url} com WAFW00F...{RESET}")
    
    try:
        # Executa o WAFW00F e captura a saída:
        result = subprocess.run(["wafw00f", url], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        output = result.stdout.decode("utf-8")
        
        print(f"{GREEN}Resultado da análise:{RESET}")
        print(output)
    except subprocess.CalledProcessError as e:
        print(f"{RED}Erro ao executar WAFW00F: {e.stderr.decode('utf-8')}{RESET}")
    except Exception as e:
        print(f"{RED}Erro inesperado: {e}{RESET}")
        
    return
        