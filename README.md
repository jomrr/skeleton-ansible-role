# ansible-role-skeleton

![GitHub](https://img.shields.io/github/license/jam82/ansible-role-skeleton) [![Build Status](https://travis-ci.org/jam82/ansible-role-skeleton.svg?branch=main)](https://travis-ci.org/jam82/ansible-role-skeleton)

**[Molecule](https://molecule.readthedocs.io/en/latest/)-based role skeleton for use with ansible-galaxy to create a new ansible role.**

> This README does not explain how to use molecule. Please read the [docs](https://molecule.readthedocs.io/en/latest/) if you need to.

Table of Contents

- [ansible-role-skeleton](#ansible-role-skeleton)
  - [Features](#features)
  - [Quickstart](#quickstart)
  - [Requirements](#requirements)
    - [Docker Scenario (default)](#docker-scenario-default)
    - [Libvirt Scenario (kvm)](#libvirt-scenario-kvm)
    - [Podman Scenario (podman)](#podman-scenario-podman)
    - [VirtualBox Scenario (vbox)](#virtualbox-scenario-vbox)
  - [Usage](#usage)
  - [Author and License](#author-and-license)

## Features

- (de)activate your role via an `{{role_name}}_role_enabled`-variable, see `defaults/main.yml`
- include os specific variables
  - first a `vars/{{ansible_os_family}}.yml` is included, automatically created when using this skeleton (e.g. `RedHat.yml` or `Archlinux.yml`)
  - then the first found of the following, if you create them (e.g. `Fedora-31.yml`)
    - `vars/{{ ansible_distribution }}-{{ ansible_distribution_major_version }}.yml`
    - `vars/{{ ansible_distribution }}.yml`
    - `vars/{{ ansible_os_family }}-{{ ansible_distribution_major_version }}.yml`
- install os specific packages
- use a predefined travis file
- use predefined containers for testing, see [buildah-molecule-images](https://github.com/jam82/buildah-molecule-images)
- have a predefined README.md skeleton
- use consistent comments in each `yml`-file

```yaml
---
# role: ansible-role-foreman
# file: defaults/main.yml

# The role is disabled by default, so you do not get in trouble.
# Checked in tasks/main.yml which executes a block if role is enabled.
foreman_role_enabled: false
```

**Listing 1:** Code Example of a newly generated role skeleton for `ansible-role-foreman`

## Quickstart

```shell
git clone https://github.com/jam82/ansible-role-skeleton.git
ansible-galaxy init --role-skeleton=ansible-role-skeleton ansible-role-<rolename>
```

For a more convenient way see [Usage](#usage).

## Requirements

For all scenarios the following is required

- python3 (install via your os package manager)
- [Ansible 2.8 or higher](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)

Then you can install the required python3 modules for all scenarios as an unprivileged user with the folliwing command:

```shell
pip3 install --user ansible-lint docker flake8 molecule molecule-vagrant testinfra yamllint
```

### Docker Scenario (default)

For running the default tests with molecule docker you just need to [install docker](https://docs.docker.com/engine/install/).

Docker offers a convenient script for installation on linux systems.
To install the repositories, get the latest version installed and adding your user to the docker group,
just run the following commands:

> **Warning:** Check the script before you run it and use on your own risk.

```shell
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker <your-username>
```

> **Warning:**
> Adding an unprivileged user to the docker group can be a security risk.
> If you want to avoid that risk, see [Rootless-mode](https://docs.docker.com/engine/security/rootless/)

The script is an official script provided by docker and to use docker as an unprivileged user, you have to add your user to the docker group.

### Libvirt Scenario (kvm)

To use the predefined tests with kvm/libvirt you need to have the following packages installed:

- qemu
- virt-manager
- libvirt-dev package of your os
- [vagrant](http://vagrantup.com)

Your user needs to be in the `libvirt` or `libvirtd` system group depending on your distribution, because the qemu system domain is used.

After [installing vagrant](https://www.vagrantup.com/downloads.html) you need the [`vagrant-libvirt` plugin](https://github.com/vagrant-libvirt/vagrant-libvirt).

You can install it with:

```shell
vagrant plugin install vagrant-libvirt
```

### Podman Scenario (podman)

[Podman](https://podman.io) should work out of the box, after it is installed.

To install it, see the [official instructions](https://podman.io/getting-started/installation.html) or you can also use my [ansible-role-podman](https://github.com/jam82/ansible-role-podman).

### VirtualBox Scenario (vbox)

For using the [VirtualBox](https://virtualbox.org) (vbox) scenario install it on your os along with [`vagrant`](https://www.vagrantup.com/downloads.html) and the [`vagrant-libvirt` plugin](https://github.com/vagrant-libvirt/vagrant-libvirt).

## Usage

To create a new ansible role with this skeleton, do the following:

```shell
git clone https://github.com/jam82/ansible-role-skeleton.git
ansible-galaxy init --role-skeleton=ansible-role-skeleton ansible-role-<rolename>
```

If you want to use it in a more convenient way, create a custom function e.g. in ~/.bashrc

```shell
# ansible-galaxy init with custom role-skeleton
aga-init() {
    if [ -z "$1" ]; then
        echo "Please specify a role name that will be appended to ansible-role-<rolename>"
        return 1
    fi
    ansible-galaxy init --role-skeleton=${2:-'./ansible-role-skeleton'} ansible-role-$1
    rm ./ansible-role-$1/docs/*
}
```

Then you are able to issue for example

```shell
aga-init dhcpd
```

to create a role skeleton for ansible-role-dhcpd.

## Author and License

- Author:: [jam82](https://github.com/jam82/)
- Copyright:: 2020, [jam82](https://github.com/jam82/)

Licensed under [MIT License](http://opensource.org/licenses/mit-license.php).
See [LICENSE](https://github.com/jam82/ansible-role-skeleton/blob/master/LICENSE) file in repository.
