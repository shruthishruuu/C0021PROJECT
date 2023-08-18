import os

import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("path,user,group,mode", [
    ("/etc/ssl/certs", "root", "root", "755"),
    ("/etc/ssl/private", "root", "root", "700"),
    ("/etc/ssl/certs/www.example.com.key", "root", "root", "600"),
    ("/etc/ssl/certs/www.example.com.crt", "root", "root", "644"),
    ("/etc/ssl/self/certs", "root", "root", "755"),
    ("/etc/ssl/self/private", "root", "root", "755"),
    ("/etc/ssl/self/certs/www.example.com-key.pem", "root", "root", "600"),
    ("/etc/ssl/self/certs/www.example.com-crt.pem", "root", "root", "644"),
    ("/etc/ssl/self/private/www.example.com.csr", "root", "root", "644"),
])
def test_ssl_files_and_directories(host, path, user, group, mode):
    f = host.file(path)

    assert f.exists
    assert f.user == user
    assert f.group == group
    """ Using `in` instead of `==` to permit testing with Python 2 or 3. """
    assert mode in oct(f.mode)
