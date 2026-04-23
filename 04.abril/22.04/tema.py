
print("\nPor favor, informe as seguintes informações:\n")
while True:
    kills = input("Digite o número de Kills:\n")

    try:
        kills_int = int(kills)
        break
    except:
        print("O valor inserido não é válido. Digite novamente")
        continue 

while True:
    deaths = input("Digite o número de Deaths:\n")
    try:
        deaths_int = int(deaths)
        break
    except:
        print("O valor inserido não é válido. Digite novamente")
        continue
while True:
    headshots = input("Digite o número de headshots:")
    try:
        headshots_int = int(headshots)
        break
    except:
        print("O valor inserido não é válido. Digite novamente")
        continue

if kills_int != 0 and deaths_int != 0:
    taxa_kd = kills_int / deaths_int
else:
    taxa_kd = 0

if kills_int != 0:
    taxa_de_headshots = headshots_int * kills_int
else: 
    taxa_de_headshots = 0

print(f"\nTaxa K/D:\n{taxa_kd}")
print(f"\nTaxa de headshots:\n {taxa_de_headshots}%")
