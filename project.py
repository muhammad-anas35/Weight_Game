Moon : float = 1.62
Mars : float = 3.71
Jupiter : float = 24.79
Saturn : float = 10.44
Uranus : float = 8.69
Neptune : float = 11.15
Venus : float =8.87

prompt_1 :str = "Enter your weight on earth : "
prompt_2 :str = "Enter a planet to claculate your weight on it : "

def main():

  User_weight = input(prompt_1)
  Planet_choice = input(prompt_2)
  Planet_choice = Planet_choice.lower()

  if Planet_choice == 'moon':
    planet_gravity = Moon
  elif Planet_choice == 'venus':
    planet_gravity = Venus
  elif Planet_choice == 'mars':
    planet_gravity = Mars
  elif Planet_choice == 'jupiter':
    planet_gravity = Jupiter
  elif Planet_choice == 'saturn':
    planet_gravity = Saturn
  elif Planet_choice == 'uranus':
    planet_gravity = Uranus
  elif Planet_choice == 'eptune':
    planet_gravity = Neptune
  else:
      print("Invalid Planet Choice chose basic planet ")

  Mass =  float(User_weight) * planet_gravity
  print(f"Your weight on {Planet_choice} is {Mass:.2f}")

if __name__ == '__main__':
  main()