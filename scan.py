import socket
import dns.resolver

dominio = input("Digite seu alvo -> ")

with open("bruteforce.txt", "r") as arquivo:
    bruteforce = arquivo.readlines()

with open("subdominios.txt", "r") as arquivo:
    subdominios = arquivo.readlines()
    for subdom in subdominios:
        subdom = subdom.strip()
        
        try:
            print(f"{subdom}.{dominio}")
            resultados = dns.resolver.resolve(f"{subdom}.{dominio}", "A")
            for rdata in resultados:
                try:
                    print(f"{rdata} : {socket.gethostbyname(str(rdata))}")
                except socket.gaierror:
                    pass
        except dns.resolver.NXDOMAIN:
            print(f"Subdomínio {subdom}.{dominio} não foi encontrado")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")    

for registro in bruteforce:
    registro = registro.strip()
    
    try:
        resultado = dns.resolver.resolve(dominio, registro)
        for rdata in resultado:
            try:
                print(f"{registro}: {rdata}")
            except socket.gaierror:
                pass
    except dns.resolver.NXDOMAIN:
        print(f"Domínio {dominio} não foi encontrado")
        break
    except Exception as e:
        print(f"Ocorreu um erro: {e}")





