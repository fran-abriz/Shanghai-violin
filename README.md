# Shanghai-violin
## Analyze scores from an international violin competition
This project was motivated by some interesting data that came my way: the judges' actual scores from a violin competition held in Summer 2016, the inaugural Shanghai Isaac Stern International Violin Competition.  Normally, judges' scores are not made public.

An account of the competition as it unfolded were blogged by Laurie Niles, editor of _violinist.com._  Several of her blogs can be found here:  www.violinist.com/blog/laurie/20168

I was intrigued by reader comments regarding the general issue of judges favoring their students and former students in violin competitions because scores are not made public, and how releasing the scores might bring that issue to light and possibly mitigate it.  When I recently decided to spend time learning some of the Python statistical add-ons such as __Matplotlib__ and __Pandas__, I thought that analyzing this data might be a fun way to do it.

I had PDF files of the quarterfinal scores (24 contestants, 11 judges) and some of the semifinal scores.  Because the semifinal round consisted of several performances by each semifinalist, I worked only with the quarterfinal data.  The final six competitors in this data became the finalists in the competition and the winner was Mayu Kishima, the 20th competitor in the dataset.

This is a preliminary exploratory analysis of the data.  My first realization was that judges do not distribute their scores in the same way.  For example, some scored all competitors uniformly low; some skewed their scores one way or another.  I standardized the scores for each judge separately to take care of the differences in spread, but this does nothing to address skewness.

The plot _quarterfinals.png_ shows these standardized scores.

I then did a Google search of some of the outliers. in particular Jee Won Kim's score from JW and Serena Huang's score from EO.  The only relationship I found between Huang and EO was that they had been associated with the same music school as students.  Huang is still in school and Oliveira has fully established his reputation as a world class violinist so the possibility that this relationship may influence the score seems tenuous.

I could find no relationship between Kim and Jian Wang.  Kim received her training in Korea, Moscow, and Cologne.  Wang is a cellist who spent all of his formative years in Shanghai.  He studied at the Yale School of Music and his career is based mainly in Shanghai and London.

While researching Kim, the following Google hit caught my eye:
http://slippedisc.com/2016/04/didgy-joachim-winner-is-on-the-shanghai-longlist/
This article referred to a previous competition where the fact that the semifinalist Dogadin (the 19th competitor in my dataset) had been a student of judge BK was not mentioned by either of them.  I then noted that Dogadin's highest score in the quarterfinals of the Shanghai competition was awarded by BK and this score was significantly higher than any of the other scores awarded by BK.  However, it does not stand out among any of the standardized scores received by Dogadin &mdash; in this case it's just an interesting sidelight and hints that readers of the violinist.com blogs have a right to be skeptical of scores handed out by judges to their former students.  If the judges are scoring independently then it was only by chance that BK's score given to Dogadin had a lesser impact than it could have.  Later, I may also examine further the low score judge DC gave Dogadin compared to the other judges.

__code__ | __Judge__
---- | ----------------
DS | David Stern
VW | Vera Tsu Weiling
ZB | Zakhar Bron
DC | David Cerone
DH | Daniel Heifetz
EH | Emmanuel Hondre
BK | Boris Kuschnir
EO | Elmar Oliveira
JW | Jian Wang
ZW | Zhenshan Wang
LY | Lina Yu
