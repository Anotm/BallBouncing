import libraries.BounceFrames as BFs
import libraries.SaveFunctions as SFs
import PIL.Image
import json

#---------------------------------------------------

class multiBounce:
	def __init__ (self, json_number:int):
		self.number = json_number
		print("LOG: Variable initialized")
		print()

	def sizeCorrection (self):
		for i in range(1, len(self.frames)):
			if self.frames[i].size != self.frames[0].size:
				newFrameSize = self.frames[0].size
				newFrame = PIL.Image.new("RGB", newFrameSize)
				newFrame.paste(
					self.frames[i], 
					(
						newFrameSize[0] - self.frames[i].size[0],
						newFrameSize[1] - self.frames[i].size[1],
					)
				)
				self.frames[i] = newFrame

	def set_inpute (self, json_file_name: str):
		f = open(json_file_name)
		self.json_data = json.load(f)

		self.list_num = int(         self.json_data["BounceTypes"][self.number]["list number"]          )
		self.duration = int(         self.json_data["BounceTypes"][self.number]["duration"]             )
		self.fpt      = int(         self.json_data["BounceTypes"][self.number]["fpt"]                  )
		self.divition = round(float( self.json_data["BounceTypes"][self.number]["divition factor"]  ), 2)
		self.gravity  = round(float( self.json_data["BounceTypes"][self.number]["gravity"]          ), 2)
		self.velocity = int(         self.json_data["BounceTypes"][self.number]["initial velocity"]     )

		ln_str = "ln" + str(hex(self.list_num))     + "_"
		d_str  = "d"  + str(self.duration)          + "_"
		f_str  = "f"  + str(self.fpt)               + "_"
		df_str = "df" + str(int(self.divition*100)) + "_"
		g_str  = "g"  + str(int(self.gravity*100))  + "_"
		iv_str = "iv" + str(self.velocity)

		self.GIFname = ln_str + d_str + f_str + df_str + g_str + iv_str + ".gif"

		print("LOG: Variables saved as:")
		print("    self.list_num =", self.list_num )
		print("    self.duration =", self.duration )
		print("    self.fpt      =", self.fpt      )
		print("    self.divition =", self.divition )
		print("    self.gravity  =", self.gravity  )
		print("    self.velocity =", self.velocity )
		print("    self.GIFname  =", self.GIFname  )
		print()

	def makeBounces (self):
		self.frames = []
		iv = self.velocity

		while (iv > 0):
			bounce_frames = BFs.bounce(self.fpt, self.gravity, iv)
			# BFs.addDefaultFrame(bounce_frames, 1)
			self.frames = self.frames + bounce_frames
			print("LOG: len(self.frames) =", len(self.frames))
			iv = iv - ((iv/self.divition)+1)

		print("LOG: self.frames has been made")
		print()

		self.sizeCorrection()

	def saveFramesPNG (self):
		SFs.frames2PNG(self.frames, self.list_num)
		print("LOG: Saved individual frames as .png")
		print()

	def saveFramesGIF (self):
		SFs.frames2GIF(self.frames, self.duration, self.GIFname)
		print("LOG: Saved frames as GIF")
		print()

#---------------------------------------------------

def main():
	test = multiBounce(1)
	test.set_inpute("INPUTE.json")
	test.makeBounces()
	test.saveFramesGIF()

#---------------------------------------------------

if __name__ == '__main__':
	main()