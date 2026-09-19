import requests
from bs4 import BeautifulSoup


LEADERSHIP_KEYWORDS = [
    "founder",
    "co-founder",
    "owner",
    "ceo",
    "managing partner",
    "president",
    "director"
]


def find_people(agency_url):
    candidates = []

    pages_to_check = [
        "/about",
        "/team",
        "/leadership",
        "/company",
        "/about-us"
    ]

    for page in pages_to_check:

        try:
            url = agency_url.rstrip("/") + page

            response = requests.get(
                url,
                timeout=15,
                headers={
                    "User-Agent": "Beacon Prospecta"
                }
            )

            if response.status_code != 200:
                continue

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            text = soup.get_text(
                separator=" ",
                strip=True
            )

            lower_text = text.lower()

            for keyword in LEADERSHIP_KEYWORDS:

                if keyword in lower_text:

                    candidates.append(
                        {
                            "role": keyword.title(),
                            "source": url,
                            "confidence": 70
                        }
                    )

        except Exception:
            continue

    return candidates


def recommend_contact(people):
    if not people:
        return None

    priority = {
        "Founder": 100,
        "Co-Founder": 95,
        "Owner": 90,
        "CEO": 85,
        "Managing Partner": 80,
        "President": 75,
        "Director": 60
    }

    best = max(
        people,
        key=lambda person:
            priority.get(
                person["role"],
                0
            )
    )

    return best
