import string

def check_human(genome_id) :

  output = False
  letters = string.ascii_uppercase
  numbers = string.digits
  if 9 <= len(genome_id) <= 11 :
    if letters.find(genome_id[0]) >= 0 :
      if letters.find(genome_id[1]) >= 0 :
        if genome_id[2] == '_' :
          i = 3
          while i <= 8 :
            if numbers.find(genome_id[i]) <= 0 :
              break
            i += 1
          if i==9 :
            if len(genome_id)>9 :
              if genome_id[9] == '.' and numbers.find(genome_id[10]) >= 0 :
                output = True
            else :
              output = True
  return output

#print check_human('XI_123456')
#print check_human('XI_123456.2')
#print check_human('XI_123456.A')
#print check_human('XI_123456809.1')
#print check_human('XI_12')
#print check_human('XI_123456.23')

def check_not_human(genome_id) :

  letters = string.ascii_uppercase
  numbers = string.digits
  isLetter = False
  isNumber = False


  if 6 <= len(genome_id) <= 14 :
    if letters.find(genome_id[0]) >= 0 :
      if letters.find(genome_id[1]) >= 0 :
        for x in range(1, 6) :
          if letters.find(genome_id[x]) < 0 :
            return False
        for y in range(7, 12) :
          if len(genome_id) >= y :
            if letters.find(genome_id[x]) >= 0 :
              return False
          else :
            break
      if numbers.find(genome_id[1]) >= 0 :
        for x in range(1, 6) :
          if numbers.find(genome_id[x]) <0 :
            return False
        for y in range(7, 12) :
          if len(genome_id) >= y :
            if numbers.find(genome_id[x]) >= 0 :
              return False
          else :
            break

      if len(genome_id) > 12 :
        if genome_id[12] != '.' and numbers.find(genome_id[13]) < 0 :
          return False
      return True
    else :
      return False
  else :
    return False

print check_not_human('X515002AAA')






