"""
.. module:: tests
.. synopsis:: tests for checkout
.. module-author:: Paul Bartholomew
"""

import unittest
import rse_interview.checkout as checkout

class test_checkout_fns(unittest.TestCase):

	def setUp(self):
		pass
	def tearDown(self):
		pass

	def test_newitem(self):
		""" Test the pricing of a single item is correct. """

		item_name = "foo"
		item_price = 11

		checkout_total = checkout.checkout(item_name, {item_name:item_price})
		self.assertEqual(checkout_total, item_price)

	def test_offers(self):
		""" Test the offers applied to apple and banana. """

		price_apple = 25
		price_banana = 40

		#
		# Test offer price of 2, 3, and 4 apples:
		#   2 apples: no offer
		#   3 apples: 2 for 3 offer
		#   4 apples: 2 for 3 offer + 1
		#
		offer_apple = checkout.apple_offer(2, price_apple)
		self.assertEqual(offer_apple, 2 * price_apple)
		offer_apple = checkout.apple_offer(3, price_apple)
		self.assertEqual(offer_apple, 2 * price_apple)
		offer_apple = checkout.apple_offer(4, price_apple)
		self.assertEqual(offer_apple, 3 * price_apple)

		#
		# Test offer price of 2, 3, and 4 bananas:
		#   2 apples: no offer
		#   3 apples: 3 for 100p offer
		#   4 apples: 3 for 100p offer + 1
		#
		offer_banana = checkout.banana_offer(2, price_banana)
		self.assertEqual(offer_banana, 2 * price_banana)
		offer_banana = checkout.banana_offer(3, price_banana)
		self.assertEqual(offer_banana, 100)
		offer_banana = checkout.banana_offer(4, price_banana)
		self.assertEqual(offer_banana, 100 + price_banana)

	def test_std(self):
		""" Test the input provided in the task.  """

		purchase_list = ["B", "A", "B", "P", "B"]
		price_dict = {"A":25, "B":40, "P":30}
		expected_total = 155

		checkout_total = checkout.checkout(purchase_list, price_dict)
		self.assertEqual(expected_total, checkout_total)

	def test_Checkout(self):
		""" Test the Checkout class. """

		# Test initialisation
		teller = checkout.Checkout({"A":25, "B":40, "P":30})
		self.assertTrue("A" in teller.price_list)
		self.assertTrue("B" in teller.price_list)
		self.assertTrue("P" in teller.price_list)
		self.assertEqual(len(teller.scanned_items), 0)

		# Test scanning items and totalling
		teller.scan("B")
		teller.scan("A")
		teller.scan("B")
		teller.scan("P")
		teller.scan("B")
		self.assertEqual(len(teller.scanned_items), 5)
		self.assertEqual(teller.total(), 155)

if __name__ == "__main__":
	unittest.main()
