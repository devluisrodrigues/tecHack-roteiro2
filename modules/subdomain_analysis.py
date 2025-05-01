import dns.resolver
import dns.exception
import os
from config import GREEN, RESET

def subdomain_analysis():
    """
    Função para realizar análise de subdomínios.
    Realiza enumeração de subdomínios comuns.
    """
    domain = input("Digite o domínio a ser pesquisado: ").strip()
    resolver = dns.resolver.Resolver()

    # Verifica se o domínio é válido
    try:
        answers = resolver.resolve(domain, 'A')
        print(f"{GREEN}Domínio encontrado: {domain}{RESET}")
    except dns.resolver.NoAnswer:
        print(f"{GREEN}Sem respostas para o domínio: {domain}{RESET}")
        return
    except dns.exception.DNSException as e:
        print(f"{GREEN}Erro ao resolver domínio: {e}{RESET}")
        return

    # Brute force:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    subdomains_file = os.path.join(script_dir, 'subdomains.txt')
    
    with open(subdomains_file, 'r') as f:
        subdomains = [line.strip() for line in f.readlines()]
        
    
    print(f"\n{GREEN}Tentativa de enumeração de subdomínios comuns:{RESET}")
    for sub in subdomains:
        subdomain = f"{sub}.{domain}"
        try:
            answers = resolver.resolve(subdomain, 'A')
            print(f" - {subdomain} encontrado:")
            for rdata in answers:
                print(f"    -> {rdata.address}")
        except dns.exception.DNSException:
            continue
        
    return