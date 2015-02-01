from utils.tools import cache_readonly


class EstimatesSingle(object):

	def __init__(self, ate, att, atc, method, model):

		self._dict = {'ate': ate, 'att': att, 'atc': atc,
		              'ate_se': None, 'att_se': None, 'atc_se': None}
		self._method = method
		self._model = model

	
	def __repr__(self):

		if self._dict['ate_se'] is None:
			self._compute_se()

		return repr(self._dict)


	def __getitem__(self, key):

		if 'se' in key and self._dict['ate_se'] is None:
			self._compute_se()

		return self._dict[key]


	def _compute_se(self):

		se = self._model._compute_se(self._method)
		self._dict['ate_se'] = se[0]
		self._dict['att_se'] = se[1]
		self._dict['atc_se'] = se[2]


	def _add_se(self, ate_se, att_se, atc_se):

		self._dict['ate_se'] = ate_se
		self._dict['att_se'] = att_se
		self._dict['atc_se'] = atc_se

	
	def keys(self):

		return self._dict.keys()


class Estimates(object):

	def __init__(self):

		self._dict = {}


	def __getitem__(self, key):

		return self._dict[key]


	def keys(self):

		return self._dict.keys()


	def _add(self, ate, att, atc, method, model):

		self._dict[method] = EstimatesSingle(ate, att, atc, method, model)

