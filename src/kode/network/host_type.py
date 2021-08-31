"""
Determine given host type.

Hosts can be of the following types:
- ipv4
- ipv6
- hostname (which can also be a FQDN)
"""

from ipaddress import ip_address, IPv4Address, IPv6Address
from publicsuffix2 import get_sld


def get_target_type(host):
    """Return given host's type (ipv4, ipv6 or hostname)."""
    try:
        r = ip_address(host)
        if isinstance(r, IPv4Address):
            return "ipv4"
        elif isinstance(r, IPv6Address):
            return "ipv6"
    except ValueError:
        return "hostname"

    return None


def get_target_type_and_subtype(target: str) -> tuple:
    """
    Return 2 item tuple containing target type (`ip` or `domain`) and
    subtype (`ipv4`, `ipv6`, `naked_domain`, `subdomain` )
    """
    tt = None
    st = None
    try:
        ip = ip_address(target)
        tt = "ip"
        if isinstance(ip, IPv4Address):
            st = "ipv4"
        elif isinstance(ip, IPv6Address):
            st = "ipv6"

    except ValueError:
        tt = "domain"
        if target == get_sld(target):
            st = "naked_domain"
        else:
            st = "subdomain"

    return (tt, st)
