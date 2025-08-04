# lab2_teoriaCompu
Este es un programa en python que simula el comportamiento de autómatas finitos deterministas (AFD) y las diferentes opciones que se pueden realizar con él:
- transition(q, a, δ) la cual devuelve el valor de la transici´on δ(q, a), para un estado q ∈ K y un s´ımbolo a ∈ Σ.
- final state(q, w, δ) la cual devuelve el estado q obtenido por el aut´omata despu´es de terminar de leer la cadena w ∈ Σ∗.
- derivation(q, w, δ) la cual derivaci´on de la cadena w ∈ Σ∗ desde el estado q ∈ K, esto es, la secuencia ordenada de transiciones obtenidas.
- accepted(q, w, F, δ) la cual devuelve verdadero si la cadena w ∈ Σ∗ es aceptada por el aut´omata partiendo desde elestado q; y falso en caso contrario

El programa interpreta los automatas desde un json.

###Instrucciones para correr
1) Clonar el repositorio desde terminal. HTTPS:
```
git clone https://github.com/Ren23813/lab2_teoriaCompu 
```

2) En la carpeta del repositorio clonado ejecutar el siguiente comando
```
python3 main.py
```
o abrir visual estudio o su editor de código para ejecutarlo manualmente
