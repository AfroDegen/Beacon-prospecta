def discover(target, candidates):
    results = []

    for candidate in candidates:
        if target.lower() in candidate["text"].lower():
            results.append({
                "name": candidate["name"],
                "website": candidate["website"],
                "location": candidate["location"],
                "category": candidate["category"],
                "source": candidate["source"],
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
        }
    ]

    prospects = discover("SEO Agency", candidates)

    for prospect in prospects:
        print(prospect)