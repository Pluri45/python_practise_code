# class Rectangle:
#     def __init__(self, length, breath):
#         self._length =  length
#         self._breath = breath
        

#     @property
#     def length (self):
#         return  self._length 
    
#     @property
#     def breath (self):
#         return  self._breath
    
    
#     def contains(self, x, y):
#         if x <=  self._length and y <= self._breath :
#             return True
#         else:
#             return False
        
        
    
#     def union(self, rect):
#         # Calculate the dimensions of the union rectangle
#         new_length = max(self._length, rect._length)
#         new_breath = max(self._breath, rect._breath)
#         # Return a new Rectangle that represents the union
#         return Rectangle(new_length, new_breath)   
    
#     def intersection(self, rect):
#         # Calculate the intersection width and height
#         intersect_length = min(self._length, rect._length)
#         intersect_breath = min(self._breath, rect._breath)
        
#         # Check if there is an intersection
#         if intersect_length > 0 and intersect_breath > 0:
#             return Rectangle(intersect_length, intersect_breath)
#         else:
#             # No intersection, return a rectangle with width and height of 0
#             return Rectangle(0, 0)



