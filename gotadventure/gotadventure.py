from sys import exit

def win():
	print "You win!"
	exit(0)
	
def die():
	print "The end."
	exit(0)

def north():
	print """
The Night's Watch has sent for help - Commander Mormont has been assassinated and
The Others have attacked the Night's Watch at Craster's Keep, North of the wall.
How many men do you send to their aid?
	"""
	
	input = raw_input("> ")
	
	try: 
		int(input)
	except:
		print "You botched the orders to your men. The Others overrun the wall, causing all of Westeros to succumb."
		die()
	
	choice = int(input)
	
	if choice < 100:
		print """
You understimated the strength of the Others! Your men are overcome and die gruesome 
deaths. The Others overrun the wall, causing all of Westeros to succumb to the long night.
		"""
		die()
	elif 100 <= choice < 500:
		commander()
	elif choice >= 500:
		bloodraven()
	else:
		print "Too late. The Others overrun the wall, causing all of Westeros to succumb."
		die()

		
def commander():
	print """
You fend off the Others for a time. You are outnumbered, but all is not lost yet. 
Your bastard son Jon Snow ascends to the position of Lord Commander. What do you advise 
for his first move - ally with the wildlings, or call for reinforcements from King's Landing?
	"""
	
	choice = raw_input("> ")
	
	if ("ally" in choice) or ("wildlings" in choice):
		print """
It is difficult, but you manage to win the trust of the King-Beyond-the-Wall Mance Rayder,
and together you and his wildings defeat the Others.
		"""
		bloodraven()
	elif ("reinforcements" in choice) or ("king" in choice) or ("King" in choice):
		print """
Unfortunately, Queen Cersei convinces the King that your call for help is a ruse to 
ambush his forces and usurp him. The Others overrun the wall, causing all of Westeros 
to succumb to the long night. 
		"""
		die()
	else:
		print "Too late. The Others overrun the wall, causing all of Westeros to succumb."
		die()

def bloodraven():
	print """
You defeat the Others, but you and your men get separated from the main force and find 
yourselves in a cave. Upon entering, you discover Bloodraven - the Three Eyed Crow. 
He asks you if you want to look into the past, or into the future. You choose:
	"""
	choice = raw_input("> ")

	if ("Past" in choice) or ("past" in choice):
		print """
You see Queen Cersei and Jaime Lannister together in the past and realize that they have been 
committing incest. You rush to King's landing on your fastest horse.
		"""
		incest()
	elif ("Future" in choice) or ("future" in choice):
		print """
You see a future where Jon Snow has been legitimized and crowned King. The secret of 
his parentage that you have kept so long is revealed! You are overjoyed and relieved.
"""
		win()
	else:
		print """
Bloodraven reveals that he orchestrated The Others, and you are doomed to remain 
a prisoner beyond the wall forever. You are trapped, doomed to never return home.
		"""
		die()
	
def hand():
	print """
You travel to King's Landing and become the King's Hand!
You begin to suspect that the children of King Robert, Joffrey, Myrcella and Tommen 
are actually the children of Queen Cersei Lannister and her twin brother, Jaime 
Lannister of the Kingsguard. What do you do?
	"""
	incest()
	
def incest():
	confrontation = False
	
	while True:
		print "Do you confront the Queen, or report them to the King?"
		choice = raw_input("> ")
	
		if ("Cersei" in choice) or ("cersei" in choice) or ("Queen" in choice) or ("queen" in choice) or ("confront" in choice):
			print "You confront Cersei, who refuses to confess."
			confrontation = True
		elif ("King" in choice or "king" in choice) and confrontation == False:
			print """
You tell the King of Cersei's infidelities and he has Cersei, Jaime, Joffrey, Myrcella 
and Tommen executed. Gendry, the King's bastard, is found and legitimized as the heir 
to the Iron Throne. Having been raised as a smith, Gendry grows up to be an honorable
and just King that is loved by all the smallfolk after Robert's passing. 
			"""
			win()
		elif ("King" in choice or "king" in choice) and confrontation == True: 
			print """
You resolve to tell the King, but he is killed in a hunting accident the very next day.
Unfortunately, we all know what happens next and you are beheaded at the Sept of Baelor. 
			"""
			die()
		else:
			print "You need to make a choice. Time is running out."

def start():
	print """
You are Ned Stark, Lord of Winterfell and Warden of the North. King Robert and his entourage
arrive for a visit. The King asks if you are willing to come to King's Landing to serve as his 
Hand. Do you accept his offer, or refuse and stay in the North?
	"""
	choice = raw_input("> ")
	
	if ("accept" in choice) or ("Hand" in choice) or ("hand" in choice) or ("King" in choice) or ("king" in choice):
		hand()
	else:
		north()

start()
	