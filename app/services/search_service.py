from ddgs import DDGS

def search_market_data(sector: str):

    query = f"{sector} industry India market trends"

    results = []

    with DDGS() as ddgs:
        search_results = ddgs.text(query, max_results=5)

        for r in search_results:
            results.append(r["title"] + " - " + r["body"])
    

    return results