def discover(target, candidates):
    results = []

    for candidate in candidates:

        searchable_text = (
            candidate["name"] +
            " " +
            candidate["category"] +
            " " +
            candidate["location"]
        )

        if target.lower() in searchable_text.lower():

            results.append({
                "name": candidate["name"],
                "website": candidate["website"],
                "location": candidate["location"],
                "category": candidate["category"],
                "source": candidate["source"]
            })

    return results


if __name__ == "__main__":

    candidates = [
        {
            "name": "Example SEO Agency",
            "website": "https://example.com",
            "location": "Austin, Texas",
            "category": "SEO Agency",
            "source": "manual"
        },
        {
            "name": "Complete SEO",
            "website": "https://completeseo.com",
            "location": "Austin, Texas",
            "category": "SEO Agency",
            "source": "manual"
        }
    ]

    prospects = discover(
        "SEO Agency",
        candidates
    )

    for prospect in prospects:
        print(prospect)
