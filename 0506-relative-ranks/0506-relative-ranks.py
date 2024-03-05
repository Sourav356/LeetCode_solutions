class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        rank_dict = {score: str(i + 1) for i, score in enumerate(sorted_score)}
            
        ranks = []
        for s in score:
            rank = rank_dict[s]
            if rank == '1':
                ranks.append("Gold Medal")
            elif rank == '2':
                ranks.append("Silver Medal")
            elif rank == '3':
                ranks.append("Bronze Medal")
            else:
                ranks.append(rank)
                
        return ranks
        