# ansible-role-metasploit #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-metasploit/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-metasploit/actions)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/cisagov/ansible-role-metasploit.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/cisagov/ansible-role-metasploit/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/cisagov/ansible-role-metasploit.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/cisagov/ansible-role-metasploit/context:python)

This Ansible role downloads and installs the
[Metasploit penetration testing framework](https://www.metasploit.com).

## Requirements ##

None.

## Role Variables ##

None.

<!--
| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| optional_variable | Describe its purpose. | `default_value` | No |
| required_variable | Describe its purpose. | n/a | Yes |
-->

## Dependencies ##

None.

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: yes
  become_method: sudo
  roles:
    - metasploit
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

Alexander King - <alexander.king@trio.dhs.gov>

I would be remiss to not mention [Liam Somerville](https://github.com/leesoh)
here. This role is largely based on their prior work.

[Metasploit](https://github.com/rapid7/metasploit-framework) is a project of
[Rapid7](https://www.rapid7.com/) in collaboration with the open source
community.
