# Assethbox

### What is Assethbox ?
Assethbox is a 64bits virtual machine provided by Asseth non-profit organization.

### What is included ?

**Ethereum tools**

* geth
* mist
* parity
* testrpc
* populus
* truffle
* embark
* dapple
<br/>

**Decentralized stuff**

* IPFS
<br/>

**Editors with solidity syntax**

* vim with solidity syntax
* sublime-text-3
<br/>

**Useful common tools for developers**

* versioning : git, tig
* monitoring : htop
* shell : zsh with oh-my-zsh
* terminal : terminator with plugins (git, virtualenv, virtualenvwrapper, ssh)
* python : v2.7, v3.5, headers provided by python-dev
* chat : slack
* web : curl, wget, firefox, chromium
* crypto : openssl
* nodejs: node, npm
<br/>

**Projects**

* all asseth's github projects are cloned in /home/vagrant/projects
<br/>

## Use pre-built ova file

### Get the image

Download the .ova file  [here](https://drive.google.com/open?id=0B8rZeDVmrvHGcEtMLTVIT0RWTzA) or [here](https://mega.nz/#!grZlVRTB!p_u5OcE1iFY0XJtYbrS7xqlnIZftYdkD0tr7epCDSYg) and import it in virtualbox
Import it in virtualbox ('File/Import...'), or just double-click on it and follow the instructions

### Checksum

    MD5
    969817f1554c1ddae2a6c4082702220c  assethbox_0.7.3.ova
    SHA1
    3c41c076c3dce3dcc1b8ccede47a897dc8ef5365  assethbox_0.7.3.ova
    SHA256
    0b51762e0b8cb225fd01204f0ab85f3829385eb428fc48bf52cfbcdaca8e83d7  assethbox_0.7.3.ova

### Login

user: vagrant
password: vagrant
<br/>

## Build from sources

    git clone https://github.com/asseth/assethbox.git
    cd assethbox
    vagrant up && vagrant ssh

To trash the VM, from your host, in the assethbox folder:

    vagrant halt && vagrant destroy
    rm -rf .vagrant
<br/>

## Generate .ova file from build

    vagrant up
    vagrant halt
    vboxmanage export asseth -o assethbox_YOUR_VERSION.ova
<br/>

## Note for Mac Users**

* The Mac keyboard configuration is available either :
    - by editing the file provisioning/roles/devtools/templates/zshrc.j2 before building from sources (see the 3 last lines)
    - by editing the file /home/vagrant/.zshrc on the VM (see the 3 last lines)
