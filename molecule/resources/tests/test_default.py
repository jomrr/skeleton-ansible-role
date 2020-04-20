import os

import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.fixture
def get_vars(host):
    ansible_facts = host.ansible("setup")
    ansible_dist = ansible_facts["ansible_facts"]["ansible_distribution"]

    defaults_files = "file=../../defaults/main.yml"
    playbook_vars = "file=../resources/playbooks/vars.yml"
    vars_files = "file=../../vars/" + ansible_dist + ".yml"

    ansible_vars = host.ansible(
        "include_vars", defaults_files)["ansible_facts"]

    ansible_vars.update(host.ansible(
        "include_vars", playbook_vars)["ansible_facts"])

    ansible_vars.update(host.ansible(
        "include_vars", vars_files)["ansible_facts"])

    return ansible_vars


def test_common(host, get_vars):
    assert get_vars['common_role_enabled'] is True


def test_system_info(host):
    os = host.system_info.distribution

    if os == 'alpine':
        assert host.file("/etc/os-release").contains("Alpine")

    elif os == 'arch':
        assert host.file("/etc/os-release").contains("Arch Linux")

    elif os == 'centos':
        assert host.file("/etc/os-release").contains("CentOS")

    elif os == 'debian':
        assert host.file("/etc/os-release").contains("Debian")

    elif os == 'manjaro':
        assert host.file("/etc/os-release").contains("Manjaro")

    elif os == 'oracle':
        assert host.file("/etc/os-release").contains("Oracle")

    elif os == 'ubuntu':
        assert host.file("/etc/os-release").contains("Ubuntu")
