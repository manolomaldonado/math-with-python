import string

def check_not_human(genome_id) :
  letters = string.ascii_uppercase
  numbers = string.digits
  output=False
  if 6 <= len(genome_id) <= 14 :
    if letters.find(genome_id[0]) >= 0 :
      x=1
      while x <= len(genome_id) :
        if letters.find(genome_id[x]) < 0 and numbers.find(genome_id[x]) < 0 :
          break
        else :
          x+=1
          if x == len(genome_id) :
            output = True
            break
          else :
            if x==12 :
              if genome_id[12]=="." and numbers.find(genome_id[13])>=0:
                output=True
                break
  return output

print (check_not_human('X515002AAA'))
print (check_not_human("AAAAAAA"))
print (check_not_human("A123456AAAAA.1"))
print (check_not_human("X51500"))
