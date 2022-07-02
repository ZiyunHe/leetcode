def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_num = prices[0]
        max_num = 0
        diff = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[i-1] and prices[i] < min_num:
                min_num = prices[i]
                max_num = 0
            elif prices[i] > prices[i-1]:
                max_num = max(prices[i], max_num)
                diff = max(max_num - min_num, diff)
        return diff