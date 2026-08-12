class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        storage = {}

        for string in strs:
            sorted_string = ''.join(sorted(string))

            if sorted_string not in storage:
                storage[sorted_string] = [string]
            else:
                storage[sorted_string].append(string)

        return  list(storage.values())
            

        