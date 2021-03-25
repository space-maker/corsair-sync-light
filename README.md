# corsair-sync-light

Un script Python permettant d'activer une *sorte* d'ambilight pour les claviers Corsairs. On peut ajouter différents claviers via le fichier de configuration `config_keys.json`. A ce stage, le projet est pour l'instant en pré-alpha.

# Utilisation

La version Python utilisée est le `3.7.5`. Un requirement est disponible pour la gestion des dépendances. Pour utiliser le programme, rien de plus simple: `python main.py` est celui-ci se lance, à condition d'avoir activer le sdk corsair. Modifier le fichier de configuration pour le faire correspondre à votre clavier. Pour l'instant, le procesus n'est pas automatique et exige de changer le code (marche pour le K95 en azerty seulement).