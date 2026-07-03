class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        arr = [0] * (n + 2)
        for book in bookings:
            arr[book[0]] += book[2]
            arr[book[1] + 1] -= book[2]
        
        answer = [0] * (n + 1)
        answer[0] = arr[0]
        for i in range(1, n + 1):
            answer[i] = answer[i - 1] + arr[i]
        return answer[1:]