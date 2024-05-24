def transcribe(strand):
  strand = ''
  complement_list = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U'
  }

  for letter in strand:
    strand += complement_list[letter]
  return strand 

print(transcribe('GCTA'))