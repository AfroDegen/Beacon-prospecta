from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup


DISCOVERY_PATTERNS = [
    "case-study",
    "case-studies",
    "portfolio",
    "clients",
    "projects",
    "testimonials",
    "success",
    "results",
    "industries",
    "work"
]


def discover_pages(agency_url):
    response = requests.get(
        agency_url,
        timeout=15,
        headers={
            "User-Agent": "Beacon Prospecta"
        }
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    discovered = []

    for link in soup.find_all("a", href=True):

        href = link["href"]

        absolute_url = urljoin(
            agency_url,
            href
        )

        href_lower = href.lower()

        for pattern in DISCOVERY_PATTERNS:

            if pattern in href_lower:

                discovered.append({
                    "url": absolute_url,
                    "type": pattern
                })

                break

    return discovered
