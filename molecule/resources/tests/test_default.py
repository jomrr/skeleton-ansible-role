import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


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
