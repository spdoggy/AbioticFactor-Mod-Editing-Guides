

Introduction

Want to create a custom painting that you can hang on the walls of your office base? Just downloaded the Official Abiotic-Factor Mod Editor and not sure where to start? This guide is for you!

This guide assumes that you have already obtained the Abiotic Mod Editor using either the Heroic Launcher ..or Epic, and have been able to get a Mod.io account linked to your email (NOT your Epic account).

Related: See also Deployables for Dummies which provides a higher-level overview for more experienced mod creators.



Setup



We will start with the First Person template under the items list. Despite the name, the First Person Template is essentially a blank starting template.





Navigating the Content Folders



Get familiar with the Layout of the Content Folders, and browse to the mod's folder under All/Plugins/.

The Custom Painting Tutorial used PaintGuide as the mod name and so the final mod folder path will be:

All/Plugins/PaintGuide Content/

Note that the editor automatically appends "Content" to the folder name.

Note2: The editor will also automatically append a unique char string to the end of your mod name. For example this guide appears to be at All/Plugins/PaintGuide Content/ but when viewing the actual folder structure on the computer it can be seen that the actual path is /All/Plugins/PaintGuidemlvUY/DataTables/ItemTable_Deployables.i.e the editor append "mlvUY" to the end of the mod name.



Practice browsing to your mod folder for the next step.



Making a new Blueprint (BP)



A Note about Blueprints (BPs)



Now that you are comfortable navigating the content folders and locating the mod's folder the next step will be to make a new blueprint in our mod folder.

Blueprints (BPs) are containers for game objects and logic. 

⚠️Important: Only items placed into the mod's content folder (i.e All/Plugins/PaintGuide Content/ in this example) will actually make it into the final mod and have any effect on the game. Mod creators can view some of the game's original logic and blueprints in All/Content/ but they CANNOT directly modify it. Any changes to All/Content/ will not be uploaded and/or will be removed during the final mod building and packaging process.



Create a New Blueprint in the Mod Folder

Browse to the mod's content folder (i.e All/Plugins/PaintGuide Content/ in this example) and you should see some a couple of basic files that configure mod data named AbioticModeConfig and UUGC_Metadata. Move the mouse to the right/below these files onto any blank space, and right-click to bring up a menu that will allow adding new items to the folder. Choose Blueprint Class from this list and the editor will prompt for a parent class. Move onto the next steps for choosing the parent.

Alternately, new blueprints can be made by pressing the Add button near the Top Right Corner of the editor.

Move onto the next steps for choosing the parent.



Specify the Parent Blueprint Class

After choosing to add a new Blueprint class, the editor will prompt to Pick a Parent Class. For this guide choose one of the existing paintings in the game: Deployed_Painting_Landscape_Fancy_C.

There is a search box under the "All Classes" menu that will allow narrowing down the list. Begin by searching for painting_landscape and then choose Deployed_Painting_Landscape_Fancy_C from the list.  Once Deployed_Painting_Landscape_Fancy_C is highlighted , press the Select button to complete the parent BP class selection.

Name the New Blueprint

Give the blueprint a new name.  You can also rename it later (Right-click and choose rename, or press F2 while the blueprint is highlighted)

Switching to the Level View-port

We need to switch to a different editor tab now, the Level view-port editor, so that we can access different modding toolbars.

Level View-port Toolbar

Take a moment to familiarize yourself with two important menus on the level view-port editor toolbar as these will be needed for important later steps.

The left icon with the test tube is the mod project menu, which will allow publishing the mod. It is also how the user would return to the initial starting Mod Browser menu seen when first opening the Abiotic Factor Mod Editor, to open another mod or create a new mod.

The right bar graph icon is the Mod Content menu which will be needed in the next few steps to create new data table row entries.



New DataTable Row

‼️Data Tables are very important to understanding how to interface with the game's logic.  In order to properly setup our new painting we'll need to register the painting in the list of deployable items. Otherwise the game won't know our painting exists!

The Create New DataTable Row is critical for our modding, and will allow us to insert a new object into one of the existing data tables. From the Mod Content Menu (the bar graph icon), choose Create New DataTable Row and then proceed to the next



Specify the Table and New Row Name



After selecting Create New DataTable row the editor will prompt for several pieces of information:

Which table to put the new row into: ItemTable_Deployables
The New Row Name: give it a unique name, preferably based on the mod name

Deployables are generally any item that can be placed into the world by the player: crafting benches, storage containers, and paintings too! By adding our new painting to the ItemTable_Deployables we are essentially registering it as a new valid type of deployable available to the player.

💡Tip: The Data Table Row editor will pop-up into a new window, but this window can be docked into the editor layout, similar to how the content folder was docked earlier in the guide.





We'll just keep it simple for the tutorial and call it PaintGuide_NewPainting

Data Table Row Setup - Copy from Existing Painting

To setup our new painting, we'll want to copy from the existing landscape painting. There are a lot of options, but copying from an existing item is a good way to get started and learn about the various settings for items.

DataTable Row Setup - Deployed Class

In order to properly differentiate our painting from the regular base game painting, we'll need to override the Deployed Item Class to point to the blueprint we created earlier in the guide. This way the game will to use our blueprint once the player places the painting down into the world (but we'll still be able to make use of all other logic related to paintings like their inventory icons, and the logic that places them down into the world, etc).

Find the Deployed Item Class in the list of settings and from the drop-down box choose the new painting blueprint we made earlier in the guide. (Refer back to the Name the New Blueprint step of the guide)

🧪 Optional: If you want to, edit the Item name, Item Description, or Item Flavor Text fields while you are here, to match the subject of your custom painting.

DataTable Row Setup - Save

Save your work

Importing a New Texture

Now we are going to import a new texture into the Mod editor. This is the part where you can chose the image that we want to be displayed in the painting! Luckily, this is as simple as dragging and dropping in an existing image file (jpg, png) into the Content Browser.



Find and Duplicate an Existing Landscape Painting Material

We will need a material to host the texture we imported in the previous steps, but we can make use of an existing material for one of the landscape paintings.

Back to the content browser, and this time we will need to search through the All folder, so:

Left-Click on the Content Browser (Or Ctrl+Shift+F or Find the Browser in the Bottom Left of the editor if you didn't dock the Content Browser Earlier in the guide) 
Click the All top level folder
Search for m_wallart
Select a suitable landscape painting that is recognizable, we'll use M_WallArt_12
Right-click the material (M_WallArt_12) and select duplicate



Name the New Material



Move the Material Back to the Mod Folder

⚠️ Remember, new assets for our mod MUST live in the mod folder! Unfortunately using the duplicate of an existing item from the original game like this will place the item inside of the main game's content folders. So we have to move our NewPainting_Material back to our PaintGuide Content folder.

This is a bit awkward in the editor. So if you learn a better way to duplicate an existing asset into the mod's folder without having to move it, please let us know in the comments!







Modify the Material

Now we need to browse back to our folder in the Content Browser and double-click to open our new material

Edit the texture of the material to point to the new texture we imported earlier, then save it!



Make it.. round?!


Save The Material







Open the Painting Blueprint

So now we have all of the items we need to finally start assembling our painting!

A Painting Blueprint
A DataTables folder with our Item Deployable Row
An imported texture
A new material to hold the texture

There will still be some more data table work to add it to the game as a craft-able recipe but let's take a moment to start to put things together.

Return to the Content Browser tab and find the painting blueprint we made earlier in the guide. Double click on the painting blueprint to open it in the editor.



Switch the Painting BP to Full Edit Mode

When first opening a blueprint the editor may display it in Data Only mode. Press Open Full Blueprint Editor now to open it in Full Edit mode.  We will need Full Edit mode to modify additional child components of the painting blueprint.



Swap in Our New Mesh

Now we need to replace the existing mesh with the new mesh we made earlier. Find the Furniture-Mesh object in the components list on the left side and left-click on the Furniture-Mesh to bring up it's options.

Then in the Details on the right side of the editor, find the Materials section and overwrite the existing Element 0 Material with the new material we made earlier. Don't forget to save! 

💡: You can see the asterisk in the name of the tab (newpainting*) to indicate that it hasn't been saved yet. Similarly for the PaintGuide_ tab. Remember to save your work regularly, and avoid losing data in a crash of the editor.

Set the Deconstructed Item Data to our NewPainting Class

Todo

Adding NewPainting as a Recipe

So we made an item, but we now we need a way for the player to actually get the item in the game! The easy way that we'll discuss in this guide is to add it as a new craft-able recipe.

Add a new DataTable row, but this time add the row to the DT_Recipes row. If you need a refresher on how to add a data table row, refer back to step on how to create a New DataTable Row



Configuring the Recipe

Let's make our recipe fairly easy to make since it's our first cosmetic mod.

Change Item to Create to be our painting.  Search for our item name (PaintGuide_NewPainting) in the list. Note that the mod editor inserts a random prefix onto the string name of the table row. This is the correct item, but just be aware that the editor will do this.  It is possible to change the mod prefix name, but that's beyond the scope of this guide.
This being our first cosmetic mod, let's override the required items for the recipe to something simple, we can craft at the start of the game like say: a single piece of paper scrap.
Finally, lets make the recipe not take any powered crafting benches. Set the benches required to None
Don't forget to Save!





Test It Out!

We did the setup, now to follow good practice for your mods by testing it out!

Fire up the in-editor viewer and load the Facility Level. (Make sure you are on the viewport tab of the editor we used earlier in the guide)

File-> Open Level (Ctrl+O), and choose Facility from the list.  Wait for it to load...

After loading the level, the viewport editor should look something like this now.

Hit play to begin the play and debug the game using the play-in-editor feature.



Find the Recipe In-Game

Once we've loaded into the game (will have to go through the char creation screen the first time), check the Crafting menu and we should see our new recipe ready to go!

Craft it and then try to place your new painting.



Finished

Congratulations, you did it!!!

Uploading the Mod

How do I actually get this mod into my game now?!

This guide will not directly cover uploading of the mod as that is already covered thoroughly by other guides. Instead please refer to Uploading for Dummies by Astro_Age for an excellent walkthrough of how to upload your first mod.



Additional Reading

Please feel free to join the Abiotic Factor Modding Discord Channel for more community guides and support.

Or check out other guides here on mod.io: https://mod.io/g/abiotic-factor/r

See also: [Modding Guide] Beginners Guide to The Mod Editor by SNEEZEROUSSNAPE for a handy reference on the Editor and terminology:   https://mod.io/g/abiotic-factor/r/beginners-guide-to-the-mod-editor

