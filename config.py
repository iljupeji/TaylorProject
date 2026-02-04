import os
#print(f"Directorio actual:{os.getcwd()}")
from dotenv import load_dotenv
import lyricsgenius

load_dotenv()
token=os.getenv('GENIUS_ACCESS_TOKEN')
os.environ['GENIUS_ACCESS_TOKEN']=token
#print(os.environ)
genius=lyricsgenius.Genius(token)