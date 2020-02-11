# Introductie
'Wie is de Mol?' is een programma op Nederland 1 dat elk jaar wordt uitgezonden. In dit programma moet kandidaten opdrachten doen waarmee je geld voor de pot kunt verdienen. Echter heb je ook een saboteur, die ook wel de 'Mol' wordt genoemd. De 'Mol' probeert te verhinderen dat er geld verdient wordt. De kandidaten moeten deze 'Mol' proberen te ontmaskeren. Bijna elke aflevering is er een test met vragen over de 'Mol' en de kandidaat die dan het minst weet over de 'Mol' valt af. Uiteindelijk blijven er op het einde 3 kandidaten over en degene die het meest weet over de 'Mol' is de winnaar van het spel en krijgt het bedrag dat in de pot zit. 

Deze serie wordt al sinds 1999 uitgezonden en er zijn daarom inmiddels al 19 seizoenen gepasseerd. Ook de kijkers thuis proberen te achter halen tijdens de serie wie de 'Mol' is. Echter heeft het meerendeel van de kijkers het vaak fout wie de 'Mol' is. Daarom ben ik dit project gestart en doe ik diepe analyses, simulaties en berekeningen om op een objectieve manier te kunnen bepalen wie de mol is.

# Moldel
Het Moldel is een programma dat voor elke kandidaat bepaald hoe waarschijnlijk deze speler de 'Mol' is. Deze score komt tot stand door de volgende layers:
* Exam Layer: Deze bepaalt wie de mol is op basis hoe spelers de vragen invullen, hoeveel jokers/vrijstellingen spelers inzetten en wie er af valt of mogelijk had af moeten vallen.
* Wiki Word Layer: Deze bepaalt wie de mol is op basis van de kandidaten wikipedia pagina's voordat het seizoen begon. De woorden die in hun pagina's staan worden gekoppeld aan bepaalde beroepen en zo wordt er gekeken in welke mate een kandidaat bij een bepaald beroep past. Vervolgens wordt gekeken hoeveel een kandidaat op kandidaten uit andere seizoenen lijkt op basis van deze beroepen. En als de kandidaten waarop deze kandidaat lijkt de mol waren, dan wordt deze kandidaat ook geclassificeerd als mol.
* Early Activity Layer: Deze layer is gebasseerd op de social media analyse door Jaap van Zessen (http://www.jaapvanzessen.nl/tag/wie-is-de-mol/). Kandidaten die gedurende de periode van opnames actief waren (dus eerder afgevallen zijn) krijgen een lagere likelihood om de mol te zijn.

# Oude Resultaten
Oude resultaten van het Moldel kun je vinden in de map 'results'.

# Credits
Ik bedank iedereen die mij meegeholpen heeft bij dit project, daaronder valt:
* Jaap van Zessen (voor het gebruik van zijn sociale media analyse voor de Early Activity Layer)
* Jesse van Elteren (voor zijn ideëen om de analyses beter te maken) 

# Contact
Als je meer wilt weten over dit project kun je mij contacteren op:
* Multifacio: mfprojects@live.nl
