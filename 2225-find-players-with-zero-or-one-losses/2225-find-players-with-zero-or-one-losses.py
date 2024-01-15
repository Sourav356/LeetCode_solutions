class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        all_players =set()
        loss_count = {}
        for winner, loser in matches:
            all_players.add(winner)
            all_players.add(loser)
            loss_count[loser] = loss_count.get(loser,0) + 1
    
        zero_losses =[player for player in all_players if player not in loss_count]
        one_loss = [player for player in loss_count if loss_count[player] == 1]
        zero_losses.sort()
        one_loss.sort()
        
        return [zero_losses,one_loss]