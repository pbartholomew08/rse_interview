"""
.. module:: checkout
.. module-author:: Paul Bartholomew
"""

#
# Define offers
#

def apple_offer(n, price_peritem):
	""" Given the total number of apples, compute the price after applying offer. """

	n_offer = 2 * (n / 3)
	n_full = n - 3 * (n / 3)
	return price_peritem * (n_full + n_offer)

def banana_offer(n, price_peritem):
	""" Given the total number of bananas, compute the price after applying the offer. """

	n_offer = n / 3
	n_full = n - 3 * (n / 3)
	return price_peritem * n_full + 100 * n_offer

#
# Set prices and any offers
#

PRICE_LIST = {"A":25, "B":40, "P":30}
OFFERS = {"A":apple_offer, "B":banana_offer}

#
# checkout function, users should not have to modify
#

def checkout(itemcodes, prices=PRICE_LIST):
	""" Given a list of item codes and a dictionary of their prices, return the total cost, after
	applying any offers.
	"""

	# Handle single item code being passed as a string
	if not isinstance(itemcodes, list):
		itemcodes = [itemcodes]

	# Compute total number of items
	item_totals = {}
	for item in itemcodes:
		if not item in item_totals.keys():
			item_totals[item] = 0
		item_totals[item] += 1

	# Compute total
	total = 0
	for item in item_totals:
		n = item_totals[item]
		p = prices[item]
		if item in OFFERS:
			total += OFFERS[item](n, p)
		else:
			total += p * n

	return total
