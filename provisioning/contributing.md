Check if everything is up to date

For ethereum softwares, the main part is in provisioning/roles/ethereum/vars/main.yml

geth

On your host clone the go-ethereum repo if you don't have
    git clone https://github.com/ethereum/go-ethereum.git
    git fetch

Pull the last version of the repo if you already have
    git pull

List all the tags
  git tag

Checkout to the tag corresponding to the last geth version (exemple with v1.6.1)
    git checkout v1.6.1

Copy the hash from the checkout output log "HEAD is now on  021c3c2..." : here it's 021c3c2
Change the geth version in provisioning/roles/ethereum/vars/main.yml

    geth_version: 021c3c2 #v1.6.1

Mist

Go to https://github.com/ethereum/mist/releases
Check the last 64bit deb version; for example Mist-linux64-0-8-10.deb

Copy it and paste it in provisioning/roles/ethereum/vars/main.yml :https://github.com/ethereum/mist/releases/download/v0.8.10/Ethereum-Wallet-linux64-0-8-10.deb

    mist_version_deb: Mist-linux64-0-8-10.deb

Right click on the deb link to get the good URL and update mist_version_url with the good version (here 0.8.10)

    mist_version_url_deb: https://github.com/ethereum/mist/releases/download/v0.8.10/{{ mist_version_deb }}

Don't forget the checksum (Mist-linux64-0-8-10.deb: ee718aeb50558c3877466d7649507025)

    mist_version_url_deb_checksum: ee718aeb50558c3877466d7649507025

Parity

Go to https://parity.io/parity.html
Go to the ubuntu download button and get the name of the version and the Checksum

    parity_1.6.6_amd64.deb
    Checksum:
    40d573218449915fb88064d0eb824c3a

In provisioning/roles/ethereum/vars/main.yml, change to the new version (1.6.6 in our example)

    parity_version: 1.6.6
    parity_deb_checksum: parity_deb_checksum


IPFS

On your host clone the go-ipfs repo if you don't have
    git clone https://github.com/ipfs/go-ipfs.git
    git fetch

Pull the last version of the repo if you already have
    git pull

In provisioning/roles/ethereum/vars/main.yml, change to the new version

    go_ipfs_version: v0.4.9-rc2

populus

Search tha latest version with pip (tested with pip 9.0.1):

    pip search populus

And change to the latest version in provisioning/roles/ethereum/vars/main.yml

    populus_version: 1.6.9


Test the virtual machine (manual)

Open virtualbox
Right click on Asseth/Delete/Delete all

Move to the assethbox directory if you're not
    cd assethbox
    vagrant up

node

Go to https://nodejs.org/en/ and check the newest version

In provisioning/roles/devtools/vars/main.yml and replace the old version by the new
    node_version: v7.10.0

Slack

go to https://slack.com/downloads/linux

In provisioning/roles/devtools/vars/main.yml and replace the old version by the new
    slack_version: slack-desktop-2.6.2-amd64.deb



TODO

refactor ansible playbook in a elegant way
shortcuts on ubuntu
add software
tutorials with assethbox
continous integration with Jenkins (building, generating .ova file and testing if possible)
