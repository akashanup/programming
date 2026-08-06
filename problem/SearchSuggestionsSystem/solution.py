class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = sorted(products)
        result = []
        for key in range(len(searchWord)):
            tempResult = []
            for product in products:
                if product.startswith(searchWord[0:key + 1]):
                    tempResult.append(product)
                if len(tempResult) == 3:
                    break
            result.append(tempResult)
        return result
