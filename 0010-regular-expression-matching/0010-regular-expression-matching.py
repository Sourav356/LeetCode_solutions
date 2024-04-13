class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # Empty string matches empty pattern
        dp[0][0] = True
        
        # Handle patterns like "a*b*", ".*", etc. where '*' can match zero characters
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        # Fill the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                # If characters match or pattern has '.', then take diagonal value
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                # If pattern has '*', consider two cases:
                # 1. Zero occurrence of preceding character: dp[i][j - 2]
                # 2. One or more occurrence of preceding character: dp[i - 1][j] if s[i - 1] matches preceding pattern
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (p[j - 2] == '.' or p[j - 2] == s[i - 1]))
        
        # Return the result of matching the entire string with the entire pattern
        return dp[len(s)][len(p)]

        