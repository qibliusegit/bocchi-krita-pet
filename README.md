# Bocchi the Desktop Pet! #

tl;dr bocchi tsuchinoko that you can click


This is a desktop pet for the drawing app Krita! It acts as a docker and sits in the bottom right corner of your screen. When you press it, the character switches images.

The other cool thing it does is that it can control music! I made it so instead of tabbing out into Spotify, I just have a music player baked into Krita. You just need to put your filepath into the code where marked, and then use the following controls:


| Left Click| Right Click |
| --- | --- |
| Plays a new track| Pauses/Plays the current track|

It specifically uses mp3 files.

___

Future plans include adding more characters that you can select from, and also possibly more commands!

This project was made for Hack Club's [Wrangler](wrangler.hackclub.com).

# HOW TO INSTALL THE PLUGIN #
1. Download the bocchi.zip file from this repository
2. Change `song_dir = Path("change to your file path!") ` to have your file path in it
3. Open Krita, click on tools, then scripts, then import python plugin from file
4. Click on gambling.zip
5. Make sure that the plugin is enabled in Settings -> Configure Krita -> Python Plugin Manager
6. Rejoice! You now have fun bocchi music click thing on your Krita!

