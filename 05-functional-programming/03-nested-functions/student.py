from util import count, indices_of

def count_older_than(people, min_age):
    def old_enough(person):
        if person.age >= min_age:
            return True
        return False
    return count(people, old_enough)

def indices_of_cards_with_suit(cards, suit):
    def is_suited(card):
        if card.suit == suit:
            return True
        return False
    return indices_of(cards, is_suited)