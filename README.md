# gibberish

## Introduction & User Guide
gibberish is a small tool that creates gibberish text. Like straight up random words with no structure. It does however mimic the English language to a very small extent on the larger scale as far as sentences and paragraphs go. I made it because I wanted a text generator for when I'm building a website or doing anything else where I may need text placeholders. I realise that most people would make it so it uses an English dictionary instead of using randomly generated text. The reason I didn't do that is because I wanted to have roughly the format of English without the words.. why? because it's distracting for me. When I'm working against a deadline I want to work as efficiently as possible with as little distraction as possible.  

Straight off the bat all it needs to run is a word count:  
`gibberish 500`   
That will generate a 500 word gibberish wall of text.  
  
Split into paragraphs.  
`gibberish 500 -p 79`  
That will split the text into paragraphs 7-9 sentences long.   
  
Set the line width.  
`gibberish 500 -w 8`  
Cuts each line off at 8 words.  
  
## Warning
There is no error handling in this script! None! Should work as long as you don't get too crazy with the parameters.   
Furthermore when you use the paragraphs flag you may run into an error where some of the first lines will be only 1 - 3 words long.
