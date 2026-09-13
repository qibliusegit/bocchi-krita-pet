# Bocchi the Desktop Pet! #

tl;dr bocchi tsuchinoko that you can click


<img width="249" height="183" alt="image" src="https://github.com/user-attachments/assets/a7bb0779-02a5-4c9b-8c6d-a512e37f9aed" />
_what bocchi looks like normally_


This is a desktop pet for the drawing app Krita! It acts as a docker and sits in the bottom right corner of your screen. When you press it, the character switches images.

The other cool thing it does is that it can control music! I made it so instead of tabbing out into Spotify, I just have a music player baked into Krita. You just need to put your filepath into the code where marked, and then use the following controls:


| Left Click| Right Click |
| --- | --- |
| Plays a new track| Pauses/Plays the current track|

It specifically uses mp3 files.

<img width="192" height="78" alt="image" src="https://github.com/user-attachments/assets/a40dd390-313c-4608-b061-87c0cfb3209b" />
_what bocchi looks like after being clicked :(_
___

Future plans include adding more characters that you can select from, and also possibly more commands!

This project was made for Hack Club's [Wrangler](wrangler.hackclub.com).

# HOW TO INSTALL THE PLUGIN #
1. Download the bocchi.zip file from this repository and install python-vlc via pip if you don't already have it
2. Change `song_dir = Path("change to your file path!") ` to have your file path in it
3. Open Krita, click on tools, then scripts, then import python plugin from file
4. Click on gambling.zip
5. Make sure that the plugin is enabled in Settings -> Configure Krita -> Python Plugin Manager
6. Rejoice! You now have fun bocchi music click thing on your Krita!

___
All art was amde by me using Krita.
