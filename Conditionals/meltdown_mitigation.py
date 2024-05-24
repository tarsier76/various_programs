def is_criticality_balanced(temperature, neutrons_emitted):
  return temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000

def reactor_efficiency(voltage, current, theoretical_max_power):
  generated_power = voltage * current 
  percentage_value = (generated_power / theoretical_max_power) * 100
  
  if percentage_value >= 80:
    return 'green'
  elif percentage_value >= 60 :
    return 'orange'
  elif percentage_value >= 30:
    return 'red'
  elif percentage_value < 30:
    return 'black' 
  
def fail_safe(temperature, neutrons_produced_per_second, threshold):
  final_value = temperature * neutrons_produced_per_second
  if final_value < 90/100 * threshold:
    return 'LOW'
  elif final_value >= 90/100 * threshold and final_value <= 110/100 * threshold:
    return 'NORMAL'
  else:
    return 'DANGER'
  

print(is_criticality_balanced(500, 800)) 
print(reactor_efficiency(200, 50, 15000))
print(fail_safe(100, 5, 500))


