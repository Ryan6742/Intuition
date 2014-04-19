from adventure import *



rm_start = Room()
rm_gas = Room()
rm_chest = Room()
rm_potato = Room()

i_torch = Item('torch')
i_potato = Item('potato')
i_axe = Item('axe')
i_chest = Item('chest', takable = False)

add_door(0, rm_start, rm_chest, locked = True)
add_door(2, rm_start, rm_gas)
add_door(1, rm_gas, rm_potato)



rm_start.description = "The cave is pretty much empty."

