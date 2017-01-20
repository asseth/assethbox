Assethbox is a virtual machine provided by Asseth non-profit organization.

Inside the VM (Non-exhaustive):

**Ethereum**

* geth
* mist
* parity
* testrpc
* populus
* truffle
* embark
* dapple

**Decentralized stuff**

* IPFS

**Editors**

* vim with solidity syntax
* sublime-text-3 with solidity syntax

**Useful common tools for developers**

* versioning : git, tig
* monitoring : htop
* shell : zsh with oh-my-zsh
* terminal : terminator with plugins (git, virtualenv, virtualenvwrapper, ssh)
* python : v2.7, v3.5, headers provided by python-dev
* chat : slack
* web : curl, wget, firefox
* crypto : openssl
* nodejs: node, npm

**Projects**

* all asseth's github projects are cloned in /home/vagrant/projects

**Note for Mac Users**

* The Mac keyboard configuration is available either :
    - by editing the file provisioning/roles/devtools/templates/zshrc.j2 before building from sources (see the 3 last lines)
    - by editing the file /home/vagrant/.zshrc on the VM (see the 3 last lines)

## Simplest install

### Get the image

Download the .ova file  [here](https://s3-eu-west-1.amazonaws.com/asseth/assethbox/assethbox_0.6.0.ova) and import it in virtualbox
Import it in virtualbox ('File/Import...')

### Login

user: vagrant
password: vagrant

### Signatures

    MD5 31afde6c48f9f8b0deb99e7920e7e0d8  assethbox_0.6.1.ova
    SHA1 ee5c11c08b93781990df086caceede32d8a65de1  assethbox_0.6.1.ova
    SHA256 b2e2f57ccb71a2791bb331080b42a17474ab905e22122ce4aad393a0d3d8b54c  assethbox_0.6.1.ova

## Build from sources

    git clone https://github.com/asseth/assethbox.git
    cd assethbox
    vagrant up && vagrant ssh

To trash the VM, from your host, in the assethbox folder:

    vagrant halt && vagrant destroy
    rm -rf .vagrant

## Generate .ova file from build

    vboxmanage export asseth -o assethbox_YOUR_VERSION.ova
