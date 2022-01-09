import PIL.Image
import math

#---------------------------------------------------

def _adjust_component(comp):
    """
    This function adjusts inpute 'comp' to be withing 
    0 and 255, inclusive.

    >>> _adjust_component(586)
    OUTPUT -> 255
    """
    comp = int(comp)
    return max(0, min(255, comp))

#---------------------------------------------------

class Color(tuple):
    __slots__ = ()

    def __new__(_cls, red, green, blue):
        return tuple.__new__(_cls, (_adjust_component(red),
                                    _adjust_component(green),
                                    _adjust_component(blue)))

    @classmethod
    def _make(cls, t):
        return tuple.__new__(cls, t)

    def __repr__(self):
        return 'Color(red={0[0]}, green={0[1]}, blue={0[2]})'.format(self)

#---------------------------------------------------

def bounce(fpt: int, gravity = -9.8, velocity = 80):
	if gravity >= 0:
		print('LOG: Gravity will be set to negative')
	if velocity <= 0:
		print('LOG: Velocity will be set to positive')
	if fpt <= 0:
		print('LOG: FPT will be set to positive')

	gravity = abs(gravity) * -1
	velocity = abs(velocity)
	fpt = abs(fpt)
	time = []

	for i in range(0, math.floor(-1 * velocity / gravity)+1):
		for j in range(fpt):
			n = i+(j/fpt)
			if math.ceil((velocity*n)+(gravity*n*n)) > 0:
				time.append(n) 

	ball_height = [math.ceil((velocity*t)+(gravity*t*t)) for t in time]

	frames = []
	for i in range(0,len(time)):
		image = PIL.Image.new(
			mode="RGB", 
			size=(41, max(ball_height)+1), 
			color=tuple(Color(0, 0, 0))
			)
		# print(ball_height[i], ' ' ,image.size[1]-ball_height[i]-1)
		image.putpixel(
			(21, image.size[1]-ball_height[i]-1), 
			tuple(Color(255, 255, 255))
			)
		frames.append(image)

	return frames

def saveFrames(frames: list, num: int):
	'''
	This Function takes, as inpute, a list of images that 
	will be saved as PNG , and an interger that will be 
	used for the naming of eah PNG.

	If there is an error with the frames, or none are 
	loaded, the function will terminate.

	>>> frames = bounceFrames.Bounce(fpt = 16, gravity = -9.8, velocity = 70)
	>>> bounceFrames.addDefaultFrame(frames, 15)
	>>> saveFrames(frames, 3)
	OUTPUT -> 0x03.png,  0x04.png,  0x05.png... 
	'''
	if len(frames) > 0:
		for i in range(0, len(frames)):
			name = hex(i+(num*16)) + '.png'
			frames[i].save(name)
	else:
		print("ERROR: No Frames loaded")
		return None

def addDefaultFrame(frames: list, nADD: int):
	'''
	This function takes, as inpute, a list of images
	and an integer (nADD). The first image will be duplicated
	nADD times and placed the the begining of the list.

	If there is an error with the frames, or none are 
	loaded, the function will terminate.

	>>> frames = bounce(fpt = 16, gravity = -9.8, velocity = 70)
	>>> frames = addDefaultFrame(frames, 3)
	OUTPUT -> frames = 0x03.png, 0x03.png, 0x03.png, 0x04.png, 0x05.png... 

	'''
	if len(frames) > 0:
		if nADD < 0:
			print("nADD set to positive")

		nADD = abs(nADD)
		for i in range(nADD):
			addedFrame = frames[0]
			frames.append(addedFrame)
			return frames

	else:
		print("ERROR: No Frames loaded")
		return None

def main():
	frames = bounce(fpt = 4, gravity = -9.8, velocity = 70)
	addDefaultFrame(frames, 3)
	saveFrames(frames, 0)

if __name__ == '__main__':
	main()
	