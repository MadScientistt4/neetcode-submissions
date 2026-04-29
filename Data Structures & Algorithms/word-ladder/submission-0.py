class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = {}
        wordList.insert(0, beginWord)
        n = len(wordList)
        print(wordList)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                diff = 0
                for a, b in zip(wordList[i], wordList[j]):
                    if a != b:
                        diff += 1
                    if diff > 1:
                        break
                if diff == 1:
                    if i in adj:
                        adj[i].append(j)
                    else:
                        adj[i] = [j]
        print(adj)
        if 0 not in adj:
            return 0 
        def bfs():
            q = collections.deque()
            q.append((0, -1))
            visited = [0 for _ in range(n)]
            visited[0] = 1
            lvl = 0
            
            while q:
                qlen = len(q)
                lvl += 1
                for i in range(qlen):
                    cur, parent = q.popleft()
                    if wordList[cur] == endWord:
                        return lvl
                    for nei in adj[cur]:
                        if nei == parent:
                            continue
                        if visited[nei] == 0:
                            q.append((nei, cur))
                    visited[cur] = 1
            return 0
        return bfs()
