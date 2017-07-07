from enum import Enum, auto

class Item_touching_state(Enum):
    TOUCHING_OBSTACLE_NONE = auto(),  # not touching
    TOUCHING_OBSTACLE_LEFT = auto(),  # touching the obstacle on the left
    TOUCHING_OBSTACLE_RIGHT = auto(), # etc.
    TOUCHING_OBSTACLE_OVER = auto(),
    TOUCHING_OBSTACLE_UNDER = auto()

# Applies to an item and an obstacle that are in a rectangular frame, like
# tkinter items. The only requirement is that they both have a coords() method
# that returns an indexable object for for which indexes 0 to 3 are valid and
# that comparison operators can be applied to the items in the lists.
def item_touching_state(item, obstacle):
    icoords = item.coords()
    ocoords = obstacle.coords()
    in_left = icoords[2] >= ocoords[0] and icoords[0] < ocoords[0]
    in_right = icoords[0] <= ocoords[2] and icoords[2] > ocoords[2]
    in_over = icoords[3] >= ocoords[1] and icoords[1] < ocoords[1]
    in_bottom = icoords[1] <= ocoords[3] and icoords[3] > ocoords[3]

