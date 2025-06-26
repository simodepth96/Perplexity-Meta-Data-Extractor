import pandas as pd

# Load JSON from file
with open('perplexity-quali-sono-le-migliori-auto-ib-ZBOLnB4zTCK0EE0FmzNilQ (1).json', encoding='utf-8') as f:
    data = json.load(f)

# Extract web results
try:
    web_results = (
        data['entries'][0]['blocks'][1]['plan_block']['steps'][2]['web_results_content']['web_results']
    )

    # Flatten into a list of dictionaries
    rows = []
    for result in web_results:
        rows.append({
            "Title": result.get("name"),
            "URL": result.get("url"),
            "Snippet": result.get("snippet"),
            "Domain": result.get("meta_data", {}).get("domain_name"),
            "Published Date": result.get("meta_data", {}).get("published_date")
        })

    # Save to Excel
    df = pd.DataFrame(rows)
    df.to_excel("web_results_output.xlsx", index=False)
    print("✅ Saved as web_results_output.xlsx")

except (KeyError, IndexError) as e:
    print("❌ Could not extract web_results. Error:", e)
