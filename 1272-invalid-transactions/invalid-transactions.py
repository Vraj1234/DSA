# class Solution:
#     def invalidTransactions(self, transactions: List[str]) -> List[str]:
#         res = []
#         by_name = defaultdict(list)
#         c = Counter(transactions)

#         for txn in transactions: #O(t)
#             name, t, a, city = txn.split(',')
#             time = int(t)
#             amount = int(a)
#             if amount > 1000 and res.count(txn) < c[txn]: #O(t)
#                 res.append(txn)
#             by_name[name].append((time, city))
        

#         for txn in transactions: #O(t)
#             cur_name, t, a, cur_city = txn.split(',')
#             cur_time = int(t)
#             cur_amount = int(a)
#             ar = by_name[cur_name]
#             for pair in ar: #O(k)
#                 time, city = pair
#                 if abs(cur_time - time) <= 60 and city != cur_city and res.count(txn) < c[txn]:
#                     res.append(txn)
        
#         return res

from collections import defaultdict

class Solution:
    def invalidTransactions(self, transactions):
        invalid = set()
        by_name = defaultdict(list)

        # build groups + amount rule
        for i, txn in enumerate(transactions):
            name, t, a, city = txn.split(',')
            time = int(t)
            amount = int(a)

            if amount > 1000:
                invalid.add(i)

            by_name[name].append((time, city, i))

        # check 60-minute city conflicts
        for name in by_name:
            arr = by_name[name]

            for i in range(len(arr)):
                time_i, city_i, idx_i = arr[i]

                for j in range(i + 1, len(arr)):
                    time_j, city_j, idx_j = arr[j]

                    if abs(time_i - time_j) <= 60 and city_i != city_j:
                        invalid.add(idx_i)
                        invalid.add(idx_j)

        # build result preserving duplicates
        return [transactions[i] for i in invalid]