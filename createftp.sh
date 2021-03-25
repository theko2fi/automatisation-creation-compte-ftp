#!/bin/sh

/bin/echo "Welcome!
Your choices are:
1       create ftp account
2       delete ftp account
3       update ftp account
q       Quit"

/bin/echo "Your choice:"
read ans

while [ "$ans" != "q" ]; do
   case "$ans" in
      1)
	 echo "Enter the username and press [ENTER]: "
	 read username
	 echo "Enter the password and press [ENTER]: "
	 read password
	 sudo /usr/bin/local/createftpaccount.sh $username $password
         /bin/echo "account created successfully"
         exit 0
         ;;
      2)
         echo "username:"
         read usernamedel
         sudo /usr/bin/local/deleteftpaccount.sh $usernamedel
         exit 0
         ;;
      3)
         echo "username:"
         read usernameupd
         echo "new password:"
         read newpassword
         sudo /usr/bin/local/updateftpaccount.sh $usernameupd $newpassword
         exit 0
         ;;
      q)
         /bin/echo "Goodbye"
         exit 0
         ;;
      *)
         /bin/echo "Invalid choice '$ans': please try again"
         ;;
   esac

done
exit 0
