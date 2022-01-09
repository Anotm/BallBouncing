import bounceFrames

def frames2GIF(frames: list, duration: int, filename = "newGIF.gif"):
	'''
	This Function takes, as inpute, a list of images that 
	will be the frames of the GIF, an interger that will 
	dictate the duration of the GIF, and a Filename that 
	will be used when saving the GIF.

	If there is an error with the frames, or none are 
	loaded, the function will terminate.

	If the duration is not greater than 0, it will be 
	automaticaly set to 20

	Default filename is set to 'newGIF.gif'. NAME MUST 
	INCLUDE '.gif'

	>>> frames = bounceFrames.Bounce(fpt = 16, gravity = -9.8, velocity = 70)
	>>> bounceFrames.addDefaultFrame(frames, 15)
	>>> frames2GIF(frames, duration = 20)
	OUTPUT -> newGIF.gif

	'''
	if len(frames) > 0:
		if duration < 0:
			print("ERROR: Duration set to be positive")
		if duration == 0:
			print("LOG: Duration set to 20")
			duration = 20
		
		duration = abs(duration)
		frames[0].save(filename,
					format='GIF',
	               	append_images=frames[0:],
	               	save_all=True,
	               	duration=duration,
	               	loop=0)
	else:
		print("ERROR: No Frames loaded")
		return None

def main():
	frames = bounceFrames.Bounce(fpt = 16, gravity = -9.8, velocity = 70)
	bounceFrames.addDefaultFrame(frames, 15)
	frames2GIF(frames, duration = 20)


if __name__ == '__main__':
	main()