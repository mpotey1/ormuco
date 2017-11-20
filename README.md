# ormuco

To install this application you need an Ubuntu. Within it, run the following commands:

1) This command will install ansible on your machine. 
   $sudo apt-get install ansible 

2) Now you have to edit ansible's hosts file. To do so, run:
   $ sudo nano /etc/ansible/hosts
   And add this at the bottom (where your_ip is the public ip of your machine):
    [servers]
    your_ip

3) Now run:
   $ sudo apt-get install sshpass

4) So far you have installed everything needed to run ansible. Now, copy and paste the vars.yml and deploy.yml found in this repository at
   /ormuco_challenge/ansible in your machine. Make sure they have the same structure as the one in the repository (sometimes it changes)
   
5) In the vars.yml file, search for:
   # the dns name or names (space separated) for your server
     server_name: #enter server's ip
     replace #enter server's ip with your ip     
   
6) $ ansible all -m ping (here you'll be asked if you want to continue, type yes)

7) $ ansible all -m ping -s -k -u root, here provide your root password when asked.

8) $ ansible-playbook deploy.yml -u root
   Here the playbook run will stop execution at the "script" task which is the one that runs the server.
   
9) Now you're able to go to http://your_ip:8000/ormuco and use the ormuco test app.
