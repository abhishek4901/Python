import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip inpyobjstall c>=9.0.1"
 
engine.say("""Twinkle, twinkle, little star 
How I wonder what you are
Up above the world so high 
Like a diamond in the sky
Twinkle, twinkle, little star
How I wonder what you are
Twinkle, twinkle, little star
How I wonder what you are
Up above the world so high   
Like a diamond in the sky
Twinkle, twinkle, little star
How I wonder what you are""")
engine.runAndWait()
