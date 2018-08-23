"""
.. module:: checkout
.. module-author:: Paul Bartholomew
"""

PRICE_LIST = {"A":25, "B":40, "P":30}

def checkout(itemcodes, prices=PRICE_LIST):
	""" Given a list of item codes and a dictionary of their prices, return the total cost, after
	applying any offers.
	"""

	# Handle single item code being passed as a string
	if not isinstance(itemcodes, list):
		itemcodes = [itemcodes]

	# Compute total
	total = 0
	for item in itemcodes:
		total += prices[item]

	return total
