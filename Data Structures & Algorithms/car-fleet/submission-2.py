class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_info = [(position[i], speed[i]) for i in range(len(position))]
        car_info.sort(reverse=True)
       
        stack = []
        for p, s in car_info:
            time = (target-p) / s
            if stack:
                if time > stack[-1] :
                    stack.append(time)
            else:
                stack.append(time)
        return len(stack)
