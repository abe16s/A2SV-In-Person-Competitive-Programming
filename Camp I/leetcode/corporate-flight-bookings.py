class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ps = [0] * (n+1)
        for f, l, s in bookings:
            ps[f-1] += s
            ps[l] -= s

        for i in range(1, n+1):
            ps[i] += ps[i-1]

        return ps[:n] 