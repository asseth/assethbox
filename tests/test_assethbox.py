# py.test -v test_myinfra.py

def test_geth_is_installed(host):
    geth = host.package("geth")
    assert geth.is_installed

# Fail because of snap ?
# def test_parity_is_installed(host):
#     parity = host.package("parity")
#     assert parity.is_installed
