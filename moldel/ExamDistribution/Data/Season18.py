from ExamDistribution.Structure import Question, TestInput, Result, Episode

# Aflevering 1 (afvaller: Ron)
# Vragen:
# 3 - In welk land zat de Mol tijdens de opdracht?
# 1: Bella, Simone 2: Stine, Emilio 3: Ruben, Olcay 4: Loes, Ron 5: Jan, Jean
# 9 - Heeft het duo waarin de Mol zat voor meer dan 1000, gebeld met Art? (Onbruikbaar)
# 17 - Heeft de Mol binnen de tijd de kluis geopend?
# 1: Jan, Jean, Loes, Ron; 2: Bella, Simone, Stine, Emilio, Ruben, Olcay
# 20 - Wie is de Mol?
# 1: Bella; 2: Emilio; 3: Jan; 4: Jean; 5: Loes; 6: Olcay; 7: Ron; 8: Ruben; 9: Simone; 10: Stine
# Vrijstellingen: Ruben, Olcay, Simone, Stine, Emilio, Bella
# Antwoorden: Jean (3, 1), Jan (17, 1), Loes (20, 10)
players1 = ['Bella', 'Emilio', 'Jan', 'Jean', 'Loes', 'Olcay', 'Ron', 'Ruben', 'Simone', 'Stine']
question1_3 = Question({1: ['Bella', 'Simone'],
                        2: ['Stine', 'Emilio'],
                        3: ['Ruben', 'Olcay'],
                        4: ['Loes', 'Ron'],
                        5: ['Jan', 'Jean']})
question1_17 = Question({1: ['Jan', 'Jean', 'Loes', 'Ron'],
                         2: ['Bella', 'Simone', 'Stine', 'Emilio', 'Ruben', 'Olcay']})
question1_20 = Question({1: ['Bella'], 2: ['Emilio'], 3: ['Jan'], 4: ['Jean'], 5: ['Loes'], 6: ['Olcay'], 7: ['Ron'],
                         8: ['Ruben'], 9: ['Simone'], 10: ['Stine']})
result1 = Result(True, ['Ron'])
episode1 = Episode(players1, result1,
                   {'Bella': TestInput(jokers = 20), 'Emilio': TestInput(jokers = 20), 'Jan': TestInput({17: 1}),
                    'Jean': TestInput({3: 1}), 'Loes': TestInput({20: 10}), 'Olcay': TestInput(jokers = 20),
                    'Ruben': TestInput(jokers = 20), 'Simone': TestInput(jokers = 20), 'Stine': TestInput(jokers = 20)},
                   {3: question1_3, 17: question1_17, 20: question1_20})

# Aflevering 2 (afvaller: Jean)
# Vrijwillig afgevallen dus vragen worden niet meegerekend
players2 = ['Bella', 'Emilio', 'Jan', 'Jean', 'Loes', 'Olcay', 'Ruben', 'Simone', 'Stine']
result2 = Result(True, ['Jean'])
episode2 = Episode(players2, result2, dict(), dict())

# Aflevering 3 (afvaller: Bella)
# Vragen:
# 3 - Heeft de Mol min-geld gepakt tijdens de Kwestie van vertrouwen-opdracht?
# 1: Bella, Ruben, Stine, Simone, Emilio; 2: Jan, Olcay, Loes
# 4 - Met wie vormde de Mol een duo tijdens de opdracht met de auto's?
# 1: Olcay; 2: Bella; 3: Stine; 4: Jan; 5: Loes; 6: Emilio; 7: Ruben, Simone
# 14 - Waar bevond de Mol zich tijdens de opdracht met de paragliders?
# 1: Ruben, Emilio, Olcay, Stine; 2: Bella, Jan, Loes, Simone;
# 15 - Met welk hoofdstuk startte de Molcast van de Mol?
# 1: Bella; 2: Jan; 3: Loes; 4: Simone 5: Ruben, Emilio, Olcay, Stine (Niet accuraat)
# 20 - Wie is de Mol?
# 1: Bella; 2: Emilio; 3: Jan; 4: Loes; 5: Olcay; 6: Ruben; 7: Simone; 8: Stine
# Antwoorden: Ruben (3, 1), Simone (15, 5) (1 joker), Emilio (4, 5) (1 joker), Loes (14, 1), Olcay (20, 6),
# Stine (1 joker)
players3 = ['Bella', 'Emilio', 'Jan', 'Loes', 'Olcay', 'Ruben', 'Simone', 'Stine']
question3_3 = Question({1: ['Bella', 'Ruben', 'Stine', 'Simone', 'Emilio'],
                        2: ['Jan', 'Olcay', 'Loes']})
question3_4 = Question({1: ['Olcay'], 2: ['Bella'], 3: ['Stine'], 4: ['Jan'], 5: ['Loes'], 6: ['Emilio'],
                        7: ['Ruben', 'Simone']})
question3_14 = Question({1: ['Ruben', 'Emilio', 'Olcay', 'Stine'],
                         2: ['Bella', 'Jan', 'Loes', 'Simone']})
question3_15 = Question({1: ['Bella'], 2: ['Jan'], 3: ['Loes'], 4: ['Simone'],
                         5: ['Ruben', 'Emilio', 'Olcay', 'Stine']})
question3_20 = Question({1: ['Bella'], 2: ['Emilio'], 3: ['Jan'], 4: ['Loes'], 5: ['Olcay'], 6: ['Ruben'],
                         7: ['Simone'], 8: ['Stine']})
result3 = Result(True, ['Bella'])
episode3 = Episode(players3, result3,
                   {'Ruben': TestInput({3: 1}), 'Simone': TestInput({15: 5}, 1), 'Emilio': TestInput({4: 5}, 1),
                    'Loes': TestInput({14: 1}), 'Olcay': TestInput({20: 6}), 'Stine': TestInput(jokers=1)},
                   {3: question3_3, 4: question3_4, 14: question3_14, 15: question3_15, 20: question3_20})

# Aflevering 4 (afvaller: Emilio)
# Vragen:
# 1 - De Mol is:
# 1: Emilio, Jan, Ruben; 2: Loes, Olcay, Simone, Stine;
# 16 - Heeft de Mol een enveloppe aan de overkant gebracht met de zipline?
# 1: Emilio, Jan, Loes, Olcay, Simone; 2: Ruben, Stine;
# 18 - Welke enveloppe koos de Mol bij de opdracht met de zipline, vanaf links geteld? (Niet accuraat)
# 1: Emilio; 2: Loes; 3: Olcay; 4: Simone; 5: Ruben, Stine; 6: Jan;
# 20 - Wie is de Mol?
# 1: Emilio; 2: Jan; 3: Loes; 4: Olcay; 5: Ruben; 6: Simone; 7: Stine
# Antwoorden: Olcay (1, 1), Ruben (20, 6), Simone (18, 6), Jan (Vrijstelling), Stine (20, 1), Emilio (16, 1),
# Loes (20, 1)
players4 = ['Emilio', 'Jan', 'Loes', 'Olcay', 'Ruben', 'Simone', 'Stine']
question4_1 = Question({1: ['Emilio', 'Jan', 'Ruben'],
                        2: ['Loes', 'Olcay', 'Simone', 'Stine']})
question4_16 = Question({1: ['Emilio', 'Jan', 'Loes', 'Olcay', 'Simone'],
                        2: ['Ruben', 'Stine']})
question4_18 = Question({1: ['Emilio'], 2: ['Loes'], 3: ['Olcay'], 4: ['Simone'],
                         5: ['Ruben', 'Stine'],
                         6: ['Jan']})
question4_20 = Question({1: ['Emilio'], 2: ['Jan'], 3: ['Loes'], 4: ['Olcay'], 5: ['Ruben'], 6: ['Simone'],
                         7: ['Stine']})
result4 = Result(True, ['Emilio'])
episode4 = Episode(players4, result4,
                   {'Olcay': TestInput({1: 1}), 'Ruben': TestInput({20: 6}), 'Simone': TestInput({18: 6}),
                    'Jan': TestInput(jokers = 20), 'Stine': TestInput({20: 1}), 'Emilio': TestInput({16: 1}),
                    'Loes': TestInput({20: 1})},
                   {1: question4_1, 16: question4_16, 18: question4_18, 20: question4_20})

# Aflevering 5 (afvaller: Loes)
# Vragen:
# 1 - De Mol is:
# 1: Jan, Ruben; 2: Loes, Olcay, Simone, Stine;
# 6 - Is de Mol de nieuwe penningmeester?
# 1: Ruben; 2: Jan, Loes, Olcay, Simone, Stine
# 12 - Als hoeveelste werd de Mol uitgeschakeld tijdens 'Chaos'? (Niet accuraat)
# 1: Jan; 2: Olcay; 3: Simone; 4: Stine; 5: Loes, Ruben
# 19 - Streepte de Mol het woord 'Mol' weg tijdens 'Woordzoekers'?
# 1: Stine; 2: Jan, Loes, Olcay, Ruben, Simone
# 20 - Wie is de Mol?
# 1: Jan; 2: Loes; 3: Olcay; 4: Ruben; 5: Simone; 6: Stine
# Antwoorden: Simone (6, 1), Jan (19, 2), Ruben (20, 2), Olcay (1, 1), Stine (12, 5)
players5 = ['Jan', 'Loes', 'Olcay', 'Ruben', 'Simone', 'Stine']
question5_1 = Question({1: ['Jan', 'Ruben'],
                        2: ['Loes', 'Olcay', 'Simone', 'Stine']})
question5_6 = Question({1: ['Ruben'],
                        2: ['Jan', 'Loes', 'Olcay', 'Simone', 'Stine']})
question5_12 = Question({1: ['Jan'],
                         2: ['Olcay'],
                         3: ['Simone'],
                         4: ['Stine'],
                         5: ['Loes', 'Ruben']})
question5_19 = Question({1: ['Stine'],
                         2: ['Jan', 'Loes', 'Olcay', 'Ruben', 'Simone']})
question5_20 = Question({1: ['Jan'], 2: ['Loes'], 3: ['Olcay'], 4: ['Ruben'], 5: ['Simone'], 6: ['Stine']})
result5 = Result(True, ['Loes'])
episode5 = Episode(players5, result5,
                   {'Simone': TestInput({6: 1}), 'Jan': TestInput({19: 2}), 'Ruben': TestInput({20: 2}),
                    'Olcay': TestInput({1: 1}), 'Stine': TestInput({12: 5})},
                   {1: question5_1, 6: question5_6, 12: question5_12, 19: question5_19, 20: question5_20})

# Aflevering 6 (geen afvaller, alleen Simone kreeg haar scherm te zien)
# Vragen:
# 4 - In welke kamer bevond de Mol zich bij aanvang van de opdracht 'Sleutelpositie'? (Niet accuraat)
# 1: Jan; 2: Olcay; 3: Simone; 4: Stine; 5: Ruben;
# 13 - Welke kleur auto had de Mol bij de opdracht 'Ladas met Lading'?
# 1: Jan ; 2: Simone, Stine; 3: Ruben, Olcay;
# 20 - Wie is de Mol?
# 1: Jan; 2: Olcay; 3: Ruben; 4: Simone; 5: Stine
# Antwoorden: Jan (4, 5), Ruben (13, 2), Simone (20, 3)
players6 = ['Jan', 'Olcay', 'Ruben', 'Simone', 'Stine']
question6_4 = Question({1: ['Jan'], 2: ['Olcay'], 3: ['Simone'], 4: ['Stine'], 5: ['Ruben']})
question6_13 = Question({1: ['Jan'], 2: ['Simone', 'Stine'], 3: ['Ruben', 'Olcay']})
question6_20 = Question({1: ['Jan'], 2: ['Olcay'], 3: ['Ruben'], 4: ['Simone'], 5: ['Stine']})
result6 = Result(False, ['Jan', 'Olcay', 'Ruben', 'Stine'])
episode6 = Episode(players6, result6,
                   {'Jan': TestInput({4: 5}), 'Ruben': TestInput({13: 2}), 'Simone': TestInput({20: 3})},
                   {4: question6_4, 13: question6_13, 20: question6_20})

# Aflevering 7 (afvaller: Stine)
# Vragen:
# 1 - De Mol is een:
# 1: Jan, Ruben; 2: Olcay, Simone, Stine
# 13 - Was de Mol de eerste die begon te schilderen bij de opdracht 'Praten als Brugman'?
# 1: Ruben, Simone, Stine; 2: Jan, Olcay;
# 18 - Welke kleur dozen moest de Mol verzamelen bij 'Perongeluk'?
# 1: Jan; 2: Simone; 3: Olcay; 4: Ruben, Stine
# Antwoorden: Ruben (1, 2), Jan (13, 1), Olcay (18, 2)
players7 = ['Jan', 'Olcay', 'Ruben', 'Simone', 'Stine']
question7_1 = Question({1: ['Jan', 'Ruben'], 2: ['Olcay', 'Simone', 'Stine']})
question7_13 = Question({1: ['Ruben', 'Simone', 'Stine'], 2: ['Jan', 'Olcay']})
question7_18 = Question({1: ['Jan'], 2: ['Olcay'], 3: ['Ruben'], 4: ['Simone'], 5: ['Stine']})
result7 = Result(True, ['Stine'])
episode7 = Episode(players7, result7,
                   {'Ruben': TestInput({1: 2}), 'Jan': TestInput({13: 1}), 'Olcay': TestInput({18: 2})},
                   {1: question7_1, 13: question7_13, 18: question7_18})

# Aflevering 8 (afvaller: Simone)
# Vragen:
# 7 - Hoeveel liedjes heeft de Mol geraden bij 'Car-aoke'? (Ruben: 2, Olcay: 3, Jan: 4)
# 1: Simone; 2: Ruben; 3: Olcay; 4: Jan
# 20 - Wie is de Mol:
# 1: Jan; 2: Olcay; 3: Ruben; 4: Simone
# Antwoorden: Jan (7, 2), Ruben (20, 1), Jan (20, 3), Olcay (20, 3), Simone (20, 3)
players8 = ['Jan', 'Olcay', 'Ruben', 'Simone']
question8_7 = Question({1: ['Simone'], 2: ['Ruben'], 3: ['Olcay'], 4: ['Jan']})
question8_20 = Question({1: ['Jan'], 2: ['Olcay'], 3: ['Ruben'], 4: ['Simone']})
result8 = Result(True, ['Simone'])
episode8 = Episode(players8, result8,
                   {'Jan': TestInput({7: 2, 20: 3}), 'Ruben': TestInput({20: 1}), 'Olcay': TestInput({20: 3}),
                    'Simone': TestInput({20: 3})},
                   {7: question8_7, 20: question8_20})
season18 = (players1, {1: episode1, 2: episode2, 3: episode3, 4: episode4, 5: episode5, 6: episode6, 7: episode7,
                       8: episode8})