### Système de Gestion d'Utilisateurs

## Description

Ce projet est une application web de gestion d'utilisateurs développée avec Flask. Elle permet aux utilisateurs de créer un compte, se connecter, et gérer leur profil. L'interface utilisateur est intuitive et responsive, offrant une expérience utilisateur fluide.





## Fonctionnalités

- **Authentification sécurisée** : Système de connexion et d'inscription avec mots de passe hashés
- **Gestion de profil** : Modification des informations utilisateur
- **Interface responsive** : Design adapté à tous les appareils
- **Messages flash** : Notifications pour informer l'utilisateur des actions effectuées


## Prérequis

- Python 3.8 ou supérieur
- MySQL Server 5.7 ou supérieur
- Navigateur web moderne


## Installation

### 1. Télécharger le code source

Téléchargez et décompressez le projet ou clonez-le depuis le dépôt Git.

```shellscript
git clone https://github.com/votre-nom/gestion-utilisateurs.git
cd gestion-utilisateurs
```

### 2. Créer un environnement virtuel Python

```shellscript
# Créer l'environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
# Sur Windows
venv\Scripts\activate
# Sur Linux/Mac
source venv/bin/activate
```

### 3. Installer les dépendances

```shellscript
pip install -r requirements.txt
```

### 4. Configuration de la base de données MySQL

#### Installation de MySQL

- **Windows** : Téléchargez et installez MySQL depuis [le site officiel](https://dev.mysql.com/downloads/installer/)
- **Linux (Ubuntu/Debian)** :

```shellscript
sudo apt update
sudo apt install mysql-server
sudo systemctl start mysql
```


- **macOS** :

```shellscript
brew install mysql
brew services start mysql
```




#### Création de la base de données

```shellscript
# Se connecter à MySQL
mysql -u root -p

# Dans la console MySQL, créer la base de données
CREATE DATABASE flask;
```

### 5. Configuration de l'application

Créez un fichier `.env` à la racine du projet avec le contenu suivant :

```plaintext
SECRET_KEY=73d5128e51b5d4088b7b779ce6e39349d08a4980830cd3659904a3e4c390d691
SQLALCHEMY_DATABASE_URI=mysql+pymysql://root:VOTRE_MOT_DE_PASSE@localhost/flask
```

Remplacez `VOTRE_MOT_DE_PASSE` par votre mot de passe MySQL.

## Démarrage de l'application

1. Assurez-vous que votre environnement virtuel est activé
2. Vérifiez que MySQL est en cours d'exécution
3. Lancez l'application :


```shellscript
python app.py
```

4. Ouvrez votre navigateur et accédez à : `http://127.0.0.1:5000`


## Guide d'utilisation

### Création d'un compte

1. Accédez à la page d'accueil de l'application
2. Cliquez sur le lien "Créer un compte"
3. Remplissez le formulaire avec vos informations
4. Cliquez sur "S'inscrire"


### Connexion

1. Accédez à la page d'accueil de l'application
2. Entrez votre nom d'utilisateur et mot de passe
3. Cliquez sur "Login"


### Gestion du profil

1. Après la connexion, vous serez redirigé vers le tableau de bord
2. Vos informations actuelles sont affichées dans un tableau
3. Pour modifier vos informations, cliquez sur le bouton "Modifier"
4. Mettez à jour vos informations et cliquez sur "Enregistrer"


### Déconnexion

- Cliquez sur le bouton "Déconnexion" dans la barre de navigation