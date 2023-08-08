def segundos_em_horas (segundos):
    minutos = segundos // 60
    segundos = segundos % 60
    horas = minutos // 60
    minutos = minutos % 60

segundos = int(input(f"=> Informe o tempo representado em segundos: "))
tempo = segundos_em_horas(segundos)