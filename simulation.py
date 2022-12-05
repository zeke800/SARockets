import math
#Calculate center of pressure.
#http://mae-nas.eng.usu.edu/MAE_5900_Web/5900/USLI_2010/Flight_Mechanics/Barrowman.html
#Created originally by ____ and edited by Zeke800
#coneType is either 'cone' or 'ogive'
#roundDigits is either a number (the number of digits to be rounded to) or False (no rounding).
def barrowmanEquation(cpvars,coneType='cone',roundDigits = False):
    #Nose Cone Terms
    cnn = 2
    conexn = 2/3*cpvars[0]
    ogivexn = 7/15*cpvars[0]
    # Original values were:
    #conexn = 0.666*ln
    #ogivexn = 0.466*ln
    
    #Conical Transition Terms
    cnt = 2*abs(((cpvars[3]/cpvars[1])**2)-((cpvars[2]/cpvars[1])**2))
    xt = cpvars[5]+(cpvars[4]/3)*abs(1+(1-(cpvars[2]/cpvars[3]))/(1-((cpvars[2]/cpvars[3])**2)))
    
    # EXASPERATING!

    # Fin terms
    cnf = (1+(r/(cpvars[8]+cpvars[10]))*((4*n*((s/d)**2))/(1+math.sqrt(1+((2*cpvars[9])/(cpvars[7]+cpvars[6]))))))
    xf = cpvars[12]+(cpvars[11]/3)*(cpvars[6]+2*cpvars[7])/(cpvars[6]+cpvars[7])+(1/6)*((cpvars[6]+cpvars[7])-(cpvars[6]*cpvars[7])/(cpvars[6]+cpvars[7]))

    # One of the final equations
    cnr = cnn + cnt + cnf

    # Determing cone type and setting Xn
    if coneType.lower() == 'cone':
        xn = conexn
    if coneType.lower() == 'ogive':
        xn = ogivexn
        
    centerOfPressure = (cnn*xn+cnt*xt+cnf*xf)/cnr
    
    if roundyn:
        return round(centerOfPressure, ndigits=roundDigits)
    else:
        
        return centerOfPressure
    return cp
# Center of Gravity Function.
# https://www.grc.nasa.gov/WWW/k-12/rocket/rktcg.html
# Here is an example of the partList: [[40,30,'Rocket fins'],[50,10,'Rocket cone']]. partList is NOT a numpy array.
def cg(partList, weightOfRocket):
    #print("ALL measurments below to be measured from tip of nose cone.")

    
    cgw = 0
    for i in range(len(partList)):
        cgw = cgw + partList[i][0]*partList[i][1]
    cg = cgw/weightOfRocket
    

    

    
