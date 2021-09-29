"""
https://realpython.com/introduction-to-python-generators/#building-generators-with-generator-expressions
"""
# csv_gen = csv_reader("some_csv.txt")
row_count = 0

for row in range(1, 10+1):
    row_count += 1

print(f"Row count is {row_count}")