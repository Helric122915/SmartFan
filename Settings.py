from enum import Enum # Requires "pip install enum34"

class OperationMode(Enum):
  Manual = 1
  Schedule = 2
  OneSourceTemp = 3
  TwoSourceTemp = 4
  
def ReadSettings(opMode):
  print str(opMode)
  # provide the necessary settings for the given operation mode?
  # query the database or web server and send a class object of the ncessary information back
