# Introductie
'Wie is de Mol?' is een programma op Nederland 1 dat elk jaar wordt uitgezonden sind 1999. In dit programma moeten kandidaten opdrachten doen waarmee je geld voor de pot kunt verdienen. Echter heb je ook een saboteur, die ook wel de 'Mol' wordt genoemd. De 'Mol' probeert te verhinderen dat er geld verdient wordt. De kandidaten moeten deze 'Mol' proberen te ontmaskeren. Bijna elke aflevering is er een test met vragen over de 'Mol' en de kandidaat die dan het minst weet over de 'Mol' valt af. Uiteindelijk blijven er op het einde 3 kandidaten over en degene die het meest weet over de 'Mol' is de winnaar van het spel en krijgt het bedrag dat in de pot zit. 

Ook de kijkers thuis proberen te achterhalen tijdens de serie wie de 'Mol' is. Echter heeft het meerendeel van de kijkers het vaak fout wie de 'Mol' is. Meestal komt dit door tunnelvisie, wat inhoudt dat iemand er vanuit gaat dat een kandidaat de 'Mol' is en alleen maar bewijs zoekt wat dat bevestigt. Je kunt deze tunnelvisie het best voorkomen door op een objectieve manier te meten wie de 'Mol'. En daarom ben ik dit project gestart en probeer ik met onder anderen statistiek en machine learning op een objectieve manier te bepalen wie de 'Mol' is.

# Moldel
Het Moldel is een programma dat voor elke kandidaat bepaald hoe waarschijnlijk deze speler de 'Mol' is. Deze score komt tot stand door de voorspellingen van de volgende layers te combineren:
* Exam Drop Layer: Deze bepaalt wie de 'Mol' is op basis van hoe afvallers hun vragen hebben ingevuld (kandidaten waarop afvallers zitten zijn vaak niet de 'Mol').
* Exam Pass Layer: Deze bepaalt wie de 'Mol' is op basis van hoeveel jokers de kandidaten tijdens de test hebben ingezet (kandidaten die meer jokers hebben ingezet zijn vaak niet de 'Mol'). De Exam Pass Layer is ontstaan door een opmerking van Dr. Jasper de Jong, die mij geïnspireerd heeft tot deze layer.
* Wikipedia Layer: Deze bepaalt wie de 'Mol' is op basis van de kandidaten wikipedia pagina's voordat het seizoen begon. Via de wikipedia pagina's proberen ze kandidaten te linken aan bepaalde beroepen en op basis hiervan en hoeveel woorden in hun wikipedia pagina staan probeert deze layer te voorspellen wie de 'Mol' is.
* Social Media Layer: Deze layer geeft kandidaten een lagere/hogere kans op basis van de social media analyse door Jaap van Zessen (http://www.jaapvanzessen.nl/tag/wie-is-de-mol/). Hierbij wordt onder andere gekeken naar foto's die gelekt zijn, hoe actief kandidaten op social media (Facebook, Twitter, Youtube, etc.) waren tijdens de opname periode en andere informatie die aantoont dat een kandidaat wel/niet aanwezig was tijdens een later stadium van de opname periode.
* Appearance Layer: Het idee van deze layer komt van Mattijn van Hoek (https://github.com/mattijn/widm). Deze layer probeert te voorspellen wie de 'Mol' is op basis van hoe vaak de 'Mol' in beeld komt tijdens de eerste 4 afleveringen (de 'Mol' komt vaak minder in beeld). 

# Oude Resultaten
Het Moldel is getest op de seizoenen 13 tot en met 21 (Renaissance) en is getest op de seizoen 9 tot en met 12. Echter voor de seizoenen 9 tot en met 12 zijn alleen de Exam Drop Layer, Exam Pass Layer, Wikipedia Layer gebruikt, omdat er geen social media analyses zijn gedaan in deze periode en omdat de 'Mol' in deze periode nog niet minder in beeld kwam. Het Moldel laat goede resultaten zien voor de seizoenen 9 t/m 21 (Renaissance), e.g. in 13 van de 13 finales krijgt de echte 'Mol' de hoogste likelihood, zie de afbeelding hieronder: 
<details>
  <summary>Spoiler Alert! Klik links op het pijltje voor de voorspellingen voor finales (seizoen 9 t/m 21)</summary>
  
  ![Finale Voorspellingen](https://github.com/Multifacio/Moldel/blob/master/results/Final%20Results%20(9-21)%20(2021-01-01).png)
</details>

Meer voorspellingen voor deze seizoenen kun je vinden in de map 'results' (https://github.com/Multifacio/Moldel/tree/master/results). De voorspellingen van de laatste versie van het Moldel vind je in de map 'results/Latest Version (2021-01-01)' (https://github.com/Multifacio/Moldel/tree/master/results/Latest%20Version%20(2021-01-01)). In alle voorspellingen zijn spelers met een likelihood lager dan 1.5% verwijdert om de leesbaarheid te bevorderen, dus als een speler niet in de plot te zien is betekent dat niet dat speler niet meer meedeed.

# Voorspelling
Ook voor de nieuwste aflevering van seizoen 21 is een voorspelling gedaan. (Laatst geüpdate op 28 Februari 2021)
<details>
  <summary>Spoiler Alert! Klink links op het pijltje voor de laatste voorspelling voor seizoen 21, aflevering 10</summary>
  
  ![Voorspelling](https://github.com/Multifacio/Moldel/blob/master/results/Season%2022%20(Original)/09%20-%20After%20Episode%209.png)
</details>

# Credits
Ik bedank iedereen die mij meegeholpen heeft bij dit project, daaronder vallen:
* Jesse van Elteren: Ik ben initieel aan dit project begonnen onder zijn repository (https://github.com/jvanelteren/wie_is_de_mol). Op 15 September 2019 heb ik echter besloten los te splitsen van zijn project, omdat mijn project meer over het voorspellen van de 'Mol' ging en zijn project meer over de algemene statistiek achter 'Wie is de Mol?' ging. Ik wil Jesse van Elteren wel bedanken voor enkele adviezen en tips die hij gegeven heeft om het Moldel mee te verbeteren.
* Adam Geitgey: Ik bedank Adam Geitgey voor het gebruik van zijn project om gezichten in afbeeldingen mee te herkennen (https://github.com/ageitgey/face_recognition) dat wordt gebruikt voor de Appearance Layer.  
* Mattijn van Hoek: Ik wil Mattijn van Hoek bedanken voor zijn toestemming voor het gebruik en verbeteren van zijn idee en code (https://github.com/mattijn/widm) voor de Appearance Layer. Alle credits van dit idee gaan naar Mattijn van Hoek, net als de video parse code die ik heb gebruikt van Mattijn van Hoek. Echter heb ik zelf wel het machine learning model voor deze layer gemaakt (dat het relatief in beeld komen transleert naar een likelihood), ben ik ook verantwoordelijk voor diepere analyse van deze resultaten voor meerdere seizoenen en heb ik er zelf voor gezorgd dat deze voorspellingen gecombineerd konden worden met de andere voorspellingen. 
* Jaap van Zessen: Ik wil Jaap van Zessen bedanken voor de toestemming om zijn voorspellingen (http://www.jaapvanzessen.nl/tag/wie-is-de-mol/) te verwerken in mijn Moldel onder de Social Media Layer.
* Dr. Jasper de Jong: Ik wil Jasper de Jong bedanken voor zijn inspiratie voor de Exam Pass Layer.

# Contact
Als je meer wilt weten over dit project kun je mij contacteren:
* Haico Dorenbos: Multifacio@gmail.com (pseudoniem: Multifacio)
