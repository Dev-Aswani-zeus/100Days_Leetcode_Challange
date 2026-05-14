class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        all_a2z_elements = {}

        for i in range(0,len(sentence)):
            all_a2z_elements[sentence[i]] = 1

        if len(all_a2z_elements) == 26:
            return True
        return False