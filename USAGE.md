# ansible-role-skeleton

Skeleton for use with ansible-galaxy to create a new ansible role.

## Requirements

Ansible 2.8 or higher is required.

For running the default tests with molecule docker you need the following packages installed:

* docker

To use the predefined tests with kvm/libvirt you need to have the following packages installed:

* qemu
* virt-manager
* [vagrant](http://vagrantup.com)
* vagrant-libvirt

Your user needs to be in the `libvirt` system group, because the qemu system domain is used.

To install os specific requirements please search the internet.

For molecule do the following:

```shell
pip install --user molecule molecule-vagrant testinfra flake8
```

For the vagrant-libvirt plugin you need the libvirt-dev package of your os installed.

Then you can install the plugin by issuing:

```shell
vagrant plugin install vagrant-libvirt
```

## Usage

To create a new ansible role with this skeleton, do the following:

```shell
git clone https://github.com/jam82/ansible-role-skeleton.git
ansible-galaxy init --role-skeleton=ansible-role-skeleton ansible-role-<rolename>
```

## License and Author

* Author:: Jonas Mauer (<jam@kabelmail.net>)
* Copyright:: 2019, Jonas Mauer

Licensed under MIT License;
See LICENSE file in repository.
