class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res = []
        by_name = defaultdict(list)
        c = Counter(transactions)

        for txn in transactions:
            name, t, a, city = txn.split(',')
            time = int(t)
            amount = int(a)
            if amount > 1000 and res.count(txn) < c[txn]:
                res.append(txn)
            by_name[name].append((time, city))
        

        for txn in transactions:
            cur_name, t, a, cur_city = txn.split(',')
            cur_time = int(t)
            cur_amount = int(a)
            ar = by_name[cur_name]
            for pair in ar:
                time, city = pair
                if abs(cur_time - time) <= 60 and city != cur_city and res.count(txn) < c[txn]:
                    res.append(txn)
        
        return res

