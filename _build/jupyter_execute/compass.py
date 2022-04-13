#!/usr/bin/env python
# coding: utf-8

# # Microbit compass

# # step 1

# # How it work

# * Your micro:bit has a built-in compass sensor called a magnetometer. You can use it to measure the Earth’s magnetic field and use it as a compass.
# * When you press the button A input, the micro:bit takes a reading from the compass sensor and shows the device’s numerical compass bearing on the LED display output. Point the micro:bit North and you should see a reading of 0 degrees.

# 

# # what you need 

# * micro:bit
# * Python editor

# # Video

# In[1]:


from IPython.display import YouTubeVideo

YouTubeVideo('KTH2yp3r4-k', width=800, height=300)


# In[2]:


from ruamel.yaml import YAML

config_document_1 = """
title                       : Interactive Learning platform for sensors # The title of the book
logo                        : "./compass image.png"  # Path to the book logo


"""

# Save our _config.yml in the book path
yaml = YAML()
config_file = open('../ibsp/_config.yml', 'w')
yaml.dump(yaml.load(config_document_1), config_file)


# # Image of microbit compass 

# ![alternative text]![](compass.jpeg)

# # Codes 

# def playSound(direction, prev_direction):
#     # please replace pass with your own logic
#     if direction != prev_direction:
#         speech.say(direction, speed=120, pitch=100, throat=100, mouth=200)
#  
# def displayDirection(bearing, prev_direction):
# 
#     if bearing < 45 or bearing > 315:
#         display.show('N')
#         direction = "North"
#     elif bearing < 315 and bearing > 225 :
#         display.show('W')
#         direction = "West"
#     elif bearing < 225 and bearing > 135:
#         display.show('S')
#         direction = "South"
#     elif bearing < 135 and bearing > 45:
#         display.show('E')
#         direction = "East"
#     else:
#         #current_bearing = 'X'
#         display.show('X')
#         direction = "No Direction"
# 
#     playSound(direction, prev_direction)
#     return direction
#  
# def main():
#   
#     while True:
#         if not compass.is_calibrated():
#             compass.calibrate()
#             prev_direction = "No Direction"
#         else:
#         # add your logic here
#             sleep(100)
#             
#             if button_a.is_pressed() and button_b.is_pressed():
#                 compass.calibrate()
#                 prev_direction = "No Direction"
#             
#             bearing = compass.heading()
#             prev_direction = displayDirection(bearing, prev_direction)
#  
# if __name__ == "__main__":
#     main()
# 

# In[3]:


from IPython import display
display.HTML('<iframe src="https://jackbonk.github.io/editor/" allow="usb;serial"  width=800 height=500></iframe>')


# # LINKS

# <https://makecode.microbit.org/projects/compass>

# <https://microbit.org/projects/make-it-code-it/compass-bearing/>
