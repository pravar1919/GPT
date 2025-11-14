from vector_db_1807 import VectorClient

client = VectorClient(
    api_key="sk_ea5726601a8444cbb02b1447", 
    base_url="https://9858918592da.ngrok-free.app"
)

response = client.add_vector(
    embedding=[0.1, 0.2, 0.3, 0.44],
    metadata={"desc": "sample vector from SDK"}
)
print("✅ Vector added:", response)

search_response = client.search(
    query_vector=[0.1, 0.2, 0.3, 0.5],
    top_k=6
)
print("🔍 Search Results:", search_response)
