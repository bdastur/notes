#!/usr/bin/env python
# -*- coding: utf-8 -*-
VLCifWIbQH=False
VLCifWIbQc=True
def getPrimeNumber(num):
 VLCifWIbQd=[]
 VLCifWIbQx=0
 VLCifWIbQl=2
 while VLCifWIbQx<num:
  VLCifWIbQT=VLCifWIbQH
  for x in VLCifWIbQd:
   if VLCifWIbQl%x==0:
    VLCifWIbQT=VLCifWIbQc
    break
  if not VLCifWIbQT:
   VLCifWIbQd.append(VLCifWIbQl)
   VLCifWIbQx+=1
  VLCifWIbQl+=1
 return VLCifWIbQd[-1]
# Created by pyminifier (https://github.com/liftoff/pyminifier)
