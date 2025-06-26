# Load the JSON file
with open('perplexity-quali-sono-le-migliori-auto-ib-ZBOLnB4zTCK0EE0FmzNilQ (1).json', encoding='utf-8') as f:
    data = json.load(f)

# Extract related_queries
try:
    related_queries = data['entries'][0].get('related_queries', [])

    # Convert to DataFrame
    df_queries = pd.DataFrame(related_queries, columns=["Related Queries"])

    # Save to Excel
    df_queries.to_excel("related_queries_output.xlsx", index=False)
    print("✅ Saved related queries to related_queries_output.xlsx")

except (KeyError, IndexError) as e:
    print("❌ Could not extract related_queries. Error:", e)
