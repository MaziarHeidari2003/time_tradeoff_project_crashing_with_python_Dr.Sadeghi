from teamwork import critical_path
import sys

def main():
  projects = {}
  dependencies = []
  while True:
    p_name = input('Enter the project name my lord: ')
    while True:
      pre_tuple = (p_name,)
      dependency = input('Enter the prereqisites separately(enter zero if you are done and if there are no prerequisites needed just press enter): ')
      if dependency == '':
        del(pre_tuple)
        break
      if dependency != '0':
        pre_tuple += (dependency,)
        dependencies.append(pre_tuple)
      else: 
        break  
      print(pre_tuple)
     
    while True:  
      try:  
        duration = float(input('Enter the regular time: '))  
        p_regular_cost = float(input('Enter the regular cost: '))
       #  p_squized_time = float(input('Enter the squized time: '))
       #  p_squized_cost = float(input('Enter the squized cost: '))
        break
      except ValueError:
        print('Invalid input my lord')

    projects[p_name] = {
      'duration':duration,
      'p_regular_cost':p_regular_cost,
      # 'p_squized_time':p_squized_time,
     #  'p_squized_cost':p_squized_cost
    }  
    con_check = input('Nicely done.Any other projects?yes/no: ').lower()
    while con_check !='yes' and con_check != 'no':
      con_check = input('Nicely done.Any other projects?yes/no: ').lower()
    if con_check == 'no':
      break
  try:     
    critical_path(projects,dependencies)  
  except UnboundLocalError:
    sys.exit('You have provided just one activity with no dependency, what should I really do??')
    
      


def calculate(projects):
  projects_slope = {}
  for key in projects.keys():
    try: 
      projects_slope[key] = (projects[key]['p_squized_cost']-projects[key]['p_regular_cost'])/(projects[key]['p_regular_time']-projects[key]['p_squized_time'])
    except ZeroDivisionError:
      pass  

  path = []
  for key in projects.keys():
    start= []
    try:
      stages = len(projects[key]['prerequisite_p'])
      
    except:
      start.append(key) 
      path.append(start)

  

  print(path)    
    




if __name__ == "__main__":
  main()


        
          
