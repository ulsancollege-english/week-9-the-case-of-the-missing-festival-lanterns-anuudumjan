# Week 9 Homework: The Case of the Missing Festival Lanterns

## Student Info

Name: Anu  
Student number: 2412096
GitHub username: AnuuDumjan  

---

## Summary

This program analyzes festival lantern records to find missing, unexpected, duplicate, and misplaced lanterns. The `analyze_lanterns` function receives a set of expected lanterns, a log of lantern records, and a dictionary of correct lantern sections. It processes the records and checks whether each lantern appears in the correct location. The program then returns a report dictionary containing useful information about the lantern records. This helps organizers quickly identify problems in the festival setup.

---

## Approach

- First, I created sets and dictionaries to store seen lanterns, duplicate lanterns, section counts, and wrong-section lanterns.
- During the loop, I checked each lantern record and added the lantern names to the correct collections.
- I used a set to detect duplicate lanterns efficiently.
- I counted how many lantern records appeared in each section using a dictionary.
- I checked whether expected lanterns were placed in the correct section.
- After the loop, I used set operations to find missing and unexpected lanterns.
- Finally, I returned all results inside one report dictionary.

---

## How I Used Dictionaries and Sets

1. Which parts of your solution used sets?

- I used sets for `seen_lanterns`, `seen_once`, `duplicate_lanterns`, `missing_lanterns`, and `unexpected_lanterns`.

2. Which parts of your solution used dictionaries?

- I used dictionaries for `count_by_section` and `wrong_section_lanterns`.

3. Why were dictionaries or sets better than using only lists?

- Sets are faster for checking duplicates and membership because lookup operations are efficient.
- Dictionaries are useful for storing key-value pairs like section counts and expected/actual section information.
- Using only lists would require extra loops and make the program slower.

Your explanation:

```text
Sets helped me quickly check whether a lantern had already been seen and made it easy to find missing or unexpected lanterns using set operations. Dictionaries helped me store counts for each section and keep track of wrong-section lantern information. They were better than lists because they provide faster lookup and cleaner code.