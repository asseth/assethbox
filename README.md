Assethbox is a virtual machine provided by Asseth non-profit organization.

## Launch the VM

    git clone https://github.com/asseth/assethbox.git
    cd assethbox
    vagrant up && vagrant ssh

## Trash the VM

From your host, in the assethbox folder:

    vagrant halt && vagrant destroy
    rm -rf .vagrant
