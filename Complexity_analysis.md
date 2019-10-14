#  Compare Real Social Systems With Simulated Systems
---

+ Athena Simulations (TA1 GT Data) vs Crime Data

1. Z-omplexity Meassure (How big/complex the models are): median/mean statespace size
   (json_read)

2. I-complexity: number of models generated (how many models above a gamma threshold:0.001)

Crime: focus on violent and non-violent  
TA1: focus on visitors, meetings (at site)

3. model how much hiostory we need to get a certain performance.
  + rereun crime data with 1 yr, 5 yrs (oos remains same)
  + rerun TA1 data 1/3 1/2 2/3 of the last part of insample data (oos remans same)
  
4. Z/I-complexity vs data-size (zipp the time series data) vs performance


```
 ~/ZED/Research/cynet_/bin/json_read -h
Usage: :
  -h [ --help ]               print help message.
  -V [ --version ]            print version number
  -v [ --verbose ]            verbose
  -p [ --stateprob ] arg      state probability vector on xpfsa [uniform]
  -j [ --jsonfile ] arg       json file []
  -l [ --listprop ] arg       list properties [on]
  -m [ --modelfiles ] arg     produce individual model files [off]
  -s [ --csvoutput ] arg      produce csvstyle output with header [off]
  -i [ --listindividual ] arg list individual files [off]

```


```
~/ZED/Research/cynet_/bin/json_read -j ~/ZED/Research/crimepred_/models/2014_2016_60/0model.json -i on

```


