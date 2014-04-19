Hopefully, this will be a full text adventure game at some point. Right now,
it's still in development and nothing really works. 

adventure.py contains the engine of the game and is the main concern at the
moment. It is a bit of a mess as I've been building the game side by side,
adding and deleting as I go. The changes I make are hard to keep up with, but
hopefully I can come up with something coherent.

Intuition.py plays the game, but you won't get very far. So far, the only
thing the game really knows how to do is recognize (some) commands.

objects.py contains the objects and descriptors of the game. Hopefully this
will be able to keep the engine and the game relatively separate.

