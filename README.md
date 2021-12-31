# pymocklib

This is a Python 3.10 port of <https://git.eisfunke.com/software/mock/>, a library for manipulating human-readable message strings.

> _Disclaimer_: This library has **nothing to do with mocking in the software development world**. Rather, it takes mocking
> in a more literal sense of _mocking sth. or someone_. I want to excuse any confusion that arises from the somewhat
> overloaded term of _mocking_

It does stuff like this:

```python
In [1]: import mock

In [2]: mock.to_random("pymocklib is a sick library. like sick as in ill")
Out[2]: 'PYMoCKlib is a SIcK LIBrary. LIkE siCK as in ILL'

In [3]: mock.to_alternating("pymocklib is really dope. Like your mom, probably")
Out[3]: 'pYmOcKlIb is reAlLy doPe. LIKe yoUr moM, prObAbLy'

In [4]: mock.to_pseudo_cyrillic("pymocklib is really dope. Like your mom probably")
Out[4]: 'pџmөcкlɪв ɪs яёдllџ dөpё. Lɪкё џөця mөm pяөвдвlџ'

In [5]: print(mock.to_square("wtf?!"))
w t f ? !
t
f
?
!

In [6]: print(mock.to_clap("what the actuall fucking shite?"))
what👏the👏actuall👏fucking👏shite?
```
