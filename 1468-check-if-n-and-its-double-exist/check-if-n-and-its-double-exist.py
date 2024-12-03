class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        visited = []
        for num in arr:
            if (num * 2 in visited) or (num % 2 == 0 and num // 2 in visited):
                return True
            visited.append(num)
        return False