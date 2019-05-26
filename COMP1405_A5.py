# ============================================================
#
# Student Name (as it appears on cuLearn): Jeff Jose
# Course Code (for this current semester): COMP1405B
#
# ============================================================

from comp1405_f17_assistant_a5 import *

#Leg 1
for i in range(13):
	move_down()
#Leg 2
while am_i_standing_on(1) != 1:
	move_right()
#Leg 3
for i in range(10):
	move_down()
#Leg 4
flag = True
while flag:
	move_left()
	if am_i_standing_on(1):
		flag = False
#Leg 5
while what_number_am_i_standing_on() != 3:
	move_down()
#Leg 6
for i in range(46):
	move_right()
#Leg 7
while True:
	move_down()
	if what_number_am_i_standing_on() == 3:
		break
#Leg 8
while True:
	move_left()
	if am_i_standing_on(1):
		break
#Leg 9
flag = True
while flag:
	move_down()
	if what_number_am_i_standing_on() == 3:
		flag = False
