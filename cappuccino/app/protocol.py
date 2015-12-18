import cbor


class Protocol:
	def decode(self, message):
		return cbor.loads(message)

	def encode(self, message):
		return cbor.dumps(message)



