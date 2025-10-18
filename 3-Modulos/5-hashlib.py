import hashlib

# 1 - Verificar os algoritmos disponíveis
print(hashlib.algorithms_available)

# 2 - Verificar algoritmos de acordo com SO
print(hashlib.algorithms_guaranteed)

# 3 - Utilizando o SHA256  
# usado para verificar 
# integridade/autenticidade 
# de arquivos
algorithm = hashlib.sha256()
print(f"digest {algorithm.digest()}\n")
message = "A melhor forma de prever o futuro é criá-lo".encode()
print(f"{message}\n")
algorithm.update(message)
print(f"{algorithm.hexdigest()}\n")


# 4 - Utilizando o MD5
# Também usado para verificar 
# integridade/autenticidade
# de arquivos
md5 = hashlib.md5()
md5.update(message)
print(f"{message}\n")
print(f"{md5.hexdigest()}\n")