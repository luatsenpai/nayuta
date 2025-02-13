
# Nayuta no Kiseki / Nayuta: Endless Trails English Translation Edit

<!-- TOC -->
- [Introduction](#introduction)
- [Patching Instructions](#patching-instructions)
- [Known Issues](#known-issues)
- [How do I use the files in this repo?](#how-do-i-use-the-files-in-this-repo)
- [Credits](#credits)
<!-- /TOC -->

<img src="https://i.imgur.com/1gWUK3w.jpg" width="360" height="204"> <img src="https://i.imgur.com/TT9smIn.jpg" width="360" height="204">


[More comparison screenshots](https://imgur.com/a/yJB1fTj). These are mostly one-liners that were particularly non-sensical. There shouldn't be any major spoilers if you're interested in avoiding them, but they might reveal some smaller details.

---
## Introduction

I wasn't happy with the English in the [existing Nayuta no Kiseki fantranslation](https://heroesoflegend.org/forums/viewtopic.php?f=22&t=73), so I used their [publicly available tools](https://heroesoflegend.org/forums/viewtopic.php?f=22&t=340) to make my own edit.


Initially I only wanted to only fix various inconsistencies, nonsensical lines, and the awkward direct-from-Japanese punctuation and sentence structure. Since I can read zero Japanese, I started out by using Google Translate and Linguee for help on trying to gauge what the more confusing parts were even trying to say, and editing the rest of the English myself.

But in addition to some parts simply not making any sense, I later noticed others had made some modicum of sense, but the online translators (especially after discovering DeepL, which lets you manually fiddle with alternative translations) made much *more* sense than the original. It seems that knowledge of the context is something that the original English writers were missing for much of the dialogue. Some of the more [drastic changes in meaning](https://i.imgur.com/YRqCdl3.png) have been things taken [almost literally from](https://i.imgur.com/M05LHD8.png) these online translators. I ended up also changing the rest of the text to whatever *I*, as a native US English speaker, subjectively think might sound better, taking into account the original translation, any new machine translation(s), and what I knew about the context.

But I'm not a big creative writer, so I think it still might be drier and close*r* to literal Japanese compared to most previous official localizations: lines with simple phrases or sounds in Japanese like *eh* or *naruhodo* are replaced with simple phrases or sounds in English, rather something potentially more expressive, meaningful, or entertaining. However, now I believe the English to be actually comprehensible. For instance, *yappari* is no longer almost always 'as expected,' even when one of the [many alternatives](https://en.wiktionary.org/wiki/やはり) or similar English phrases make more sense. But again, I don't even know Japanese, so maybe I just made everything worse, especially for anything more nuanced.

I would appreciate reporting of any issues: technical bugs, mistranslations, lore inconsistencies, or even just general English weirdness and typos. I've fixed a number of mistakes, but it is possible that I missed some. There are a few remaining [issues](#known-issues). 

Go to the [release page](https://github.com/dackst/nayuta/releases) for a changelog. If you're interested in more detail on the changes made from the original project, you can look at the [script notes](./notes.md) file. If you're *really* interested, you can easily view almost all the text changes from the original at once [here](https://github.com/dackst/nayuta/compare/a6cecc6651f386ab3fabcab64cf440e021fa99bd...original).


## Patching Instructions
1. Download xdelta patch from latest<sup>[1](#note1)</sup> [release](https://github.com/dackst/nayuta/releases). 


2. Apply the xdelta patch to an unmodified<sup>[2](#note2)</sup> Nayuta no Kiseki ISO.

    Useful xdelta patching tools:
    - [Web browser](https://hack64.net/tools/patcher.php)
    - [Windows](https://www.romhacking.net/utilities/598/)
    - [Android](https://www.romhacking.net/utilities/959/)

    Select the xdelta file you downloaded when prompted for a "Patch". Select your Nayuta no Kiseki ISO when asked for a "Source" or "ROM".

    Be sure to supply a name for the output file that ends in ".iso" or ".ISO" so that the patched file is recognized by PSP CFWs and emulators.

    If xdelta3 is already installed on your system elsewhere, you should also be able to run something similar to this:
```
xdelta3 -ds original.iso patch.xdelta patched.iso
```

### Checksums

* Clean Japanese ISO : 
    * CRC32: `c3b0c989`
    * MD5: `02adefbdef8197cca872268d5c01b277`
    * SHA-1: `126139a10911e02fa27f1e49b165887eac8759f2`

* ISO patched with this current release (1.08): 
    * CRC32: `75e466a9`
    * MD5: `bda6803e59fdcc67a17829fb6b49e134`
    * SHA-1: `b4b35037854abeeb9a1283ba3a77b602a6d58705`


## Known Issues

These are all issues that exist in the original fantranslation that I don't know how or care enough to try to fix myself.

* boss and new area intro graphics still untranslated ([example](https://i.imgur.com/xizzVel.jpg))
* erasing save data from in-game menu doesn't work
* strange text spacing in some (but not all) longer spell and item descriptions ([example](https://i.imgur.com/Crf076h.jpg))
* long achievement names are cut off in the notification box when unlocking them, e.g. "armor of anhillat"
  * the above two *could* be solved by shortening them, but I'm not willing to butcher them further
* characters that use idiosyncratic manners of speaking in Japanese probably still don't here
  * E.g. Geo is supposed to [sound like an old man](https://kiseki.fandom.com/wiki/Gio) (characters even comment on it several times in-game), Eris is supposed to sound [domineering](https://kiseki.fandom.com/wiki/Erislet) or something. Algol and Nemeas are definitely supposed to sound unique too
  * Noi has her own verbal tic that is lost
  * things like slang or shifts in politeness or tone are probably still not accurately conveyed
* text speed isn't as synced to voices as it is in Japanese (text speed should still be modified to be faster than the voices, if anything)




## How do I use the files in this repo?

This repository contains modifications of [flame's 2017 tools](https://heroesoflegend.org/forums/viewtopic.php?f=22&t=340) for modifying the text and images in Nayuta no Kiseki, as well as modifications of the English text and images dumped from version 4.15 of original project from 2016.

The original tools require a Windows installation of Python 3 to ["work"](./notes.md#why-not-just-use-flames-tools-directly). With the changes made in this repo, all of the non-working parts of these tools should be fixed. Also, the Python scripts for the dumping and inserting of binary files no longer require a Windows-based version of Python, but the beginning ISO extraction/workspace setup scripts and the final ISO rebuilding scripts still do.

You should still have access to an unmodified<sup>[2](#note2)</sup> Nayuta no Kiseki ISO.

1. Download and extract [the original tools](https://heroesoflegend.org/forums/viewtopic.php?f=22&t=340), and paste the [contents of this repository](https://github.com/dackst/nayuta/archive/master.zip) into the extracted folder. Overwrite files if necessary.
2. Drag your unmodified ISO over `_extract_new.bat` to set up a new environment (Run `_extract_new.bat path/to/original.iso`)
3. Modify files to your liking. See flame's `readme.txt` for more on this.
4. Run `build_all.bat` (or `build_all.sh`) to build the a new ISO out of the `ISO` folder with the changes, named `output.iso`. 
    * If you changed files that weren't modified before, you will have to have to add them to `copy_all.py` or copy them to the correct location yourself. You also *might* have to run the pack editing function in `copy_all.py` on some relevant file for your changes to appear. 



## Credits

Based on the work of a previous fan translation project:

* Flame - Project leader, main programmer, translator
* SkyeWelse - images
* naachan - translation assistance - helped with boss, character and location names
* Kelebek - programming assistance
* CUE - programming assistance
* zero_g_monkey - programming assistance (images)
* M_bot - image programming

This project:
* Wandering-Heiho - video editing, image editing assistance

Also thanks to anyone who [reported](https://github.com/dackst/nayuta/issues) any specific issues.

---

<a name="note1">1</a>: Prior to 1.07, you could choose `clean.xdelta` to patch an unmodified Japanese ISO, or choose `4.15.xdelta` to patch to an ISO patched with version 4.15 of the previous fan-translation. The previous fan-translation is based on the same image that `clean.xdelta` is based on.

<a name="note2">2</a>: This assumes an [ISO dumped from a physical UMD](https://datomatic.no-intro.org/index.php?page=show_record&s=62&n=2924) and NOT [one extracted from a PSN PKG](https://datomatic.no-intro.org/index.php?page=show_record&s=63&n=3569).

