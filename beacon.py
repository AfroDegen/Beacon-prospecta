from agency_discovery import discover_agencies


def run(query):
    agencies = discover_agencies(query)

    return {
        "query": query,
        "agencies_found": len(agencies),
        "agencies": agencies
    }


if __name__ == "__main__":

    result = run(
        "restoration marketing agency texas"
    )

    print("\n=== BEACON PROSPECTA ===\n")

    print(
        f"Query: {result['query']}"
    )

    print(
        f"Agencies Found: {result['agencies_found']}\n"
    )

    for agency in result["agencies"]:

        print(
            {
                "name":
                    agency["name"],

                "website":
                    agency["website"],

                "source":
                    agency["source"]
            }
        )
