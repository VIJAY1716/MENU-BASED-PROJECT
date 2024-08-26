from googlesearch import search

# Define the search query
query = "Python programming"

# Perform the search and get the top 5 results
search_results = search(query, num_results=5)

# Print the results
for idx, result in enumerate(search_results, start=1):
    print(f"Result {idx}: {result}")
