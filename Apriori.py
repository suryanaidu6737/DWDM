
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

# 1. Define fruit shopping transactions
fruit_dataset = [
    ["Apple", "Banana", "Mango"],
    ["Orange", "Banana", "Mango"],
    ["Apple", "Orange", "Banana"],
    ["Apple", "Mango"],
    ["Apple", "Orange", "Banana", "Mango"]
]

# 2. Transform the lists into True/False table
te = TransactionEncoder()
te_array = te.fit(fruit_dataset).transform(fruit_dataset)
df = pd.DataFrame(te_array, columns=te.columns_)

print("--- Step 1: Transformed Fruit Table ---")
print(df)
print("\n" + "=" * 50 + "\n")

# 3. Find frequent itemsets (Minimum Support = 60%)
frequent_fruits = apriori(
    df, min_support=0.6, use_colnames=True
)

print("--- Step 2: Frequent Fruit Groups ---")
print(frequent_fruits)
print("\n" + "=" * 50 + "\n")

# 4. Generate association rules (Minimum Confidence = 70%)
rules = association_rules(
    frequent_fruits, metric="confidence", min_threshold=0.7
)

# Display selected columns
final_rules = rules[
    ["antecedents", "consequents", "support", "confidence", "lift"]
]

print("--- Step 3: Actionable Rules ---")
print(final_rules)
