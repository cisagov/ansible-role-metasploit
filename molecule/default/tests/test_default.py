"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_installer_deleted(host):
    """Test that the Metasploit Framework installer was removed."""
    path = "/tmp/msfinstall"
    f = host.file(path)
    assert not f.exists


def test_msf_installed(host):
    """Test that the Metasploit Framework was installed."""
    dir_full_path = "/opt/metasploit-framework/"
    directory = host.file(dir_full_path)
    assert directory.exists
    assert directory.is_directory
    # Assert directory is non-empty
    assert host.run_expect([0], f'[ -n "$(ls --almost-all {dir_full_path})" ]')
