import json

def search_catalog(query: str):
    with open("catalog.json") as f:
        catalog = json.load(f)
    for plan in catalog["plans"]:
        if query.lower() in plan["name"].lower() or query.lower() in plan["features"]:
            return f"{plan['name']} plan: {plan['price']} with {', '.join(plan['features'])}"
    return "No match found"
