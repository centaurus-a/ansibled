#testserver ansible_ssh_host=127.0.0.1 ansible_ssh_port=22 ansible_ssh_user=vagrant ansible_ssh_pass=123456
controld ansible_ssh_host=127.0.0.1 ansible_ssh_port=22 ansible_ssh_user=vagrant ansible_ssh_private_key_file=~/.ssh/id_rsa
vagrant1 ansible_ssh_host=192.168.56.11 ansible_ssh_port=22 ansible_ssh_user=vagrant
vagrant2 ansible_ssh_host=192.168.56.12 ansible_ssh_port=22 ansible_ssh_user=vagrant
vagrant3 ansible_ssh_host=192.168.56.13 ansible_ssh_port=22 ansible_ssh_user=vagrant

[webservers]
controld ansible_ssh_host=127.0.0.1 ansible_ssh_port=22

[vagrant]
vagrant1
vagrant2
vagrant3

[web]
vagrant1

[task]
vagrant2

[db]
vagrant3

[django:children]
web
task

