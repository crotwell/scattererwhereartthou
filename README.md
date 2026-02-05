# scattererwhereartthou
Find possible scatterers from slowness and back azimuth

# Requirement
This makes use of the TauP Toolkit for the path and time calculations and the version must be > 3.2.0.

# Install
I assume you are on a vaguely *nix like system, are using conda,
and can do normal download and install activities.

1) Install version 3.2.0-snapshot4 or greater of the TauP Toolkit.
This is available here:
https://www.seis.sc.edu/downloads/TauP/prerelease/TauP-3.2.0-SNAPSHOT4.tgz

2) Probably put the TauP/bin on your path, although you can override this

3) Grab the latest taup_python package, here:
https://www.seis.sc.edu/downloads/TauP/prerelease/taup-0.2.0a1-py3-none-any.whl

4) create a conda environment, python>=3.11, install taup_python
conda create -n swat python=3.11
conda activate swat
pip install taup-0.2.0a1-py3-none-any.whl

5) checkout this repo, install it
git clone https://github.com/crotwell/scattererwhereartthou.git
cd scattererwhereartthou
pip install -v -e .

6) run the example tool
```
swat --evt -1 -101 --sta 34 -80 --delay 5 --map swat.png  --slow 8.0 --mindepth 500 --showmap
```

There are more options:
```
swat -h
usage: swat [-h] [-v] [-c CONF] [--eventdepth EVENTDEPTH] --evt EVT EVT --sta STA STA [-p PHASE] --delay DELAY --slow SLOW
            [--mindepth MINDEPTH] [--model MODEL] [--taup TAUP] [--json JSON] [--map MAP] [--showmap] [--slice SLICE]
            [--showslice]

Find possible scatterers. Version=0.0.1

options:
  -h, --help            show this help message and exit
  -v, --verbose         increase output verbosity
  -c CONF, --conf CONF  Configuration as TOML
  --eventdepth EVENTDEPTH
                        event depth.
  --evt EVT EVT         event latitude and longitude.
  --sta STA STA         station latitude and longitude.
  -p PHASE, --phase PHASE
                        reference phase.
  --delay DELAY         time delay of arrival relative to reference phase.
  --slow SLOW           observed slowness of suspected scatterer (s/deg)
  --mindepth MINDEPTH   minimum depth of suspected scatterer (km)
  --model MODEL         earth model, as used by TauP.
  --taup TAUP           path to the TauP executable.
  --json JSON           output to json file
  --map MAP             output as matplotlib map
  --showmap             show matplotlib map to screen
  --slice SLICE         output as matplotlib polar slice
  --showslice           show matplotlib polar slice to screen
```
