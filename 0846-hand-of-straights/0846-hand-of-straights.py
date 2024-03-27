class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hand = sorted(hand)
        while hand:
            h = hand[0]
            # print(hand)
            for i in range(groupSize):
                if h+i in hand:
                    hand.remove(h+i)
                else:
                    return False
        return True