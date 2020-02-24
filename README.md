# Visualization of Collatz conjecture and its generalization

This is my visualization and Python source code for Collatz conjecture and a generalization proposed by Zhang Zhongfu and Yang Shiming. See also my blog post, which is more detailed, [here].

## Contents
- [Preliminaries](#preliminaries)
- [Important notes](#important-notes)
- [Examples](#examples)
- [References](#references)

## Preliminaries

[**Collatz conjecture** and **Zhongfu and Shiming's generalization**]

## Important notes

- The visualization ignores cases where total stopping time exceeds a certain threshold (automatically set 1e4) to save computational resources.
- Parameter `log_scale` of the `main_plot` function allows log scale and linear scale visualization preferences. 

## Examples

**Example 1**

This example plots total stopping time in the original Collatz conjecture for integers from 1 to 1e5 in linear scales.

`main_plot(prime = 3, max_value = 100000)`

![ex1](Examples/ex1.png)

**Example 2**

This example plots total stopping time in the case "5n + 1" for integers from 1 to 1e5 in linear scales.

`main_plot(prime = 5, max_value = 100000)`

![ex2](Examples/ex2.png)

**Example 3**

This example plots total stopping time in the case "3n + 1" for integers from 1 to 1e5. x axis is in log scale.

`main_plot(prime = 3, max_value = 100000, log_scale = (True, False))`

![ex3](Examples/ex3.png)

**Example 4**

This example plots total stopping time in the case "7n + 1" for integers from 1 to 1e4 in linear scales.

`main_plot(prime = 7, max_value = 10000)`

![ex4](Examples/ex4.png)

## References

[1]J. Lesieutre, 'On a Generalization of the Collatz Conjecture’, p. 31.

[here]: https://minnq.github.io/coding%20practice/2019/09/03/collatz/
[**Collatz conjecture** and **Zhongfu and Shiming's generalization**]: https://minnq.github.io/website/visualization/2019-09-03/collatz.html#preliminaries
