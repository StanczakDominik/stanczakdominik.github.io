---
categories:
  - python
  - TIL
  - linux
date: 2024-11-01T16:16:00
date_created: 2024-11-01T10:31:12+01:00
title: "`whisper_mic`, a simple Python voice dictation utility"
---
I've been using  Google's speech-to-text input on my Android phone, to note things down on the go while walking the dog etc, and I've realized that I don't actually know anything like that on Linux! While looking for tools solving that use case, I found this [`whisper_mic`](https://github.com/mallorbc/whisper_mic) little utility that you can just install with `pipx install whisper_mic`, and it works pretty nicely! I just had to tinker with with the settings a little bit. Here's what finally worked for me:

```bash
whisper_mic --mic_index 7 --loop --dictate --model large-v3 --english
```

The weird thing about this is that it doesn't output the text it parses into standard output, which is how I thought it would work. Instead it emulates the keyboard using the [pynput](https://github.com/moses-palmer/pynput) library. First it turns your speech into text, and then it turns that into keystrokes into the window you have focused with your mouse. In fact, this whole blog post was typed, (well, dictated, then edited) right into ~~abszigám~~ Obsidian. You can see the raw output at the end of the post.

Did you see that Hungarian-looking word, though? It's a trend for its fatal flaw: if you don't specify `--english`,  then it starts making mistakes on, I suspect, stuff I'm mispronouncing. Still, this is mostly usable for everyday use cases.

Let me do a couple more tests, such as a few keystrokes with my mechanical keyboard, which is pretty loud:

> abcdefghijkはい

Well, I certainly didn't input any... What script is that? Is that Japanese? [Wow I'll have to identify it later.](https://www.linguee.com/japanese-english/translation/%E3%81%AF%E3%81%84.html "While the most common usage of that is 'yes', in accordance with all laws of irony, another possible reading of that was 'loss'.") For the second test, I'll give it [a quote from Star Trek](https://www.youtube.com/watch?v=LTye5SHVQl0)...

> Darmok at Tanagra. いelát etnáři. Tanagra. Tanagra. Ta nagra on the ocean. Darmok and Jelad at and Agra. The Beast at Tanagra? Husani, his army, when the mol When the walls fell? No, Shaka, when the world... when the walls fell with the world. Darma Kent Gelat on the ocean.
	
So, obviously it's struggling on the names, which is not unexpected. The second thing I would like to do is to check whether it actually understands Polish language. I think the the large models. for Whisper did promise to handle Polish, but let's see how well it does at that. and see whether that makes a difference. I'll use the [Scribe's monologue from Asterix & Obelix Mission Cleopatra](https://www.youtube.com/watch?v=aiHW6BSm_p0 "Jak to jest być skrybą, dobrze?"), a cult classic here in Poland. *ahem*

> Wie pan, moim zdaniem to nie ma tak, Ze dobrze albo, Ze niedobrze. Gdybym miaL powiedzieC co ceniE w Zyciu najbardziej powiedziaLbym, Ze ludzi. по дальній війні, по мосту Удвоєнкк, де особі не... dziwiE, kiedy byLem sam i to ciekawe. To wLaSnie przypadkowe spotkania... majA na nasze Zycie. Chodzi o to, Ze kiedy wyznaleXC pewnA wartoSC nawet pozornie uniwersalne. ... znajduje siE, by tak szedL, zrozumienia, ktOre pomaga siE nam rozwijaC. Ja miaLem szczEScie, poniewaZ poniewaZ siE znalazLem i dziEkujE mu, dziEkujE, Ze Zycie to jest taniec, Zycie to jest Smiech. Ze Zycie to miLoSC. Wiele ludzi pyta mnie, o to samo, ale jak se to robí? skAd czerpiesz tE radoSC, a ja odpowiadam, Ze Ze to proste. To umiLowanie Zycia. to wLaSnie ono sprawia, Ze CiS na przykLad BudujE maszynE, a jutro kto wie? Dlaczego by nie? Oddam siE... pracy spoLecznej i bEdE choCby sadziL, znaczy tak Ik ben... Normaal.

Okay, it tried bravely and did its best, definitely, but not only did it mangle all the diacritics (ąęćęłńóśżź) into their basic characters' uppercase variants, it's also a little bit too jumpy between languages. I could tell you ahead of time that I'm only going to use English and Polish for the test here, and instead I think it did a bit of [Ukrainian](https://translate.google.com/?sl=auto&tl=en&text=%D0%BF%D0%BE%20%D0%B4%D0%B0%D0%BB%D1%8C%D0%BD%D1%96%D0%B9%20%D0%B2%D1%96%D0%B9%D0%BD%D1%96%2C%20%D0%BF%D0%BE%20%D0%BC%D0%BE%D1%81%D1%82%D1%83%20%D0%A3%D0%B4%D0%B2%D0%BE%D1%94%D0%BD%D0%BA%D0%BA%2C%20%D0%B4%D0%B5%20%D0%BE%D1%81%D0%BE%D0%B1%D1%96%20%D0%BD%D0%B5&op=translate "after a distant war, along the Udvoenkk bridge, where no one is") and at the end of the Otis quote it just went straight into Dutch! Checking the settings, there is unfortunately no option to specify prior languages like that, only to switch fully to the model trained entirely on English.

What's more, I kept trying this, and it actually started crashing on trying to input letters you can't input using my current `pl_PL` keyboard layout:

 ```python
 Traceback (most recent call last):
  File "/home/dominik/.local/pipx/venvs/whisper-mic/lib/python3.12/site-packages/pynput/keyboard/_base.py", line 492, in type
    self.release(key)
  File "/home/dominik/.local/pipx/venvs/whisper-mic/lib/python3.12/site-packages/pynput/keyboard/_base.py", line 427, in release
    self._handle(resolved, False)
  File "/home/dominik/.local/pipx/venvs/whisper-mic/lib/python3.12/site-packages/pynput/keyboard/_xorg.py", line 235, in _handle
    raise self.InvalidKeyException(key)
pynput.keyboard._base.Controller.InvalidKeyException: 'š'
```

š being an oryginally Czech symbol.

I also tried a few more examples with the `--english` flag:

> Obsidian Darmok. Tanagra. Then I'm looking into gelato on a 10-hour gram no scratch that Darmok and Jalad at Tenagra. Darmok and the gelat on the ocean. Chaka, when the walls fell.

Well, at least it's no longer outputting keystrokes that crash when my Polish layout fails to input them, so that's an improvement, and I can safely recommend it with `--english`. I would not, however, use it to communicate with ~~telegrams~~ Tanagrans, they're bound to be mighty confused about Darmok with a gelato on a 10-hour gram!
 
<details>

<summary>Raw output plus the commands</summary>

  ```
  whisper_mic --mic_index 7 --loop --dictate
  ```

> I recently started that we are using Google's. speech to text on Um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um, um Android 2 To note down. F4 spectrometer intensity Course filter silence была get C C right dog etc. What the actual fuck? Okay, that's pretty simple terrible. Let me try another model.


  ```
  whisper_mic --mic_index 7 --loop --dictate --model large-v3
  ```

> Let's see whether this is... better perhaps. Okay, looks promising. Okay So take two. I recently started using Google's speak to text on my Android phone. to note things down on the go. while walking the dog etc. And I've realized that I've been looking for something like that on Linux for a while actually. Um And I, while looking For tools solving that use case I found this whistle whisper_mine mic as in microphone little utility that you can just install with pipx using pipx install whisper mic And literally just kind of except I had to tinker with with the settings a little bit. Here's what I by what worked for me. to do paste the line I use. The weird thing about this is that It doesn't output P-strokes into like standard output which is something but I expected from this? I thought that that was how... it would work. Instead it I think it emulates the keyboard, actually how does it do that? That's to do. And it... outputs keystroke for the text it interprets from from your speech into the window you have sort of focused with your mouse. I'm uh... Typing. Well, typing. dictating this right into abszigám for example, obsidian No, okay. It's doing actually quite well. It's making a few... mistakes on I suspect stuff I'm mispronouncing because again not a native speaker car Suddenly there's a car. But still, this is actually pretty pretty decent and mostly usable. or for everyday use cases. Let me do a couple more tests. So actually... Let me do a keystroke. with my mechanical keyboard. which was pretty loud. Maybe a couple.abcdefghijkはい Well, I certainly didn't input any. What script is that? Is that Japanese? Wow fancy I'll have to identify it later Okay, and for the second test, I would... actually give it first. quote from Star Trek. Darmok at Tanagra. いelát etnáři. Tanagra. Tanagra. Ta nagra on the ocean. Darmok and Jelad at and Agra. The Beast at Tanagra? Husani, his army, when the mol When the walls fell? No, Shaka, when the world... when the walls fell with the world. Darma Kent Gelat on the ocean. So obviously it's struggling. on the names Right, which is not... not unexpected. The second thing I would like to do and I'm going to do this twice. is Let's give it a test for... actually understanding policy language. I think the the large V3 model. for whisper Um... did promise to handle Polish but let's see How well it does at that I'm going to do Do it twice. first up I'm going to just continue speaking in this sort of session I guess and then I'm going to start another session. and see whether that makes a difference. *ahem* Wie pan, moim zdaniem to nie ma tak, Ze dobrze albo, Ze niedobrze. Gdybym miaL powiedzieC co ceniE w Zyciu najbardziej powiedziaLbym, Ze ludzi. по дальній війні, по мосту Удвоєнкк, де особі не... dziwiE, kiedy byLem sam i to ciekawe. To wLaSnie przypadkowe spotkania... majA na nasze Zycie. Chodzi o to, Ze kiedy wyznaleXC pewnA wartoSC nawet pozornie uniwersalne. ... znajduje siE, by tak szedL, zrozumienia, ktOre pomaga siE nam rozwijaC. Ja miaLem szczEScie, poniewaZ poniewaZ siE znalazLem i dziEkujE mu, dziEkujE, Ze Zycie to jest taniec, Zycie to jest Smiech. Ze Zycie to miLoSC. Wiele ludzi pyta mnie, o to samo, ale jak se to robí? skAd czerpiesz tE radoSC, a ja odpowiadam, Ze Ze to proste. To umiLowanie Zycia. to wLaSnie ono sprawia, Ze CiS na przykLad BudujE maszynE, a jutro kto wie? Dlaczego by nie? Oddam siE... pracy spoLecznej i bEdE choCby sadziL, znaczy tak Ik ben... Normaal.

> Ok, wiEc prObowaL bardzo dzielnie. Okay, so it tried... And uh... did its best, definitely. Uh... but it's a little bit It's maybe a little bit... too jumpy between lengths. languages. Like I could tell you I have of time but I'm only going to English and Polish the test here and here I think it did a bug of text in Russian or Ukrainian I see a little bit of I think I saw a little bit of Czech or Slovakian in there and at the end of the Otis quote It just went straight up Uh... Nederlandish? Let me check the settings whether there there's an option to specify the languages I'm going to be using.
> No, unfortunately... There is no such option. Thank you for watching. Okay, I'm now going to repeat da poli
 
```python
 Traceback (most recent call last):
  File "/home/dominik/.local/pipx/venvs/whisper-mic/lib/python3.12/site-packages/pynput/keyboard/_base.py", line 492, in type
    self.release(key)
  File "/home/dominik/.local/pipx/venvs/whisper-mic/lib/python3.12/site-packages/pynput/keyboard/_base.py", line 427, in release
    self._handle(resolved, False)
  File "/home/dominik/.local/pipx/venvs/whisper-mic/lib/python3.12/site-packages/pynput/keyboard/_xorg.py", line 235, in _handle
    raise self.InvalidKeyException(key)
pynput.keyboard._base.Controller.InvalidKeyException: 'š'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/dominik/.local/bin/whisper_mic", line 8, in <module>
    sys.exit(main())
             ^^^^^^
  File "/home/dominik/.local/pipx/venvs/whisper-mic/lib/python3.12/site-packages/click/core.py", line 1157, in __call__
    return self.main(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dominik/.local/pipx/venvs/whisper-mic/lib/python3.12/site-packages/click/core.py", line 1078, in main
    rv = self.invoke(ctx)
         ^^^^^^^^^^^^^^^^
  File "/home/dominik/.local/pipx/venvs/whisper-mic/lib/python3.12/site-packages/click/core.py", line 1434, in invoke
    return ctx.invoke(self.callback, **ctx.params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dominik/.local/pipx/venvs/whisper-mic/lib/python3.12/site-packages/click/core.py", line 783, in invoke
    return __callback(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dominik/.local/pipx/venvs/whisper-mic/lib/python3.12/site-packages/whisper_mic/cli.py", line 42, in main
    mic.listen_loop(dictate=dictate,phrase_time_limit=2)
  File "/home/dominik/.local/pipx/venvs/whisper-mic/lib/python3.12/site-packages/whisper_mic/whisper_mic.py", line 212, in listen_loop
    self.keyboard.type(result)
  File "/home/dominik/.local/pipx/venvs/whisper-mic/lib/python3.12/site-packages/pynput/keyboard/_base.py", line 495, in type
    raise self.InvalidCharacterException(i, character)
pynput.keyboard._base.Controller.InvalidCharacterException: (8, 'š')
```

> Okay, so this is fascinating. I was going to to check afterwards. what library at the season that it actually crashed on Trying to... I'll have to check. what kind of character. from what script it says but it's It's not one... my Polish keyboard layout. can actually input. It looks like some sort of Slovakian Yes. Thing. S. the letter S. Thank you. Okay, on to the game. quote Q Wie Pan, moim zdaniem to nie ma tak, Ze dobrze, albo Ze niedobrze. Gdybym miaL powiedzieC co stanie w Zyciu najgorsze bardziej powiedziaLbym, Ze ludzi, ludzi, ktOrzy в

  ```
  whisper_mic --mic_index 7 --loop --dictate --model large-v3 --english
  ```
> Let me actually try this again now I'm going to use the English flag for the model. Obsidian Darmok. Tanagra. Then I'm looking into gelato on a 10-hour gram no scratch that Darmok and Jalad at Tenagra. Darmok and the gelat on the ocean. Chaka, when the walls fell. Well, at least it's no longer out- putting keystrokes that help crash when my Polish layout fails. to input them, so that's... an improvement I suppose. But I don't think this would be a quite communicative for a telegram.


</details>
