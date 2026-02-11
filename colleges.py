def recommend_colleges(chance):

    if chance >= 0.8:
        tier = "Dream Universities"
        colleges = [
            "MIT",
            "Stanford University",
            "Harvard University"
        ]

    elif chance >= 0.6:
        tier = "Moderate Universities"
        colleges = [
            "New York University",
            "Columbia University",
            "UCLA"
        ]

    else:
        tier = "Safe Universities"
        colleges = [
            "Arizona State University",
            "UT Dallas",
            "SUNY Buffalo"
        ]

    return tier, colleges
