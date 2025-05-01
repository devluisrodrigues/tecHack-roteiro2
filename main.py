from init import init_colorama, init_interface, show_options
from config import GREEN, RESET

# MODULOS:
from modules.port_scanner import port_scanner
from modules.vulnerability_analysis import vulnerability_analysis
from modules.whois_search import whois_search
from modules.dns_enumeration import dns_enumeration
from modules.subdomain_analysis import subdomain_analysis
from modules.wafwoof import wafwoof

debug = True
if __name__ == "__main__":
    init_colorama()
    init_interface()
    continuar = True

    
    while continuar:
        error = False
        option = input(f"{GREEN} Digite a opção desejada: {RESET}")
        if option == "1":
            port_scanner()
        elif option == "2":
            vulnerability_analysis()
        elif option == "3":
            whois_search()
        elif option == "4":
            dns_enumeration()
        elif option == "5":
            subdomain_analysis()
        elif option == "6":
            wafwoof()
        else:
            print(f"{GREEN} Opção inválida! Tente novamente.{RESET}")
            error = True
        
        if not error:
            continuar = input(f"{GREEN}\nDeseja continuar? (s/n): {RESET}").lower() == "s"
            if continuar:
                show_options()
            else:
                print(f"{GREEN}Obrigado por usar o programa!{RESET}")
                print(f"{GREEN}Saindo...{RESET}")
        
    