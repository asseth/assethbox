# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/trusty64"
  config.vm.hostname = "asseth"

  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = "1024"
    vb.name = "asseth"
  end

  config.vm.network "forwarded_port", guest: 30303, host: 30303
  config.vm.network "forwarded_port", guest: 8545, host: 8545

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    sudo apt-get install -y cowsay ansible sshpass
    su - vagrant -c 'ssh-keygen -t rsa -f "$HOME/.ssh/id_rsa" -q -N ""'
    su - vagrant -c 'cat /home/vagrant/.ssh/id_rsa.pub >> /home/vagrant/.ssh/authorized_keys'
    su - vagrant -c 'echo StrictHostKeyChecking no >> /home/vagrant/.ssh/config'
    sudo service ssh restart
    su - vagrant -c 'sshpass -p vagrant ssh-copy-id vagrant@asseth'
    su - vagrant -c 'ansible-playbook /vagrant/provisioning/bootstrap.yml -i /vagrant/provisioning/hosts -vvvv'
  SHELL
end
