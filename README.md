# Rip-BD-1-sounds-Collection
Here is the collection of sounds by BD-1 as used in Jedi Fallen Orer
# BD-1 Voice Assistant Project

Welcome to the **BD-1 Voice Assistant Project**!  
This repository aims to create a voice assistant using BD-1’s sound library.

![BD-1 Sound Project](https://th.bing.com/th/id/OIP.Shcaq2sc_Ovxg0BefIrLsAHaLO?rs=1&pid=ImgDetMain)


**Work in Progress:** The database is not yet complete (I still have around 5 hours of audio files to review).

---

## Project Goal

The objective of this project is to **build an AI-driven assistant** that responds using BD-1’s iconic sounds in an emotionally coherent way.  

For example:  
- When the user says *"No"*, BD-1 should sound disappointed.  
- When the user says *"Hello"*, BD-1 should sound happy.

I'll be using and ESP32S3 for this project.

The challenge? **I have no idea how to achieve this yet.**   

However, the BD-1 soundbank contains:  
- **Complete phrases** that could be used directly.  
- **Shorter sounds** that might be combined to form meaningful responses.  

---

## How You Can Contribute

I welcome any help, as I’m new to this field!   
Here are some key tasks where you can assist:

### **1. Clean & Organize the Sound Database**
- **Remove duplicate sounds** (some clips seem to be repeated).  
- **Rename files** to reflect their emotional intent while keeping the original numbering:  
  Example: `xxxxxx-AngryBeeps.wav`, `xxxxxx-HappyChirp.wav`  
- **Sort files** into directories by emotion (Happy, Sad, Angry, etc.).
- **Important** All modification must be done inside sounds/uncompressed. Then we can run "conversion_all.py" to regenerate the uncompressed folder


### **2. Build the Response System**
- Scripts ttsbd1.py and ttsbd1sanswait.py are 2 translator (2nd is tried without wait but not found of it). They work as a TTS with a dictionnary. By studying some keyword in the answer, the program reads a sounds from one of the folder.

### **3. To be done**
- Assemble longer answer. Find a way to assemble sounds to create a longer answer when the sentence is longer.
- Ad conversationnal IA (answer from IA will be run throught the TTS)
---

## Tech & Tools

### 🔹 Proposed Approach:
I plan to use **OpenSmile** to classify BD-1 sounds by emotion.  
Then, a **script** will fetch an appropriate sound from the corresponding emotional category whenever the user expresses an emotion.

**If you have other ideas, feel free to share them!**

---

## License

This project is **community-driven** and intended for **non-commercial and fan-based use only**.  
Please verify individual file licenses before using them.

---

## Get Involved!

If you're interested in contributing:
1. **Fork this repository**  
2. **Work on any of the tasks above**  
3. **Submit a pull request** with your improvements  

Let’s bring BD-1 to life together! 🤖🎶  

---

## Thanks

Special thanks to:  
- **[vigonotion/tts.astromech](https://github.com/vigonotion/tts.astromech)** for inspiring this project!  
- **[BD-1 Sound Database Spreadsheet](https://docs.google.com/spreadsheets/d/1isG7yhRa6qXGd1NMjFjuTrLWa93BwfY8t4Y0y8e7ufs/edit?pli=1&gid=541004497#gid=541004497)** for helping navigate the game’s audio files.  

---

**Thank you for your help! May the Force be with you.** 