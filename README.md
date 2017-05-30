Assethbox is a 64bits virtual machine provided by Asseth non-profit organization.

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
* sublime-text-3 with following packages :
  - "Ethereum" _solidity syntax_
  - "GitSavvy" _git and GitHub integration_
  - "Pretty JSON" _JSON plugin_
  - "Markdown Preview" _Markdown2html generator_
  - "MarkdownEditing" _Markdown syntax_

  **NB** : restart sublime Text at first use to complete the packages activation via Package Control.

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

**Projects**

* all asseth's github projects are cloned in /home/vagrant/projects

**Note for Mac Users**

* The Mac keyboard configuration is available either :
    - by editing the file provisioning/roles/devtools/templates/zshrc.j2 before building from sources (see the 3 last lines)
    - by editing the file /home/vagrant/.zshrc on the VM (see the 3 last lines)

## Simplest install

### Get the image

Download the .ova file  [here](https://1drv.ms/u/s!AFs1s-upPTKViis) and import it in virtualbox
Import it in virtualbox ('File/Import...')

### Checksum

    MD5
    a2f4855e8bc68e2a15c39f0a2b531bb4  assethbox_v0.7.2.ova
    SHA1
    b5cff27ed48394195ecee8ccb1f36909f066b68f  assethbox_v0.7.2.ova
    SHA256
    288d8f47457baedb1fa6549baece77c516b1ce657b12684417b7840be833b239  assethbox_v0.7.2.ova


### Login

user: vagrant
password: vagrant

## Build from sources

    git clone https://github.com/asseth/assethbox.git
    cd assethbox
    vagrant up && vagrant ssh

To trash the VM, from your host, in the assethbox folder:

    vagrant halt && vagrant destroy
    rm -rf .vagrant

## Generate .ova file from build

    vagrant up
    vagrant halt
    vboxmanage export asseth -o assethbox_YOUR_VERSION.ova
