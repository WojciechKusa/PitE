import random, time

class Gate(object):
	fee = 10
	currentAmount = 0
	open = False

	def __init__(self):
		super().__init__()
		open = False
		currentAmount = 0
		fee = 10

	def isOpen(self):
		return self.open

	def openGate(self):
		self.open = True
		print("\tgate opened", end="")

	def closeGate(self):
		self.open = False
		self.currentAmount = 0
		print("\tgate closed", end="")


	def insertCoins(self, amount):
		self.currentAmount += amount

		print("inserted:", amount, "\tcurrent amount:", self.currentAmount, end="\t", flush=True)

		if self.currentAmount >= self.fee and self.open is False:
			self.openGate()
			


class GateController(object):
	gate = Gate()
	maxOpenTime = 2
	currentOpenTime = 0

	def __init__(self):
		super().__init__()

		gate = Gate()
		maxOpenTime = 2
		currentOpenTime = 0

	def startSimulation(self, maxTime = 0):
		t = 0
		while True:
			if maxTime > 0  and t > maxTime:
				if self.gate.open:
					self.gate.closeGate()
				break

			print("simulation time:", t, end="\t", flush=True)

			coins = random.randint(0, 3)

			if self.gate.open:
				self.currentOpenTime += 1

			if not self.gate.open:
				self.gate.insertCoins(coins)
			elif self.gate.open and self.currentOpenTime >= self.maxOpenTime:
				self.gate.closeGate()
				self.currentOpenTime = 0

			print("")
			t += 1
			time.sleep(0.5)


if __name__ == '__main__':
	gateController = GateController()
	gateController.startSimulation(20)


			
