"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_msf_installed(host):
    """Test that the Metasploit framework installer was installed."""
    full_path = "/tmp/msfinstall"
    file = host.file(full_path)
    assert file.exists
