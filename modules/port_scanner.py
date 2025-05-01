# Motor do port_scanner foi reutilizado do projeto desenvolvido durante o roteiro 1.
# O qual está disponível no repositório do GitHub: https://github.com/devluisrodrigues/tecHack-roteiro1

import socket
from config import GREEN, RESET, YELLOW

def is_port_open(host, port):
    """
    Função para verificar se uma porta está aberta em um host específico.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    
    try:
        result = sock.connect_ex((host, port))
        if result == 0:
            return 1
        elif result == 111 or result == 10061:
            return -1 # Porta fechada, connection refused
        else:
            0
    except socket.gaierror:
        print(f"{YELLOW}Erro: Host não encontrado.{RESET}")
        return None
    except Exception as e:
        print(f"{YELLOW}Erro: {e}{RESET}")
        return None

def port_scanner():
    """
    Função para escanear portas TCP de um host específico.
    """
    print(f"Iniciando o escaneamento de portas...\n{RESET}")
    
    host = input(f"Digite o endereço IP ou nome do host: {RESET}")
    
    # Se o host for um domínio, converte para IP
    try:
        ip = socket.gethostbyname(host)
        if ip != host:
            print(f"{YELLOW}Host convertido para IP: {ip}{RESET}")
    except socket.gaierror:
        print(f"{YELLOW}Erro: Host não encontrado, tente digitar o ip.{RESET}")
        return
    
    start_port = int(input(f"Digite a porta inicial: {RESET}"))
    end_port = int(input(f"Digite a porta final: {RESET}"))
    
    open_ports = []
    
    is_verbose = input(f"Deseja ativar o modo verboso? (s/n): {RESET}").lower() == "s"
    
    print("-" * 50)
    
    for port in range(start_port, end_port + 1):
        result = is_port_open(ip, port)
        
        if result == 1:
            open_ports.append(port)
            print(f"{GREEN}Porta {port} está aberta.{RESET}")
        elif result == -1:
            if is_verbose:
                print(f"{YELLOW}Porta {port} está fechada.{RESET}")
        elif result == 0:
            if is_verbose:
                print(f"{YELLOW}Porta {port} não está acessível.{RESET}")
                
    print("-" * 50)
                
    print(f"\n{GREEN}RESUMO: Após Port_Scan, as portas abertas são: {open_ports}")
    
