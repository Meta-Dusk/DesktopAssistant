# A Desktop Assistant App made especially for Marcus Lance

> Current version: v0.4.1

**Happy Birthday, Marcus Lance!**

> Started on September 22, 2025

I just made a Wiki for this project, you can access it here now: [DesktopAssistant Wiki](https://github.com/Meta-Dusk/DesktopAssistant/wiki)

> I'm thinking if I should just move everything to the Wiki instead of having most of the information here in the `README.md`... Should I?

## Features

1. Hatsune Miku
2. Randomized Movement
3. Randomized Messages
4. Different Expressions
5. Flips
6. Animations
7. A Menu

## Planned Features

1. SFX
2. More Easter Eggs
3. Extensive Menus **< (In Development in Experimental)**
4. Settings Menu **< (In Development in Experimental)**
5. Minigames
6. Make Miku an actual "Desktop Assistant" and not just a pet

## Unintended Behaviors

- You can run multiple instances of Miku, by just simply running the executable again; the result is a shocker... **Mikus Galore!** (This is a bit buggy, but works, and may or may not use a lot of your pc's resources)

## Controls

> This section will be removed once the menu feature has been implemented.
> The controls being referred here are for interacting with Miku, or used directly on her.

| Action | Behavior |
| ------ | -------- |
| **Left-Click** | Default interaction. Click twice for a menu. Clicking then holding is a placeholder for now. |
| **Right-Click** | Click twice to exit. |
| **Left-Click + Drag** | Will move Miku around. |

## Known Issues and Fixes

Please do report any issues found that are not solvable with the fixes provided below:

| No. | Issue | Fix | Severity | Description |
| --- | ----- | --- | -------- | ----------- |
| 1 | A border around Miku appears during app launch | Relaunch the app | Minor graphical issue | This issue could also be because of how `Flet` handles transparent windows. |
| 2 | Miku suddenly stops her idle animation | Move Miku around your screen, then stop | Minor interaction issue | This issue occurs when clicking her registers as a drag event, but is immediately canceled, resulting in the events not registering correctly |
| 3 | After dragging Miku, her position doesn't update, and will return to her initial position pre-drag | _This issue is still under scrutiny_ | Minor interaction issue | Happens occasionally, but nothing serious |
| 4 | Miku's randomized movement anchor is misplaced once dragged off-screen at the bottom | _This issue is still under scrutiny_ | Minor interaction issue | Only happens if you intentionally drag her way below bounds of the monitor |
| 5 | When launching the app, it sometimes just doesn't stop loading | Relaunch the app | Startup issue | _This issue is still under scrutiny_ |
