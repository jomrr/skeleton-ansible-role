#####################
ansible-role-skeleton
#####################

Ok, lets call githubs rst rendering features somewhat "reduced".
I will rewrite this to markdown after work today...

`Molecule <https://molecule.readthedocs.io/en/latest/>`_-based role skeleton for use with ansible-galaxy to create a new ansible role.

************
Requirements
************

For all scenarios the following is required

* python3 (install via your os package manager)
* `Ansible 2.8 or higher <https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html>`_

Then you can install the required python3 modules for all scenarios as an unprivileged user with the folliwing command:

.. code-block:: shell

   pip3 install --user ansible-lint docker flake8 molecule molecule-vagrant testinfra yamllint

Docker Scenario (default)
=========================

For running the default tests with molecule docker you just need to `install docker <https://docs.docker.com/engine/install/>`_.

Docker offers a convenient script for installation on linux systems.
To install the repositories, get the latest version installed and adding your user to the docker group,
just run the following commands:

.. warning:: Check the script before you run it and use on your own risk.

.. code-block:: shell

    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker <your-username>

.. warning:: Adding an unprivileged user to the docker group can be a security risk. If you want to avoid that risk, see `Rootless-mode <https://docs.docker.com/engine/security/rootless/>`_.

.. note:: The script is an official script provided by docker and to use docker as an unprivileged user, you have to add your user to the docker group.

Libvirt Scenario (kvm)
======================

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

Podman Scenario (podman)
========================

VirtualBox Scenario (vbox)

Usage
-----

To create a new ansible role with this skeleton, do the following:

```shell
git clone https://github.com/jam82/ansible-role-skeleton.git
ansible-galaxy init --role-skeleton=ansible-role-skeleton ansible-role-<rolename>
```

Authors
-------

License
-------

* Author:: Jonas Mauer (<jam@kabelmail.net>)
* Copyright:: 2019, Jonas Mauer

Licensed under MIT License;
See LICENSE file in repository.
