class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = [(p, s) for p, s in zip(position, speed)]
        
        
        cars.sort(key=lambda x: x[0])

        elem = cars.pop()
        stack.append(elem)

        while cars:
            elem = cars.pop()
            other = stack[-1]
            time_e = (target - elem[0]) / elem[1]
            time_o = (target - other[0]) / other[1]
            if time_o < time_e:
                stack.append(elem)
        return len(stack)

