import time
# Title for the email reminder maker. DON'T USE THE SAME TITLE NAME.
print("""

 ######     #   #          #####    #####  #    #   ######  ####                                                      
 #        #  # #  #      ##        #       #    #   #       #   #                                 
 ######  #    #    #        ##    #        ######   ######  #    #                                                  
 #       #         #          ##   #       #    #   #       #   #                                
 ######  #         #     #####      #####  #    #   ######  ####   

------------------------------------------------------------------- 
                        Welcome to Em Sched!
-------------------------------------------------------------------
A dayly email scheduled reminder maker.
You have the option to add or remove reminders for every day of the 
week.
""")

# Class that can open files and print the text in them to the terminal.
class remin():
  def __init__(self, fils):
      self.fil = fils
  def remindstat(self):
      file1 = open(self.fil, "r")
      print("\n" + file1.read())
      print()
      file1.close()

# Class that can open files and write new reminders in them. 
class reminder():
  def __init__(self, day, file, reminder):
      self.day = day
      self.file = file
      self.reminder = reminder

  def makereminder(self):
      time.sleep(1)
      file1 = open(self.file, "a")  # append mode
      file1.write(self.reminder + "\n")
      file1.close()
            
day = input("what day would you like to have a reminder? [mon/exit] ")
#looping so you can make as many reminders as you want for any day each time you run the program.
while day == "mon" or "tue" or "wed" or "thu" or "fri" or "sat" or "sun":
    #creating a file for a day of the week that is imported into the email.
    if day == "mon":
      f = "monday.txt"
      stat = remin(f)
      stat.remindstat()
      re = input("What would you like to add to monday's reminder? ")
      daily = reminder(day, f, re)
      daily.makereminder()
      stat.remindstat()
      day = input("what day would you like to have a reminder? [mon/exit] ")
      continue
    #creating a file for a day of the week that is imported into the email.
    elif day == "tue":
      f = "tuesday.txt"
      stat = remin(f)
      stat.remindstat()
      re = input("What would you like to add to tuesday's reminder? ")
      daily = reminder(day, f, re)
      daily.makereminder()
      stat.remindstat()
      day = input("what day would you like to have a reminder? [mon/exit] ")
      continue
    #creating a file for a day of the week that is imported into the email.
    elif day == "wed":
      f = "wednesday.txt"
      stat = remin(f)
      stat.remindstat()
      re = input("What would you like to add to wednesday's reminder? ")
      daily = reminder(day, f, re)
      daily.makereminder()
      stat.remindstat()
      day = input("what day would you like to have a reminder? [mon/exit] ")
      continue
    #creating a file for a day of the week that is imported into the email.
    elif day == "thu":
      f = "thursday.txt"
      stat = remin(f)
      stat.remindstat()
      re = input("What would you like to add to thursday's reminder? ")
      daily = reminder(day, f, re)
      daily.makereminder()
      stat.remindstat()
      day = input("what day would you like to have a reminder? [mon/exit] ")
      continue
    #creating a file for a day of the week that is imported into the email.
    elif day == "fri":
      f = "friday.txt"
      stat = remin(f)
      stat.remindstat()
      re = input("What would you like to add to friday's reminder? ")
      daily = reminder(day, f, re)
      daily.makereminder()
      stat.remindstat()
      day = input("what day would you like to have a reminder? [mon/exit] ")
      continue
    #creating a file for a day of the week that is imported into the email.
    elif day == "sat":
      f = "saturday.txt"
      stat = remin(f)
      stat.remindstat()
      re = input("What would you like to add to saturday's reminder? ")
      daily = reminder(day, f, re)
      daily.makereminder()
      stat.remindstat()
      day = input("what day would you like to have a reminder? [mon/exit] ")
      continue
    #creating a file for a day of the week that is imported into the email.
    elif day == "sun":
      f = "sunday.txt"
      stat = remin(f)
      stat.remindstat()
      re = input("What would you like to add to sunday's reminder? ")
      daily = reminder(day, f, re)
      daily.makereminder()
      stat.remindstat()
      day = input("what day would you like to have a reminder? [mon/exit] ")
      continue
    else:
      break

def d(na, nu):
  
  # opens the file, reads and stores each line into a list
  with open(na) as file:
    lines = file.readlines()
  
  # if the line number is in the file, we can delete it
  if (nu <= len(lines)):
  
    # delete the line from the list, which will be at line_number - 1 because 
    # lists are zero-indexed in Python
    del lines[nu - 1]
    
    # open the file for writing with "w" which will make the file blank
    with open(na, "w") as file:

      # write as the new content of the file, the remaining lines in the list
      for line in lines:
        file.write(line)
  
   #if the line number exceeds the length of the file, output an error message
  else:
    
    # inform the user the line is not in the file, and how many lines there is
    print("Line", nu, "not in file.")
    print("File has", len(lines), "lines.")


days = input("\n" + "what day do you want to delete a reminder from? [mon/exit] ")
#looping so you can remove as many reminders as you want for any day each time you run the program.
while days == "mon" or "tue" or "wed" or "thu" or "fri" or "sat" or "sun":
    # Editing a file for a day of the week that removes reminders.
    if days == "mon":
      df = "monday.txt"
      sta = remin(df)
      sta.remindstat()
      time.sleep(1)
      dl = int(input("Line: "))
      d(df, dl)
      time.sleep(1)
      sta.remindstat()
      time.sleep(1)
      days = input("What day do you want to delete a reminder from? [mon/exit] ")
      continue
    # Editing a file for a day of the week that removes reminders.
    elif days == "tue":
      df = "tuesday.txt"
      sta = remin(df)
      sta.remindstat()
      time.sleep(1)
      dl = int(input("Line: "))
      d(df, dl)
      time.sleep(1)
      sta.remindstat()
      time.sleep(1)
      days = input("What day do you want to delete a reminder from? [mon/exit] ")
      continue
    # Editing a file for a day of the week that removes reminders.
    elif days == "wed":
      df = "wednesday.txt"
      sta = remin(df)
      sta.remindstat()
      time.sleep(1)
      dl = int(input("Line: "))
      d(df, dl)
      time.sleep(1)
      sta.remindstat()
      time.sleep(1)
      days = input("What day do you want to delete a reminder from? [mon/exit] ")
      continue
    # Editing a file for a day of the week that removes reminders.
    elif days == "thu":
      df = "thursday.txt"
      sta = remin(df)
      sta.remindstat()
      time.sleep(1)
      dl = int(input("Line: "))
      d(df, dl)
      time.sleep(1)
      sta.remindstat()
      time.sleep(1)
      days = input("What day do you want to delete a reminder from? [mon/exit] ")
      continue
    # Editing a file for a day of the week that removes reminders.
    elif days == "fri":
      df = "friday.txt"
      sta = remin(df)
      dl = int(input("Line: "))
      d(df, dl)
      time.sleep(1)
      sta.remindstat()
      time.sleep(1)
      days = input("What day do you want to delete a reminder from? [mon/exit] ")
      continue
    # Editing a file for a day of the week that removes reminders.
    elif days == "sat":
      df = "saturday.txt"
      sta = remin(df)
      sta.remindstat()
      time.sleep(1)
      dl = int(input("Line: "))
      d(df, dl)
      time.sleep(1)
      sta.remindstat()
      time.sleep(1)
      days = input("What day do you want to delete a reminder from? [mon/exit] ")
      continue
    # Editing a file for a day of the week that removes reminders.
    elif days == "sun":
      df = "sunday.txt"
      sta = remin(df)
      sta.remindstat()
      time.sleep(1)
      dl = int(input("Line: "))
      d(df, dl)
      time.sleep(1)
      sta.remindstat()
      time.sleep(1)
      days = input("What day do you want to delete a reminder from? [mon/exit] ")
      continue
    else:
      break
