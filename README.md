takeover
========

Python 3.4 is required; if you can't import Enum check your version.

The trueskill python module is also required; install it with "easy_install trueskill" from a command prompt. You'll need to execute this from Python34/Scripts if python isn't in your path.

Run the project with main.py. When parameters get added they should be documented there as well.

Bots consist of a single python file committed to the bots directory; please limit names to alphanumeric characters and underscores. Poke me for commit access when you have a bot ready.

**Bots need to be committed.** The competition will run by doing a checkout of the project, so any uncommitted bots aren't relevant. More bots also makes it easier to test the engine, and provides a better competitive landscape for bot development.

Bots needs to implement the make_bot(identifier) method that returns an object derived from Bot. Look at turtle_bot for an example. Bots should also implement all Bot methods that expect a return value to avoid warnings.

There's only minimal restriction against bots trying to interfere with the game outside the defined interface; those issues will get resolved socially and not technically. Bots should not:
* Rely on external libraries or services
* Take long to make decisions (this will be enforced technically if required)
* Interact with the game state or other bots except through the Bot interface
* Intentionally signal other bots

Matches are a series of rounds -- probably like 10k in competition -- between a fixed set of bots that maintain seating order. Bots are identified by their seat, not by name. This is to force bots to discover how their opponents play rather than having that information known in advance.

Feel free to patch the engine itself if you find bugs or want to add features -- I'll try to review all changes. Please do not change the rules interpretation, Bot interface (including method invocation order), or anything that might break external integration without poking me first.
