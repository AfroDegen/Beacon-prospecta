import os
import requests


SERPAPI_URL = "https://serpapi.com/search.json"


def discover_agencies(query):
    """
    Discover agencies from Google search results
    using SerpAPI.
    """

    api_key = os.getenv("SERPAPI_KEY")

    if not api_key:
        raise ValueError(
            "SERPAPI_KEY environment variable not found."
        )

    response = requests.get(
        SERPAPI_URL,
        params={
            "engine": "google",
            "q": query,
            "api_key": api_key
        },
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    agencies = []

    for result in data.get(
        "organic_results",
        []
    )[:10]:

        agencies.append(
            {
                "name": result.get(
                    "title",
                    "Unknown Agency"
                ),

                "website": result.get(
                    "link",
                    ""
                ),

                "location": "Unknown",

                "category": "Agency",

                "source": "serpapi"
            }
        )

    return agencies


if __name__ == "__main__":

    agencies = discover_agencies(
        "restoration marketing agency texas"
    )

    for agency in agencies:
        print(agency)
