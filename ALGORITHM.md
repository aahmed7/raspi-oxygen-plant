## Main algorithm(One round)
- step 1: Inlet
- step 2: Outlet
- step 3: Balance

- One round is one run for left tank and one run for right.
- The time for each stage is user-defined, and adjusted automatically during auto-process(multiples of 7)


## Controlling factors
- 5 Pressure sensors(airtank, inlet, gen left tank, gen right tank, oxygen tank)
- oxygen purity sensor

## System startup 
When the system is first started, there will be no existing pressure in the generator tanks. So we need to build up the intial pressure. This is done by running a number of user defined rounds, while skipping the outlet stage

## Pressure exceeds on tank sensor
If the pressure on any gen tank exceeds the limit, skip the inlet stage for that tank

## Pressure is out of ranges on airtank or inlet sensor
Pause the process

## Pressure exceeds on the oxygen tank
Pause the process