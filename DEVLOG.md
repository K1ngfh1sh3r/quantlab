# QuantLab Development Log

## Jour 4

### Objectifs

- Créer le module des indicateurs techniques.
- Implémenter la première moyenne mobile.
- Ajouter les tests associés.

## Jour 5 :
- Ajout de l'indicateur EMA
- Implémentation SMA/EMA avec validation des paramètres
- Ajout de 12+ tests unitaires pytest
- Utilisation de pandas ewm() pour le calcul exponentiel

## Jour 6

### Objectifs

- Finaliser le module des indicateurs techniques.
- Ajouter des indicateurs supplémentaires.
- Renforcer la couverture de tests.

### Réalisations

- Ajout de nouveaux indicateurs techniques.
- Validation des paramètres d'entrée.
- Ajout de tests unitaires supplémentaires avec pytest.
- Amélioration de la structure du module indicators.


## Jour 7

### Objectifs

- Préparer la base du moteur de backtesting.
- Concevoir les premiers composants nécessaires.

### Réalisations

- Création du module backtesting.
- Mise en place de la structure Portfolio / Trade.
- Définition des premières interactions entre portefeuille et moteur.
- Préparation des tests associés.


## Jour 8

### Objectifs

- Implémenter la gestion des transactions.
- Ajouter la représentation des opérations financières.

### Réalisations

- Création de la classe Trade.
- Gestion des opérations BUY et SELL.
- Ajout des validations :
  - type de transaction valide ;
  - quantité positive.
- Ajout des tests unitaires.


## Jour 9

### Objectifs

- Développer la gestion du portefeuille.
- Permettre le suivi d'une position.

### Réalisations

- Implémentation de la classe Portfolio.
- Gestion :
  - du capital initial ;
  - du cash disponible ;
  - des actions détenues ;
  - de l'historique des transactions.
- Ajout du calcul de valeur du portefeuille.
- Ajout des tests associés.


## Jour 10

### Objectifs

- Créer le moteur principal de backtesting.
- Connecter stratégies et portefeuille.

### Réalisations

- Création de BacktestEngine.
- Exécution d'une stratégie sur des données historiques.
- Génération des signaux BUY/HOLD/SELL.
- Suivi de l'évolution du portefeuille.
- Ajout des premiers tests du moteur.


## Jour 11

### Objectifs

- Améliorer la robustesse du moteur.
- Ajouter des validations.

### Réalisations

- Ajout des contrôles :
  - colonne de prix inexistante ;
  - stratégie invalide ;
  - signal incorrect.
- Gestion des erreurs avec exceptions adaptées.
- Augmentation de la couverture de tests.


## Jour 12

### Objectifs

- Finaliser la première version du moteur de backtesting.
- Stabiliser l'architecture.

### Réalisations

- Validation complète du workflow :
  - données historiques ;
  - stratégie ;
  - exécution ;
  - portefeuille ;
  - résultats.
- Architecture stabilisée.
- Validation avec pytest et Ruff.


## Jour 13

### Objectifs

- Améliorer la qualité du moteur.
- Ajouter des fonctionnalités d'analyse.

### Réalisations

- Ajout du calcul des statistiques de backtest :
  - valeur finale ;
  - profit ;
  - rendement en pourcentage.
- Ajout de la gestion du dernier prix utilisé.
- Ajout des tests associés.


## Jour 14

### Objectifs

- Ajouter la gestion des quantités de positions.
- Améliorer la flexibilité du backtesting.

### Réalisations

- Ajout du paramètre quantity dans BacktestEngine.
- Support de plusieurs actions par transaction.
- Validation des quantités positives.
- Ajout des tests :
  - achat avec quantité personnalisée ;
  - évolution du portefeuille ;
  - validation des erreurs.
- Tous les tests passent avec pytest.


## Jour 15

### Objectifs

- Ajouter la gestion des frais de transaction.
- Rendre les simulations plus réalistes.

### Réalisations

- Ajout du système de commission sur les transactions.
- Gestion des frais lors des achats et ventes.
- Validation des commissions positives.
- Mise à jour des tests existants.
- Correction des attentes liées aux frais.
- Validation complète avec pytest.


## Jour 16

### Objectifs

- Ajouter une fonctionnalité d'export des résultats.
- Faciliter l'utilisation des résultats de backtest.

### Réalisations

- Ajout de la sauvegarde du dernier résultat de backtest.
- Ajout de la méthode export_csv().
- Export des résultats contenant :
  - les signaux ;
  - l'évolution de la valeur du portefeuille.
- Ajout des tests :
  - création du fichier CSV ;
  - erreur sans backtest préalable ;
  - vérification du contenu exporté.
- Validation avec pytest et Ruff.