n = int (input())
sereja_score = 0
dima_score = 0
cards = list(map(int, input().split()))
serejas_turn = True
 
while len(cards) > 0:
    if cards[0] > cards[-1]:
        card_chosen = cards.pop(0)
    else:
        card_chosen = cards.pop()
    if serejas_turn:
        sereja_score += card_chosen
    else:
        dima_score += card_chosen
    serejas_turn = not serejas_turn
print(sereja_score, dima_score)
