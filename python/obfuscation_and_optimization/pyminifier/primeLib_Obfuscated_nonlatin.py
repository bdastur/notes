#!/usr/bin/env python
# -*- coding: utf-8 -*-
𞡋𩉀𦅸𐬃𪫀ﱏ명𪠨𗠑𐠌=False
𞡋𩉀𦅸𐬃𪫀ﱏ명𪠨𗠑ﵮ=True
def 𞡋𩉀𦅸𐬃𪫀ﱏ명𪠨𗠑ﭝ(num):
 𞡋𩉀𦅸𐬃𪫀ﱏ명𪠨𗠑ࡑ=[]
 𞡋𩉀𦅸𐬃𪫀ﱏ명𪠨𗠑춬=0
 𞡋𩉀𦅸𐬃𪫀ﱏ명𪠨𗠑ಖ=2
 while 𞡋𩉀𦅸𐬃𪫀ﱏ명𪠨𗠑춬<num:
  𞡋𩉀𦅸𐬃𪫀ﱏ명𪠨𗠑𞸕=𞡋𩉀𦅸𐬃𪫀ﱏ명𪠨𗠑𐠌
  for x in 𞡋𩉀𦅸𐬃𪫀ﱏ명𪠨𗠑ࡑ:
   if 𞡋𩉀𦅸𐬃𪫀ﱏ명𪠨𗠑ಖ%x==0:
    𞡋𩉀𦅸𐬃𪫀ﱏ명𪠨𗠑𞸕=𞡋𩉀𦅸𐬃𪫀ﱏ명𪠨𗠑ﵮ
    break
  if not 𞡋𩉀𦅸𐬃𪫀ﱏ명𪠨𗠑𞸕:
   𞡋𩉀𦅸𐬃𪫀ﱏ명𪠨𗠑ࡑ.append(𞡋𩉀𦅸𐬃𪫀ﱏ명𪠨𗠑ಖ)
   𞡋𩉀𦅸𐬃𪫀ﱏ명𪠨𗠑춬+=1
  𞡋𩉀𦅸𐬃𪫀ﱏ명𪠨𗠑ಖ+=1
 return 𞡋𩉀𦅸𐬃𪫀ﱏ명𪠨𗠑ࡑ[-1]
# Created by pyminifier (https://github.com/liftoff/pyminifier)
