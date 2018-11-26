from commons import NameSpace
import json

class Response(object):

	def __init__(self):
		self.values = { 'values' : list() }

	def parse(self, output):
		return getattr(self, output)()

	def json(self):
		return json.dumps(self.values)

	def append(self, **kwargs):
		self.values['values'].append(kwargs)

	def dump(self, strFormat='console'):
		dump_map = {
			'json' : self.json,
		}
		dump_func = dump_map.get(strFormat, None)
		if dump_func : print (dump_func())
