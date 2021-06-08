# Car Fueling

You are going to travel to another city that is located d miles away from your home city. Your car can travel
at most m miles on a full tank and you start with a full tank. Along your way, there are gas stations at
distances stop 1 , stop 2 , . . ., stop n from your home city. What is the minimum number of refills needed?

### Example 1
```sh
Input: distance = 950, tank = 400, stops = [200, 375, 550, 750] 
Output: 2
Explanation: The distance between the cities is 950, the car can travel at most 400 miles on a full tank. It sufficesto make two refills: at points 375 and 750. This is the minimum number of refills as with a single refill one would only be able to travel at most 800 miles.
```

### Example 2
```sh
Input: distance = 10, tank = 3, stops = [1, 2, 5, 9] 
Output: -1
Explanation: One cannot reach the gas station at point 9 as the previous gas station is too far away.
```

### Example 3
```sh
Input: distance = 200, tank = 250, stops = [100, 150] 
Output: 0
Explanation: There is no need to refill the tank as the car starts with a full tank and can travel for 250 miles whereas the distance to the destination point is 200 miles.
```

### Constraints
```sh
1 <= distance <= 10^5
1 <= tank <= 400
1 <= length(stops) <= 300
0 < stop1 < stop2 < stop3 .... < stopN < distance. 
```
