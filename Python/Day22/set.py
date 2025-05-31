Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s={1,2,3,4,5}
>>> r={4,5,6,7,8}
>>> s.union(r)
{1, 2, 3, 4, 5, 6, 7, 8}
>>> s.intersection(r)
{4, 5}
>>> r.difference(s)
{8, 6, 7}
>>> s.difference(r)
{1, 2, 3}
>>> s|r
{1, 2, 3, 4, 5, 6, 7, 8}
>>> s&r
{4, 5}
>>> s-r
{1, 2, 3}
>>> r-s
{8, 6, 7}
>>> s^r
{1, 2, 3, 6, 7, 8}
>>> s.symmetric_difference(r)
{1, 2, 3, 6, 7, 8}
