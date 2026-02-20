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
        res = []
        added = set()          # track indices already added
        by_name = defaultdict(list)

        # first pass
        for i, txn in enumerate(transactions):
            name, t, a, city = txn.split(',')
            time = int(t)
            amount = int(a)

            if amount > 1000 and i not in added:
                res.append(txn)
                added.add(i)

            by_name[name].append((time, city, i))

        # second pass
        for i, txn in enumerate(transactions):
            cur_name, t, a, cur_city = txn.split(',')
            cur_time = int(t)

            for time, city, idx in by_name[cur_name]:
                if abs(cur_time - time) <= 60 and city != cur_city:
                    if i not in added:
                        res.append(txn)
                        added.add(i)

        return res