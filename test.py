import collections
from typing import List




def groupAnagrams(strs):
    ans = collections.defaultdict(list)
    print(ans)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        print(tuple(count))
        ans[tuple(count)].append(s)
        print(ans)
    return ans.values()


if __name__ == '__main__':
    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
