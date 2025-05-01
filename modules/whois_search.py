from config import GREEN, RESET, YELLOW
import whois

def whois_search():
    """
    Função para realizar uma pesquisa WHOIS em um domínio específico.
    """
    print("Iniciando a pesquisa WHOIS...\n")
    
    domain = input("Digite o domínio (exemplo: avelinux.com): ")

    try:
        w = whois.whois(domain)
        # print(w)
        print(f"{GREEN}Resultados da pesquisa WHOIS para {domain}:{RESET}")
        print('-' * 50)
        print(f"Nome do domínio: {w.domain_name}{RESET}") if w.domain_name else None
        print(f"País: {w.country}{RESET}") if w.country else None
        print(f"Nome do registrante: {w.registrant_name}{RESET}") if w.registrant_name else None
        print(f"CPF/CNPJ do registrante: {w.registrant_id}{RESET}") if w.registrant_id else None
        
        print(f"Pessoa para contato: {w.person}{RESET}") if w.person else None
        print(f"Email: {w.email}{RESET}") if w.email else print(f"Emails: {w.emails}{RESET}") if w.emails else None
        print(f"Telefone: {w.phone}{RESET}") if w.phone else None
        
        print(f"Data de criação: {w.creation_date}{RESET}") if w.creation_date else None
        print(f"Data de expiração: {w.expiration_date}{RESET}") if w.expiration_date else None
        
        print(f"Servidor DNS: {w.name_server}{RESET}") if w.name_server else None
        print(f"Organização: {w.org}{RESET}") if w.org else None
        
        print('-' * 50)
    except Exception as e:
        print(f"{YELLOW}Erro ao realizar a pesquisa WHOIS: {e}{RESET}") 