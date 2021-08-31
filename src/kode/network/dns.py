"""DNS related functions"""

import dns.resolver
import dns.rdatatype
import dns.zone
import dns.exception


def resolve(domain_name, query_type):
    "Resolve given query"

    results = []

    try:
        ans = dns.resolver.query(domain_name, query_type)
        for a_res in ans.rrset:
            if query_type == dns.rdatatype.to_text(a_res.rdtype):
                results.append(a_res.to_text())

    except dns.resolver.NoAnswer:
        return results

    return results


def get_dns_records(
    domain: str,
    record_types: tuple = ('A', 'AAAA', 'TXT', 'CNAME', 'NS', 'MX')
) -> dict:

    records = {}

    for rtype in record_types:
        r = resolve(domain, rtype)
        if r:
            records[rtype] = r

    return records
