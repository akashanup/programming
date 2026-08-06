class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Initialize both the basket with values as [fruitType, fruitTypeCount, lastIndexOfThisFruitType]
        basket1, basket2 = [None, 0, -1], [None, 0, -1]
        maxFruits = 0

        for end, fruitType in enumerate(fruits):
            if basket1[0] is None:
                # Fill first basket
                basket1 = [fruitType, 1, end]
            elif basket2[0] is None and fruitType != basket1[0]:
                # Fill second basket
                basket2 = [fruitType, 1, end]
            else:
                if basket1[0] == fruitType:
                    basket1[1] += 1
                    basket1[2] = end
                elif basket2[0] == fruitType:
                    basket2[1] += 1
                    basket2[2] = end
                else:
                    maxFruits = max(maxFruits, basket1[1]+basket2[1])
                    
                    # A new fruit type is encountered. Need to empty one of the baskets to store fruits of this new fruit type.
                    # Since we have to maintain the sequence as mentioned in the question- "Once you reach a tree with fruit that cannot fit in your baskets, you must stop."
                    # We need to empty the basket of that fruitType whose last index is smaller than other.
                    if fruits[end-1] == basket1[0]:
                        # Eligible number of fruits of basket1 would be those fruits which occurred after the lastIndex of basket2.
                        basket1[1] = end - basket2[2] - 1
                        # Empty basket2 and store new fruit type into it.
                        basket2 = [fruitType, 1, end]
                    else:
                        # Eligible number of fruits of basket2 would be those fruits which occurred after the lastIndex of basket1.
                        basket2[1] = end - basket1[2] - 1
                        # Empty basket1 and store new fruit type into it.
                        basket1 = [fruitType, 1, end]

        maxFruits = max(maxFruits, basket1[1]+basket2[1])
        return maxFruits
