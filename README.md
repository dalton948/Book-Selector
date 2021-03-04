# Book-Selector


Small project that takes a list of books from a CSV and randomly selects 1 from the list. I was going to include genre selection but didn't have a clear picture on how I wanted that to work. Decided to add logging as a 4th feature.

The 4 features i have met are as follows:
1. Implement a "Master Loop" - The program will not exit unless you tell it to do so.
2. Create and call 3 functions - There are 4 functions that operate off each other. First function greets the user and asks them what they want to do, the second generates a random book if chosen to do so, the third creates the loop to continue or exit, and the final function pulls them together and does a bit of error filtering.
3. Read data from an external file - the Books are imported via CSV and is where the random selection takes place.
4. Implement a log that records errors\invalid inputs - Implemented logging that captures value and type errors while also giving what was inputted. Also tells me when the program is in its choosing phase or exited.