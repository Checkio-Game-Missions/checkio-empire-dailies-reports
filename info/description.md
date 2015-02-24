Ingots in each consignment are numbered in the row from A1 to Z9 as A1, A2,..., A9, B1, B2, ..., Z9. 
Each consignment is marked with the number of the last ingot in it so you can define the quantity of ingots by the number of marks.
Each daily report is written as a list of marks in a string separated by commas.
This way you can count the total quantity of ingots produced in a day.

The full report contains daily reports for several days.
Each report is given with a date in the following format:
`YYYY-MM-DD`, where YYYY is year, MM is month, DD is day.
Dates and reports are separated by whitespace. Each date-report is placed on a separate line.

You are given a full report as multiline text with two dates.
You should calculate the total quantity of ingots for the days between the given dates (**including the given dates**).

For example, you are given the following report:

```
2015-01-01 A1,B2
2015-01-05 C3,C2,C1
2015-02-01 B4
2015-01-03 Z9,Z9

From: 2015-01-01
To:   2015-01-31
```

For these dates we see three "good" days: 2015-01-01, 2015-01-03, 2015-01-05.
- 2015-01-01 == 1 + 11 == 12
- 2015-01-03 == 21 + 20 + 19 == 60
- 2015-01-05 == 234 + 234 == 468

So the result is 540.
