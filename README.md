# DriveFinancer

DriveFinancer est une application simple de simulateur d'emprunt pour l'achat d'une voiture. Elle vous permet de déterminer le taux d'emprunt basé sur différents critères tels que le type de véhicule, le type d'énergie, le kilométrage, l'année de fabrication et le nombre de passagers.

## Prérequis

Avant d'utiliser cette application, assurez-vous d'avoir les dépendances suivantes installées :

- Python 3 (testé avec Python 3.7.9)
- Les bibliothèques Python suivantes : `customtkinter`, `packaging`

## Architecture du projet

Le projet est divisé en trois fichiers principaux :

1. `gui.py` : Ce fichier contient le code de l'interface utilisateur graphique (GUI) de l'application. Il utilise la bibliothèque `customtkinter` pour créer une fenêtre graphique et des éléments d'interface tels que des menus déroulants et des boutons.

2. `taux_calculator.py` : Ce fichier contient la logique de calcul du taux d'emprunt en fonction des critères sélectionnés. Il utilise des scores préalablement définis pour chaque critère pour effectuer les calculs.

3. `main.py` : Ce fichier est le point d'entrée de l'application. Il crée une instance de l'interface utilisateur à partir de `gui.py` et gère les interactions avec l'utilisateur, y compris le calcul du taux d'emprunt.

## Utilisation

1. Exécutez `installer.bat` pour créer un environnement, installer les packages et lancer le projet. Sinon, exécutez le code en invite de commande avec `./main.py`.

2. Sélectionnez les critères tels que le type de véhicule, le type d'énergie, le kilométrage, l'année de fabrication et le nombre de passagers à l'aide des menus déroulants.

3. Cliquez sur le bouton "Calcul taux" pour obtenir le taux d'emprunt estimé.

4. Vous devez remplir tous les menus déroulants, sinon un message rouge apparaîtra pour vous indiquer où vous n'avez pas rempli en cas d'erreur et redeviendront verts une fois que l'utilisateur aura fait un choix valide.

## Auteur

Théo D
