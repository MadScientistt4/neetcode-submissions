class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = {}
        for i in range(len(position)):
            pos_speed[position[i]] = speed[i]
        position.sort(reverse=True)
        print(position)
        print(pos_speed)
        fleet = 1
        time = (target-position[0])/pos_speed[position[0]]
        for i in range(1, len(position)):
            cur_time = (target-position[i])/pos_speed[position[i]]
            print(cur_time, time)
            if cur_time > time:
                time = cur_time
                fleet += 1
        return fleet