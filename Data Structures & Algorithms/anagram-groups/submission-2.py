class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == [""]:
             return [[""]]

        groups = {}

        for i in strs:
            key = "".join(sorted(i))

            if key not in groups:
                groups[key] = []

            groups[key].append(i)
        return list(groups.values())
            # if len(s) != len(t):
            #     return False

            # countS, countT = {}, {}
            # for i in range(len(s)):
            #     countS[s[i]] = 1 + countS.get(s[i], 0)
            #     countT[t[i]] = 1 + countT.get(t[i], 0)
            # for c in countS:
            #     if countS[c] != countT.get(c, 0):
            #         return False

            # return True
        