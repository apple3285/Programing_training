#백준 - 카드셋트(https://www.acmicpc.net/problem/11507)
cards = input()
now = 0
card_list =[]
while now < len(cards):
    card_list.append(cards[now:now+3])
    now +=3
card_cnt = {"P":13, "K":13,"H":13,"T":13}
for card in card_list:
    if 1 < card_list.count(card):
        print("GRESKA")
        exit()
    
    else:
        card_cnt[card[0]] -= 1

print("%d %d %d %d" %(card_cnt["P"], card_cnt["K"] ,card_cnt["H"] ,card_cnt["T"]))
