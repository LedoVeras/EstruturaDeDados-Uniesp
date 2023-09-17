vec = [11, 9, 7, 6, 5, 4, 3, 2, 1, 0, -1, - 3, -6, -6, -7, -7, -8, - 8]

#questão 1 e 2
def ordenar(vec:list, reverse = False):
    
    i = 1
    
    while(True):
        
        prev = vec[i - 1]
        cur = vec[i]
        
        #troca de maior que para menor que, se for reverse
        if(cur > prev if reverse else cur < prev):
            (vec[i - 1], vec[i]) = (cur, prev)
            i = max(1, i - 1)
        else:
            i += 1
        
        if(i > len(vec) - 1):
            break
        
    return vec

#questão 3
def mmax(vec:list):
    
    ma = vec[0]
    
    for cur in vec:
        if(cur > ma):
            ma = cur
            
    return ma
        
#questão 3
def mmin(vec:list):
    
    mi = vec[0]
    
    for cur in vec:
        if(cur < mi):
            mi = cur
            
    return mi

#questão 5
def remover_duplicados(vec:list):
    return list(set(vec))

#questão 4
def segundo_menor(vec:list):
    #ordena e depois pega o segundo menor pelo index 1 do array
    return ordenar(remover_duplicados(vec))[1]

#questão 7
def tercmax(vec:list):
    #ordena e depois pega o terceiro maior pelo index 2 do array
    return ordenar(remover_duplicados(vec), True)[2]

#questão 6
def par_impar(vec:list):
    
    resul = [0, 0]
    
    for cur in vec:
        resul[cur % 2] += 1
    
    print(f"o vetor tem {resul[0]} numeros pares, e {resul[1]} numeros impares")
    return resul

#questão 8
def mediana(vec:list):
    
    size = len(vec)
    index = int(size / 2) + 1
    
    orde = ordenar(vec)
    
    if(size % 2 == 0):
        return (orde[index] + orde[index - 1]) / 2
    else:
        return orde[index]
        

    

print("lista ordenada: ", ordenar(vec, False))
print("lista ordenada decrescente: ", ordenar(vec, True))
print("maior valor: " , mmax(vec))
print("menor valor: " , mmin(vec))
print("segundo menor: " , segundo_menor(vec))
print("sem duplicados: " , remover_duplicados(vec))
print("par e impar respectivamente: " , par_impar(vec))
print("terceiro maior: " , tercmax(vec))
print("mediana do vetor: " , mediana(vec))