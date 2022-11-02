# sklearn models have get_params() method which returns a dict of params with their default values

def get_params_custom(model):
  
  from inspect import getsource
  doc = getsource(model)
  
  param_lines = []
  for row in doc.split('\n'):
    if ':' in row and row.startswith(' ') and 'default' in row.lower():
      param_lines.append(row)
    if 'attribute' in row.lower():
      break
  
  from collections import defaultdict
  param_names = defaultdict(dict)
  for param_line in param_lines:
    param_name = param_line.split(':')[0].strip()
    if '{' in param_line and '}' in param_line:
      #values = param_line.split('{')[1].split('}')[0].replace('"', '').split(',')
      import re
      values = eval(re.search('.*(\{.*?\}).*', param_line).group(1))
      param_names[param_name] = values
    else:
      param_names[param_name] = []
    
  return param_names


# from sklearn.tree import DecisionTreeRegressor
# get_params_custom(DecisionTreeRegressor)
