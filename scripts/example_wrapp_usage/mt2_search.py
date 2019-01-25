

# Script to calculate cross-sections 
import re
import ast
from request_wrapper import RequestWrapper

xsdb_req = RequestWrapper()

""" -- 1. SIMPLE QUERY - passing only search fields -- """

#query = {'matrix_generator': 'Herw.*', 'energy': '[67]{1}'}

samples = [
(502, 'WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8'),
(503, 'DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8'),
]


for id,sample in samples:
#  print '\n\n#Query for sample ', sample, '\n'
  query = {  'process_name' : sample }
#  #



#print '%s='%id
  xsdb_req.simple_search(query)

xsdb_req.end()




#print 'result is', result
fp=open('./KNOW_YOUR_XSECS', 'r')
for line in fp:
    #line = line.strip()
    print '***************************'
    #print line
    results = re.split('\]\[|\[|\]',line)
    results = filter(lambda x: x!='', results)
    #print results

    for result in results:
      result = ast.literal_eval(result)
      #print result.items()

      sName = result['process_name']
      unc = result['total_uncertainty']
      xSec = result['cross_section']
      accuracy = result['accuracy']
      kFac = result['kFactor'] if 'kFactor' in result.items() else 'NA'

      out = '{:70} {:10.5f} {:10.5f}   {:2}    {:4}'.format(sName, float(xSec), float(unc), accuracy, kFac)
      print out




