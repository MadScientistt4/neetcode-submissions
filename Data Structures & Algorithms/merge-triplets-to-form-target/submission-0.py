class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        boolean = [False]*3
        for i in range(len(triplets)):
            if triplets[i][0] == target[0] and triplets[i][1] <= target[1] and triplets[i][2] <= target[2]:
                boolean[0] = True
            if triplets[i][1] == target[1] and triplets[i][0] <= target[0] and triplets[i][2] <= target[2]:
                boolean[1] = True
            if triplets[i][2] == target[2] and triplets[i][1] <= target[1] and triplets[i][0] <= target[0]:
                boolean[2] = True
        for b in boolean:
            if b == False:
                return False
        return True