class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        arr = [[hand[0], hand[0]]]
        for i in range(1, len(hand)):
            flag = 0
            for ele in arr:
                print(arr, ele, hand[i], i)
                if hand[i] - 1 == ele[1] and ele[1] - ele[0] != groupSize - 1:
                    ele[1] = hand[i]
                    flag = 1
                    break
            if flag == 0:
                arr.append([hand[i], hand[i]])
        print(arr)
        flag = 0
        for i in range(len(arr)):
            if arr[i][1] - arr[i][0] != groupSize - 1:
                flag = 1
                break
        if flag == 0:
            return True
        return False
                

            