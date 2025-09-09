# CMPS 2200  Recitation 02

**Name (Team Member 1):**Davis Voelkel
**Name (Team Member 2):**Isaiah Kushner

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.



## Running and testing your code
- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [ ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [ ] 2. (2 point) Test that your function is correct by calling from the command-line `pytest test_main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [ ] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [ ] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.

We consider the recurrence

$$
W(n) = \sum_{k=0}^{\log_2 n} 2^k\left(\tfrac{n}{2^k}\right), 
\quad W(1)=1.
$$


**Case 1: $f(n) = 1$**

$$
W(n) = \sum_{k=0}^{\log_2 n} 2^k \cdot 1
= 2^{\log_2 n + 1} - 1
= 2n - 1
= \Theta(n).
$$

**Case 2: $f(n) = \log n$**

$$
W(n) = \sum_{k=0}^{\log_2 n} 2^k \cdot \log\left(\tfrac{n}{2^k}\right).
$$

Expand the logarithm:

$$
W(n) = \sum_{k=0}^{\log_2 n} 2^k (\log_2 n - k).
$$

Split into two sums:

$$
W(n) = (\log_2 n) \sum_{k=0}^{\log_2 n} 2^k \-\sum_{k=0}^{\log_2 n} k 2^k.
$$

Evaluate each part:

$$
\sum_{k=0}^{\log_2 n} 2^k = 2^{\log_2 n + 1} - 1 = 2n - 1,
$$

$$
\sum_{k=0}^{\log_2 n} k 2^k = (\log_2 n - 1)2^{\log_2 n+1} + 2 = 2(\log_2 n - 1)n + 2.
$$

Put them together:

$$
W(n) = (\log_2 n)(2n - 1) - \big(2(\log_2 n - 1)n + 2\big)
= 2n - \log_2 n - 2
= \Theta(n).
$$


**Case 3: $f(n) = n$**

$$
W(n) = \sum_{k=0}^{\log_2 n} 2^k \cdot \tfrac{n}{2^k}
= n \sum_{k=0}^{\log_2 n} 1
= n(\log_2 n + 1)
= \Theta(n \log n).
$$

The code outputs match this trend for $n=100$ and $a=b=2$:

- $f(n) = 1$: 127  
- $f(n) = \log_2(n)$: 157.26489336880783  
- $f(n) = n$: 652


- [ ] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `test_compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer. 

We consider the recurrence

$$
W(n) = \sum_{k=0}^{\log_b n} a^k \ f\left(\tfrac{n}{b^k}\right),
\quad f(n) = n^c.
$$

Substitute $f(n) = n^c$:

$$
W(n) = \sum_{k=0}^{\log_b n} a^k \left(\tfrac{n}{b^k}\right)^c
= n^c \sum_{k=0}^{\log_b n} \left(\tfrac{a}{b^c}\right)^k.
$$

This is a geometric series with ratio

$$
r = \frac{a}{b^c}.
$$

To connect $r$ with the condition on $c$, notice:

$$
r > 1 \;\;\Longleftrightarrow\;\; \frac{a}{b^c} > 1
\Longleftrightarrow\ a > b^c
\Longleftrightarrow\log_b a > c,
$$

which gives

$$
W(n) = \Theta\big(n^{\log_b a}\big).
$$


$$
r = 1 \Longleftrightarrow\log_b a = c,
$$

which gives

$$
W(n) = \Theta\big(n^{\log_b a}\log n\big).
$$


$$
r < 1 \Longleftrightarrow\log_b a < c,
$$

which gives

$$
W(n) = \Theta(n^c).
$$

When setting a=b=2, we have c<1, c=1, and c>1 , which our test function passes for c=0.5 < c=1 < c= 2
- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

We consider the span:

$$
S(n) = \sum_{k=0}^{\log_2 n} f\left(\tfrac{n}{2^k}\right), \quad S(1)=f(1).
$$


**Case 1: $f(n) = 1$**

$$
S(n) = \sum_{k=0}^{\log_2 n} 1
= \log_2 n + 1
= \Theta(\log n).
$$


**Case 2: $f(n) = \log n$**

$$
S(n) = \sum_{k=0}^{\log_2 n} \log\left(\tfrac{n}{2^k}\right)
= \sum_{k=0}^{\log_2 n} \big(\log_2 n - k\big)
= (\log_2 n + 1)\log_2 n - \sum_{k=0}^{\log_2 n} k.
$$

Using $\sum_{k=0}^{m} k = \frac{m(m+1)}{2}$ with $m=\log_2 n$,

$$
S(n) = (\log_2 n + 1)\log_2 n - \frac{\log_2 n \, (\log_2 n + 1)}{2}
= \frac{1}{2}\big(\log_2 n\big)\big(\log_2 n + 1\big)
= \Theta\big((\log n)^2\big).
$$


**Case 3: $f(n) = n$**

$$
S(n) = \sum_{k=0}^{\log_2 n} \frac{n}{2^k}
= n \sum_{k=0}^{\log_2 n} \left(\frac{1}{2}\right)^k
= n \cdot \frac{1 - (1/2)^{\log_2 n + 1}}{1 - 1/2}
= 2n\left(1 - \frac{1}{2^{\log_2 n + 1}}\right).
$$

Since $2^{\log_2 n} = n$,

$$
S(n) = 2n - \frac{2n}{2^{\log_2 n + 1}}
= 2n - \frac{2n}{2 \cdot 2^{\log_2 n}}
= 2n - \frac{2n}{2n}
= 2n - 1
= \Theta(n).
$$

The test function asserts that f(n) = 1 < f(n) = logn < f(n) = n.
