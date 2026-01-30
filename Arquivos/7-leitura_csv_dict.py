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
            curso = {}
            curso["language"] = linguagem
            curso["category"] = categoria
            cursos.append(curso)


# Cabeçalho formatado (15 espaços para linguagem, 25 para categoria)
print(f"{'Language':^15} | {'Category':^25}")
print("-" * 43)

#Funções get para linguagem e categoria
def get_language(course):
    return course["language"]

def get_category(course):
    return course["category"]

# Ordenamos a lista e imprimimos centralizado
for curso in sorted(cursos, key=lambda c: c["language"]):
    print(f"{curso["language"]:^15}   {curso["category"]:^25}")