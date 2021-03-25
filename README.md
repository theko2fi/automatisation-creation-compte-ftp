# automatisation-creation-compte-ftp
automatise la creation et la suppression de compte sftp sur un serveur linux (centos) via un script python pour être intégrer dans une appli web (Flask)


Etapes à suivre:

sudo adduser <username>
usermod -aG wheel <username>

sudo nano <my script>
sudo chown root:root <my script>
sudo chmod 4755 <my script>

Dans le fichier /etc/passwd changez le shell de l'utilisateur <username>


Add these two lines at the end of your sudoers file. You can use nano to edit the sudoers file:(A faire pour tous les scripts)
	Cmnd_Alias        CMDS = /path/to/your/script
	<username>  ALL=NOPASSWD: CMDS

Important: Toujours vérifier que le nom d'utilisateur n'est pas vide sinon le service ssh arrêtera de fonctionner

Références:

https://ctrlnotes.com/restrict-a-user-to-ssh-forced-command/#
https://askubuntu.com/questions/167847/how-to-run-bash-script-as-root-with-no-password
