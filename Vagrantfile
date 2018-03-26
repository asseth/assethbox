# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/xenial64"
  config.vm.hostname = "asseth"

  config.vm.provider "virtualbox" do |vb|
    vb.gui = true
    vb.memory = "4096"
    vb.name = "asseth"
    vb.cpus = 2
    vb.customize ["modifyvm", :id, "--vram", "128"] # video memory
  end

  config.vm.synced_folder ".", "/vagrant", type: "rsync"

  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-add-repository ppa:ansible/ansible
    sudo apt-get -y update
    sudo apt-get install -y xubuntu-desktop virtualbox-guest-x11 virtualbox-guest-dkms software-properties-common cowsay sshpass language-pack-fr python-pip ansible
    sudo pip install --upgrade pip
    sudo pip install markupsafe
    sudo apt-get install -y python3-pip
    #sudo pip3 install --upgrade pip
    su - vagrant -c 'ssh-keygen -t rsa -f "$HOME/.ssh/id_rsa" -q -N ""'
    su - vagrant -c 'cat /home/vagrant/.ssh/id_rsa.pub >> /home/vagrant/.ssh/authorized_keys'
    su - vagrant -c 'echo StrictHostKeyChecking no >> /home/vagrant/.ssh/config'
    sudo service ssh restart
    su - vagrant -c 'sshpass -p vagrant ssh-copy-id vagrant@asseth'
    su - vagrant -c 'ansible-playbook /vagrant/provisioning/bootstrap.yml -i /vagrant/provisioning/hosts -vvvv'
    sudo reboot
  SHELL

end
