## Plurality C (from CS50 course Problem Set 3)

#### Description
Program that runs a plurality election using plurality vote method.

#### Technologies used:
- *C*

#### Usage example
```
$ ./plurality Alice Bob Charlie
Number of voters: 4
Vote: Alice
Vote: Bob
Vote: Charlie
Vote: Alice
Alice
```

### Background
Elections come in all shapes and sizes. In the UK, the [Prime Minister](https://www.parliament.uk/about/how/elections-and-voting/general/ "General elections") is officially appointed by the monarch, who generally chooses the leader of the political party that wins the most seats in the House of Commons. The United States uses a multi-step [Electoral College](https://www.archives.gov/federal-register/electoral-college/about.html "What is the Electoral College?") process where citizens vote on how each state should allocate Electors who then elect the President.
Perhaps the simplest way to hold an election, though, is via a method commonly known as the “plurality vote” (also known as “first-past-the-post” or “winner take all”). In the plurality vote, every voter gets to vote for one candidate. At the end of the election, whichever candidate has the greatest number of votes is declared the winner of the election.

#### Contributing
Pull requests are welcome. For major changes please open an issue first to discuss what you would like to change.