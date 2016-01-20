'''This is the docstring for the tables module.

'''

# -*- coding: utf-8 -*-
import pandas as pd

def df_to_markdown_table(df, return_str=True):
    '''Creates markdown tables of pandas dataframes

    Parameters
    ----------
    df : pandas DataFrame

    return_str : boolean (True)
        If True, return string, else, return Markdown object
    
    Returns
    -------
    md : str or IPython.core.display.Markdown object

    '''
    from IPython.display import Markdown
    fmt = ['---' for i in range(len(df.columns))]
    df_fmt = pd.DataFrame([fmt], columns=df.columns)
    df_formatted = pd.concat([df_fmt, df])
    md = Markdown(df_formatted.to_csv(sep="|", index=False))
    if return_str:
        return str(md.data)
    else:
        return md


def get_style(h2 = None, p = None, hover_color = '8fbcbc'):
    '''Returns HTML head string to add style to a html table.
    
    Parameters
    ----------
    h2 : str
        Title text for head
    p : str
        Paragraph text for head
    hover_color : str (8fbcbc)
        Color for hover over highlight

    Returns
    -------
    style : str

    Notes
    -----
    Adds boostrap `table`, `table-hover`, and `table-striped` classes to table

    '''    
    style = '''
<!DOCTYPE html>
<html lang="en">

<head>
  <title>Logged Signals</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
  <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>

  <style>
  td {
    font-size: 13px;
  } 
  .table-hover tbody tr:hover td, .table-hover tbody tr:hover th {
  background-color: #%s;
  }
  </style>
</head>

<body>
<div class="container">
  <h2>%s</h2>
  <p>%s</p>
  <br>
  <table class="table table-hover table-striped">
  '''%(str(hover_color), str(h2), str(p))
    return style

def df_to_html_str(df):
    '''Creates HTML string of pandas DataFrame with no formatting.

    Parameters
    ----------
    df : pandas DataFrame

    Returns
    -------
    df_html : str

    '''
    df_html = df.to_html(na_rep='', )
    return df_html

def df_to_html_table(df, save_as, style=None, **kwargs):
    '''Writes HTML table of pandas DataFrame with style to save_as.

    Parameters
    ----------
    df : pandas DataFrame

    save_as : str
        Full path to save html file

    style : str (optional)
        Style string outputted from `get_style`

    kwargs
        Args for `get_style` (`h2`, `p`, and `hover_color`)

    Returns
    -------
    None

    '''
    df = df_to_html_str(df)
    df = df.split('<table border="1" class="dataframe">')[1]
    if style is None:
        style = get_style(**kwargs)
    f = open(save_as+'.html', 'w')
    f.write(style)
    f.write(df)
    f.write('\n</body>')
    f.close()
    return 








def foo(var1, var2, long_var_name='hi') :
    '''A one-line summary that does not use variable names or the
    function name.

    Several sentences providing an extended description. Refer to
    variables using back-ticks, e.g. `var`.

    Parameters
    ----------
    var1 : array_like
        Array_like means all those objects -- lists, nested lists, etc. --
        that can be converted to an array.  We can also refer to
        variables like `var1`.
    var2 : int
        The type above can either refer to an actual Python type
        (e.g. ``int``), or describe the type of the variable in more
        detail, e.g. ``(N,) ndarray`` or ``array_like``.
    Long_variable_name : {'hi', 'ho'}, optional
        Choices in brackets, default first when optional.

    Returns
    -------
    type
        Explanation of anonymous return value of type ``type``.
    describe : type
        Explanation of return value named `describe`.
    out : type
        Explanation of `out`.

    Raises
    ------
    BadException
        Because you shouldn't have done that.

    See Also
    --------
    thirdfunc, fourthfunc, fifthfunc

    Notes
    -----
    Notes about the implementation algorithm (if needed).

    References
    ----------
    Cite the relevant literature

    Examples
    --------
    These are written in doctest format, and should illustrate how to
    use the function.

    >>> a=[1,2,3]
    >>> print [x + 3 for x in a]
    [4, 5, 6]
    >>> print "a\n\nb"
    a
    b

    '''
    pass