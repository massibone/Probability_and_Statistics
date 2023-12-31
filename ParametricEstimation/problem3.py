
'''
un campione casuale di 16 professori di una grande università ha una media campionaria del reddito annuale di 90500€ con una deviazione standard campionaria di 9400€. a)determina come siamo arrivati a queste due cifre b) determina un intervallo di confidenza al 95% per lo stipendio medio di tutti i professori di quella università.
'''
import numpy as np
import scipy.stats as stats

# Dati del campione
reddito_annuale = np.array([90500, 92500, 88000, 92000, 89000, 95000, 91000, 90000, 91500, 88000, 93000, 92000, 89000, 92500, 89000, 93000])
n = len(reddito_annuale)

# Calcolo della media campionaria
media_campionaria = np.mean(reddito_annuale)
print("Media campionaria:", media_campionaria)
# Calcolo della deviazione standard campionaria
deviazione_standard_campionaria = np.std(reddito_annuale, ddof=1)
print("Deviazione standard campionaria:", deviazione_standard_campionaria)

# Calcolo dell'intervallo di confidenza al 95%
intervallo_confidenza = stats.t.interval(0.95, df=n-1, loc=media_campionaria, scale=deviazione_standard_campionaria/np.sqrt(n))
print("Intervallo di confidenza al 95%:", intervallo_confidenza)
