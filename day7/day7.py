from collections import Counter

def sort_hand_type(list_of_hand_lists,card_value_list):
    def value_of_hand(hand):
        return [card_value_list[card] for card in hand]
    return sorted(list_of_hand_lists, key = lambda x: value_of_hand(x[0])) #sort ascending so because lower cards have lower ranks

card_value = {'A' : 14, 'K' : 13, 'Q' : 12, 'J' : 11, 'T' : 10, '9' : 9, '8' : 8, '7' : 7, '6' : 6, '5' : 5, '4' : 4, '3' : 3, '2' : 2}
card_value_q2 = {'A' : 14, 'K' : 13, 'Q' : 12, 'T' : 10, '9' : 9, '8' : 8, '7' : 7, '6' : 6, '5' : 5, '4' : 4, '3' : 3, '2' : 2, 'J' : 1}

with open('day7_input.txt') as input:
    input_array = [row.replace('\n','') for row in input]
    all_hands = []
    for row in input_array:
        hand = row.split()[0]
        bid = int(row.split()[-1])
        all_hands.append([hand,bid])

    #Q1
    five_of_a_kind = []
    four_of_a_kind = []
    full_house = []
    three_of_a_kind = []
    two_pair = []
    one_pair = []
    high_card = []
    
    for hand in all_hands:
        freq = Counter(hand[0])
        if max(freq.values()) == 5:
            five_of_a_kind.append(hand)
        elif max(freq.values()) == 4:
            four_of_a_kind.append(hand)
        elif max(freq.values()) == 3:
            if min(freq.values()) == 2:
                full_house.append(hand)
            elif min(freq.values()) == 1:
                three_of_a_kind.append(hand)
        elif max(freq.values()) == 2:
            values = list(freq.values())
            if values.count(max(freq.values())) == 2:
                two_pair.append(hand)
            elif values.count(max(freq.values())) == 1:
                one_pair.append(hand)
        elif max(freq.values()) == 1:
            high_card.append(hand)

    five_of_a_kind = sort_hand_type(five_of_a_kind,card_value)
    four_of_a_kind = sort_hand_type(four_of_a_kind,card_value)
    full_house = sort_hand_type(full_house,card_value)
    three_of_a_kind = sort_hand_type(three_of_a_kind,card_value)
    two_pair = sort_hand_type(two_pair,card_value)
    one_pair = sort_hand_type(one_pair,card_value)
    high_card = sort_hand_type(high_card,card_value)

    all_ranks = high_card + one_pair + two_pair + three_of_a_kind + full_house + four_of_a_kind + five_of_a_kind
    q1_total = 0
    for rank,hand in enumerate(all_ranks,1):
        q1_total += hand[1]*rank

    print(q1_total)

    #Q2
    five_of_a_kind_q2 = []
    four_of_a_kind_q2 = []
    full_house_q2 = []
    three_of_a_kind_q2 = []
    two_pair_q2 = []
    one_pair_q2 = []
    high_card_q2 = []

    for hand in all_hands:
        freq = Counter(hand[0])
        freq_no_j = Counter(hand[0])
        freq_no_j.pop('J',None)
        if max(freq.values()) == 5 or max(freq_no_j.values()) + freq['J'] == 5: 
            five_of_a_kind_q2.append(hand)
        elif max(freq.values()) == 4 or max(freq_no_j.values()) + freq['J'] == 4:  
            four_of_a_kind_q2.append(hand)
        elif max(freq.values()) == 3 or max(freq_no_j.values()) + freq['J'] == 3:
            if (max(freq_no_j.values()) == 3 and min(freq_no_j.values()) == 2) or (max(freq_no_j.values()) == 2 and min(freq_no_j.values()) == 2 and freq['J'] == 1):
                full_house_q2.append(hand)
            elif min(freq_no_j.values()) == 1:
                three_of_a_kind_q2.append(hand)
        elif max(freq.values()) == 2 or max(freq_no_j.values()) + freq['J'] == 2:
            values = list(freq_no_j.values())
            if values.count(max(freq_no_j.values())) == 2:
                two_pair_q2.append(hand)  #technically wont have any two pairs with Jokers since any Jokers will make it three of a kind
            elif values.count(max(freq_no_j.values())) == 1 or freq['J'] == 1:
                one_pair_q2.append(hand)
        elif max(freq.values()) == 1 and 'J' not in freq:
            high_card_q2.append(hand)

    five_of_a_kind_q2 = sort_hand_type(five_of_a_kind_q2,card_value_q2)
    four_of_a_kind_q2 = sort_hand_type(four_of_a_kind_q2,card_value_q2)
    full_house_q2 = sort_hand_type(full_house_q2,card_value_q2)
    three_of_a_kind_q2 = sort_hand_type(three_of_a_kind_q2,card_value_q2)
    two_pair_q2 = sort_hand_type(two_pair_q2,card_value_q2)
    one_pair_q2 = sort_hand_type(one_pair_q2,card_value_q2)
    high_card_q2 = sort_hand_type(high_card_q2,card_value_q2)

    all_ranks_q2 = high_card_q2 + one_pair_q2 + two_pair_q2 + three_of_a_kind_q2 + full_house_q2 + four_of_a_kind_q2 + five_of_a_kind_q2
    q2_total = 0
    for rank,hand in enumerate(all_ranks_q2,1):
        q2_total += hand[1]*rank

    print(q2_total)
