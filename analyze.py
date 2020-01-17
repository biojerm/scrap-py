#!/usr/bin/env python3

import pandas as pd
import numpy as np

sf = pd.read_csv("scrap.csv", encoding = "ISO-8859-1")
lf = pd.read_csv("lt.csv", encoding = "ISO-8859-1")


def get_resources_pn(pn): 
    l = lf[lf['PART_ID'].str.match(pn[:5],na=False)]['RESOURCE_ID'].unique()
    l.sort()
    return l

def get_resources_wo(wo): 
    l = lf[lf['WORKORDER_BASE_ID'].str.match(wo,na=False)]['RESOURCE_ID'].unique()
    l.sort()
    return l

def str_arr(arr):
    return ' '.join(str(s) for s in arr)

sf['ResourceList_byPN'] = sf.apply(lambda r: 
        str_arr(get_resources_pn(r.PART)), axis = 1)
sf['ResourceList_byWO'] = sf.apply(lambda r: 
        str_arr(get_resources_wo(r.WO)), axis = 1)

print(sf.to_csv())
