import numpy as np

def densite_normale_centree_reduite(x):
    return (1/np.sqrt(2*np.pi)) * np.exp(-0.5*x**2)

def fonction_repartition_normale_centree_reduite(x):
    return (1 + np.math.erf(x / np.sqrt(2))) / 2

def monte_carlo_estimation_probabilite(a, b, nombre_iterations):
    nombre_reussites = 0
    
    for i in range(nombre_iterations):
        x = np.random.normal(0, 1)  # Générer une réalisation de la variable aléatoire X
        if a <= x <= b:
            nombre_reussites += 1
    
    probabilite_estimee = nombre_reussites / nombre_iterations
    return probabilite_estimee

# Paramètres
a = -1.65
b = 1.65
nombre_iterations = 1000000

# Estimation de la probabilité avec la méthode de Monte Carlo
probabilite_monte_carlo = monte_carlo_estimation_probabilite(a, b, nombre_iterations)

# Calcul de la probabilité avec la fonction de répartition
probabilite_fonction_repartition = fonction_repartition_normale_centree_reduite(b) - fonction_repartition_normale_centree_reduite(a)

# Calcul de l'erreur relative
erreur_relative = abs(probabilite_monte_carlo - probabilite_fonction_repartition) / probabilite_fonction_repartition

# Affichage des résultats
print(f"Probabilité estimée (Monte Carlo) : {probabilite_monte_carlo}")
print(f"Probabilité calculée (Fonction de répartition) : {probabilite_fonction_repartition}")
print(f"Erreur relative : {erreur_relative}")

