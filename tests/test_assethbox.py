# py.test -v test_myinfra.py

def test_geth_is_installed(host):
    geth = host.package("geth")
    assert geth.is_installed
