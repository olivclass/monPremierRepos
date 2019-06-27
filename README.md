# Description:
Projet de sauvegarde d'un site web fonctionnant avec Apache et du CMS Wordpress:
- le script va sauvegarder la base de données MYSQL ainsi que le contenu du site web dans le dossier /var/www et exporté les sauvegardes sur un serveur distant.

# Configuration:
Pour ce projet voici ma configuration:
 - un serveur web sous Debian, avec rsync, openssh-server, apache2, wordpress, mysql-server.
 - un serveur de sauvegarde sous Debian, avec rsync, openssh-server.

# Création:
Ce script a été crée et testé en Juin 2019, sur une machine linux "Debian" version 9 et de python version 2.7.13.

# Prérequis:
- Télécharger le script "save.py"
- Il est nécessaire de disposer des paquets "rsync" et "openssh-server" sur les machines locale et distante. Si nécessaire vous devez l'installer: apt-get install rsync openssh-server.
- Les machines locale et distante doivent communiquer entre elles.
- Disposer des droits superutilisateurs ( soit avec sudo ou le compte "root")

# Utilisation:
- Vous devez renseigner les variables du serveur web à sauvegarder, en remplacant les "*****" par le nom et le chemin de:
  - Des dossiers du site web,
  - Le nom de la base de données Mysql,
  - Le nom de l'utilisateur Mysql et son mot de passe.

 
- Vous devez également renseigner les variables du serveur distant, servant de sauvegarde:
   - le nom de la machine distante (hostname)
   - le chemin et le nom du dossier de sauvegarde
   - Le nom de l'utilisateur du système.
 
 Lors de l'exécution du script, le mot de passe de la session de l'utilisateur vous sera demandé pour la connexion ssh. Dans mon cas j'ai opté pour la création d'un certificat SSH (ssh keygen + ssh-copy-id) pour ne pas avoir à renseigner de mot de passe.
Ci-dessous les variables précédemment citées avec un exemple:

        'folder_wordpress' : '/var/www/',      #name of the directory containing the website on the local server
        'folder_backup' : '/tmp/backup',       #name of the directory which use for the backup 
        'wp_mysql_db' : 'wordpress',           #name of the mysql database
        'wp_mysql_user' : 'wordpressuser',     #name of the mysql database user
        'wp_mysql_password' : 'sysadmin',      #password of the user account of the mysql database


#backup server's variables

        'folder_ansible' : '/etc/ansible/roles/files/', #remote server backup directory
        'server' : 'REMOTE',                            #Name of the remote machine for backup
        'user' : 'root',                                #Username of the remote server account for the ssh connection
        
Les fichiers "*.tar" (sauvegarde des fichiers du site web) et "*.sql" (sauvegarde de la base de données mysql) seront datés de la date du jour de l'exécution du script.

# Pour les contributeurs:

Les variables des serveurs local et distant sont regroupées pour chaque serveur afin d'apporter de la lisibilité et d'éviter les erreurs d'affectation.
Exemple:
Déclaration de la variable:
  REMOTE = {
              'folder_ansible' : '*****'

Utilisation de la variable:
 '+REMOTE['folder_ansible']
        
# Les étapes du script en détail:
 - importation des modules:
   - subprocess,
   - os,
   - datetime,
   - time,
   - shutil
 
 - Affectation de la date à une variable
 
 - Affectation des configurations des serveurs aux variables
 
 - Création du répertoire de sauvegarde temporaire sur le serveur web, s'il n'existe pas

 - Sauvegarde de la base de données Mysql
 
 - Sauvegarde du dossier du site web (ici j'utilise apache donc le dossier est situé dans /var/www) sous la forme d'une archive TAR
 
 - Copie des sauvegardes dans le dossier de destination du serveur distant ( j'ai utilisé les paramètres -hP pour afficher la progression et les tailles des fichiers en Ko,Mo)
 
 - Suppression du dossier temporaire de sauvegarde sur le serveur local
        
# LICENCE
"This project is licensed under the terms of the GPLv3 license."

   
        
        

