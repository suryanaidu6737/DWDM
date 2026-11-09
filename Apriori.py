
from itertools import combinations

# Transaction database
transactions = [
    ['Milk', 'Bread', 'Butter'],
    ['Bread', 'Butter'],
    ['Milk', 'Bread'],
    ['Milk', 'Butter'],
    ['Milk', 'Bread', 'Butter']
]

min_support = 0.4
min_confidence = 0.6

n = len(transactions)

# Generate frequent itemsets
items = set(item for t in transactions for item in t)

frequent = []

# Generate itemsets of different sizes
for size in range(1, len(items) + 1):
    for itemset in combinations(sorted(items), size):

        count = sum(
            1 for t in transactions
            if set(itemset).issubset(set(t))
        )

        support = count / n

        if support >= min_support:
            frequent.append((itemset, support))

# Display frequent itemsets
print("Frequent Itemsets:")
for itemset, support in frequent:
    print(itemset, "Support:", round(support, 2))

# Generate association rules
print("\nAssociation Rules:")

for itemset, support in frequent:
    if len(itemset) > 1:
        for i in range(1, len(itemset)):
            for left in combinations(itemset, i):
                right = tuple(
                    item for item in itemset if item not in left
                )

                left_count = sum(
                    1 for t in transactions
                    if set(left).issubset(set(t))
                )

                confidence = (support * n) / left_count

                if confidence >= min_confidence:
                    print(left, "->", right,
                          "Confidence:", round(confidence, 2))
