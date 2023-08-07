class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            smallestChar = min(s)
            return s.count(smallestChar)
        
        wordsFreq = sorted([f(w) for w in words])
        answer = []

        for query in queries:
            queryFreq = f(query)

            start, end = 0, len(wordsFreq)

            while start < end:
                mid = (start + end) // 2

                if wordsFreq[mid] <= queryFreq:
                    start = mid + 1
                else:
                    end = mid
            
            answer.append(len(words) - start)

        return answer