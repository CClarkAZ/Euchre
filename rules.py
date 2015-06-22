suits = ["club", "spade", "heart", "diamond"]
values = ["nine", "ten", "jack", "queen", "king", "ace"]
card_weights = {"nine": 9, "ten": 10, "jack": 11, "queen": 12, "king": 13, "ace": 14}

deck = []
trump_list = []

class Card(object):
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def __str__(self):
		return self.value + " of " + self.suit

	def __repr__(self):
		return str(self)

	def __cmp__(self, other):
		return self.suit == other.suit and self.value == other.value

	def __eq__(self, other):
		return self.suit == other.suit and self.value == other.value

for i in suits:
	for j in values:
		deck.append(Card(i, j))

hand = [Card("club", "jack"), Card("spade", "jack"), Card("spade", "ace"), Card("spade", "king"), Card("spade", "queen")]

def getOppositeTrumpSuit(trump_suit):
	if trump_suit == "club":
		return "spade"
	if trump_suit == "spade":
		return "club"
	if trump_suit == "heart":
		return "diamond"
	if trump_suit == "diamond":
		return "heart"

def getTrumpCardsList(trump_suit):
	# return list of trump in game scoring order
	if not trump_list:
		for v in values[0:2]:
			trump_list.append(Card(trump_suit, v))
		for v in values[3:5]:
			trump_list.append(Card(trump_suit, v))
		trump_list.append(Card(getOppositeTrumpSuit(trump_suit), "jack"))
		trump_list.append(Card(trump_suit, "jack"))

	return trump_list

def generateLegalMoves(hand, trump_suit, lead_suit):
	legal = []
	if lead_suit == None:
		return hand

	if trump_suit == lead_suit:
		trump_list = getTrumpCardsList(trump_suit)
		for card in hand:
			if card in trump_list:
				legal.append(card)

	else:
		for card in hand:
			if card.value == "jack" and card.suit == getOppositeTrumpSuit(trump_suit):
				continue
			if card.suit == lead_suit:
				legal.append(card)

	if len(legal) == 0:
		return hand

	return legal

def compareCards(card1, card2):
	# return the "higher" card, used for non trump
	if card1.suit != card2.suit:
		return None
	else:
		if card_weights[card1.value] > card_weights[card2.value]:
			return card1
		else:
			return card2


def scoreTrick(line, trump_suit):
	# score a trick and determine the winner. 
	# line is a list starting with the first player and advancing through each play sequentially
	played_trump = []
	trump_list = getTrumpCardsList(trump_suit)

	for c in line:
		if c in trump_list:
			played_trump.append(c)

	if len(played_trump) == 1:
		return played_trump[0]

	elif len(played_trump) > 1:
		highest_trump = played_trump[0]
		for p in played_trump[1:]:
			if trump_list.index(p) > trump_list.index(highest_trump):
				highest_trump = p
		return highest_trump
	else:
		max_played = line[0]
		for c in line[1:]:
			if c.suit != max_played.suit:
				continue
			else:
				if card_weights[c.value] > card_weights[max_played.value]:
					max_played = c
		return max_played



played_hand = [Card("heart", "jack"), Card("heart", "king"), Card("diamond", "jack"), Card("diamond", "ace")]


print(scoreTrick(played_hand, "diamond"))
