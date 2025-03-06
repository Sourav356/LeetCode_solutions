class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        mainlist = []
        for row in grid:
            mainlist.extend(row)

    # Step 2: Sort the list
        mainlist.sort()

    # Step 3: Identify duplicates and missing numbers
        duplicates = []
        missing = []
        seen = set()

        for num in mainlist:
            if num in seen:
                duplicates.append(num)  # Found a duplicate
            seen.add(num)

    # Find missing numbers in the expected sequence
        expected_num = 1
        while len(missing) < len(duplicates):  # Need the same count as duplicates
            if expected_num not in seen:
                missing.append(expected_num)
            expected_num += 1

    # Step 4: Replace duplicates with missing numbers
    # modified_list = mainlist[:]
    # for i in range(len(modified_list)):
    #     if modified_list[i] in duplicates:
    #         modified_list[i] = missing.pop(0)  # Replace duplicate with missing number
    #         duplicates.remove(modified_list[i])  # Remove from duplicates list

        return duplicates+ missing 