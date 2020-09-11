







# Author: Xiaolong Lin xxl5453@psu.edu
# Collaborator:Manraj Kumar mmk6281@psu.edu
# Collaborator:John Malay jmm9098@psu.edu   
# Collaborator:Irfan Khan imk5134@psu.edu
# Section: 006R
# Breakout: 15

def getLettergrade(numbergrade):
  
  if  numbergrade>=93 :
     grade = "A";
  elif numbergrade>=90 :
     grade = "A-";
  elif numbergrade>=87 :
    grade = "B+";
  elif numbergrade>=83 :
    grade = "B" ;
  elif numbergrade>=80 :
    grade = "B-"
  elif numbergrade>=77 :
    grade = "C+";
  elif numbergrade>=70 :
    grade = "C";
  elif numbergrade>=60 :
    grade = "D"; 
  else :  
    grade = "F";  
  return grade
def run():
  numbergrade = float(input("Enter your CMPSC 131 grade:  "))

  
 print(f"Your letter grade for CMPSC 131 is {getlettergrade(numbergrade)}.")

if __name__ ==  "__main__":
  run()
