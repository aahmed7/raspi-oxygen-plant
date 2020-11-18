## Sensors
- P1 - air tank
- P2 - inlet of air to oxygen tank
- P3 - OG left
- P4 - OG right
- P5 - Oxygen tank
- O1 - Oxygen tank

## Sensor functions
- If 5 < P1 < 8 , OXYGEN_GEN => ON
- If 5 < P2 < 8 , OXYGEN_GEN => ON
- If P5 < 4 => Fill O2 tank else if P5 >= 8 => standby

## Oxygen generator algorithm
- Inlet for N sec
- Balance
- Extract to O2 Tank

## Valves
- V1 - left in  
- V2 - right in
- V3 - balance 1
- V4 - balance 2
- V5 - left out
- V6 - right out

## Valve GPIOs:
12, 16, 18, 22, 24, 32