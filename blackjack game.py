from random import randrange

def getCardInfo(card, cardType):
    if card == 11:
        cardNumber = "Jack"
    elif card == 12:
        cardNumber = "Queen"
    elif card == 13:
        cardNumber = "King"
    else:
        cardNumber = str(card)

    if cardType == 1:
        cardSuit = "Hearts"
    elif cardType == 2:
        cardSuit = "Clubs"
    elif cardType == 3:
        cardSuit = "Diamonds"
    else:
        cardSuit = "Spades"

    return cardNumber, cardSuit

def calculateCardTotal(card):
    if card == 1:
        return 11
    elif card > 10:
        return 10
    else:
        return card

def playGame():
    # Dealers first card
    dealerCard = randrange(1, 14)
    dealerCardType = randrange(1, 5)
    dealerCardNumber, dealerCardSuit = getCardInfo(dealerCard, dealerCardType)
    dealerCardTotal = calculateCardTotal(dealerCard)

    if dealerCard == 1:
        dealerCardTotal = 11
        print("The dealer has an Ace of", dealerCardSuit + "!\n")
    else:
        print("The dealer has a", dealerCardNumber, "of", dealerCardSuit + "!\n")

    # Dealers < 17 cards
    dealerCards = [(dealerCardNumber, dealerCardSuit)]

    while dealerCardTotal < 17:
        card = randrange(1, 14)
        cardType = randrange(1, 5)
        cardNumber, cardSuit = getCardInfo(card, cardType)
        cardTotal = calculateCardTotal(card)

        if card == 1:
            if dealerCardTotal + 11 <= 21:
                cardTotal = 11
            else:
                cardTotal = 1

        dealerCardTotal += cardTotal
        dealerCards.append((cardNumber, cardSuit))

    # Remove the # to see dealers cards
    # print("Dealer's cards: (debugging)")
    # for cardNumber, cardSuit in dealerCards:
    #     print("{} of {}".format(cardNumber, cardSuit))
    #
    # print("Total points for the dealer:", dealerCardTotal, "\n")

    # Players cards
    total = 0
    while True:
        play = input("Draw cards? ")

        if play.lower() not in ["yes", "draw"]:
            break

        card = randrange(1, 14)
        cardType = randrange(1, 5)
        cardNumber, cardSuit = getCardInfo(card, cardType)
        cardTotal = calculateCardTotal(card)

        if card == 1:
            cardTotal = int(input("You got an Ace of " + cardSuit + "!\nChoose 1 or 11 points: "))
        else:
            print("You got a", cardNumber, "of", cardSuit + "!")
        total += cardTotal
        print("You have a total of", total, "points!\n")

        if total > 21:
            print("You Bust! You lost the game!")
            print("Total points for the dealer:", dealerCardTotal)
            return

        if dealerCardTotal > 21:
            print("Dealer Bust! You won the game!")
            print("Total points for the dealer:", dealerCardTotal)
            return

    if total > dealerCardTotal:
        print("Total points for the dealer:", dealerCardTotal)
        print("You Win!")
    elif total < dealerCardTotal:
        print("Total points for the dealer:", dealerCardTotal)
        print("You Lost!")
    elif total == dealerCardTotal:
        print("Total points for the dealer:", dealerCardTotal)
        print("You tied!")


playGame()
