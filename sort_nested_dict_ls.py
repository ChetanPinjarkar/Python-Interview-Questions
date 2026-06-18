from collections import defaultdict
data = [
    {"name": "A", "count": 10},
    {"name": "B", "count": 20},
    {"name": "A", "count": 15},
    {"name": "C", "count": 5},
    {"name": "B", "count": 10}
]
result = defaultdict(int)
for item in data:
    result[item["name"]] += item["count"]
output = [{"name": k, "count": v}
    for k, v in result.items()]
# Sort by count (descending)
output = sorted(output, key=lambda x: x["count"], reverse=True)
print(output)
