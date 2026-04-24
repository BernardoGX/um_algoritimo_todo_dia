lista_de_ips = ["192.168.0.10","10.0.0.1","172.16.0.5","192.168.0.10","192.168.0.10","8.8.8.8","10.0.0.1","192.168.0.10","172.16.0.5","192.168.0.10","192.168.0.10","10.0.0.1","200.200.200.200","192.168.0.20","1.1.1.1","192.168.0.10","10.0.0.2","172.16.0.5","8.8.4.4","192.168.0.10","10.0.0.1","172.16.0.9","192.168.0.10","203.0.113.5","192.168.0.30","10.10.10.10","192.168.0.10","172.16.0.5","198.51.100.8","192.168.0.10"]
while True:
    ip_digitado = input("Digite o seu ip:\n")
    quantidade_de_entradas = lista_de_ips.count(ip_digitado)
    print(f"O ip {ip_digitado} acessou o sistema {quantidade_de_entradas} vezes")
    if quantidade_de_entradas <= 5:
        print("Ip disponivel.")
        break
    else:
        print("ALERTA: numero de acessos acima do limite permitido! Digite outro ip válido")
        continue