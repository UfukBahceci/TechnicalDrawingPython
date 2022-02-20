import math
def calculatefromratios_thetaphi(ratios):
  r1square=(float(ratios[0])/float(ratios[1]))**2
  r2square=(float(ratios[2])/float(ratios[1]))**2
  phi=-math.acos(math.sqrt(2/(1+r1square+r2square)))
  asquare=math.cos(phi)**2
  theta=math.asin(math.sqrt((1-asquare*r1square)/asquare))
  return [theta, phi]