class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        records = defaultdict(list)
        res = []
        c = Counter(transactions)

        for x in transactions:
            name, time, amt, city = x.split(',')
            records[name].append([int(time), city])
            if int(amt) > 1000 and res.count(x) < c[x]:
                res.append(x)
        
        for x in transactions:
            name, time, amt, city = x.split(',')
            val = records[name]
            val.sort(key = lambda x: x[0])
            print(val)
            for v in val:
                diff = abs(v[0] - int(time))
                if diff <= 60 and v[1] != city and res.count(x) < c[x]:
                    res.append(x)
                
        return res



        
        

        


            