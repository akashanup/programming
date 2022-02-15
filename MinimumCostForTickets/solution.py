class Solution:
    def dp(self, days, costs, ticketExpiryDay, lookup):
        if ticketExpiryDay > days[-1]:
            return 0
        if lookup[ticketExpiryDay] == -1:
            if ticketExpiryDay in days:
                lookup[ticketExpiryDay] = min(
                    costs[0]+self.dp(days, costs, ticketExpiryDay+1, lookup),
                    costs[1]+self.dp(days, costs, ticketExpiryDay+7, lookup),
                    costs[2]+self.dp(days, costs, ticketExpiryDay+30, lookup))
            else:
                lookup[ticketExpiryDay] = self.dp(days, costs, ticketExpiryDay+1, lookup)
        return lookup[ticketExpiryDay]

    def mincostTickets(self, days, costs):
        return self.dp(days, costs, days[0], [-1 for _ in range(max(days)+1)])
