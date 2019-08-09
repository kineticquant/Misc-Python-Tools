#MM 08.09.2019

####                       ####      ####                       ####
####  ###             ###  ####      ####  ###             ###  ####
####     ###      ###      ####      ####     ###      ###      ####
####        ## ##          ####      ####        ## ##          ####
####          #            ####      ####          #            ####
####                       ####      ####                       ####
####                       ####      ####                       ####
####                       ####      ####                       ####
####                       ####      ####                       ####

import Monit0r

#First parameter is timer interval in seconds, Second is email, Third is password
my_Monit0r = Monit0r.Visibility(3600, "myexampleemail@gmail.com", "mypassword")
my_Monit0r.start()