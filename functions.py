import random

def assign_team(team_a_count, team_b_count):
    total_count = team_a_count + team_b_count
    if total_count == 0:
        # If both teams have no members, randomly choose a team
        return random.choice([0, 1])

    # Calculate the percentage of members in each team
    percentage_team_a = team_a_count / total_count
    percentage_team_b = team_b_count / total_count

    # Calculate the threshold based on the percentage difference
    threshold = int(skewnumber(percentage_team_a * 10000))

    # Generate a random number between 0 and 9999
    rand_num = random.randint(0, 9999)

    # Assign the team based on the threshold
    if rand_num < threshold:
        return threshold, "Gold"
    else:
        return threshold, "Lapis"

def skewnumber(input):
  if (input == 5000):   # If it is even the don't skew it at all towards either team
    return 5000
  elif(input < 5000):   # For if the input is skewed towards Lapis
    if(input < 4000):   # If the ratio is more than 40/60 guarantee that the next person goes to Lapis
      return 0
    elif (input < 4200):# If the ratio is equal to or more than 42/58, 75 percent change next person goes to lapis
      return 2500
    elif (input < 4400):# If the ratio is equal to or more than 44/56, 70 percent change next person goes to lapis
      return 3000
    elif (input < 4600):# If the ratio is equal to or more than 46/54, 65 percent change next person goes to lapis
      return 3500
    elif (input < 4800):# If the ratio is equal to or more than 48/52, 60 percent change next person goes to lapis
      return 4000
    else:
      return 4500       # If the ratio is between 50/50 or 48/52, 55 percent change next person goes to lapis
                        # ------------------------------------------------------------------------------------------
  if(input > 6000):   # If the ratio is more than 40/60 guarantee that the next person goes to Gold
    return 10000
  elif(input>5800):   # If the ratio is equal to or more than 42/58, 75 percent change next person goes to Gold
    return 7500
  elif(input>5600):   # If the ratio is equal to or more than 44/56, 70 percent change next person goes to Gold
    return 7000
  elif(input>5400):   # If the ratio is equal to or more than 46/54, 65 percent change next person goes to Gold
    return 6500
  elif(input>5200):   # If the ratio is equal to or more than 48/52, 60 percent change next person goes to Gold
    return 6000
  else:
    return 5500       # If the ratio is between 50/50 or 48/52, 55 percent change next person goes to Gold

def run_tester(amount, Lapis, Gold):
    threshold = assign_team(Lapis, Gold)
    Lcount = 0
    Gcount = 0
    while amount > 0:
      threshold, next_member_team = assign_team(Lapis, Gold)
      if (next_member_team == "Lapis"):
        Lcount = Lcount + 1
      else:
        Gcount = Gcount + 1
      amount = amount - 1

    print("-------Run Tester Output-------")
    print(f"Team Lapis {Lcount}")
    print(f"Team Gold {Gcount}")

def team_assigner(Lapis, Gold):
  threshold, next_member_team = assign_team(Lapis, Gold)
  print("-------Team Assigner Output-------")
  print(f"Threshold: {threshold}" + " with "+ f"{Lapis}"+ " Lapis members and "+ f"{Gold}"+ " Gold members")
  print(f"Next member goes to Team {next_member_team}")