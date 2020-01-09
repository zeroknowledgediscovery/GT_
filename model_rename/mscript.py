#!/usr/bin/python

from cynet.cynet import uNetworkModels as models
import pandas as pd
import numpy as np
import json
from tqdm import tqdm
import glob

def getModelSet(FILES,UID,CORR,write=True,NUM_MODELS=20,
                reverse=False,high=None,low=None,var='gamma',
                VARLIST=['MeetFrac','singles'],
                TGTLIST=['myFriends']):
    outFile='model'+UID+'.json'
    
    Ms=[models(f) for f in tqdm(FILES)]
    for i in Ms[1:]:
        Ms[0].append(i.models)
    M=Ms[0]
    
    D={}
    count=0
    for (key,value) in tqdm(M.models.iteritems()):
        srctgt=key.split("_")

        src=srctgt[1]
        tgt=srctgt[2]

        srcvar=src.split('#')[4]
        tgtvar=tgt.split('#')[4]

        #print srcvar,tgtvar
        if srcvar not in VARLIST:
            continue
        if tgtvar not in TGTLIST:
            continue

        #CORR=CORR+[UID]
        for corr_uid in CORR:
            print corr_uid
            new_key='_'+corr_uid+'#'+srcvar+'_'+UID+'#'+tgtvar+str(count)\
            +'_'+srctgt[3]\
            +'_'+srctgt[4]
            M.models[key]['src']=corr_uid+'#'+srcvar
            M.models[key]['tgt']=UID+'#'+tgtvar
            #print new_key
            D[new_key]=M.models[key]
            count=count+1


    n=NUM_MODELS
    
    this_dict={value[var]:key
               for (key,value) in D.iteritems() }

    if low is not None:
        this_dict={key:this_dict[key] for key in this_dict.keys() if key >= low }
    if high is not None:
        this_dict={key:this_dict[key] for key in this_dict.keys() if key <= high }

    if n is None:
        n=len(this_dict)
    if n > len(this_dict):
        n=len(this_dict)

    out = {this_dict[k]:D[this_dict[k]]
           for k in sorted(this_dict.keys(),
                           reverse=reverse)[0:n]}
                
    if write:
        with open(outFile,'w') as outfile:
            json.dump(out, outfile)
    return out



FILES=glob.glob('./fmodels/*model.json')
CORR_UIDS=['x123','x125','x321','x456']
UID='xxx12'

varlist=['meetingPairs','singles','MeetFrac']

getModelSet(FILES=FILES,UID=UID,CORR=CORR_UIDS,
            reverse=True,high=0.95,
            NUM_MODELS=300,
            VARLIST=varlist)
