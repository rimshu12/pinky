#!/usr/bin/env python
# coding: utf-8

# # Sunlight Sensors 

# # How it works

# * As well as working as an output, the LEDs on your micro:bit can also work as an input device light sensor, measuring the amount of light falling on them.
# * Flash this program onto your micro:bit and shine a light source, like a torch, daylight or bright ceiling light on to the micro:bit, and you should see the sun appear

# # what you need 

# - micro:bit
# - python editor
# - a light source and something to cover the micro:bit with – your hand will do!

# # Video

# In[1]:


from IPython.display import YouTubeVideo

YouTubeVideo('ii0U_FMr-Z4', width=800, height=300)


# # Image of sunlight sensor 

# ![alternative text]![](sunlight.png)

# # Codes 

# ```{hint} try using this code
# ```

# ``` {toggle} click to view code
# :show:  
#     from microbit import *
# 
#     while True:
#         if display.read_light_level() > 100:
#             display.show(Image(
#             "90909:"
#             "09990:"
#             "99999:"
#             "09990:"
#             "90909"))
#         else:
#             display.clear()
# ````            

# ``` {attention} 
# This is just an example.
# ```

# In[2]:


from IPython import display
import warnings
warnings.filterwarnings('ignore')
display.HTML('<iframe src="https://jackbonk.github.io/editor/" allow="usb;serial"  width=800 height=500></iframe>')


# # LINKS

# <https://microbit.org/projects/make-it-code-it/sunlight-sensor/#how-it-works>

# <https://microbit.org/>

# <https://digitalmaestro.org/microbit>

# In[ ]:




