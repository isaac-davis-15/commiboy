from fbchat import log, Client
from fbchat.models import *
import time

email = "gamer_kid_7@yahoo.com"
if 1==1:
	password = "Unreal_132000"
groupThread = "2910063125686556"

groupTitle = "COMUNISIM"
groupImage = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIWJFagAww_yIoYqYoa5xivBf_UcnGy4vRmC2fA33uuctYFFT4"

print("Staring COMMIE BOY 9000...")
time.sleep(2)

checkClient = Client(email, password)
activation = False

class commieBoy(Client):
	def onMessage(self, author_id, message_object, thread_id, thread_type, **kargs):
		print("Message: {}".format(message_object.text))
		
		if message_object.text == "test" and thread_id == groupThread:
			self.send(Message(text="COMMIE BOY ACTIVATED..."), thread_id=groupThread, thread_type=ThreadType.GROUP)
			activation != activation
	def onTitleChange(self, author_id, new_title, thread_id, thread_type, **kargs):
		print("Title was changed to {} changing to {}".format(new_title, groupTitle))
		
		if new_title != groupTitle and author_id != self.uid:
			self.changeThreadTitle(groupTitle, thread_id=groupThread, thread_type=ThreadType.GROUP)

client = commieBoy(email, password)
client.listen()