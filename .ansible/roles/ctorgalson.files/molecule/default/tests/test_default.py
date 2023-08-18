import os

import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_directory_mode(host):
    f = host.file('/home/lorem')

    assert f.is_directory
    assert oct(f.mode) == '0700'


@pytest.mark.parametrize("path", [
    "/home/lorem/foo",
    "/home/lorem/foo/bar",
])
def test_directory_recursion(host, path):
    f = host.file(path)

    assert f.exists
    assert f.is_directory
    assert f.user == 'lorem'
    assert f.group == 'lorem'
    assert oct(f.mode) == '0750'


def test_touch(host):
    f = host.file('/home/lorem/baz')

    assert f.exists
    assert f.is_file
    assert f.user == 'lorem'
    assert f.group == 'lorem'


def test_file(host):
    f = host.file('/home/lorem/.bashrc')

    assert oct(f.mode) == '0644'


def test_file_absent(host):
    f = host.file('/home/lorem/DELETE')

    assert not f.exists


def test_link(host):
    f = host.file('/home/lorem/foobar')

    assert f.is_symlink


def test_link_force(host):
    f = host.file('/home/lorem/fubar-link')

    assert f.is_symlink
    assert f.linked_to == '/home/lorem/foo/bar'
