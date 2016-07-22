Assethbox is a virtual machine provided by Asseth non-profit organization.

In the VM:

**Ethereum**

* geth
* mist

**Editors**

* vim with solidity syntax
* sublime-text-3 with solidity syntax

**Useful common tools for developers**

## Simple install

    vagrant init asseth/assethbox; vagrant up --provider virtualbox

## Build from sources

    git clone https://github.com/asseth/assethbox.git
    cd assethbox
    vagrant up && vagrant ssh

To trash the VM, from your host, in the assethbox folder:

    vagrant halt && vagrant destroy
    rm -rf .vagrant
