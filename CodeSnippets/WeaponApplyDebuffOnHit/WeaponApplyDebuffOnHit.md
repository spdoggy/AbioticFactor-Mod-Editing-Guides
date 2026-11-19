# Weapon Apply Debuff on Hit

- Class: `Weapon_Melee`
- Submitter: `Astro_age`, `Zubi`

## Usage

Using this node sequence in a weapon blueprint graph will allow the `Debuffs to Apply` field of the
`ItemTable_Weapons` table row entry for a weapon to actually apply the debuff on hit.
There is not a parent BP method that automatically invokes this, it is actually up to each
melee weapon to handle this itself it it's node graph.


Astro_age: `It can be a little confusing since there's a few different ways a weapon can apply debuffs (through its damage type, through that node, etc)`

Sp: `So there's not any default logic in the weapon BPs to automatically check for debuffs and then call Server Apply Damage Buffs I guess? It's up to each weapon blueprint to implement that if needed? (i.e just because it's in the Data Table row doesn't mean we should assume it'll be used)`

Astro_age: `Afaik yeah, for most weapons its easier to let their damage type handle it (bleeding, burn, etc)`

## Example

![[WeaponApplyDebuffOnHit.png]]


## Example BP Copy Paste Code

[[WeaponApplyDebuffOnHit.txt]]

