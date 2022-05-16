import pyttsx3
engine = pyttsx3.init() # object creation


""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say("1. Wyjaśnij istotę fascynacji romantyków ludowością Miłość, która jest prawdziwa,"
". Na podstawie Cierpień młodego Wertera opisz postawę bohatera werterycznego."
"Bohatera wertyrycznego cechowały: wybujała wyobraźnia, uczuciowość, brak zdecydowanego"
"działania, dążenie do samozagłady, widzenie świata przez pryzmat marzeń i poezji, niezgoda"
"na konwencje obyczajowe i normy moralne, której towarzyszy pesymistyczne poczucie"
"bezcelowości życia."
"3. Określ, w jaki sposób Oda do młodości spełnia wymogi gatunkowe ody. Podaj co najmniej"
"cztery argumenty."
"- wysoki styl"
"- nawiązanie do mitologii"
"- forma, zwrot do adresata"
"- wywodzi się z antyku greckiego"
"4. Jakie wartości przypisywane są młodości w odzie Mickiewicza?"
"Jest uważana za najlepszą i najbardziej rozsądną, jest porównywana do nowego pokolenia"
"romantyków, ambicja i nastawianie ludzi do walczenia o niepodległość polski, mądrość ludzie"
"mieli być bardzie mądrzejsi"
"5. Wyjaśnij, jaki spór został zasygnalizowany w pierwszych wersach Ody do młodości: Bez"
"serc, bez ducha, to szkieletów. ludy;/Młodości! dodaj mi skrzydła!/Niech nad martwym wzlecę"
"światem/W rajską dziedzinę ułudy.."
"Tutaj chodzi o to że młodość może dodać mocy i siły by wytrwać w świecie dorosłych i starych"
"osób którym już nic się nie chcę"
"6. Wyjaśnij, w jaki sposób motto Romantyczności: Zdaje mi się, że widzę... Gdzie? / Przed"
"oczyma duszy mojej . zaczerpnięte z utworu Williama Szekspira, łączy się z treścią utworu."
"Jest to pokazane za pomocą sporu narratora i uczonego interpretacje zachowania dziewczyny,"
"która w biały dzień widzi zmarłego Kochanka Jasieńko."
"7. Wyjaśnij, dlaczego Romantyczność została uznana za manifest programowy nowego"
"pokolenia twórców."
"Romantyzm jest uważany za lepszy i mądrzejszy, a klasycyzm jako coś przestarzałego i"
"bezsensownego."
"8. Przedstaw emocje i uczucia Pielgrzyma ze Stepów akermańskich i Burzy (najpierw sytuacja, a"
"potem uczucia Pielgrzyma wobec niej)."
"podmiot liryczny opisuje jak bardzo podoba mu się otaczający go krajobraz. Znajduje się w krainie"
"pięknej i bogatej - u stóp moich kraina dostatków i krasy, która jest zamieszkała przez pięknych"
"ludzi - obok piękne lice. Zachwyca się pięknem otaczającego go krajobrazu, ale równocześnie"
"tęskni za swoją ojczyzną oraz przeszłością."
"9. Przedstaw krótko typ bohatera wykreowanego przez Mickiewicza w Konradzie Wallenrodzie."
"Bardzo sprytny , woli niszczyć wroga od środka"
"Porwany i wychowany na obczyźnie"
"Jest w stanie poświęcić wszystko by osiągnąć cel"
"10. Opisz krótko kim jest Halban dla Konrada Wallenroda. Podaj przynajmniej trzy funkcje,"
"które wajdelota pełnił w życiu młodego mężczyzny."
"Przyjaciel, nauczyciel, opiekun, mentor, strażnik tradycji"
"11. Nazwij gatunek reprezentowany przez utwór Konrad Wallenrod Adama Mickiewicza."
"GATUNEK - POWIEŚĆ POETYCKA Cechami powieści poetyckiej są przede wszystkim:"
"- zerwanie z łańcuchem przyczynowo skutkowym"
"- achronologiczność"
"- synkretyzm rodzajowy"
"- synkretyzm gatunkowy"
"- umieszczanie akcji w przeszłości historycznej"
"12. Dziady część III to dramat romantyczny. Udowodnij to, wymieniając sześć cech tego"
"gatunku literackiego i poprzyj je informacjami z tekstu."
"- otwarta kompozycja"
"- brak łańcucha przyczynowo skutkowego"
"- brak chronologii"
"- realistyczne: fantastyczne wydarzenia"
"- całość łączy główny bohater, który jest tajemniczą postacią"
"13. Wymień i opisz cztery zagadnienia podejmowane przez Konrada w Wielkiej Improwizacji."
"- Jak ciężko być poetą"
"-Zaczyna dyskutować z Bogiem"
"14. Wyjaśnij metaforyczne znaczenie słów wypowiedzianych przez Wysockiego ,,Nasz naród jak"
"lawa,/Z wierzchu zimna i twarda, sucha i plugawa, / Lecz wewnętrznego ognia sto lat nie"
"wyziębi"
"Opisuje lojalistów i zdrajców. Przykładem jest towarzystwo stolikowe i poeci którzy z nim"
"rozmawiali."
"Opisuje młodych patriotów którzy chcą walczyć za ojczyznę np. Towarzystwo przy drzwiach"
"15. Omów wizję poety-wieszcza, ukazaną w III części Dziadów."
"Przeczuwa istnienie świata metafizycznego i pragnie go poznać. Poeta przeżywa stany uniesień,"
"wówczas improwizuje, o czym wspomina się w scenie więziennej"
"v16. Nazwij i opisz koncepcję narodowo-wyzwoleńczą zawartą w słowach Nazywam się Milionbo za miliony / Kocham cierpię katusze"
"vvjest to prometeizm"
"Czyli poświęcenie się jednostki dla dobra ogółu."
"Konrad chce sam walczyć o szczęście narodu, tak jak Prometeusz, który wykradł bogom ogień i"
"ofiarował go ludziom."
"v17. Wyjaśnij, czego dowiaduje się Kordian o ludziach i świecie podczas swej podróży po Europie"
"i odwiedzania wymienionych miejsc."
"a. Anglia, James Park."
"Podczas rozmowy z doradcą w James Park Kordian dowiedział się, że pieniądz rządzi światem"
"b. Włochy, włoska willa."
"W willi spotyka Wiolettę, która zakochuje się w nim tylko dla pieniędzy, Kordian zauważa że za"
"pieniądz można kupić wszystko nawet miłość"
"c. Watykan."
"Rozmawiając z papieżem, dowiaduje się że papież nie jest taki sam jak się wydaje, myśli tylko o"
"sobie, a nie o innych i dla niego Polska nic nie znaczy"
"18. Opisz cztery zagadnienia rozważane przez Kordiana w jego monologu na szczycie Mont"
"Blanc."
"Kordian na szczycie góry Mont Blanc czuje się wolny i opisuje spokój i ogrom tego co go otacza."
"Bohater zaczyna swoje rozmyślania o tym czy nie lepiej byłoby po prostu zeskoczyć z góry/"
"Rezygnuje z tej myśli, ponieważ chęć uratowania narodu i stania na jego czele była większa"
"Kordian na szczycie porównuje się też do Boga – uważa, e posiada moc potrzebną do ocalenia"
"Polski, jest gotowy poświęcić się żeby uratować kraj"
"19. Wyjaśnij, na czym polega idea winkelrydyzmu"
"Winklerydyzm to podstawa, która mówi, ze czasem lepiej poświęcić się żeby większość wygrała"
"i przeżyła"
"20. Podaj trzy argumenty, którymi Prezes próbował odwieść Podchorążego od dokonania"
"zamachu na cara"
"- Morderstwo to grzech"
"- Dzięki poetom da się rozwiązać spór bez rozlewu krwi"
"- zabicie Króla jest hańbą"
"- Obawy reakcji innego kraju"
"21. Wyjaśnij, dlaczego Kordianowi nie udaje się ostatecznie dokonać zamachu na cara."
"Ponieważ zemdlał przez stres i wycieńczenia. W głowie Kordiana toczyła się wewnętrzna walka"
"imaginacji ze Stachem"
"22. Przedstaw krótko, jakie przyczyny upadku powstania listopadowego wskazał Słowacki w"
"swoim utworze"
"- zdrajcy"
"- ciągła zmiana dowódców"
"- brak wiary w zwycięstwo"
"- źli dowódcy"
"23. Nazwij zakończenie zastosowane przez Słowackiego w swoim utworze i wyjaśnij, dlaczego"
"poeta zdecydował się właśnie na taki jego typ"
"Zakończenie otwarte którego celem jest możliwość kontynuacji dzieła, danie możliwość"
"czytelnikowi na własną interpretacje zakończenia"
"24. Wskaż cztery elementy łączące Kordiana i Konrada z III części Dziadów."
"- Porównują się do Boga"
"- Obaj są narcystyczni"
"- mają podobne imiona"
"- zdeterminowani by osiągnąć swój cel"
"- poświęcili wszystko na swój cel"
"- nieszczęśliwa miłość"
"25. Wymień trzy zalecenia zapisane w poetyckim testamencie Juliusza Słowackiego Testament"
"mój"
"oświecali, kształtowali naród, przewodzili mu w drodze do wolności i dążeniu do osiągnięcia"
"potęgi propagować jego utwory"
"26. Nazwij, wskaz i wyjaśnij topos obecny w utworze Juliusza Słowackiego Testament mój,"
"mający swoje źródło w poezji Horacego"
"Poeta nie umrze zostaną po nim jego utwory"
"Kostium poetycki"
"Utwór kreacjonisyczny")

engine.runAndWait()
engine.stop()

"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
engine.save_to_file('D:\Repository\PythonVoice', 'test.mp3')
engine.runAndWait()