#!/usr/bin/python

#-------------------------------------------------
#-- BQ Human rights to technology
#--    Tienes derecho a la tecnologia
#-------------------------------------------------
#-- Released under the LGPL license
#-- May, 2015
#-------------------------------------------------
#-- Alvaro Ferran
#-- Pighixxx
#-------------------------------------------------
#-- Upload your code to an ARM Mbed board
#--  with a LPC11u24 in GNU/Linux
#--
#--  1) Connect your board while pressing the 
#--	 button
#--  2) Find the path to your code, for example
#--	 "~/Downloads/blink.bin"
#--  3) Execute this script passing the path as 
#--	 an argument, for example: 
#--	 "python Mbed.py ~/Downloads/blink.bin" 
#--  4) Your code is uploaded!
#--------------------------------------------------

import sys
import os
import subprocess

fileName= sys.argv[1]											#The path to the code, eg. ~/Downloads/blink.bin

#-- Code to find the board automatically
allDevices = ''.join(subprocess.check_output(["df"])) 			#Find the devices mounted on our computer; return string with the results of 'df'
indexOfName=allDevices.find("CRP DISABLD") 						#Find the board's name; index of 'C'
indexOfLine=allDevices.rfind("\n",0, indexOfName) 				#Find the index our board's line beginning; index of last '\n' before 'C' 
indexOfSpace=allDevices.find(" ",indexOfLine)					#Find the index our board's name ending; index of first ' ' after '\n'
device=allDevices[indexOfLine+1:indexOfSpace]					#Find our board's device name; get substring of format '/dev/sdx' in correct line

os.system('umount %s' % (device))								#Unmounts the board 
os.system('sudo dd if=%s of=%s seek=4' % (fileName,device) )	#Uploads the code
