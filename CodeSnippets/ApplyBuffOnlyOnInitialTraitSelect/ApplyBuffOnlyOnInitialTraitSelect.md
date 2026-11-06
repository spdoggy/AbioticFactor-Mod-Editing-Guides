Follow AlexTheDragonn's guide on running logic on player join:
https://mod.io/g/abiotic-factor/r/how-to-immediately-run-actors-independently

Then check the `Initialized Traits` flag to see if the player finished.
This will get entered again when the player finishes and the game actually applies the traits, so some kind of check if needed.  Like the Has Actor check that the guide suggests.

For this current mod I don't need a helper object for every player char, so I am simply using Current Sanity as a toggle flag to check for re-entry until Initialized Traits is set = False and the player is in the game.
