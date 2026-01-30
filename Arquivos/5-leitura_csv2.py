with open("dados/cursos.csv", "r", encoding="utf-8") as file:
    # 1. Lemos a primeira linha para extrair os nomes das colunas
    header = next(file).rstrip().split(",")
    col1, col2 = header[0].strip(), header[1].strip()

    # 2. Imprimimos o cabeçalho com um espaçamento fixo (ex: 15 caracteres)
    # O símbolo '^' centraliza o texto
    print(f"{col1:^15} | {col2:^20}")
    print("-" * 38) # Linha separadora

    for line in file:
        # 3. Limpamos e dividimos os dados
        partes = line.rstrip().split(",")
        
        # Garantimos que a linha tem os dois elementos antes de descompactar
        if len(partes) == 2:
            linguagem, categoria = partes[0].strip(), partes[1].strip()
            
            # 4. Imprimimos os dados centralizados com o mesmo recuo (15 e 20)
            print(f"{linguagem:^15}   {categoria:^20}")