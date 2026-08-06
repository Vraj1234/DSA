from sortedcontainers import SortedList

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        parent = [x for x in range(c)]
        rank = [0 for i in range(c)]

        def union(a,b):
            parA = find(a)
            parB = find(b)

            if rank[parA] == rank[parB]:
                parent[parB] = parA
                rank[parA]+=1
            elif rank[parA] < rank[parB]:
                parent[parA] = parB
            else:
                parent[parB] = parA


        def find(a):
            if parent[a] == a:
                return a

            parent[a] = find(parent[a])
            return parent[a]
    
        relationships = defaultdict(SortedList)
        for a,b in connections:
            union(a-1,b-1)
        
        for i in range(len(parent)):
            parent[i] = find(parent[i])
            relationships[parent[i]].add(i)
        
        res = []
        for code, node in queries:
            root = parent[node - 1]
            if code == 1:
                if (node - 1) in relationships[root]:
                    res.append(node)
                elif relationships[root]:
                    res.append(relationships[root][0] + 1)
                else:
                    # Component is completely empty
                    res.append(-1)
            elif code == 2:
                relationships[root].discard(node - 1)
        
        return res
        
