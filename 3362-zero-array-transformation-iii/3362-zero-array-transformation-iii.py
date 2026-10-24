class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        if n == 0:
            return len(queries)
        
        queries.sort()

        delta_array = [0] * (n + 1)

        availabel_queries_pq = []

        query_idx = 0
        current_operations = 0

        for i in range(n):
            current_operations += delta_array[i]

            while query_idx < len(queries) and queries[query_idx][0] == i:
                left, right = queries[query_idx]
                heapq.heappush(availabel_queries_pq, -right)
                query_idx += 1

            while current_operations < nums[i]:
                if not availabel_queries_pq or -availabel_queries_pq[0] < i:
                    return -1
                
                selected_query_right_endpoint = -heapq.heappop(availabel_queries_pq)

                current_operations += 1

                if selected_query_right_endpoint + 1 <= n:
                    delta_array[selected_query_right_endpoint + 1] -= 1

            if current_operations < nums[i]:
                return -1
        
        return len(availabel_queries_pq)