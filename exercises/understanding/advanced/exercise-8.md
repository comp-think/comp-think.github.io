## Understanding - Advanced, exercise 8

### Text
The variable `my_gr` contains the string of one or more words in lowercase (e.g. `"what a wonderful world"`), the variable `my_fn` contains the string of a family name in lowercase (e.g. `"doe"`), and the variable `my_mat` the string of ten 0-9 digits (e.g. `"0000123456"`). Study the execution of the following functions when they are called as follows: `m(my_gr, my_fn, my_mat)`.

```python
def m(gr, fn, mat):
    c = ""
    gr_l = list(gr)
    fn_l = list(fn)
    if len(mat):
        idx = int(mat[0])
        gn_idx = idx % len(gr_l)
        fn_idx = idx % len(fn_l)
        n_idx = gn_idx + fn_idx
        if gr_l[gn_idx] < fn_l[fn_idx]:
            gr_l[n_idx % len(gr_l)] = fn_l[n_idx % len(fn_l)]
        else:
            fn_l[n_idx % len(fn_l)] = gr_l[n_idx % len(gr_l)]
        c = gr_l[n_idx % len(gr_l)]
        return c + m("".join(gr_l), "".join(fn_l), mat[1:])
    else:
        return c
```

### Hints
The recursive function `m` processes all the digits in `mat` until the end. Each time such a digit is processed, a characters coming from the other two input strings is chosen and composed in the final result the function will return. 

### Additional material
The runnable [Python file](exercise_8.py) is available online. You can run it executing the command `python exercise_8.py` in a shell, and then following the instructions on screen to specify the intended input.
