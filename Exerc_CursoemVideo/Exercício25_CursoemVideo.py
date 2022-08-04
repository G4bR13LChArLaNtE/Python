no = str(input("Qual seu nome? "))
nm = no.lower()
nm = nm.split()
print('Seu nome tem Silva?  {}'.format( 'silva' in nm))