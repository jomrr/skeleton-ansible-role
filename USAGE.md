# ansible-skeleton

Skeleton for use with ansible-galaxy to create a new role.

## Requirements
===

Ansible 2.5 or higher is required.

To use the predefined tests you need to have the following packages installed:

* qemu
* virt-manager
* molecule
* molecule[vagrant]
* molecule[libvirt]
* [vagrant](http://vagrantup.com)
* vagrant-libvirt

To install os specific requirements please search the internet.

For molecule do the following:

```shell
pip install --user 'molecule'
pip install --user 'molecule[vagrant]'
pip install --user 'molecule[libvirt]'
```

For the vagrant-libvirt plugin you need the libvirt-dev package of your os installed.

Then you can install the plugin by issuing:

```shell
vagrant plugin install vagrant-libvirt
```

## Usage
===

To create a new ansible role with this skeleton, do the following:

```shell
git clone https://github.com/jam82/ansible-skeleton.git
ansible-galaxy --role-skeleton=ansible-skeleton ansible-role-<rolename>
```

## License and Author
===

- Author:: Jonas Mauer (<jam@kabelmail.net>)
- Copyright:: 2019, Jonas Mauer

Licensed under MIT License;
See LICENSE file in repository.
