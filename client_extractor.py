import requests
from bs4 import BeautifulSoup
import re


def extract_clients(discovered_pages):
    clients = []

    business_suffixes = [
        "LLC",
        "Inc",
        "Company",
        "Services",
        "Group",
        "Solutions",
        "Restoration",
        "Roofing",
        "Plumbing",
        "HVAC"
    ]

    for page in discovered_pages:

        url = page["url"]

        try:
            response = requests.get(
                url,
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

            candidates = []

            # Look at headings first
            for tag in ["h1", "h2", "h3"]:

                for node in soup.find_all(tag):

                    text = node.get_text(
                        strip=True
                    )

                    if len(text) < 3:
                        continue

                    candidates.append(text)

            # Look for likely business entities
            for candidate in candidates:

                for suffix in business_suffixes:

                    if suffix.lower() in candidate.lower():

                        clients.append({
                            "name": candidate,
                            "source_page": url,
                            "confidence": 70
                        })

                        break

            # De-duplicate
            unique = {}

            for client in clients:

                unique[
                    client["name"]
                ] = client

            clients = list(
                unique.values()
            )

        except Exception as error:

            print(
                f"Failed to process {url}"
            )

            print(error)

    return clients


if __name__ == "__main__":

    discovered_pages = [
        {
            "url":
            "https://completeseo.com/case-studies/",
            "type":
            "case-study"
        }
    ]

    clients = extract_clients(
        discovered_pages
    )

    print(
        "\n=== CLIENTS FOUND ===\n"
    )

    for client in clients:
        print(client)
