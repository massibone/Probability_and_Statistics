'''
una compagnia di assicurazione emette una polizza che garantisce che verrà pagata una cifra A,in caso si verifichi un evento E entro un anno.Se la compagnia stimas che questo evento accada entro l'anno con probabilità P,quanto deve far pagare la polizza al cliente per avere un ricavo il cui valore atteso sia il 10% di A?
'''

'''
Il valore atteso (expected value) di una variabile casuale rappresenta la somma dei prodotti tra i possibili valori della variabile e le probabilità associate a tali valori.

In questo caso, il ricavo della compagnia di assicurazione è rappresentato dalla cifra che la compagnia incassa dalla polizza, che chiameremo C. Quindi dobbiamo trovare la cifra C tale che il valore atteso del ricavo sia il 10% di A.

Il valore atteso del ricavo può essere calcolato come:

Valore atteso del ricavo = C * P

Dato che vogliamo che il valore atteso del ricavo sia il 10% di A, possiamo impostare l'equazione:
C * P = 0.1 * A

Quindi la cifra C che la compagnia dovrebbe far pagare alla polizza al cliente è:

C = (0.1 * A) / P
'''
def calcola_cifra_polizza(cifra_garantita, probabilita):
    cifra_polizza = (0.1 * cifra_garantita) / probabilita
    return cifra_polizza
cifra_garantita = 1000  # Cifra garantita A
probabilita = 0.2  # Probabilità P

cifra_polizza = calcola_cifra_polizza(cifra_garantita, probabilita)
print(f"La compagnia dovrebbe far pagare alla polizza al cliente la cifra di: {cifra_polizza}")

#La compagnia dovrebbe far pagare alla polizza al cliente la cifra di: 500.0

