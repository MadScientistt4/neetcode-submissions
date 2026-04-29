class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)-1
        row = -1
        while l <= r:
            mid = l + (r-l)//2
            print(l, r, matrix[mid][0])
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                print(row)
                break
            elif matrix[mid][0] < target:
                l = mid+1
            else:
                r = mid-1
        l = 0
        r = len(matrix[0])-1
        while l <= r:
            mid = l + (r-l)//2
            print(l, r, matrix[row][mid])
            if matrix[row][mid] == target:
                print(mid)
                return True
            elif matrix[row][mid] < target:
                l = mid+1
            else:
                r = mid-1
        print(mid)
        return False
