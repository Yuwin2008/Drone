from controller import Robot
from controller import Camera
from controller import Keyboard

bot = Robot()

keyboard = Keyboard()

timestep = 64

m1 = bot.getDevice('m1_motor')

m2 = bot.getDevice('m2_motor')

m3 = bot.getDevice('m3_motor')

m4 = bot.getDevice('m4_motor')

cam = bot.getDevice('camera')

cam.enable(timestep)

keyboard.enable(timestep)

key_pressed = -1

## press 'p' key
if (key_pressed == 80):
    cam.getImage()
    img_name = "img" + str(img_num) + ".png"
    cam.saveImage(img_name,50)
    img_num = img_num + 1
    
m1.setVelocity(600)
m2.setVelocity(600)
m3.setVelocity(600)
m4.setVelocity(600)