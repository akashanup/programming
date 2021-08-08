# Job Sequencing Problem

Given a set of n jobs where each job i has a deadline di >=1 and profit pi>=0. Only one job can be scheduled at a time. 
Each job takes 1 unit of time to complete. 
We earn the profit if and only if the job is completed by its deadline. 
The task is to find the subset of jobs that maximizes profit.

### Example 1
```sh
Input: Four Jobs with following deadlines and profits
JobID Deadline Profit
   a      4      20
   b      1      10
   c      1      40
   d      1      30
Output: Following is maximum profit sequence of jobs:
       c, a
```

### Example 2
```sh
Input: Five Jobs with following deadlines and profits
JobID Deadline Profit
   a     2       100
   b     1       19
   c     2       27
   d     1       25
   e     3       15
Output: Following is maximum profit sequence of jobs:
       c, a, e
```
