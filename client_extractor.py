import re
import requests
from bs4 import BeautifulSoup


def extract_clients(urls):
    clients = []

    for item in urls:

        url = item["url"]

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

            text = soup.get_text(
                separator=" ",
                strip=True
            )

            patterns = [
                r"Client:\s*([A-Z][A-Za-z0-9 &\-]+)",
                r"Customer:\s*([A-Z][A-Za-z0-9 &\-]+)",
                r"Worked with\s*([A-Z][A-Za-z0-9 &\-]+)",
                r"Case Study:\s*([A-Z][A-Za-z0-9 &\-]+)"
            ]

            for pattern in patterns:

                matches = re.findall(
                    pattern,
                    text
                )

                for match in matches:

                    clients.append({
                        "name": match.strip(),
                        "source_page": url
                    })

        except Exception as error:

            print(
                f"Error reading {url}: {error}"
            )

    return clients
