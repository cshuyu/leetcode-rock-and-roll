# Last updated: 2/23/2026, 6:45:03 PM
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [False]*len(rooms)
        roomStack = []
        roomStack.append(0)
        while roomStack:
            curr = roomStack.pop()
            seen[curr] = True
            if rooms[curr]:
                for room in rooms[curr]:
                    if not seen[room]:
                        roomStack.append(room)
        
        for i in seen:
            if not i:
                return False
        
        return True
            

