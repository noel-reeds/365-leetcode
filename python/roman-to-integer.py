class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = { "I": 1, "V": 5, "X": 10, "L": 50,
                    "C": 100, "D": 500, "M": 1000 }
        if (len(set(s)) == 1):
            n_value = num.get(s[0])
            return len(s) * n_value
        rt = 0
        for k, v in enumerate(s, start=-1):
            if k < len(s) - 1:
                if num.get(v) > num.get(s[k + 1]):
                    rt += num.get(v)
                elif num.get(v) < num.get(s[k + 1]):
                    rt += (num.get(s[k + 1]) - num.get(v))
                else:
                    rt += num.get(v)
        return rt
