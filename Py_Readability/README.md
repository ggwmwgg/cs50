## Readability (from CS50 course Problem Set 6)

#### Description 
Program that calculates the approximate grade level needed to comprehend some text using Coleman-Liau index.

#### Technologies used:
- *Python*

#### Usage example
```
$ python readability.py
Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
Grade 3
```

### Coleman-Liau index
A number of “readability tests” have been developed over the years that define formulas for computing the reading level of a text. One such readability test is the Coleman-Liau index. The Coleman-Liau index of a text is designed to output that (U.S.) grade level that is needed to understand some text. The formula is
```index = 0.0588 * L - 0.296 * S - 15.8```
where ```L``` is the average number of letters per 100 words in the text, and S is the average number of sentences per 100 words in the text.

#### Contributing
Pull requests are welcome. For major changes please open an issue first to discuss what you would like to change.