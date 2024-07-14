# skeleton-ansible-role

![GitHub](https://img.shields.io/github/license/jomrr/skeleton-ansible-role) ![GitHub last commit](https://img.shields.io/github/last-commit/jomrr/skeleton-ansible-role) ![GitHub issues](https://img.shields.io/github/issues-raw/jomrr/skeleton-ansible-role) ![Travis (.com) branch](https://img.shields.io/travis/com/jomrr/skeleton-ansible-role/main?label=build)

**[Molecule](https://molecule.readthedocs.io/en/latest/)-based role skeleton for use with ansible-galaxy to create a new ansible role.**

> This README does not explain how to use molecule. Please read the [docs](https://ansible.readthedocs.io/projects/molecule/) if you need to.

Table of Contents

- [skeleton-ansible-role](#skeleton-ansible-role)
  - [Features](#features)
  - [Quickstart](#quickstart)
  - [Requirements](#requirements)
    - [Docker Scenario (default)](#docker-scenario-default)
    - [Libvirt Scenario (kvm)](#libvirt-scenario-kvm)
    - [Podman Scenario (podman)](#podman-scenario-podman)
    - [Tox Scenario (tox)](#tox-scenario-tox)
    - [VirtualBox Scenario (vbox)](#virtualbox-scenario-vbox)
  - [Usage](#usage)
  - [Author and License](#author-and-license)

## Features

- include os specific variables
  - first a `vars/{{ansible_os_family}}.yml` is included, automatically created when using this skeleton (e.g. `RedHat.yml` or `Archlinux.yml`)
  - then the first found of the following, if you create them (e.g. `Fedora-31.yml`)
    - `vars/{{ ansible_distribution }}-{{ ansible_distribution_major_version }}.yml`
    - `vars/{{ ansible_distribution }}.yml`
    - `vars/{{ ansible_os_family }}-{{ ansible_distribution_major_version }}.yml`
- install os specific packages
- use predefined containers for testing, see [ansible-molecule-images](https://github.com/jomrr/ansible-molecule-images)
- have a predefined README.md skeleton
- use consistent comments in each `yml`-file

```yaml
---
# role: ansible-role-foreman
# file: defaults/main.yml

# Default variables for foreman

```

**Listing 1:** Code Example of a newly generated role skeleton for `ansible-role-foreman`

## Quickstart

```shell
git clone https://github.com/jomrr/skeleton-ansible-role
ansible-galaxy role init --role-skeleton=./skeleton-ansible-role <rolename>
```

For a more convenient way see [Usage](#usage).

## Requirements

For all scenarios the following is required

- python3 (install via your os package manager)
- [Ansible 2.17 or higher](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)

```shell
pipx install ansible
```

Then you can install the required python3 modules for all scenarios as an unprivileged user with the folliwing command:

```shell
pipx inject --indlcude-deps ansible ansible-lint molecule molecule-plugins[podman] molecule-plugins[vagrant] jmespath keyring
```

### Podman Scenario (default)

For running the default tests with molecule podman you just need to [install podman](https://podman.io/docs/installation).

### Libvirt Scenario (kvm)

To use the predefined tests with vagrant libvirt you need to have the following packages installed:

- qemu
- virt-manager
- libvirt-dev(el) package, dependnt on your os
- [vagrant](http://vagrantup.com)

Your user needs to be in the `libvirt` or `libvirtd` system group depending on your distribution, because the qemu system domain is used.

After [installing vagrant](https://www.vagrantup.com/downloads.html) you need the [`vagrant-libvirt` plugin](https://github.com/vagrant-libvirt/vagrant-libvirt).

You can install it with:

```shell
vagrant plugin install vagrant-libvirt
```

### Podman Scenario (podman)

[Podman](https://podman.io) should work out of the box, after it is installed.

To install it, see the [official instructions](https://podman.io/getting-started/installation.html) or you can also use my [ansible-role-podman](https://github.com/jomrr/ansible-role-podman).

## Usage

To create a new ansible role with this skeleton, do the following:

```shell
git clone https://github.com/jomrr/skeleton-ansible-role.git
ansible-galaxy role init --role-skeleton=./skeleton-ansible-role <rolename>
```

If you want to use it in a more convenient way, create a custom function e.g. in ~/.bashrc

```shell
# ansible-galaxy init with custom role-skeleton
ag-role() {
    if [ -z "$1" ]; then
        echo "Please specify a role name that will be appended to <rolename>"
        return 1
    fi
    ansible-galaxy role init --role-skeleton=${2:-'./skeleton-ansible-role'} $1
}
```

Then you are able to issue for example

```shell
ag-role dhcpd
```

to create a role skeleton for ansible-role-dhcpd.

## Author(s) and License

- :octocat:                 Author::    [jomrr](https://github.com/jomrr)
- :triangular_flag_on_post: Copyright:: 2020, Jonas Mauer
- :page_with_curl:          License::   [MIT](LICENSE)

Licensed under [MIT License](http://opensource.org/licenses/mit-license.php).
See [LICENSE](https://github.com/jomrr/skeleton-ansible-role/blob/main/LICENSE) file in repository.
