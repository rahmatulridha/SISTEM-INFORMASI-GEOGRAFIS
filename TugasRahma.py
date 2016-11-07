import shapefile

class TugasRahma(object):
	def __init__(self,namafile):
		self.sf=shapefile.Reader(namafile)
		
	def itungBaris(self):
		rec = self.sf.shape()
		return len(rec)
		
	def selectNegara(self,NEGARA):
		i = 0
		for a in self.sf.records():
			if a[5] == NEGARA:
				return i
			i = i+1