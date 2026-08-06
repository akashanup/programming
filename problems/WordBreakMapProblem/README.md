# Word Break Map Problem

Given a list of words return a Map of words which can be formed by using other words which exist in the same list. 

### Example 1
```sh
Input = ["happy", "rise", "for", "set", "sunrise", "su", "nset", "sunset", "mind", "happymind", "n", "rise", "happysunrise"]

Output = {
  'nrise': [['n', 'rise']], 
  'sunrise': [['su', 'nrise'], ['su', 'n', 'rise']], 
  'nset': [['n', 'set']], 
  'sunset': [['su', 'nset'], ['su', 'n', 'set']], 
  'happymind': [['happy', 'mind']], 
  'happysunrise': [['happy', 'sunrise'], ['happy', 'su', 'nrise'], ['happy', 'su', 'n', 'rise']]
}
```
