import re


def domain_name(url):
    domain = re.search('(https?://)?(www\d?\.)?(?P<domain_name>[\w-]+)\.', url)
    if domain:
        return domain.group('domain_name')