# Roteiro 2 - Tecnologias Hacker

Aluno: Luis Antonio Santana Rodrigues

---

## Pentest Toolkit:

Conforme solicitado no roteiro, foi desenvolvido um programa em python que reúne uma série de ferramentas úteis para realizar testes de penetração e análise de segurança em sistemas. 

O programa apresenta um menu interativo que permite ao usuário escolher entre diferentes opções de ferramentas, como:
- Scanner de portas
- Scanner de vulnerabilidades
- Busca de informações (Whois)
- Busca de subdomínios
- Busca de DNS (DNS Lookup)
- WafW00f (Web Application Firewall Fingerprinting)

Assim, o usuário pode selecionar a ferramenta desejada e o programa executará a função correspondente, exibindo os resultados na tela. O código foi estruturado de forma modular, com cada ferramenta implementada em uma função separada, facilitando a manutenção e a adição de novas funcionalidades no futuro.

## Como rodar?

1. Crie um ambiente virtual:
```bash
python3 -m venv venv
```
2. Ative o ambiente virtual:
```bash
source venv/bin/activate
```
3. Instale as dependências:
```bash
pip install -r requirements.txt
```
4. Execute o programa:
```bash
python main.py
```

## Observação: 

Para a execução da segunda ferramenta, "Scanner de Vulnerabilidades", dependendo da configuração do sistema pode ser necessário fornecer permissões de superusuário (root) para as execuções dos scripts de vulnerabilidade. Caso o programa não funcione corretamente, execute-o com o comando `sudo python main.py`.

## Referências
- Port Scanner: 
  - [Roteiro 1](https://github.com/devluisrodrigues/tecHack-roteiro1)

- Vulnerability Scanner:
    - [Nmap Vuln Scan](https://www.esecurityplanet.com/networks/nmap-vulnerability-scanning-made-easy/)
    - [Python Nmap](https://pypi.org/project/python-nmap/)

- Whois:
    - [Python Whois](https://pypi.org/project/python-whois/)

- DNS Enumeration:
    - [Python DNS](https://pypi.org/project/dnspython/)
    - [Exemplo](https://medium.com/@jsquared7/dns-enumeration-using-python-772bbeea7b0e)

- Subdomain Enumeration:
    - [Exemplo](https://www.geeksforgeeks.org/how-to-make-a-subdomain-scanner-in-python/)
    - Para maior riqueza de resultados, foi utilizada uma cópia da lista de subdomínios utilizada pela ferramenta "dnsEnum". Essa lista pode ser encontrada na pasta modules, sob nome de "subdomains.txt". 
- WafW00f:
    - [WafW00f](https://pypi.org/project/wafw00f/0.9.4/)
    - Esse módulo faz uso da ferramenta externa "wafw00f", que deve ser instalada separadamente. O módulo foi projetado para realizar o download automaticamente da ferramenta caso não a encontre, mas em caso de erro, basta acessar o ambiente da env e executar o seguinte comando:
    ```bash
    pip install wafw00f
    ```