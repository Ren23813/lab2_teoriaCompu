#Programa para la simulación de un autómata determinista, para la clase de Teoría de la Computación (sección 20)
#Melisa Mendizabal y Renato Rojas
import json

# 1. transition(q, a, δ)
# ¿Qué hace?
# Simula una sola transición del autómata: le das un estado y un símbolo, 
# y te dice a qué estado va el autómata según la función de transición δ.

# Ejemplo:
# Si estás en el estado "A" y lees el símbolo "1", y δ("A", "1") = "B", 
# entonces esta función devuelve "B".
def transition(q,a, automata):
    print("\n Transición: ")
    estados = automata["estados"]
    alfabeto = automata["alfabeto"]
    transiciones = automata["transiciones"]

    if q in estados and a in alfabeto:
        opcionesEstado = transiciones[q]
        resultado = opcionesEstado[a]
        print(f"Dado el estado {q} y el simbolo {a} se llega al estado {resultado}")
        return resultado
    else: 
        print("El estado no existe dentro del automata o el simbolo no pertenece al alfabeto")
        return "no existe"

# 2. final_state(q, w, δ)
# ¿Qué hace?
# Recorre toda la cadena w símbolo por símbolo, comenzando en el estado q, aplicando la función de transición δ, hasta llegar al estado final.
# Devuelve ese estado final (no importa si es de aceptación o no).

# Ejemplo:
# Desde q = "A" y con w = "1011", te dirá en qué estado termina el autómata tras leer todos los símbolos.
def finalState(q,w, automata):
    estados = automata["estados"]
    alfabeto = automata["alfabeto"]
    transiciones = automata["transiciones"]

    if q in estados:

        cadenaDividida = []
        i= 0
        while i < len(w):
            encontrado = False
            for j in sorted(alfabeto, key=len, reverse=True):
                if w[i:i+len(j)] == j: #corta la cadena y compara si esta en el alfabeto
                    cadenaDividida.append(j)
                    i += len(j)
                    encontrado = True
                    break
            if not encontrado:
                cadenaDividida.append(w[i])
                i += 1

        if set(cadenaDividida) == set(alfabeto):

            estadoActual = q
            for simbolo in cadenaDividida:
                opcionesEstado = transiciones[estadoActual]
                estadoResultante = opcionesEstado[simbolo]
                estadoActual = estadoResultante
                
            print(f"El estado final de la cadena {w}, empezando con el estado {q} es {estadoActual}")
            return estadoActual
        else: 
            print("La cadena incluye elementos que no pertenencen al alfabeto del automata")
            return "no existe" 
    
    else:
        print("El estado no es valido en el automata")
        return "no existe"           

## derivation(q, w, δ)
# ¿Qué hace?
# Devuelve la secuencia completa de transiciones que realiza el autómata al procesar la cadena w desde el estado q.
# Es decir, te dice: "A" --1--> "B" --0--> "A" --1--> "B", etc.
# Esto es útil para ver paso a paso cómo avanza el autómata. 

def derivation(q,w,automata):    
    estados = automata["estados"]
    alfabeto = automata["alfabeto"]
    transiciones = automata["transiciones"]
    todasTransiciones = []

    if q in estados:
        

        cadenaDividida = []
        i= 0
        while i < len(w):
            encontrado = False
            for j in sorted(alfabeto, key=len, reverse=True):
                if w[i:i+len(j)] == j: #corta la cadena y compara si está en el alfabeto
                    cadenaDividida.append(j)
                    i += len(j)
                    encontrado = True
                    break
            if not encontrado:
                cadenaDividida.append(w[i])
                i += 1

        if set(cadenaDividida) == set(alfabeto):
            estadoActual = q
            for simbolo in cadenaDividida:
                opcionesEstado = transiciones[estadoActual]
                estadoResultante = opcionesEstado[simbolo]
                cadena = f"{estadoActual} -- {simbolo} -> {estadoResultante}" 
                todasTransiciones.append(cadena)
                estadoActual = estadoResultante
                
                
            print(f"Las transiciones de la cadena {w}, empezando con el estado {q}, son {todasTransiciones}")
            
            return todasTransiciones
        else: 
            print("La cadena incluye elementos que no pertenencen al alfabeto del automata")
            return "no existe" 
    

    else: 
        print("El estado no existe dentro del automata o el simbolo no pertenece al alfabeto")
        return "no existe"
    

# accepted(q, w, F, δ)
# ¿Qué hace?
# Te dice si la cadena w es aceptada por el autómata partiendo desde el estado q.
# ¿Cómo se define "aceptada"? Si al terminar de procesar w, el autómata termina en un estado que está en el conjunto de aceptación F.
# Devuelve True o False.

def accepted(q,w,automata):
    print("\n Comprobando aceptación...")
    estadosAceptacion = automata["aceptacion"]
    if finalState(q,w,automata) in estadosAceptacion: 
        print(f"Se llegó satisfactoriamente a un estado de aceptación usando la palabra {w}")
        return True
    else:
        print(f"La palabra {w} no llegó a un estado de aceptación")
        return False



#abrir el json
with open('ej1.json') as f:
    data = json.load(f)


#Ejemplos
transition1_test = transition("D", "1", data["primerEjercicio"])
transition2_test = transition('Y','wii', data["segundoEjercicio"])

print("\n FinalState:")
finalState1_test = finalState('A','11011',data["primerEjercicio"])
finalState2_test = finalState('Z','waawiiwiiwaa',data["segundoEjercicio"]) 
finalState3_test = finalState('Z','waawiiwiiwaaa',data["segundoEjercicio"]) #Se espera que falle, ya que tiene un "waaa", con 3 a's

print("\n Derivación")
derivation1_test = derivation('C','01101001',data["primerEjercicio"])
derivation2_test = derivation('Y','wiiwaawiiwiiwaawii',data["segundoEjercicio"])

accepted1_test = accepted('A','1011011',data["primerEjercicio"])  #será False
accepted2_test = accepted('X','wiiwiiwaa',data["segundoEjercicio"]) #será True
