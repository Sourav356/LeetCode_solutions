MOD = 10**9 + 7
class Solution:
    def checkRecord(self, n: int) -> int:
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]
        dp[0][0][0] = 1  # Base case: empty sequence

        for length in range(1, n + 1):
            for absent in range(2):
                for late in range(3):
                # Adding a 'P'
                    dp[length][absent][0] = (dp[length][absent][0] + dp[length - 1][absent][late]) % MOD

                # Adding an 'A'
                    if absent < 1:
                        dp[length][absent + 1][0] = (dp[length][absent + 1][0] + dp[length - 1][absent][late]) % MOD

                # Adding an 'L'
                    if late < 2:
                        dp[length][absent][late + 1] = (dp[length][absent][late + 1] + dp[length - 1][absent][late]) % MOD

        total_valid_records = 0
        for absent in range(2):
            for late in range(3):
                total_valid_records = (total_valid_records + dp[n][absent][late]) % MOD

        return total_valid_records
        