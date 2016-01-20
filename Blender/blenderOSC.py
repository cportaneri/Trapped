#!/usr/bin/python3
import OSC # no use yet to go and see OSC.py file in folder
import math # general python module

IP = '127.0.0.1'
HOST = 12002
# ----------------------------------------------------------------
def carth2Polaire(x,y,z):
	rad2deg = 180/3.1416
	r = math.sqrt(x*x + y*y + z*z)
	phi = math.asin(y/r)
	if y == 0 and x < 0: teta = math.pi
	else: teta = 2*math.atan(x/(-z+math.sqrt(z*z + x*x)))
	r, theta, phi = round(r,1), round(teta*rad2deg,1), round(phi*rad2deg,1)
	return (r,theta,phi)
# ----------------------------------------------------------------
def adaptCoordSystem2SoundEngine(r,theta,phi):
	if theta < 0: theta_mod = -theta
	else: theta_mod = 360 - theta
	phi_mod = phi
	r_mod = r
	return (r_mod,theta_mod,phi_mod)
#--------------------------------------------
def getRelativePos(origin, targ):
	# get origin and targ Vect/Mat
	matRotTarget = targ.orientation
	vectPosTarget = targ.worldPosition
	matRotOwner = origin.worldOrientation
	vectPosOwner = origin.worldPosition
	# get Relative Vect/Mat
	InvMatRotOwner = matRotOwner.inverted()
	# matRelRot = vectPosTarget*matRotOwner
	vectRelPos = InvMatRotOwner*(vectPosTarget-vectPosOwner)
	return vectRelPos
# ----------------------------------------------------------------
def sendOscMsg(header,msg):
	client = OSC.OSCClient()
	msgPosPol = OSC.OSCMessage()
	msgPosPol.setAddress(header)
	msgPosPol.append(msg)
	client.sendto(msgPosPol,(IP, HOST))
	# print ('sent to ' + str(HOST) + '@' + IP + ' OSC msg: ' + str(msgPosPol))
	
	


