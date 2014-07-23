takeover
========

Python 3.4 is required; if you can't import Enum check your version.

Run the project with main.py. When parameters get added they should be documented there as well.

Bots consist of a single python file committed to the bots directory; please limit names to alphanumeric characters and underscores. Poke me for commit access when you have a bot ready.

Bots needs to implement the make_bot(identifier) method that returns an object derived from Bot. Look at turtle_bot for an example.

Feel free to patch the engine itself if you find bugs or want to add features -- I'll try to review all changes. Please do not change the rules interpretation, Bot interface (including method invocation order), or anything that might break external integration without poking me first.
