from os import system as limp 
limp("cls")

while True:

    temp = float(input("Digite sua Temperatura Corporal: "))  
    pressão = float(input("Digite sua pressão arterial: "))
    bat_bpm = float(input("Digite seus batimentos cardiacos por minito: "))

    if temp >= 35 and temp <= 37.5 and pressão >= 10.1 and pressão <= 14 and bat_bpm >= 60 and bat_bpm <= 100:
        print("CASO DE ATENDIMENTO NORMAL:")

    elif temp > 39 or pressão > 14 or bat_bpm > 100:
        print("CASO DE ATENDIMENTO GRAVE:")

    elif temp < 35 or temp > 39 or pressão < 10.1 or bat_bpm < 60:
        print("CASO DE ATENDIMENTO URGENTE")

    if temp < 35:
        print(f"Temperatura de {temp}°C PROCURE UM MEDICO URGENTE.")

    elif temp >= 35 and temp <= 37.5: 
        print(f"sua temperatura é de {temp}°C está normal.")

    elif temp >= 37.6 and temp <= 39:
        print(f"sua temperatura é de {temp}°C FEBRE LEVE.") 

    elif temp > 39:
        print(f"Temperaura de {temp}°C FREBE ALTA PPROCURE UM MEDICO.")

    if pressão >= 10.1 and pressão <= 14:
        print(f"sua pressão é de {pressão} esta normal")    

    elif pressão > 14.1:
        print(f"Sua pressão é de {pressão} E ESTÁ ALTA.")

    elif pressão < 10.1:
        print(f"Sua pressão é de {pressão} E ESTÁ BAIXA.")


    if bat_bpm > 100:
        print(f"TAQUICARDIA seus batimentos são de {bat_bpm} BPM, se não estiver exercendo nenhuma atividade procure um medico.") 

    elif bat_bpm < 60:
        print(f"BRADICARDIA seus batimentos são de {bat_bpm} bpm, se voce não estiver dormindo procure um medico.")

    elif bat_bpm >= 60 and bat_bpm <= 100:
        print(f"Seus batimentos são de {bat_bpm} BPM NORMAL")