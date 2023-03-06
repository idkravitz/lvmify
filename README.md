# Ansible Collection - idkravitz.lvmify

Documentation for the collection. The gods have spoken that one day the lazy dev will write it.

Currently you can use it in your playbooks like this:

```
- name: Perform lvmification of hosts
  hosts: lvmify
  roles:
    - idkravitz.lvmify.lvmify
```

Controlling vars are:

```
root_partition: Root partition of instance (/dev/sda)
volume_drive: Drive of the attached volume (/dev/sdb)
```