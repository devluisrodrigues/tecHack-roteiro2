import dns.resolver
import dns.reversename
import dns.exception
import os

from config import GREEN, RESET

def resolve_to_ip(name):
    """Tenta resolver um nome para IPs (A e AAAA)."""
    ips = []
    try:
        answers = dns.resolver.resolve(name, 'A')
        ips.extend([r.address for r in answers])
    except dns.exception.DNSException:
        pass
    try:
        answers = dns.resolver.resolve(name, 'AAAA')
        ips.extend([r.address for r in answers])
    except dns.exception.DNSException:
        pass
    return ips

def dns_enumeration():
    """
    Função para enumerar registros DNS de um domínio.
    Semelhante ao dnsenum, tenta recuperar diversos registros DNS.
    """
    
    domain = input("Digite o domínio a ser pesquisado: ").strip()
    
    resolver = dns.resolver.Resolver()

    record_types = ['A', 'AAAA', 'CNAME', 'MX', 'NS', 'TXT', 'SOA']
    
    for type in record_types:
        print(f"{GREEN}\nBuscando registros {type} para {domain}{RESET}")
        try:
            answers = resolver.resolve(domain, type, raise_on_no_answer=False)
            if answers.rrset:
                for rdata in answers:
                    output = f" - {type} {domain}: {rdata.to_text()}"
                    if type != 'A' and type != 'AAAA':
                        target = str(rdata.exchange if type == 'MX' else rdata.target if type == 'CNAME' else rdata) 
                        ips = resolve_to_ip(target)
                        if ips:
                            output += f" -> IPs: {', '.join(ips)}"
                    else:
                        output += f" -> IP: {rdata.address}"
                    print(output)   
            else:
                print(f" - Nenhum registro {type} encontrado para {domain}.")
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.DNSException) as e:
            print(f" - Erro ao buscar {type}: {e}")
            
    # Domínios do tipo A podem ter reverso:
    print(f"\n{GREEN}Buscando reverso para {domain}{RESET}")
    try:
        answers = resolver.resolve(domain, 'A')
        for rdata in answers:
            ip = rdata.address
            try:
                rev_name = dns.reversename.from_address(ip)
                rev_result = resolver.resolve(rev_name, "PTR")
                print(f"\nReverso do IP {ip}:")
                for ptr in rev_result:
                    print(f" - {ptr.to_text()}")
            except dns.exception.DNSException as e:
                print(f"Falha no reverso de {ip}: {e}")
    except:
        pass

    return