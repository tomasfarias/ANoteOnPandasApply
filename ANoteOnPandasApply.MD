## A quick note on pandas' apply

While working with `pandas` in several ocassions I have come across what I consider to be an abuse of the `apply` method. Picture the following example: you are reading some JSON data from an external API into a DataFrame and this data has a `PurchaseDate` column. Since you are going to do some filtering, you will need to convert the `PurchaseDate` column from `string` to `datetime.datetime` (or some other datetime-like type). One way of achieving this is with `apply`:

<script src="https://gist.github.com/tomasfarias/6caa940796142c49f100a0937223557d.js"></script>

Running this script works as expected:

```
$ python example.py
0   2019-08-12
1   2019-08-11
Name: PurchaseDate, dtype: datetime64[ns]
```

Is this the optimal way of achieving this result? Pandas has it's own `to_datetime` method which works just as fine:

<script src="https://gist.github.com/tomasfarias/35fb2a830f81520e68a8b16d21b32a03.js"></script>

So, which one should we use? Let's run some `timeit` tests in a [Jupyter Notebook](https://github.com/tomasfarias/ANoteOnPandasApply/blob/master/TimeitTests.ipynb) to try to catch any speed differences:

<img src="https://raw.githubusercontent.com/tomasfarias/ANoteOnPandasApply/master/imgs/apply_vs_to_datetime.png" alt="apply vs to_datetime" align="middle">

Not so surprisingly, the `apply` method ran close to linear time. The more surprising result, at least it was for me the first time I did this, was that `to_datetime` ran at an almost constant time. It appears that when the number of rows is on the lower side `apply` runs faster, but as soon as we go a bit large `to_datetime` starts working significantly faster.

I repeated the tests for a few more comparisons. In all cases the `pandas` alternative outperformed apply:

Comparing `apply` vs `add` to sum a constant value:

<img src="https://raw.githubusercontent.com/tomasfarias/ANoteOnPandasApply/master/imgs/apply_vs_add.png" alt="apply vs add" align="middle">

Comparing `apply` vs `str.replace` to do simple string replacement:

<img src="https://raw.githubusercontent.com/tomasfarias/ANoteOnPandasApply/master/imgs/apply_vs_str_replace.png" alt="apply vs str.replace" align="middle">

I expected this one to take the same as `pandas` simply let's us access the underlying string object's `replace` method. Both options have apparently the same complexity, as the difference between them remains constant. The constant difference might be related to `pandas` calling the [applied function twice on the first row](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html).

## Conclusion

While writing this quick note I intended to gather evidence to convice myself of always checking the documentation to see if pandas already implemented a method I can use for whatever I'm doing. I hope this can serve as a source of inspiration for you too and I'll keep adding more examples to the blogpost and [Jupyter Notebook](https://github.com/tomasfarias/ANoteOnPandasApply/blob/master/TimeitTests.ipynb) as I come across them.
