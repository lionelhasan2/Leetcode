class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for asteroid in asteroids:
            alive = True
            
            while alive and asteroid < 0 and stack and stack[-1] > 0:
                top = stack[-1]  # Just peek, don't pop yet
                
                if abs(asteroid) > abs(top):
                    stack.pop()  
                elif abs(asteroid) == abs(top):
                    alive = False
                    stack.pop()  
                else:
                    alive = False
            
            if alive:
                stack.append(asteroid)
        
        return stack