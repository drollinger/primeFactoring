* PRIME FACTORING

I'm sure this algorythm exists somewhere but I couldn't find it so I decided to write it.

A little factoring program that uses the fact that there exists a square number such that it, minus a semi prime number equals another square number. Using some optimization to factor a semi-prime, it solves by digits, which is not very effiecient. The main gains are seen in solving the first 7-8 digits. These are the digits of the square number. The program will print out the number 'a' such that a^2 - sp = b^2. To find the prime simply calculate a - b. Slow down is significant after semiprime numbers larger than 20 digits. The sample is 21 digits (69bits) and takes about a minute to finish. This was a simple day project so there are many further optimizations that could be made but this program is more to test an idea than be fully optimized. Biggest lack of optimization is in memory usage. Also, values are hard coded. If this is actually interesting to anyone let me know and I can clean up a lot of stuff.  