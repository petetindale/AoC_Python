import common.fileutils as fu

class datahandler:
  def __init__(self, year:int, day:int) :
    self.year = year
    self.day = day
    
    self.path = fu.getpath(1, year, day)
    
    self._tests = fu.gettests(self.path, year, day)
    
    self._data = None
    self._testdata = None
  
  def _cleanlist(self, input_data:list):
    return list(map(lambda x : x.strip(), input_data))
  
  @property  
  def data(self):
    if self._data is None :
      self._data = self._cleanlist(fu.getlos(self.path, False))
    return self._data
    #return 
  
  @property
  def testdata(self):
    if self._testdata is None :
      self._testdata = self._cleanlist(fu.getlos(self.path, True))
    return self._testdata
    #return 
    
  def testans(self, part:int):
    return self._tests[f"part{part}"]


