import requests
import os
import sys
import time

def substr(sentence,patron) :
  sentence = sentence.upper()
  ocurrences = 0
  i = 0
  while i < len(sentence) :
    sentence = sentence[i:]
    i=0
    k = sentence.find(patron)
    if k >= 0 :
        ocurrences+=1
        i=k+len(patron)
    else:
        break
  return ocurrences

def fetch_genome(genome_id, directory):
  url_template = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=%s&rettype=fasta&retmode=text"
  genome_id = genome_id.strip()
  print("Fetching ", genome_id, "...")
  out_file = os.path.join(directory, genome_id + ".fa")
  if os.path.exists(out_file):
      print("already fetched")
  resp = requests.get(url_template % genome_id)
  open(out_file, "w").write(resp.text)
  return resp.text.split("\n",1)[1].replace('\n', '');


kktua = fetch_genome('X51499', '/Users/manuelmaldonado/Sites/python/genomes')
print "The length of genome is: ", len(kktua)
print "The number of A's is: ", substr(kktua, 'A')
print "The number of C's is: ", substr(kktua, 'C')
print "The number of G's is: ", substr(kktua, 'G')
print "The number of T's is: ", substr(kktua, 'T')
print "The number of ACGC's is: ", substr(kktua, 'ACGC')
