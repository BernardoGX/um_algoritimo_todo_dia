Desafio: Monitoramento de acessos por IP.

Contexto:
Voce tem uma lista fixa com registros de acessos ao sistema. Alguns enderecos IP aparecem mais de uma vez.

Objetivo:
O usuario deve digitar um IP e o programa precisa percorrer a lista para:
- contar quantas vezes esse IP apareceu
- mostrar a quantidade encontrada
- exibir alerta se ultrapassar o limite de acessos

Regra de alerta:
- limite de acessos: 5
- se a quantidade for maior que 5, mostrar mensagem de alerta (simulando protecao contra DDoS)

Lista fixa de IPs (30 itens):
- 192.168.0.10
- 10.0.0.1
- 172.16.0.5
- 192.168.0.10
- 192.168.0.10
- 8.8.8.8
- 10.0.0.1
- 192.168.0.10
- 172.16.0.5
- 192.168.0.10
- 192.168.0.10
- 10.0.0.1
- 200.200.200.200
- 192.168.0.20
- 1.1.1.1
- 192.168.0.10
- 10.0.0.2
- 172.16.0.5
- 8.8.4.4
- 192.168.0.10
- 10.0.0.1
- 172.16.0.9
- 192.168.0.10
- 203.0.113.5
- 192.168.0.30
- 10.10.10.10
- 192.168.0.10
- 172.16.0.5
- 198.51.100.8
- 192.168.0.10

Exemplo de saída esperada:

=== Monitor de Acessos por IP ===
Digite o IP para verificar: 192.168.0.10
O IP 192.168.0.10 acessou o sistema 11 vez(es).
ALERTA: numero de acessos acima do limite permitido!