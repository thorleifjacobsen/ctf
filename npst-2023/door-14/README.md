# 📖 Bokorm

En snok vi mistenker å stå i ledetog med Pen GWYN har blitt arrestert etter å ha brutt seg inn i NordPolarBiblioteket og stjålet noen bøker. Vi mistenker at de har vært ute etter noe spesifikt, men vi blir ikke helt kloke på hva det er. Snoken ble tatt med en stabel bøker og et notat.

Bøkene har vi gitt tilbake til biblioteket, men her er en liste av dem som ble stjålet:

*   
* Radium og radioaktive stoffer, samt nyere opdagelser angaaende straaler
* Undertrykking av objekter med høy luminans ved hjelp av en romlig lysmodulator under avbildning med CCD- og lysforsterkningskamera
* Om den yngre Jernalder i Norge : 1. afdeling
* Storlogens Konstitution og Tillægslove
* Sild- og saltfiskretter

Notatet inneholdt dette her:
```
(55, 1, 2, 1), (65, 17, 6, 3), (19, 3, 8, 1), (13, 5, 6, 2), (14, 11, 4, 8), (27, 32, 12, 2), (9, 7, 12, 3), (82, 5, 2, 8), (78, 3, 11, 1), (71, 5, 1, 8), (76, 1, 6, 2), (92, 1, 1, 1), (50, 2, 1, 5), (15, 1, 1, 1), (82, 16, 10, 4), (23, 6, 1, 1), (34, 16, 7, 1), (92, 11, 3, 2), (50, 5, 6, 1), (1, 3, 5, 12), (42, 2, 1, 1), (15, 3, 1, 3), (23, 8, 1, 2), (90, 2, 5, 1), (83, 1, 1, 2), (59, 29, 9, 4), (93, 4, 1, 16), (82, 8, 3, 5), (39, 1, 1, 8), (77, 7, 9, 1), (93, 8, 6, 8), (1, 1, 3, 6), (83, 10, 8, 1), (23, 1, 1, 1), (69, 2, 9, 2), (76, 12, 3, 4), (7, 1, 3, 1), (3, 9, 9, 2), (19, 1, 6, 10), (93, 14, 7, 5), (13, 31, 7, 10), (3, 1, 9, 2), (7, 2, 6, 1), (23, 19, 4, 3), (50, 6, 5, 11)
```

Send svar til meg om du finner ut av det.

- Tastefinger

# Writeup

Looks like a page, line, word, letter cipher. Need to find the book. As this is the Pen GWYN I can guess they like their herrings? The book `Herring and salt water fish dishes` sounds apetizing. But google shows nothing. So guessing it was red.

Found one book available at the norwegian library the [Om den yngre Jernalder i Norge : 1. afdeling](https://www.nb.no/items/ca795dec965d2fb7abb5dffa71a7f81c?page=61&searchText=Om%20den%20yngre%20Jernalder%20i%20Norge)

This is my working area: 

```
(55, 1, 2, 1) = p
(65, 17, 6, 3) = s
(19, 3, 8, 1) = t
(13, 5, 6, 2) = ) / k
(14, 11, 4, 8) = r
(27, 32, 12, 2) = ø?
(9, 7, 12, 3) = l?
(82, 5, 2, 8) = l?
(78, 3, 11, 1) = p
(71, 5, 1, 8) = a?
(76, 1, 6, 2) = r?
(92, 1, 1, 1) = a?
(50, 2, 1, 5) = n?
(15, 1, 1, 1) = t?
(82, 16, 10, 4) = e? 
(23, 6, 1, 1) = s

(34, 16, 7, 1) = b
(92, 11, 3, 2) = o
(50, 5, 6, 1) = K
(1, 3, 5, 12) = s
(42, 2, 1, 1) = t
(15, 3, 1, 3) = a
(23, 8, 1, 2) = v
(90, 2, 5, 1) = J
(83, 1, 1, 2) = a
(59, 29, 9, 4) = k?
(93, 4, 1, 16) = t
(82, 8, 3, 5) = k
(39, 1, 1, 8) = r
(77, 7, 9, 1) = Ø !
(93, 8, 6, 8) = d !
(1, 1, 3, 6) = l !

(83, 10, 8, 1) = k?
(23, 1, 1, 1) = r?
(69, 2, 9, 2) = ø?
(76, 12, 3, 4) = l?
(7, 1, 3, 1) = l?
(3, 9, 9, 2) = p?
(19, 1, 6, 10) = a?
(93, 14, 7, 5) = r?
(13, 31, 7, 10) = a?
(3, 1, 9, 2) = n?
(7, 2, 6, 1) = t?
(23, 19, 4, 3) = e?
(50, 6, 5, 11) = s?
```

Made my own logic by doing `?` as guessed letter. `!` is double confirmed and nothing is confirmed.
Figured out that it said `krøllparentes` pretty fast which is `{}` then `bokstavjaktkrødl`. I figured out after a while that there is a mistake here. That `d` should be `l` so probably the whole word is:

`pst-krøllparantes-bokstavjakt-krøllparentesslutt`

# Flag

```
PST{BokstavJakt}
```

# Mistake

I think this was supposed to be `93, 8, 6, 7`

```
(93, 8, 6, 8) = d !
```