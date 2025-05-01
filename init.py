import colorama
from config import GREEN, RESET

def init_colorama():
    # Init colorama:
    colorama.init()
    
def init_interface():
    # Limpa o terminal:
    print("\033[H\033[J")
    
    print(f"""{GREEN}
  ____            _            _     _              _ _    _ _   
 |  _ \ ___ _ __ | |_ ___  ___| |_  | |_ ___   ___ | | | _(_) |_ 
 | |_) / _ \ '_ \| __/ _ \/ __| __| | __/ _ \ / _ \| | |/ / | __|
 |  __/  __/ | | | ||  __/\__ \ |_  | || (_) | (_) | |   <| | |_ 
 |_|   \___|_| |_|\__\___||___/\__|  \__\___/ \___/|_|_|\_\_|\__|
                                                                 
          {GREEN}""")
    
    print(f"{GREEN}                             Busque conhecimento...\n\n\n\n{RESET}")
    
    print(f"{GREEN} Seleciona uma das opções abaixo:\n\n")
    print(f"{GREEN} 1 - Escaneamento de portas TCP")
    print(f"{GREEN} 2 - Análise de vulnerabilidades")
    print(f"{GREEN} 3 - Busca de informações (Whois)")
    print(f"{GREEN} 4 - DNS Enumeration")
    print(f"{GREEN} 5 - Análise de Subdomínios")
    print(f"{GREEN} 6 - WAFW00F (Detecção de firewalls web)")
    print(f"{RESET}")
    
def show_options():
    print('\n'+'-'*50)
    print(f"{GREEN} 1 - Escaneamento de portas TCP")
    print(f"{GREEN} 2 - Análise de vulnerabilidades")
    print(f"{GREEN} 3 - Busca de informações (Whois)")
    print(f"{GREEN} 4 - DNS Enumeration")
    print(f"{GREEN} 5 - Análise de Subdomínios")
    print(f"{GREEN} 6 - WAFW00F (Detecção de firewalls web)")
    print(f"{RESET}")