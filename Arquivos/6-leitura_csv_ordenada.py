cursos = []

with open("dados/cursos.csv", "r", encoding="utf-8") as file:
    # Pula o cabeçalho para ele não entrar na lista 'cursos'
    header = next(file) 
    
    for line in file:
        # Usamos strip() em cada parte para remover espaços extras (como o espaço após a vírgula)
        partes = line.rstrip().split(",")
        if len(partes) == 2:
            linguagem = partes[0].strip()
            categoria = partes[1].strip()
            cursos.append((linguagem, categoria)) # Guardamos como tupla para facilitar a ordenação

# Cabeçalho formatado (15 espaços para linguagem, 25 para categoria)
print(f"{'Language':^15} | {'Category':^25}")
print("-" * 43)

# Ordenamos a lista e imprimimos centralizado
for linguagem, categoria in sorted(cursos):
    print(f"{linguagem:^15}   {categoria:^25}")