from mcpi.minecraft import Minecraft
mc = Minecraft.create()
a, b, c = mc.player.getPos()

from mcpi import block
air = 0
stone = 1
grass = 2
water = 9
sand=12
glass = 20
iron=42
gold=41
slab=44
stairs=67
ao=246
tnt=46
gstone=89


x=-66.5
x1=-80.5
y=0.0
z1=-15.5
z=-29.5


#Building and Roof
mc.setBlocks(x+1, y+0, z+1, x+11, y+40, z+11, iron)
mc.setBlocks(x+2, y+0, z+2, x+10, y+40, z+10, air)
mc.setBlocks(x+2, y+39, z+2, x+10, y+39, z+10, iron)

#front glass pillars
mc.setBlocks(x+2, y+1, z+1, x+2, y+38, z+1, glass)
mc.setBlocks(x+4, y+1, z+1, x+4, y+38, z+1, glass)
mc.setBlocks(x+6, y+1, z+1, x+6, y+38, z+1, glass)
mc.setBlocks(x+8, y+1, z+1, x+8, y+38, z+1, glass)
mc.setBlocks(x+10, y+1, z+1, x+10, y+38, z+1, glass)

#right glass pillars
mc.setBlocks(x+1, y+1, z+2, x+1, y+38, z+2, glass)
mc.setBlocks(x+1, y+1, z+4, x+1, y+38, z+4, glass)
mc.setBlocks(x+1, y+1, z+6, x+1, y+38, z+6, glass)
mc.setBlocks(x+1, y+1, z+8, x+1, y+38, z+8, glass)
mc.setBlocks(x+1, y+1, z+10, x+1, y+38, z+10, glass)

#back glass pillars
mc.setBlocks(x+2, y+1, z+11, x+2, y+38, z+11, glass)
mc.setBlocks(x+4, y+1, z+11, x+4, y+38, z+11, glass)
mc.setBlocks(x+6, y+1, z+11, x+6, y+38, z+11, glass)
mc.setBlocks(x+8, y+1, z+11, x+8, y+38, z+11, glass)
mc.setBlocks(x+10, y+1, z+11, x+10, y+38, z+11, glass)

#left glass pillars
mc.setBlocks(x+11, y+1, z+2, x+11, y+38, z+2, glass)
mc.setBlocks(x+11, y+1, z+4, x+11, y+38, z+4, glass)
mc.setBlocks(x+11, y+1, z+6, x+11, y+38, z+6, glass)
mc.setBlocks(x+11, y+1, z+8, x+11, y+38, z+8, glass)
mc.setBlocks(x+11, y+1, z+10, x+11, y+38, z+10, glass)


#Grass and Door
mc.setBlocks(x+2, y-1, z+2, x+10, y-1, z+10, ao)
mc.setBlocks(x+1, y+0, z+2, x+1, y+1, z+4, air)

#____________________________________________________

#Floors
mc.setBlocks(x+2, y+3, z+2, x+10, y+3, z+10, slab, 8)
mc.setBlocks(x+2, y+7, z+2, x+10, y+7, z+10, slab, 8)
mc.setBlocks(x+2, y+11, z+2, x+10, y+11, z+10, slab, 8)
mc.setBlocks(x+2, y+15, z+2, x+10, y+15, z+10, slab, 8)
mc.setBlocks(x+2, y+19, z+2, x+10, y+19, z+10, slab, 8)
mc.setBlocks(x+2, y+23, z+2, x+10, y+23, z+10, slab, 8)
mc.setBlocks(x+2, y+27, z+2, x+10, y+27, z+10, slab, 8)
mc.setBlocks(x+2, y+31, z+2, x+10, y+31, z+10, slab, 8)
mc.setBlocks(x+2, y+35, z+2, x+10, y+35, z+10, slab, 8)

#remove stair space
mc.setBlocks(x+2, y+0, z+5, x+3, y+39, z+7, air)

#stairs
mc.setBlocks(x+2, y+0, z+5, x+3, y+0, z+5, stairs,2)
mc.setBlocks(x+2, y+1, z+6, x+3, y+1, z+6, stairs,2)
mc.setBlocks(x+2, y+2, z+7, x+3, y+2, z+7, stairs,2)
mc.setBlocks(x+2, y+3, z+8, x+3, y+3, z+8, stairs,2)

mc.setBlocks(x+2, y+4, z+5, x+3, y+4, z+5, stairs,2)
mc.setBlocks(x+2, y+5, z+6, x+3, y+5, z+6, stairs,2)
mc.setBlocks(x+2, y+6, z+7, x+3, y+6, z+7, stairs,2)
mc.setBlocks(x+2, y+7, z+8, x+3, y+7, z+8, stairs,2)

mc.setBlocks(x+2, y+8, z+5, x+3, y+8, z+5, stairs,2)
mc.setBlocks(x+2, y+9, z+6, x+3, y+9, z+6, stairs,2)
mc.setBlocks(x+2, y+10, z+7, x+3, y+10, z+7, stairs,2)
mc.setBlocks(x+2, y+11, z+8, x+3, y+11, z+8, stairs,2)

mc.setBlocks(x+2, y+12, z+5, x+3, y+12, z+5, stairs,2)
mc.setBlocks(x+2, y+13, z+6, x+3, y+13, z+6, stairs,2)
mc.setBlocks(x+2, y+14, z+7, x+3, y+14, z+7, stairs,2)
mc.setBlocks(x+2, y+15, z+8, x+3, y+15, z+8, stairs,2)

mc.setBlocks(x+2, y+16, z+5, x+3, y+16, z+5, stairs,2)
mc.setBlocks(x+2, y+17, z+6, x+3, y+17, z+6, stairs,2)
mc.setBlocks(x+2, y+18, z+7, x+3, y+18, z+7, stairs,2)
mc.setBlocks(x+2, y+19, z+8, x+3, y+19, z+8, stairs,2)

mc.setBlocks(x+2, y+20, z+5, x+3, y+20, z+5, stairs,2)
mc.setBlocks(x+2, y+21, z+6, x+3, y+21, z+6, stairs,2)
mc.setBlocks(x+2, y+22, z+7, x+3, y+22, z+7, stairs,2)
mc.setBlocks(x+2, y+23, z+8, x+3, y+23, z+8, stairs,2)

mc.setBlocks(x+2, y+24, z+5, x+3, y+24, z+5, stairs,2)
mc.setBlocks(x+2, y+25, z+6, x+3, y+25, z+6, stairs,2)
mc.setBlocks(x+2, y+26, z+7, x+3, y+26, z+7, stairs,2)
mc.setBlocks(x+2, y+27, z+8, x+3, y+27, z+8, stairs,2)

mc.setBlocks(x+2, y+28, z+5, x+3, y+28, z+5, stairs,2)
mc.setBlocks(x+2, y+29, z+6, x+3, y+29, z+6, stairs,2)
mc.setBlocks(x+2, y+30, z+7, x+3, y+30, z+7, stairs,2)
mc.setBlocks(x+2, y+31, z+8, x+3, y+31, z+8, stairs,2)

mc.setBlocks(x+2, y+32, z+5, x+3, y+32, z+5, stairs,2)
mc.setBlocks(x+2, y+33, z+6, x+3, y+33, z+6, stairs,2)
mc.setBlocks(x+2, y+34, z+7, x+3, y+34, z+7, stairs,2)
mc.setBlocks(x+2, y+35, z+8, x+3, y+35, z+8, stairs,2)

mc.setBlocks(x+2, y+36, z+5, x+3, y+36, z+5, stairs,2)
mc.setBlocks(x+2, y+37, z+6, x+3, y+37, z+6, stairs,2)
mc.setBlocks(x+2, y+38, z+7, x+3, y+38, z+7, stairs,2)
mc.setBlocks(x+2, y+39, z+8, x+3, y+39, z+8, stairs,2)


