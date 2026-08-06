# LeetCode Agent

This repository now includes a local scaffold generator at [tools/leetcode_agent.py](../tools/leetcode_agent.py).

## What it does

When you finish a problem, run the script with the problem title. It will:

**Step 1:**
- create a new problem folder and README
- write `README.md` with problem statement and metadata
- create an empty `solution.py` file

**Step 2:**
- update the root [README.md](../README.md) index with the problem details
- create a commit with the problem name as the message
- push to the repository

If you pass a LeetCode problem URL or a submission URL, the script will fetch
the problem metadata from LeetCode and use it to populate the new folder.

## Examples

```powershell
python tools/leetcode_agent.py "https://leetcode.com/problems/binary-gap/description/"
```

```powershell
python tools/leetcode_agent.py "https://leetcode.com/problems/binary-gap/description/" --step 1
```

```powershell
python tools/leetcode_agent.py "Binary Gap" --step 2
```

```powershell
python tools/leetcode_agent.py "https://leetcode.com/problems/binary-gap/solutions/8313119/simple-python-solution-beats-100-by-akas-zqtr" --step 1
```

```powershell
python tools/leetcode_agent.py "K-diff Pairs in an Array" --folder K-DiffPairsInAnArray
```

## Recommended flow

1. Run the script with a LeetCode problem or submission URL with `--step 1` (creates folder, README.md, and empty solution.py)
2. Add your solution code to `solution.py`
3. Run the script again with `--step 2` (updates root index, creates commit with problem name, and pushes)
