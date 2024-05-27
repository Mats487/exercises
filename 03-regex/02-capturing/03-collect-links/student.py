import re


def collect_links(string):
    links = re.findall(r'<a href="(.*)">', string)

    return links
