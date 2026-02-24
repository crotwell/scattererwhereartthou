#!/usr/bin/env python

import taup
from scattererwhereartthou import SWAT, mapplot, sliceplot

# location of taup version 3 executable, not needed if already on PATH
taup_path="../../../seis/TauP/build/install/TauP/bin/taup"


model="prem"    # velocity model
evt=(66, 166)   # eq lat, lon
eventdepth=200  # eq depth
sta=(-11, 120)  # station lat, lon
phase="P"   # reference phase
max_dist_step=1.0 # max separation between path scatterers in degrees, default is 2 deg

slowrange=(4.5,4.8,0.2)  # min, max, step
delayrange=(5,7,1.0)     # min, max, step
bazoffset=3
bazdelta=0.5


with taup.TauPServer( taup_path=taup_path) as taupserver:
    print("starting...")
    params = taup.PathQuery()
    params.model(model)
    params.event(*evt)
    params.sourcedepth(eventdepth)
    params.station(*sta)
    params.phase(phase)
    timeResult = params.calc(taupserver)
    swatList = []
    for a in timeResult.arrivals:
        print(f"Arrival: {a}")
        swat = SWAT(taupserver, eventdepth, model=model)
        swat.event(*evt)
        swat.station(*sta)
        swat.dist_step = max_dist_step
        slow = slowrange[0]
        while slow <= slowrange[1]:
            delay = delayrange[0]
            while delay <= delayrange[1]:
                print(f"slow: {slow}  delay: {delay}")
                ans = swat.find_via_path(slow, a.time+delay, bazoffset=bazoffset, bazdelta=bazdelta)
                swatList.append(ans)
                delay += delayrange[2]
            slow += slowrange[2]
    mapplot(swatList, tauptimes=timeResult)
    sliceplot(swatList, tauptimes=timeResult)
