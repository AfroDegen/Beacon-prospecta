def qualify(client):

    score = 0

    if client["website"]:
        score += 25

    if client["reviews"] > 50:
        score += 25

    if client["category"]:
        score += 25

    if client["location"]:
        score += 25

    return score
