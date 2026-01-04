"""Tests for restore_ip_addresses problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


def is_valid_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part:
            return False
        if len(part) > 1 and part[0] == '0':
            return False
        if not part.isdigit() or int(part) > 255:
            return False
    return True


@pytest.fixture
def restore_ip_addresses():
    func = get_function("restore_ip_addresses")
    if func is None:
        pytest.skip("Function 'restore_ip_addresses' not registered.")
    return func


class TestRestoreIPAddressesBasic:
    def test_example_1(self, restore_ip_addresses):
        result = restore_ip_addresses("25525511135")
        expected = ["255.255.11.135", "255.255.111.35"]
        assert sorted(result) == sorted(expected)

    def test_example_2(self, restore_ip_addresses):
        result = restore_ip_addresses("0000")
        assert result == ["0.0.0.0"]

    def test_example_3(self, restore_ip_addresses):
        result = restore_ip_addresses("101023")
        for ip in result:
            assert is_valid_ip(ip)


class TestRestoreIPAddressesEdgeCases:
    def test_too_short(self, restore_ip_addresses):
        result = restore_ip_addresses("123")
        assert result == []

    def test_too_long(self, restore_ip_addresses):
        result = restore_ip_addresses("1234567890123")
        assert result == []

    def test_leading_zeros(self, restore_ip_addresses):
        result = restore_ip_addresses("010010")
        # Should not have segments like "01" or "001"
        for ip in result:
            assert is_valid_ip(ip)
