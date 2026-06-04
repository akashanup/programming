# LeetCode Agent

This repository now includes a local scaffold generator at [tools/leetcode_agent.py](../tools/leetcode_agent.py).

## What it does

When you finish a problem, run the script with the problem title. It will:

- create a new problem folder and README in step 1
- write `README.md`
- update the root [README.md](../README.md) index in step 2
- create a commit and push it in step 2

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

1. Run the script with a LeetCode problem or submission URL with `--step 1`.
2. Manually create `solution.py` inside the generated folder.
3. Run the script again with `--step 2` to update the root index, create a commit, and push.
