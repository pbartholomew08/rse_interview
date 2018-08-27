"""
.. module:: checkout
.. module-author:: Paul Bartholomew
"""

#
# Define offers
#

def apple_offer(n, price_peritem):
	""" Given the total number of apples, compute the price after applying offer. """

	offer_per = 3
	offer_price = 2 * price_peritem

	n_full = n % offer_per
	n_offer = (n - n_full) / offer_per

	return price_peritem * n_full + offer_price * n_offer

def banana_offer(n, price_peritem):
	""" Given the total number of bananas, compute the price after applying the offer. """

	offer_per = 3
	offer_price = 100

	n_full = n % offer_per
	n_offer = (n - n_full) / offer_per

	return price_peritem * n_full + offer_price * n_offer

#
# Set prices and any offers
#

PRICE_LIST = {"A":25, "B":40, "P":30}
OFFERS = {"A":apple_offer, "B":banana_offer}

#
# checkout function, users should not have to modify
#

def checkout(itemcodes, price_list=PRICE_LIST):
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
		p = price_list[item]
		if item in OFFERS:
			total += OFFERS[item](n, p)
		else:
			total += p * n

	return total

#
# Checkout class
#
class Checkout(object):
	""" Checkout class definition, takes a pricelist for instantiation and provides scan(itemcode) and
	total() methods."""

	def __init__(self, price_list):
		""" Instantiate a new Checkout object. """
		self.price_list = price_list
		self.scanned_items = []

	def scan(self, itemcode):
		""" Scan an item. """
		self.scanned_items.append(itemcode)

	def total(self):
		""" Return the total cost of scanned items. """
		return checkout(self.scanned_items, self.price_list)
