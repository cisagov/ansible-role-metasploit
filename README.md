# ansible-role-metasploit #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-metasploit/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-metasploit/actions)
[![CodeQL](https://github.com/cisagov/ansible-role-metasploit/workflows/CodeQL/badge.svg)](https://github.com/cisagov/ansible-role-metasploit/actions/workflows/codeql-analysis.yml)

This Ansible role downloads and installs the
[Metasploit penetration testing framework](https://www.metasploit.com).

## Requirements ##

None.

## Role Variables ##

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| metasploit_installer_version | A git commit hash, tag, or branch specifying the version of the Metasploit Framework installer to use. | `6.2.20` | No |

## Dependencies ##

None.

## Installation ##

This role can be installed via the command:

```console
ansible-galaxy ansible-galaxy install --role-file path/to/requirements.yml
```

where `requirements.yml` looks like:

```yaml
---
- name: skeleton
  src: https://github.com/cisagov/skeleton-ansible-role
```

and may contain other roles as well.

For more information about installing Ansible roles via a YAML file,
please see [the `ansible-galaxy`
documentation](https://docs.ansible.com/ansible/latest/galaxy/user_guide.html#installing-multiple-roles-from-a-file).

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: true
  become_method: sudo
  tasks:
    - name: Install the Metasploit Framework
      ansible.builtin.include_role:
        name: metasploit
```

## Contributing ##

We welcome contributions!  Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.

## Author Information ##

Alexander King - <alexander.king@gwe.cisa.dhs.gov>

I would be remiss to not mention [Liam Somerville](https://github.com/leesoh)
here. This role is largely based on their prior work.

The [Metasploit Framework](https://github.com/rapid7/metasploit-framework) is a
project of [Rapid7](https://www.rapid7.com/) in collaboration with the open
source community.
