# Ohlajanje vodnikov nadzemnih vodov pri horizontalnih hitrostih pod 0,6 m/s 

Ljubljana, april 2018

| Izvajalec: | Inštitut Jožef Stefan (IJS), Elektroinštitut Milan Vidmar (EIMV) |
| :--- | :--- |
| Naročnik: | ELES d.o.o., Ljubljana, Hajdrihova 2 |
| Številka pogodbe: | POG2017/0356 |
| Naslov študije: | Ohlajanje vodnikov nadzemnih vodov pri horizontalnih hitrostih pod $0,6 \mathrm{~m} / \mathrm{s}$ |
| Predstavnik izvajalca: Izdelovalci študije: | dr. Gregor Kosec, univ. dipl. fiz. (IJS) dr. Gregor Kosec, univ. dipl. fiz. (IJS)![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-03.jpg?height=112&width=430&top_left_y=693&top_left_x=1348) <br> Jure Slak, mag. mat (IJS) <br> dr. Matjaž Depolli, univ. dipl. rač. (IJS) <br> mag. Andrej Souvent, univ. dipl. ing. el. (EIMV) <br> dr. Miloš Maksič, univ. dipl. ing. el. (EIMV) <br> mag. Vladimir Djurica, univ. dipl. ing. el. (EIMV) |
| Predstavnik naročnika: Spremljevalci: | Špela Vidrih, mag. ing. el. <br> dr. Janko Kosmač, univ. dipl. ing. el. <br> Dušan Kozjek, univ. dipl. ing. el. <br> Borut Vertačnik, univ. dipl. ing. el. <br> Roman Tomažič, univ. dipl. ing. el. <br> Bojan Volk, univ. dipl. ing. el. |
| Datum izdelave: | Oktober, 2018 |

## Utemeljitev naloge

Prenos toplote iz daljnovodne vrvi v okolico je posledica več sočasnih mehanizmov - radiacije, konvekcije in obtekanja kapljevine, npr. v primeru dežja. Primarni mehanizem na katerega lahko vedno zanesljivo računamo je konvekcija. Za razumevanje konvekcije je potrebno v prvi vrsti dobro razumeti mehaniko tekočine.

Standard SIST EN 50182:2001 pri oceni statične vrednosti termičnega toka za daljnovodne vrvi uporablja kot referenčno vrednost hitrost vetra $0,6 \mathrm{~m} / \mathrm{s} \mathrm{z}$ vpadnim kotom $90^{\circ}$ glede na vzdolžno os vrvi. V praksi se izkaže, da so dejanske izmerjene hitrosti vetra tudi nižje. Veter, ki dejansko hladi vodnik, ima vzdolžno, prečno in vertikalno komponento. Z ultrazvočnimi merilniki hitrosti vetra, ki jih imamo nameščene na več lokacijah merimo, veter v vzdolžni in prečni smeri, ne pa tudi v vertikalni smeri. Zato veter izražamo s skalarjem in kotom dvorazsežnega (2D) vektorja, ki predstavlja pravokotno projekcijo trirazsežnega (3D) vektorja vetra na horizontalno ravnino. Pri hitrostih vetra nad 1 do $2 \mathrm{~m} / \mathrm{s}$ predvidevamo, da sta prevladujoči 2D komponenti, saj se zrak premika vzporedno s podlago. Pri nižjih hitrostih pride v okolici toplega vodnika do pojava naravne konvekcije.

Naravna konvekcija je pojav, kjer gibanje zraka povzroči razlika v gostoti hladnega in toplega zraka. Topel zrak je redkejši in sili višje, medtem ko hladen zrak zaradi večje gostote tone nižje. Pri obravnavi daljnovodnih vodnikov, posebej pri nizkih hitrostih vetra, se pojavljajo stanja, ko je naravna konvekcija prevladujoč način hlajenja vodnika. Ključno vprašanje, ki se ob tem postavlja, je, ali so pri hitrostih pod $0,6 \mathrm{~m} / \mathrm{s}$ moči ohlajanja na ravni, ki jo zagotavlja horizontalna hitrost vetra $0,6 \mathrm{~m} / \mathrm{s}$. Nižja hitrost vetra namreč pomeni potencialno zmanjšano sposobnost vodnika, da bi lahko brez trajnih posledic prevajal statično določeni termični tok.

Za potrebe DTR se uporabljajo empirične formulacije. V literaturi zasledimo različne zveze za opis prisilne konvekcije, npr. Churchill-Bernsteinovo relacijo [1], McAdamsovo relacijo [2], Zhukavskasovo relacijo [3] in druge. Prav tako obstajajo različne formulacije opisa naravne konvekcije, recimo Morganova relacija [4], ki jo navajajo tudi v CIGRE [5].

Najbolj problematična je obravnava prehoda med popolnoma naravno konvekcijo, kjer je hitrost vetra nič, in popolnoma prisilno konvekcijo, ko je veter dovolj močan, da postane naravna konvekcija zanemarljiva. V uporabi so različni algoritmi za preklapljanje med režimoma. Nas zanima ozadje teh algoritmov in odgovor na vprašanje, ali hlajenje z naravno konvekcijo vedno zagotavlja najmanj statično določen termični tok po zgoraj navedenem standardu.

## Cilji naloge

1. pregledati strokovno in znanstveno literaturo s tega področja in izluščiti, kdaj je prišlo do prvega pojavljanja vrednosti $0,6 \mathrm{~m} / \mathrm{s}$ ter ali ima ta vrednost določeno fizikalno ozadje, npr. gostota zraka v relaciji s premerom in površino vodnika ali je mogoče vezano na zmožnost merilne tehnike iz petdesetih let 20. stoletja,
2. enoznačno odgovoriti na vprašanje »Ali je pri hitrostih vetra pod $0,6 \mathrm{~m} / \mathrm{s}$ moč hlajenja zaradi naravne konvekcije dovolj velika, da je pri temperaturi okolice $T_{\mathrm{a}}=35^{\circ} \mathrm{C}$, sončnem sevanju $S_{\mathrm{j}}=900 \mathrm{W} / \mathrm{m}^{2}$, koeficientu absorpcije 0,5 in emisivnosti 0,5 dopustni tok daljnovodne vrvi vedno višji ali enak statičnemu termični toku določenemu s standardom SIST EN 50182:2001?«

V primeru, da se izkaže, da področje hitrosti vetra pod $0,6 \mathrm{~m} / \mathrm{s}$ ne zagotavlja hlajenja za dosego statičnega termičnega toka, naročniku podati tabelo tokovnih redukcijskih faktorjev v odvisnosti od izmerjene horizontalne hitrosti vetra in zunanje temperature ali empirično relacijo za izračun tokovnega redukcijskega faktorja v odvisnosti od navedenih veličin.

## Izvedba naloge je predvidena v sledečih sklopih:

1. Pregled obstoječih empiričnih modelov in vetrovne statistike $z$ analizo podatkov $z$ ELESovih merilnih postaj
1.1. Pregled znanstvene in strokovne literature iz področja naravne konvekcije
1.2. Pregled literature iz področja konvektivnega prenosa toplote v DTR modelih
1.3. Pregled pogostosti stanj glede na hitrost vetra
2. Formulacija fizikalnega modela, numerična rešitev in analiza rezultatov
2.1. Postavitev termo-tekočinskega modela za laminaren režim obtekanja daljnovodne vrvi
2.2. Implementacija rešitvenega postopka
2.3. Verifikacija simulatorja na standardnih testih
3. Vzpostavitev eksperimentalnega poligona in izvedba preskusov
3.1. Priprava eksperimentalnega okolja za merjenje temperature vrvi v kontroliranih pogojih
3.2. Priprava eksperimentalnega okolja za merjenje nizkih hitrosti vetra pri naravni konvekciji
3.3. Izvedba meritev za validacijo numeričnega okolja.
4. Analiza rezultatov
4.1. Primerjava numeričnih in eksperimentalnih meritev
4.2. Študija numeričnih izračunov
4.3. Določitev meje med prevladujočo naravno konvekcijo in prisilno konvekcijo
5. Zaključki študije

## Povzetek:

V študiji »Ohlajanje vodnikov nadzemnih vodov pri horizontalnih hitrostih pod $0,6 \mathrm{~m} / \mathrm{s}$ « obravnavamo termično obnašanje vrvi v režimih s prevladujočo naravno konvekcijo. Prvi del študije je posvečen pregledu literature na področju naravne konvekcije in dinamičnih termičnih modelov, kjer identificiramo prvo pojavljanje vrednosti $0,6 \mathrm{~m} / \mathrm{s}$ v kontekstu termične obravnave daljnovodnih vrvi. Poleg pregleda literature pripravimo tudi pregled pogostosti stanj glede na hitrost vetra na podlagi podatkov iz ELESovih merilnih postaj.

V nadaljevanju postavimo fizikalni model za opis pojava. Upoštevamo prenos in generacijo toplote znotraj vrvi, prenos preko roba vrvi in sklopljen prenos gibalne količine ter toplote v okolici vrvi. Podrobno si ogledamo še odvisnost snovnih lastnosti zraka od temperature in vlage. Študijo nadaljujemo z reševanjem razvitega modela z uporabo lastne numerične rešitve na podlagi lokalne brezmrežne metode. Pravilnost rešitvenega postopka preverimo na standardnih testih in poenostavljenih primerih z znano analitično rešitvijo.

Vzporedno z numeričnim reševanjem problem obravnavamo tudi eksperimentalno. Predstavljen je merilni eksperiment s katerim posnemamo daljnovod med obratovanjem v brezvetrju in izvedemo meritve s skočnimi spremembami toka. Poleg kvantitativnih meritev pripravimo tudi eksperimentalno okolje za kvalitativno opazovanje gibanja zraka ob segrevanju vodnika, preko katerega preverimo, da smo med meritvami res merili samo gibanje zraka zaradi naravne konvekcije.

Zadnji del študije je namenjen analizi rezultatov, kjer predstavimo stabilnostno analizo numerične rešitve, primerjavo izračunov z meritvami in CIGRE priporočili ter analiziramo hlajenje vrvi v režimih šibkega zunanjega vetra. Pokažemo, da prisilna konvekcija relativno hitro nadvlada naravno konvekcijo in da hlajenje z naravno konvekcijo ni dovolj veliko, da je pri temperaturi okolice $35{ }^{\circ} \mathrm{C}$, sončnem sevanju $900 \mathrm{~W} / \mathrm{m}^{2}$, koeficientu absorpcije 0,5 in emisivnosti 0,5 dopustni tok daljnovodne vrvi vedno višji ali enak statičnemu termični toku določenemu s standardom SIST EN 50182:2001.

Študijo zaključimo s pregledom glavnih prispevkov in smernicami za nadaljnje delo.

Ključne besede: naravna konvekcija, ohlajanje vodnikov, Nusseltovo število, Navier-Stokes, laboratorijsko merjenje temperature vodnika, DTR.
Kazalo

1. Pregled obstoječih empiričnih modelov in vetrovne statistike z analizo podatkov z ELESovih merilnih postaj ..... 10
1.1 Pregled znanstvene in strokovne literature s področja naravne konvekcije ..... 10
1.2 Pregled literature s področja obravnave konvektivnega prenosa toplote v DTR modelih ..... 11
1.2.1. Konvekcija v CIGRE ..... 13
1.2.2. Konvekcija v IEEE ..... 14
1.2.3. Konvekcija v IEC ..... 15
1.3 Pregled pogostosti stanj glede na hitrost vetra ..... 16
2. Formulacija fizikalnega modela, numerična rešitev in analiza rezultatov ..... 22
2.1 Postavitev fizikalnega modela obtekanja daljnovodne vrvi ..... 22
2.1.1. Prenos in generacija toplote skozi vrv ..... 23
2.1.2. Prenos toplote in gibalne količine v zraku ..... 24
2.1.3. Joulsko segrevanje ..... 26
2.1.4. Sončno obsevanje ..... 27
2.1.5. Sevanja površine vodnika ..... 27
2.1.6. Snovne lastnosti zraka ..... 28
2.2 Implementacija rešitvenega postopka ..... 31
2.2.1. Krajevna diskretizacija domene ..... 31
2.2.2. Postavitev računskih točk ..... 33
2.2.3. Časovna diskretizacija ..... 33
2.2.4. Implementacija ..... 35
2.3 Verifikacija simulatorja na standardnih testih ..... 39
2.3.1. de Vahl Davisov test ..... 39
2.3.2. Naravna konvekcija okoli cilindra ..... 42
2.3.3. Prenos toplote iz ogrevane vrvi na okolico brez naravne konvekcije ..... 44
3. Vzpostavitev eksperimentalnega poligona in izvedba preskusov ..... 46
3.1 Priprava eksperimentalnega okolja za merjenje temperature vrvi v kontroliranih pogojih ..... 46
3.1.1. Zgradba merilnega eksperimenta ..... 46
3.1.2. Namestitev TC senzorjev temperature ..... 48
3.1.3. Zajem, digitalna pretvorba in obdelava meritev ..... 48
3.2 Priprava eksperimentalnega okolja za opazovanje gibanja zraka ob segrevanju vodnika ..... 53
3.3 Izvedba meritev za validacijo numerična okolja ..... 55
4. Analiza rezultatov ..... 58
4.1 Analiza numeričnih izračunov ..... 58
4.2 Primerjava numeričnih in eksperimentalnih meritev ..... 63
4.2.1. Ocena merilnega pogreška ..... 63
4.2.2. Določitev velikosti odstopanja temperature pri meritvah ..... 64
4.2.3. Primerjava modelskih izračunov in meritev ..... 68
4.2.4. Določitev meje med prevladujočo naravno konvekcijo in prisilno konvekcijo ..... 75
5. Zaključki študije ..... 80
5.1 Povzetek glavnih prispevkov študije ..... 80
5.2 Možnosti za nadgradnje ..... 81
6. Viri ..... 82

Seznam pogosto uporabljenih simbolov:
| $\alpha_{20}\left[{ }^{\circ} \mathrm{C}^{-1}\right]$ | koeficient temp. odvisnosti upornosti | $L$ | splošni diferencialni operator |
| :--- | :--- | :--- | :--- |
| $\alpha_{s}$ | absorptivnost vodnika | $\lambda[\mathrm{W} / \mathrm{mK}]$ | toplotna prevodnost |
| $\boldsymbol{\alpha}$ | vektor koeficientov razvoja | $m$ | število baznih funkcij |
| b [ $\mathrm{N} / \mathrm{m}^{3}$ ] | gostota telesne sile | MLSM | Meshless Local Strong Form Method |
| B | aproksimacijska matrika | $\mu\left[\mathrm{m}^{2} / \mathrm{s}\right]$ | kinematična viskoznost zraka |
| $b(\mathbf{p})$ | bazna funkcija | $n$ | število podpornih točk |
| $\beta_{20}\left[{ }^{\circ} \mathrm{C}^{-2}\right]$ | koeficient temp. odvisnosti upornosti | $N$ | število računskih vozlišč |
| $C^{2}[\mathrm{~m} / \mathrm{s}]$ | zvočna hitrost | n | Normalni vektor |
| C | jedro vrvi | Nu | Nusseltovo število |
| $c_{p}[\mathrm{~J} /(\mathrm{kgK})]$ | spec. toplotna kapacitivnost | $P[\mathrm{~Pa}]$ | tlak |
| D | premer vodnika | p( $x, \mathrm{y}$ ) | radij vektor |
| $D_{1}$ | premer nosilnega dela | $P_{C}[\mathrm{~W} / \mathrm{m}]$ | moč hlajenja zaradi konvekcije |
| $\epsilon$ | emisivnost vodnika | $q_{j}\left[\mathrm{~W} / \mathrm{m}^{3}\right]$ | gostota toplotnih izvorov |
| $q_{r}\left[\mathrm{~W} / \mathrm{m}^{2}\right]$ | gostota toplotnega toka sevanja | $q_{s}\left[\mathrm{~W} / \mathrm{m}^{2}\right]$ | gostota toplotnega toka sončnega obsevanja |
| Gr | Grashofovo število | $\rho\left[\mathrm{kg} / \mathrm{m}^{3}\right]$ | gostota |
| h [m] | nadmorska višina. | $R[\Omega / \mathrm{m}]$ | specifična upornost |
| $I[\mathrm{~A}]$ | električni tok | $I_{\text {stat }}[\mathrm{A}]$ | statični termični tok |
| $I_{t h}[\mathrm{~A}]$ | dinamični termični tok | $r$ | relativna vlaga |
| $I_{T}\left[W / m^{2}\right]$ | intenziteta sončnega obsevanja | Ra | Rayleighovo število |


| a | območje zraka | Re | Reynoldsovo število |
| :--- | :--- | :--- | :--- |
| al | območje aluminija | $P_{J}[\mathrm{~W} / \mathrm{m}]$ | moč joulskih izgub |
| st | območje jekla | ref | referenčna vrednost |
| $\chi$ | oblikovna funkcija | $S^{a l}\left[\mathrm{~m}^{2}\right]$ | presek vodnika |
| $\sigma_{B}\left[\mathrm{~W} / \mathrm{m}^{2} \mathrm{~K}^{4}\right]$ | Stefanova konstanta | $S$ | Površina vrvi |
| $\sigma$ | utežni parameter | $T_{s}\left[{ }^{\circ} \mathrm{C}\right]$ | temperatura površine vodnika |
| $t$ [s] | čas | $u[\mathrm{~m} / \mathrm{s}]$ | hitrost vetra |
| $T\left[{ }^{\circ} \mathrm{C}\right]$ | temperatura | $\mathbf{v}[\mathrm{m} / \mathrm{s}]$ | hitrost |
| $T_{a}\left[{ }^{\circ} \mathrm{C}\right]$ | ambientalna temperatura | $\hat{u}_{F}[\mathrm{~m} / \mathrm{s}]$ | mejna hitrost med prevladujočo naravno in prisilno konvekcijo |
| $T_{\text {MLSM }}\left[{ }^{\circ} \mathrm{C}\right]$ | temperatura površine vodnika izračunan z MLSM | $\hat{u}_{F 45}[\mathrm{~m} / \mathrm{s}]$ | mejna hitrost med prevladujočo naravno in prisilno konvekcijo pri vpadnem kotu $45{ }^{\circ}$ |
| $\Delta t[\mathrm{~s}]$ | časovni korak |  |  |

## 1. Pregled obstoječih empiričnih modelov in vetrovne statistike $z$ analizo podatkov $z$ ELESovih merilnih postaj

### 1.1 Pregled znanstvene in strokovne literature s področja naravne konvekcije

Naravna konvekcija je proces, ki nas spremlja pri vsakem koraku. Verjetno jo najbolj očitno opazimo pri vremenu, ko opazujemo, kako se recimo hladen zrak zliva v dolino, ali pa ko pri nevihtah močno segret zrak silovito prodira v višje plasti ozračja [6]. Po drugi strani je tudi pomemben proces v mnogih industrijskih panogah. Morda je še najbolj slikovit primer ulivanje kovinskih materialov, kjer med strjevanjem zlitin zaradi visokih temperaturnih gradientov izrazita naravna konvekcija povzroča neenakomerno porazdelitev zmesi in posledično napake v končnem izdelku [7, 8]. Iz stališča naše študije je naravna konvekcija pomembna pri ohlajanju daljnovodne vrvi v brezvetrju. Zaradi njene vseprisotnosti je študija naravne konvekcija priljubljena raziskovalna tematika in tako so raziskovalci opravili že vrsto teoretičnih [9-12], eksperimentalnih [13-15] in numeričnih študij [16-19], da bi poglobili naše znanje o tem pojavu.

V sklopu študije »Ohlajanje vodnikov nadzemnih vodov pri horizontalnih hitrostih pod 0,6 m/s« nas bo zanimala obravnava naravne konvekcije zraka okoli daljnovodne vrvi. V prvem približku si lahko vrv predstavljamo kot valj in tako razmišljamo o problemu naravne konvekcije okoli ogrevanega oziroma homogeno segretega valja. Splošen pregled tega in podobnih prenosnih problemov je predstavljen v [20]. Vsekakor lahko med začetnike raziskovalcev na tem področju štejemo Morgana, ki je v članku [21] predstavil korelacijo med Grashofovem, Prandtlovem in Nusseltovem številom. Z drugimi besedami, predstavil je korelacijo med močjo hlajenja v odvisnosti od snovnih lastnosti ter temperaturne razlike med valjem in okolico. Obstaja še več drugih podobnih študij, kjer avtorji iščejo korelacije med prenosom toplote iz valja v okolico pri različnih pogojih. Dober pregled teh študij je predstavljen v [20].

Kar nekaj dela je bilo opravljenega tudi iz eksperimentalnega vidika. V študiji iz leta 2003 [22] avtorji preučujejo vpliv omejevanja gibanja kapljevine pri naravni konvekciji. V zaprti z vodo napolnjeni škatli s pomočjo sledenja delcem (Particle Image Velocimetry) avtorji izmerijo hitrosti gibanja tekočine zaradi segrevanja preko horizontalno postavljenega cilindra. V podobni eksperimentalni študiji [23] avtorji tudi primerjajo izmerjene podatke z numerično rešitvijo Navier-Stokesovega problema. To pot je tesno
okolje zaprta škatla napolnjena z zrakom. Kot rezultat avtorji predstavijo hitrostna polja ter Nusseltova števila pri različnih Rayleighjevih številih.

Simuliranje mehanike tekočin je paradna disciplina iz področja numerične analize [16] in simulacije naravne konvekcije spadajo v to področje. Verjetno je najbolj znan članek iz leta 1983 [19], kjer de Vahl Davis postavi referenčno rešitev naravne konvekcije zraka v zaprti škatli. Mnogi avtorji so ta izračun ponovili in s tem potrdili numerično rešitev [24-26]. Za referenčni numerični izračun naravne konvekcije okoli valja lahko štejemo [27], kjer so avtorji s pomočjo metode končnih volumnov na neregularni mreži rešili različne probleme, med njimi tudi naravno konvekcijo okoli homogeno segretega valja. Novejši članek [28] obravnava identičen problem z nekoliko drugačnim numeričnim pristopom. Obstajajo tudi druge numerične študije naravne konvekcije okoli segretega telesa, kjer se avtorji ukvarjajo z numeričnimi izboljšavami [29], različnimi geometrijami [30, 31], različnimi robnimi pogoji [32] in z dodano prisilno konvekcijo [33, 34].

V našteti literaturi imamo dovolj podatkov, da lahko sestavimo fizikalni model za obravnavo naravne konvekcije okoli daljnovodnih vrvi [16-20]. Prav tako imamo veliko referenčnih rezultatov [27, 28], da bomo lahko naš model in numerično rešitev na vsakem koraku temeljito preverili.

### 1.2 Pregled literature s področja obravnave konvektivnega prenosa toplote v DTR modelih

Strmo naraščanje potreb po električni energiji zahteva neprestano večanje prenosnih zmogljivosti in tako je v preteklosti zaradi preobremenjenosti prenosnih linij večkrat prihajalo tudi do izpadov [35]. Maksimalni tok, ki lahko teče po vrvi, je omejen z največjo dovoljeno temperaturo površine vodnika, v Sloveniji je to običajno $80^{\circ} \mathrm{C}$, in se določa po standardu EN 50181:2001 glede na neugodne razmere, in sicer glede na zunanjo temperaturo zraka $35^{\circ} \mathrm{C}$ in hitrost vetra $0,6 \mathrm{~m} / \mathrm{s}$ (Slika 1). Ta meja izvira iz študije iz leta 1930 [36], kjer ocenijo, da je hitrost vetra, ki jo povzroči naravna konvekcija pri temperaturni razliki med vodnikom in okolico $30^{\circ} \mathrm{C}$ za majhen vodik velikosti $2 \mathrm{f} / \mathrm{s}$ hitrostjo vetra ( $0,6 \mathrm{~m} / \mathrm{s}$ ). Prav tako v [36] predpostavijo, da je v naravnem okolju veter vedno večji od $0,6 \mathrm{~m} / \mathrm{s}$. Torej je meja $0,6 \mathrm{~m} / \mathrm{s}$ postavljena kot najbolj neugoden scenarij. V nekoliko novejšem članku, ki se tudi sklicuje na [36], razdelijo jakost vetra na dve območji [37], in sicer na do $0,6 \mathrm{~m} / \mathrm{s}$ in nad $0,6 \mathrm{~m} / \mathrm{s}$. Za vsako območje predstavijo svojo relacijo za konvektivni prenos toplote, kjer se sklicujejo na empirično študijo predstavljeno v [38]. V letih od prvih DTR modelov je bilo narejeno veliko študij, ki so na tak ali drugačen način pripomogle k boljšemu razumevanju prenosa toplote iz daljnovodne vrvi na okolico [39-42]. V večini modelov sta naravna in prisilna konvekcija modelirani preko empiričnih zvez. Obstajajo tudi študije z direktnimi simulacijami hitrostnega polja [43]. Vsekakor bi lahko poiskali še veliko različnih prispev-
kov, vendar se v nadaljevanju raje posvetimo trem standardom, ki so pravzaprav destilacija svetovne literature, to so CIGRE [5], IEEE [44] in IEC [45]. V [46] je mogoče najti primerjavo med IEEE in CIGRE.

Vsi trije standardi predpostavijo ohranitev energije, ki jo zapišemo kot

$$
\begin{equation*}
\rho c_{p} \frac{d T}{d t}=q_{s}+q_{J}-q_{c}-q_{r}, \tag{1.1}
\end{equation*}
$$

kjer so $T$ temperatura vodnika, $\rho$ gostota vodika, $c_{p}$ specifična toplotna kapacitivnost vodnika, $q_{c}$ ohlajanje zaradi konvekcije, $q_{r}$ ohlajanje zaradi sevanja, $q_{s}$ sončno obsevanje in $q_{J}$ toplotni izvir zaradi joulskih izgub. Nekateri avtorji dodajo še druge člene, kot so hlajenje zaradi dežja ali izhlapevanja [41, 42], trenja [47]. V tej študiji se ukvarjamo s suho vrvjo pri šibkih vetrovih in so zato ti pojavi za našo obravnavo nepomembni.

Vsi trije modeli obravnavajo sevanje enako, in sicer s Stefan-Boltzmannovim zakonom. Za sončno obsevanja IEEE in CIGRE upoštevata geometrijo in izrazita sončno obsevanje kot funkcijo časa in geografske širine, medtem ko IEC predpostavi, da je podatek o sončnem obsevanju znan. Vsi trije standardi tudi na enak način izračunajo joulske izgube, kjer v CIGRE in IEC upoštevajo še temperaturno odvisno upornost. Nekoliko drugačni so njihovi modeli računanja konvektivnega ohlajanja. V naslednjih treh razdelkih si bolj podrobno oglejmo te modele.

Table F. 19 - Characteristics of aluminium conductors steel reinforced used in Germany - Type AL1/ST1A

| Code | Old code | Areas |  |  | No. of wires |  | Wire diameter |  | Diameter |  | Mass per unit length | Rated strength | DC resistance <br> 1 | Final modulus of elasticity | Coefficient of <br> Current Ilnear carrying expansion capacily |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  | AI | Steel | Total |  |  | AI | Steel | Core | Cond. |  |  |  |  |  |  |
|  |  | $\mathrm{mm}^{2}$ | $\mathrm{mm}^{2}$ | $\mathrm{mm}^{2}$ | Al | Steet | mm | mm | mm | mm | kg/km | kN | $\Omega / \mathrm{km}$ | $\mathrm{N} / \mathrm{mm}^{2}$ | 1/K | A |
| 15-AL 1/3-ST1A | 16/2,5 | 15,3 | 2,54 | 17,8 | 6 | 1 | 1,80 | 1,80 | 1,80 | 5,40 | 61,6 | 5,80 | 1,876 9 | 81000 | $1,92 \mathrm{E}$-05 | 105 |
| 24-AL1/4-ST1A | 25/4 | 23,9 | 3,98 | 27,8 | 6 | 1 | 2.25 | 2.25 | 2.25 | 6,75 | 96,3 | 8,95 | 1,2012 | 81000 | 1,92E-05 | 140 |
| 34-AL1/6-ST1A | 35/6 | 34,4 | 5,73 | 40,1 | 6 | 1 | 2,70 | 2,70 | 2,70 | 8,10 | 138,7 | 12,37 | 0,8342 | 81000 | $1,92 \mathrm{E}$-05 | 170 |
| 44-AL1/32-ST1A | 44/32 | 44,0 | 31,7 | 75,6 | 14 | 7 | 2,00 | 2,40 | 7,20 | 11.2 | 369,3 | 44,24 | 0,657 4 | 110000 | 1.50E-05 | - |
| 48-AL1/8-ST1A | 50/8 | 48,3 | 8,04 | 56,3 | 6 | 1 | 3,20 | 3,20 | 3,20 | 9,60 | 194,8 | 16,81 | 0,5939 | 81000 | 1,92E-05 | 210 |
| 51-AL 1/30-ST 1A | 50/30 | 51,2 | 29.8 | 81,0 | 12 | 7 | 2,33 | 2,33 | 6,99 | 11,7 | 374,7 | 42,98 | 0,564 4 | 107000 | 1,53E-05 | * |
| 70-AL1/11-ST1A | 70/12 | 69,9 | 11,4 | 81,3 | 26 | 7 | 1.85 | 1,44 | 4,32 | 11,7 | 282,2 | 26,27 | 0,4132 | 77000 | 1,89E-05 | 290 |
| 94-AL 1/15-ST1A | 95/15 | 94,4 | 15,3 | 109,7 | 26 | 7 | 2.15 | 1,67 | 5,01 | 13,6 | 380,6 | 34,93 | 0,3060 | 77000 | 1,89E-05 | 350 |
| 97-AL 1/56-ST1A | 95/55 | 96,5 | 56,3 | 152,8 | 12 | 7 | 3,20 | 3,20 | 9,60 | 16,0 | 706,8 | 77,85 | 0,2992 | 107000 | 1,53E-05 | - |
| 106-AL1/76-ST1A | 105/75 | 105,7 | 75,5 | 181,2 | 14 | 19 | 3,10 | 2,25 | 11.3 | 17,5 | 885,3 | 105,82 | 0,2742 | 110000 | 1,50E-05 | * |
| 122-AL1/20-ST1A | 120/20 | 121,6 | 19,8 | 141,4 | 26 | 7 | 2,44 | 1,90 | 5,70 | 15,5 | 491,0 | 44,50 | 0,2376 | 77000 | 1,89E-05 | 410 |
| 122-AL1/71-ST1A | 120/70 | 122,1 | 71,3 | 193,4 | 12 | 7 | 3,60 | 3,60 | 10,8 | 18,0 | 894,5 | 97,92 | 0,236 4 | 107000 | 1,53E-05 | - |
| 128-AL1/30-ST1A | 125/30 | 127,9 | 29,8 | 157,8 | 30 | 7 | 2,33 | 2,33 | 6,99 | 16,3 | 587,0 | 56,41 | 0,2260 | 82000 | 1,78E-05 | 425 |
| 149-AL1/24-ST1A | 150/25 | 148,9 | 24,2 | 173,1 | 26 | 7 | 2,70 | 2.10 | 6,30 | 17,1 | 600,8 | 53,67 | 0,1940 | 77000 | 1.89 E -05 | 470 |
| 172-AL1/40-ST1A | 170/40 | 171,8 | 40,1 | 211,8 | 30 | 7 | 2,70 | 2.70 | 8,10 | 18,9 | 788,2 | 74,89 | 0,168 3 | 82000 | 1,78E-05 | 520 |
| 184-AL1/30-ST1A | 185/30 | 183,8 | 29,8 | 213,6 | 26 | 7 | 3.00 | 2,33 | 6,99 | 19,0 | 741,0 | 65.27 | 0,157 1 | 77000 | 1,89E-05 | 535 |
| 209-AL1/34-ST1A | 210/35 | 209,1 | 34,1 | 243,2 | 26 | 7 | 3.20 | 2,49 | 7,47 | 20,3 | 844,1 | 73,36 | 0,138 1 | 77000 | 1,89E-05 | 590 |
| 212-AL1/49-ST1A | 210/50 | 212,1 | 49,5 | 261,5 | 30 | 7 | 3,00 | 3,00 | 9,00 | 21,0 | 973,1 | 92.46 | 0,136 3 | 82000 | 1,78E-05 | 610 |
| 231-AL1/30-ST1A | 230/30 | 230,9 | 29,8 | 260,8 | 24 | 7 | 3,50 | 2,33 | 6,99 | 21,0 | 870,9 | 72,13 | 0,1250 | 74000 | 1,96E-05 | 630 |
| 243-AL1/39-ST1A | 240/40 | 243,1 | 39,5 | 282,5 | 26 | 7 | 3.45 | 2,68 | 8,04 | 21,8 | 980,1 | 85,12 | 0,118 8 | 77000 | 1,89E-05 | 645 |
| 264-AL 1/34-ST 1A | 265/35 | 263,7 | 34,1 | 297,7 | 24 | 7 | 3,74 | 2,49 | 7.47 | 22,4 | 994,4 | 81,04 | 0,109 5 | 74000 | $1,96 \mathrm{E}$-05 | 680 |
| 305-AL1/39-ST1A | 305/40 | 304,6 | 39,5 | 353.7 | 26 | 7 | 3,86 | 3,00 | 9,00 | 24,4 | 1227,3 | 105,09 | 0,094 9 | 77000 | 1,89E-05 | 740 |
| 339-AL1/30-ST1A | 340/30 |  |  | 344,1 | 54 | 7 | 2,68 | 2,68 | 8.04 | 24,1 | 1151,2 | 96,80 | 0,0949 | 70000 | $1,93 \mathrm{E}$-05 | 740 |
|  |  | 339,3 | 29,8 | 369,1 | 48 | 7 | 3,00 | 2,33 | 6,99 | 25.0 | 1171,2 | 91,71 | 0,0852 | 62000 | 2,05E-05 | 790 |
| 382-AL1/49-ST1A | 380/50 | 381,7 | 49.5 | 431,2 | 54 | 7 | 3.00 | 3,00 | 9,00 | 27,0 | 1442,5 | 121,30 | 0,075 8 | 70000 | 1.93 E -05 | 840 |
| 386-AL1/34-ST1A | 385/35 | 386,0 | 34.1 | 420,1 | 48 | 7 | 3.20 | 2.49 | 7,47 | 26,7 | 1333,6 | 102,56 | 0,0749 | 62000 | 2,05E-05 | 850 |
| 434-AL1/56-ST1A | 435/55 | 434,3 | 56,3 | 490,6 | 54 | 7 | 3,20 | 3,20 | 9,60 | 28,8 | 1641,3 | 133,59 | 0,066 6 | 70000 | 1,93E-05 | 900 |
| 449-AL1/39-ST1A | 450/40 | 448,7 | 39,5 | 488,2 | 48 | 7 | 3,45 | 2,68 | 8,04 | 28,7 | 1549,1 | 119,05 | 0,064 4 | 62000 | 2,05E-05 | 920 |
| 490-AL1/64-ST1A | $490 / 65$ | 490,3 | 63,6 | 553,8 | 54 | 7 | 3,40 | 3,40 | 10,2 | 30,6 | 1852,9 | 150,81 | 0,0590 | 70000 | 1.93E-05 | 960 |
| 494-AL1/34-ST1A | 495/35 | 494,4 | 34,1 | 528,4 | 45 | 7 | 3,74 | 2,49 | 7,47 | 29,9 | 1632,6 | 117,96 | 0,058 4 | 61000 | 2,09E-05 | 985 |
| 550-AL1/71-ST1A | 510/45 | 510,5 | 45,3 | 555,8 | 48 | 7 | 3,68 | 2,87 | 8,61 | 30,7 | 1765,3 | 133,31 | 0,05666 | 62000 | 2,05E-05 | 995 |
| 562-AL1/49-ST1A | 560/50 | 549,7 | 71,3 | 620,9 | 54 | 7 | 3,60 | 3,60 | 10,8 | 32,4 | 2077,2 | 166,32 | 0,052 6 | 70000 | 1.93 E -05 | 1020 |
| 571-AL1/39-ST1A | 570/40 | 571,2 | 49,5 | 611,2 | 48 | 7 | 3,86 | 3,00 | 9,00 | 32,2 | 1939,5 | 146,28 | 0,0515 | 62000 | 2,05E-05 | 1040 |
| 653-AL1/45-ST1A | 650/45 | 653,5 | 45,3 | 610,6 | 45 | 7 | 4,02 | 2,68 | 8,04 | 32,2 | 1887,1 | 136,40 | 0,0506 | 61000 | 2,09E-05 | 1050 |
| 679-AL1/86-ST1A | 680/85 | 678,6 | 86,0 | 764,5 | 54 | 19 | 4,30 | 2,87 | 8,61 | 34,4 | 2159,9 | 156,18 | 0,044 2 | 61000 | 2,09 E-05 | 1120 |
| 1046-AL 1/45-ST1A | 1045/45 | 1045,6 | 45,3 | 1090,9 | 72 | 7 | 4,00 | 2,40 | 12,0 | 36,0 | 2549,7 | 206,56 | 0,0426 | 68000 | $1,94 \mathrm{E}-05$ | 1150 |
| NOTE 1 Direction of lay of external layer is right-hand (Z) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

EN 50182:2001

Slika 1: Karakteristike vrvi, ki so v obravnavi v študiji, in sicer 243-AL1/39-ST1A in 490-AL1/64ST1A (vir: EN 50181:2001)

### 1.2.1. Konvekcija v CIGRE

Splošna relacija za opis tako naravne in prisilne konvekcije $P_{C}$ je v CIGRE predstavljena kot

$$
\begin{equation*}
P_{C}=\pi\left(T_{s}-T_{a}\right) \lambda_{a} \mathrm{Nu}\left[\frac{\mathrm{~W}}{\mathrm{~m}}\right], \tag{1.2}
\end{equation*}
$$

kjer sta $T_{s}\left[{ }^{\circ} \mathrm{C}\right]$ in $T_{a}\left[{ }^{\circ} \mathrm{C}\right]$ temperaturi površine vodnika in okoliškega zraka, Nu Nusseltovo število in $\lambda_{a}[\mathrm{~W} / \mathrm{mK}]$. V CIGRE upoštevajo, da je toplotna prevodnost zraka odvisna od temperature, kot

$$
\begin{equation*}
\lambda_{a}(T)=2.368 \cdot 10^{-2}+7.23 \cdot 10^{-5} T-2.763 \cdot 10^{-8} T^{2}\left[\frac{\mathrm{~W}}{\mathrm{mK}}\right], \tag{1.3}
\end{equation*}
$$

kjer za izračun (1.2) toplotno prevodnost izračunajo pri temperaturi filma $T_{f}=0.5\left(T_{a}+T_{s}\right)\left[{ }^{\circ} \mathrm{C}\right]$, ki je aritmetična sredina med temperaturam zraka in površine vrvi. Kritični del ocene konvektivnega prenosa toplote je seveda izračun Nusseltovega števila, v katerem je zajeta mehanika kapljevine (zraka) v okolici vodnika. V CIGRE upoštevajo Morganov [4] predlog za opis pretoka tekočine pravokotno na valj

$$
\begin{equation*}
\mathrm{Nu}_{90}=B \mathrm{Re}^{n}, \tag{1.4}
\end{equation*}
$$

kjer sta $B$ in $n$ tabelirani konstanti in Re Reynoldsovo število

$$
\begin{equation*}
\operatorname{Re}=\frac{u D \rho_{a}}{\mu_{a}}, \tag{1.5}
\end{equation*}
$$

kjer je $u[\mathrm{~m} / \mathrm{s}]$ hitrost vetra in $\mu_{a}\left[\mathrm{~m}^{2} / \mathrm{s}\right]$ kinematična viskoznost zraka pri temperaturi filma $T_{f}$, ki jo izračunamo kot

$$
\begin{equation*}
\mu_{a}(T)=\frac{17.239+4.635 \cdot 10^{2} T-2.03 \cdot 10^{-5} T^{2}}{\rho_{a}} 10^{-6}\left[\frac{\mathrm{~m}^{2}}{\mathrm{~s}}\right] \tag{1.6}
\end{equation*}
$$

Za primer, ko smer vetra ni pravokotna na cilinder, se v CIGRE ponovno uporabi Morganove predpostavke za dodatne zveze oblike $\mathrm{Nu}_{\delta} / \mathrm{Nu}_{90}=f(\delta)$, in sicer

$$
\begin{gather*}
\frac{\mathrm{Nu}_{\delta}}{\mathrm{Nu}_{90}}=\left(\sin ^{2}(\delta)+0.0169 \cos ^{2}(\delta)\right)^{0.225} ; \text { za gladke vodnike, }  \tag{1.7}\\
\frac{\mathrm{Nu}_{\delta}}{\mathrm{Nu}_{90}}=0.42+0.68 \sin ^{1.08}(\delta) ; \text { za pletenice in kot manj kot } 24^{\circ},  \tag{1.8}\\
\frac{\mathrm{Nu}_{\delta}}{\mathrm{Nu}_{90}}=0.42+0.58 \sin ^{0.90}(\delta) ; \text { za pletenice in kot več kot } 24^{\circ} . \tag{1.9}
\end{gather*}
$$

V brezvetrju je dominantni prispevek h koeficientu prestopa prispevek naravne konvekcije, ki se določi kot

$$
\begin{equation*}
\mathrm{Nu}_{n a t}=\xi(\mathrm{Ra})^{m} \tag{1.10}
\end{equation*}
$$

Kjer je Rayleighjevo število (Ra) vpeljano kot [19]

$$
\begin{equation*}
\mathrm{Ra}=\frac{\rho^{2} c_{p} g \beta\left(T-T_{a}\right) L^{3}}{\lambda \mu} \tag{1.11}
\end{equation*}
$$

z brez-dimenzijskimi števili $\xi$ in $m$ tabelirani za različne pogoje. Pri nizkih hitrostih vetra se Nu izračuna preko (1.10) in (1.4) ter upošteva večjo vrednost. Taka predpostavka ima zanimivo posledico, in sicer, da imajo toplotne izgube pri prehodu iz nizkih hitrosti proti večjim hitrostim vetra nezvezno obnašanje. Možna rešitev je, da v prehodnem območju uporabimo linearno kombinacijo obeh izračunov ali pa da vektorsko seštejemo oba prispevka. CIGRE upošteva tudi odvisnost gostote od višine in temperature kot

$$
\begin{equation*}
\rho(T, h)=\frac{1.293-1.524 \cdot 10^{-4} h+6.379 \cdot 10^{-9} h^{2}}{1+0.00367 T}\left[\frac{\mathrm{~kg}}{\mathrm{~m}^{3}}\right] \tag{1.12}
\end{equation*}
$$

kjer je $h[\mathrm{~m}]$ nadmorska višina.

### 1.2.2 Konvekcija v IEEE

IEEE podobno kot CIGRE obravnava različne režime glede na jakost vetra. Pri hitrosti vetra pod 0,2 $\mathrm{m} / \mathrm{s}$ upoštevajo relacijo za naravno konvekcijo, in sicer

$$
\begin{equation*}
P_{C}=3.645 \rho^{0.5} D^{0.75}\left(T_{s}-T_{a}\right)^{1.25}\left[\frac{\mathrm{~W}}{\mathrm{~m}}\right] \tag{1.13}
\end{equation*}
$$

Pri znatnih hitrostih vetra nad $0,2 \mathrm{~m} / \mathrm{s}$ upoštevajo večjo izmed naslednjih dve relacij

$$
\begin{gather*}
{ }^{1} P_{C}=K_{a}\left(1.01+1.35 \mathrm{Re}^{0.52}\right) \lambda\left(T_{s}-T_{a}\right)\left[\frac{\mathrm{W}}{\mathrm{~m}}\right]  \tag{1.14}\\
{ }^{2} P_{C}=K_{a} 0.754 \operatorname{Re}^{0.6} \lambda\left(T_{s}-T_{a}\right)\left[\frac{\mathrm{W}}{\mathrm{~m}}\right] \tag{1.15}
\end{gather*}
$$

kjer ${ }^{1} P_{C}$ opiše primere z nizko hitrostjo in ${ }^{2} P_{C}$ primere z veliko hitrostjo vetra. Kot vetra se upošteva kot

$$
\begin{equation*}
K_{a}=1.194-\cos (\delta)+0.194 \cos (2 \delta)+0.368 \sin (2 \delta) \tag{1.16}
\end{equation*}
$$

IEEE podobno kot CIGRE upošteva temperaturno odvisne snovne lastnosti, in sicer gostoto enako kot CIGRE ter toplotno prevodnost in viskoznost kot

$$
\begin{equation*}
\lambda_{a}(T)=242 \cdot 10^{-2}+7.477 \cdot 10^{-5} T-4.407 \cdot 10^{-9} T^{2} \tag{1.17}
\end{equation*}
$$

$$
\begin{equation*}
\mu_{a}(T)=\frac{1}{\rho_{a}} \frac{1.458 \cdot 10^{-6}(T+273)}{T+383.4}\left[\frac{\mathrm{~m}^{2}}{\mathrm{~s}}\right], \tag{1.18}
\end{equation*}
$$

kjer enako kot pri CIGRE snovne lastnosti ocenijo pri temperaturi filma $T_{f}$.

### 1.2.3. Konvekcija v IEC

IEC standard poenostavi obravnavo in sicer kar na

$$
\begin{gather*}
P_{C}=\pi\left(T_{s}-T_{a}\right) \lambda_{a} \mathrm{Nu}\left[\frac{\mathrm{~W}}{\mathrm{~m}}\right],  \tag{1.19}\\
\mathrm{Nu}=0.65 \mathrm{Re}^{0.2}+0.23 \mathrm{Re}^{0.6},  \tag{1.20}\\
\mathrm{Re}=1.644 \cdot 10^{9} u D\left(\frac{T_{a}+T_{s}}{2}\right)^{-1.78}, \tag{1.21}
\end{gather*}
$$

kjer se ne ubadajo niti z naravno konvekcijo niti z vpadnim kotom vetra.

Vse tri modele prepišemo v najljubše interpretrsko okolje in jih primerjamo. Oglejmo si primerjavo izračuna konvekcije po IEEE, CIGRE in IEC glede na hitrost vetra (levo) pri temperaturi vodnika $80^{\circ} \mathrm{C}$ in temperaturi okolice $35{ }^{\circ} \mathrm{C}$ ter glede na temperaturo vodnika (desno) pri hitrosti vetra $0,6 \mathrm{~m} / \mathrm{s}$ (Slika 2). Ta primerjava nam bo služila tudi kot opora za preverjanje naše numerične rešitve problema.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-18.jpg?height=665&width=1332&top_left_y=1459&top_left_x=380)
Slika 2: Primerjava izračuna konvekcije po IEEE, CIGRE in IEC glede na hitrost vetra (levo) pri temperaturi vodnika $80^{\circ} \mathrm{C}$ in temperaturi okolice $35{ }^{\circ} \mathrm{C}$ ter glede na temperaturo vodnika (desno) pri hitrosti vetra $0,6 \mathrm{~m} / \mathrm{s}$.

### 1.3 Pregled pogostosti stanj glede na hitrost vetra

Oglejmo si še motiv za študijo. Vprašamo se kolikšen je delež stanj pri katerih naravna konvekcija ni zanemarljiva, torej stanj z nizko jakostjo vetra. Pomembno se je tudi zavedati vrednosti temperature, saj nas na koncu koncev zanima ogroženost daljnovodnih vrvi zaradi pregrevanja, torej stanja z nizko hitrostjo vetra in visoko temperaturo. Na to vprašanje si najlažje odgovorimo s preprosto statistično analizo izmerjenih podatkov. Tako analiziramo meritve temperature, hitrosti in smeri vetra s 5 minutno ločljivostjo za obdobje 2007-2017 na šestih lokacijah: Beričevo (BE), Divača (DI), Krško (KK), Maribor (MB), Okroglo (OK) in Podlog (PL).

Najprej nas zanima statistika za eno lokacijo in posamezne mesece (Slika 3 in Slika 4). Takoj opazimo, da ne glede na mesec, lahko pričakujemo največ dogodkov z jakostjo vetra okoli $0,5 \mathrm{~m} / \mathrm{s}$, kar je ravno v območju, kjer naravna konvekcija glede na [36-38] še igra vlogo. Najbolj pričakovana temperatura je seveda odvisna od letnega časa. Opazimo tudi korelacijo med temperaturo in jakostjo vetra, in sicer večja je verjetnost za močnejši veter pri višjih temperaturah.

V naslednjem koraku nas zanima krajevna odvisnost, zato si oglejmo statistiko tudi za različna merilna mesta. Zimski meseci niso problematični, zato omejimo analizo le na tople mesece, in sicer na obdobje od maja do septembra (Slika 5). Iz rezultatov po pričakovanjih opazimo krajevno odvisnost, recimo Divača in Maribor sta bolj vetrovna kot druge lokacije. Ne glede na lokacijo pa je vedno prisoten delež stanj z nizko jakostjo vetra.

Nazadnje si oglejmo še časovno porazdelitev nam zanimivih dogodkov, in sicer največjo in povprečno temperaturo pri hitrosti pod $0,6 \mathrm{~m} / \mathrm{s}$ za posamezne mesece od leta 2007 do 2017 za vseh šest lokacij (Slika 6). Opazimo, da imamo vsako leto na vsaki lokaciji dogodke z izredno visoko temperaturo pri praktično nič vetra. Poleg tega opazimo, da so podatki do leta 2010 precej pomanjkljivi.

Najhujšìh scenarij, ki ga predvideva standard EN 50181:2001, ko je temperatura nad $35{ }^{\circ} \mathrm{C}$ in hitrost vetra pod $0,6 \mathrm{~m} / \mathrm{s}$ je v npr. Beričevem malo, in sicer pod $0,1 \%$. Že pri nekoliko manj strogem kriteriju, in sicer najvišjo dovoljeno temperaturo $25^{\circ} \mathrm{C}$ pa delež dogodkov hitro naraste na $1-2 \%$. Pri meji $20^{\circ} \mathrm{C}$ smo pa že v velikostnem razredu 5 \% deleža dogodkov (Slika 7).

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-20.jpg?height=2042&width=1378&top_left_y=242&top_left_x=369)
Slika 3: Statistika vetrovnih dogodkov po mesecih za prvo polovico leto za celotno obdobje (20072017) izmerjeno v Beričevem.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-21.jpg?height=2042&width=1380&top_left_y=242&top_left_x=369)
Slika 4: Statistika vetrovnih dogodkov po mesecih za drugo polovico leto za celotno obdobje (2007 2017) izmerjeno v Beričevem.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-22.jpg?height=2045&width=1376&top_left_y=244&top_left_x=371)
Slika 5: Statistika vetrovnih dogodkov v obdobju toplih mesecev (maj - september) za celotno obdobje (2007-2017) za vseh šest lokacij.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-23.jpg?height=643&width=1309&top_left_y=281&top_left_x=382)
Slika 6: Največja in povprečna temperatura pri hitrosti pod $0,6 \mathrm{~m} / \mathrm{s}$ za posamezne mesece od leta 2007 do 2017 za vseh šest lokacij.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-23.jpg?height=650&width=1281&top_left_y=1108&top_left_x=397)
Slika 7: Verjetnost za dogodke s hitrostjo do $0,6 \mathrm{~m} / \mathrm{s}$ glede na spodnjo mejo temperature.

## 2. Formulacija fizikalnega modela, numerična rešitev in analiza rezultatov

### 2.1 Postavitev fizikalnega modela obtekanja daljnovodne vrvi

Cilj modeliranja naravne konvekcija okoli daljnovodne vrvi je bolj podrobno razumevanje prenosa toplote iz vrvi na okolico v brezvetrju. V tem razdelku postavimo fizikalni model, s pomočjo katerega bomo kasneje analizirali različne scenarije.

Zaradi velikega razmerja med dolžino in presekom vrvi se bomo omejili na dvodimenzionalno obravnavo. Obravnavali bomo tri področja, in sicer nosilni jekleni del, aluminijasti prevodni del in okoliški zrak (Slika 8). V vsakem področju bomo zapisali prenosne enačbe in nazadnje področja sklopili preko robnih pogojev oziroma eno-domenske obravnave [48].

V nosilni vrvi bomo upoštevali samo prenos toplote, saj je električna prevodnost jekla $\left(\sigma_{s t} \sim 1,5 \cdot 10^{6}[1 / \Omega \mathrm{m}]\right) \quad \mathrm{v} \quad$ primerjavi $\quad \mathrm{s} \quad$ prevodnostjo aluminijastega vodnika ( $\sigma_{a l} \sim 35 \cdot 10^{6}[1 / \Omega \mathrm{m}]$ ) majhna in tako električni tok skozi nosilno vrv predstavlja zgolj reda $1 \%$ celotnega toka skozi vrv [49]. V prevodnem delu bomo prenosu toplote dodali še generacijo toplotnega toka, kar bomo upoštevali kot dodatni izvor v prenosni enačbi. Za toplotne izvire bomo upoštevali joulske izgube in temperaturno odvisno upornost.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-25.jpg?height=647&width=1045&top_left_y=1551&top_left_x=539)
Slika 8: Shema problema

Nekoliko bolj zapletena bo obravnava okoliškega zraka, kjer je potrebno poleg prenosa toplote upoštevati še prenos gibalne količine ter masno kontinuiteto. Vse tri pojave je potrebno sklopiti in izkaže se, da je predvsem sklopitev masne kontinuitete in prenosa gibalne količine nekoliko nerodna. V nadaljevanju podrobneje razčlenimo posamezne elemente modela.

### 2.1.1. Prenos in generacija toplote skozi vrv

Najprej zapišimo model prenosa toplote znotraj vrvi

$$
\begin{gather*}
c_{p}^{s t} \rho^{s t} \frac{\partial T^{s t}}{\partial t}=\lambda^{s t} \nabla^{2} T^{s t}  \tag{2.1}\\
c_{p}^{a l} \rho^{a l} \frac{\partial T^{a l}}{\partial t}=\lambda^{a l} \nabla^{2} T^{a l}+q_{J} \tag{2.2}
\end{gather*}
$$

kjer indeksa st, al označujeta območje nosilne vrvi in vodnika ter $q_{j}\left[\mathrm{~W} / \mathrm{m}^{3}\right]$ gostoto toplotnih virov zaradi joulskih izgub. Na mejah med nosilno vrvjo in vodnikom ter vodnikom in okolico morajo držati ohranitveni zakoni, tako lahko zapišemo robne pogoje

$$
\begin{gather*}
T^{a l}\left(r_{1}\right)=T^{s t}\left(r_{1}\right),  \tag{2.3}\\
\left.\lambda^{a l} \frac{\partial T^{a l}}{\partial \mathbf{n}}\right|_{r_{1}}=\left.\lambda^{s t} \frac{\partial T^{s t}}{\partial \mathbf{n}}\right|_{r_{1}},  \tag{2.4}\\
T^{a l}\left(r_{2}\right)=T^{a}\left(r_{2}\right),  \tag{2.5}\\
\left.\lambda^{a l} \frac{\partial T^{a}}{\partial \mathbf{n}}\right|_{r_{2}}-\left.\lambda^{a} \frac{\partial T^{a}}{\partial \mathbf{n}}\right|_{r_{2}}=q_{s}+q_{r}, \tag{2.6}
\end{gather*}
$$

kjer $r_{1}[\mathrm{~m}]$ in $r_{2}[\mathrm{~m}]$ označujeta polmer jeklenega dela in celotne vrvi ter indeks $a$ okoliško območje, $\mathbf{n}$ normali vektor, $q_{r}\left[\mathrm{~W} / \mathrm{m}^{2}\right]$ in $q_{s}\left[\mathrm{~W} / \mathrm{m}^{2}\right]$ toplotne vire/ponore zaradi sevanja in sončnega obsevanja.

Sistem (2.1)-(2.6) lahko zapišemo bolj kompaktno v eno-domensko enačbo

$$
\begin{equation*}
c_{p}(\mathbf{p}) \rho(\mathbf{p}) \frac{\partial T}{\partial t}=\nabla \cdot(\lambda(\mathbf{p}) \nabla T)+q(\mathbf{p}) \tag{2.7}
\end{equation*}
$$

kjer smo vpeljali krajevno odvisne snovne lastnosti in toplotne izvore

$$
\begin{align*}
& c_{p}(\mathbf{p})=\left\{\begin{array}{ll}
c_{p}^{s t} ; & r<r_{1} \\
c_{p}^{a l} ; & r \geq r_{1}
\end{array}\right\}, \\
& \rho(\mathbf{p})=\left\{\begin{array}{ll}
\rho^{s t} ; & r<r_{1} \\
\rho^{a l} ; & r \geq r_{1}
\end{array}\right\}, \\
& \lambda(\mathbf{p})=\left\{\begin{array}{ll}
\lambda^{s t} ; & r<r_{1} \\
\lambda^{a l} ; & r \geq r_{1}
\end{array}\right\},  \tag{2.8}\\
& q(\mathbf{p})=\left\{\begin{array}{cc}
q_{j} ; & r_{2}>r>r_{1} \\
q_{s}+q_{r} ; & r=r 2 \\
0 & \text { sicer }
\end{array}\right\},
\end{align*}
$$

kjer so gostota aluminija $\rho_{a l}=2703 \mathrm{~kg} / \mathrm{m}^{3}$, gostota jekla $\rho_{s t}=7780 \mathrm{~kg} / \mathrm{m}^{3}$, specifična toplotna kapacitivnost aluminija $c_{p}^{a l}=897 \mathrm{~J} /(\mathrm{kgK})$ in specifična toplotna kapacitivnost jekla $c_{p}^{a l}=481 \mathrm{~J} /(\mathrm{kgK})$. Toplotna prevodnost aluminija se giblje okoli $\lambda_{\text {Al }}=200[\mathrm{~W} / \mathrm{mK}]$, medtem ko v CIGRE predlagajo vrednosti $\lambda \in[0.5,7][\mathrm{W} / \mathrm{mK}]$. Razlika nastane zaradi geometrije pletenice. Velik del prenosa toplote se $\rho_{s t}=7780 \mathrm{~kg} / \mathrm{m}^{3}$ ogaja v zračnih kanalih med posameznimi vodniki [49], poleg tega pa spoji med vodniki niso idealni. Obširna diskusija o efektivni radialni toplotni prevodnosti je predstavljena v [49]. V naši obravnavi bomo uporabili efektivno prevodnost pridobljeno iz meritev.

### 2.1.2. Prenos toplote in gibalne količine v zraku

Za izračun prenosa toplote iz površine vrvi moramo poznati temperaturo tik ob vrvi, ki seveda ni enaka ambientalni temperaturi, temveč prehaja iz temperature površine vrvi proti ambientalni temperaturi. Za opis te mejne plasti moramo poznati prenos toplote v zraku, kar pa ni tako preprosto, kot v vrvi, saj je zrak tekočina z nizko toplotno prevodnostjo ( $\left.\lambda^{a}=0.0244 \mathrm{~W} /(\mathrm{mK})\right)$ in je tako prevladujoč mehanizem prenosa toplote konvekcija. Za izračun konvekcije moramo pa seveda poznati hitrostno polje. Zrak obravnavamo kot newtonsko kapljevino v nestisljivem režimu, saj pričakujemo da bo Machovo število (razmerje zvočne hitrosti in hitrosti toka) globoko pod 0,3 in zato lahko njegovo gibanje opišemo z Navier-Stokesovo in masno kontinuitetno enačbo [50]

$$
\begin{gather*}
\rho^{a} \frac{\partial \mathbf{v}}{\partial t}+\rho^{a} \nabla \cdot(\mathbf{v} \mathbf{v})=-\nabla P+\nabla \cdot\left(\mu^{a} \nabla \mathbf{v}\right)+\mathbf{b}  \tag{2.9}\\
\nabla \cdot \mathbf{v}=0 \tag{2.10}
\end{gather*}
$$

kjer smo z v označili hitrost, b telesno silo in $P$ tlak. V enačbi prepoznamo enačbo gibanja za kontinuum in v drugi masno kontinuiteto za nestisljivo tekočino, kjer je časovni odvod gostote nič. Zapišimo še prenos toplote

$$
\begin{equation*}
\rho^{a} c_{p}^{a} \frac{\partial T}{\partial t}+\rho^{a} c_{p}^{a} \nabla \cdot(T \mathbf{v})=\nabla \cdot\left(\lambda^{a} \nabla T\right) \tag{2.11}
\end{equation*}
$$

kjer smo k časovnemu odvodu temperature dodali še konvektivni prispevek. Enačba (2.11) je preko tega člena sklopljena z (2.9), manjka nam še povratna sklopitev, ki pa jo vpeljemo preko temperaturno odvisne gostote. Uporabimo znano Bossinequejevo relacijo

$$
\begin{equation*}
\mathbf{b}=\rho_{r e f}\left[1-\beta_{T}\left(T-T_{\mathrm{ref}}\right)\right] \mathbf{g} \tag{2.12}
\end{equation*}
$$

kjer je $\mathbf{g}\left[\mathrm{m} / \mathrm{s}^{2}\right]$ gravitacijski pospešek, $\beta_{T}[1 / \mathrm{K}]$ linearni koeficient toplotnega raztezka, $\rho_{\text {ref }}\left[\mathrm{kg} / \mathrm{m}^{3}\right]$ referenčna gostota pri referenčni temperaturi $T_{\text {ref }}\left[{ }^{\circ} C\right]$. Enačbo (2.12) lahko povežemo s CIGRE relacijo za gostoto tako da (1.12) razvijemo v vrsto do prvega člena okoli $T_{\text {ref }}$, dobimo

$$
\begin{equation*}
\rho(T, h) \approx\left(1,293-1,524 \cdot 10^{-4} h+6,379 \cdot 10^{-9} h^{2}\right)\left(1-0,00367\left(T-T_{r e f}\right)\right) \tag{2.13}
\end{equation*}
$$

In takoj opazimo podobnost z enačbo (2.12)

$$
\begin{equation*}
\rho(T, h) \approx \rho_{0}\left(1-\beta_{T}\left(T-T_{r e f}\right)\right) \tag{2.14}
\end{equation*}
$$

kjer je $\rho_{0}=1,293-1,524 \cdot 10^{-4} h+6,379 \cdot 10^{-9} h^{2}\left[\mathrm{~kg} / \mathrm{m}^{3}\right]$ in $\beta_{T}=0,00367[1 / \mathrm{K}]$, kar je ravno koeficient temperaturne razteznosti zraka. Namesto relacij, ki jih ponujata CIGRE in IEEE, lahko uporabimo tudi bolj splošne relacije predstavljene v poglavju 2.1.6.

Sistem (2.9), (2.10) in (2.11) še ni popolnoma sklopljen, manjka nam še neposredna povezava s tlakom. To lahko naredimo na več načinov. Oglejmo si dva pristopa, ki ju bomo preizkusili. Najlažje je težavo s sklopitvijo rešiti preko vpeljave umetne stisljivosti [51, 52] (ang. Artificial compressibility Method (ACM)), tako da enačba (2.10) postane parabolična

$$
\begin{equation*}
\frac{\partial \rho}{\partial p} \frac{\partial p}{\partial t}+\nabla \cdot \mathbf{v}=0 \tag{2.15}
\end{equation*}
$$

kjer prepoznamo zvočno hitrost $C^{2}=\partial p / \partial \rho$. Tako postane sistem neposredno rešljiv in ga lahko rešimo tudi z eksplicitnim korakanjem. Slabost je, da smo uvedli nekaj napake v časovni potek, medtem ko je ustaljeno stanje ponovno pravilno, saj gre prvi člen na levi strani enačbe (2.15) proti nič. Do podobnega razmisleka pridemo, če rešujemo tlačno enačbo preko navideznega časovnega korakanja [25]. Metodo se da dodatno stabilizirati s pomočjo CBS (Characteristics-Based Split) algoritmom [18], kjer enačbi (2.15) dodamo še laplacejev člen. Izkaže se, da je ta stabilizacija dobrodošla pri obravnavi na neenakomernih geometrijah [53], kakršna bo tudi naša. Zapišimo splošno obliko enačbe za izračun tlaka

$$
\begin{equation*}
\frac{\partial P}{\partial t}=\xi_{1} \nabla^{2} P+\xi_{2} \nabla \cdot \mathbf{v} \tag{2.16}
\end{equation*}
$$

kjer smo vpeljali dve relaksacijski števili $\xi_{1,2}$, ki jih bomo bolj podrobno komentirali pri izračunih.

Nekoliko bolj konvencionalen je pristop z reševanjem tlačne enačbe ali korekcijske enačbe za tlak [16]. Oba pristopa sta podobna, tako da bomo opisali samo prvega. Delujmo z operatorjem divergence na enačbo (2.9)

$$
\begin{equation*}
\nabla \cdot\left(\rho^{a} \frac{\partial \mathbf{v}}{\partial t}\right)+\nabla \cdot\left(\rho^{a} \nabla \cdot(\mathbf{v})\right)=-\nabla^{2} P+\nabla \cdot\left(\nabla \cdot\left(\mu^{a} \nabla \mathbf{v}\right)\right)+\nabla \cdot \mathbf{b} \tag{2.17}
\end{equation*}
$$

ker velja (2.10) in seveda lahko zamenjamo $\nabla \cdot\left(\nabla^{2} \mathbf{u}\right)=\nabla^{2}(\nabla \cdot \mathbf{u})$ se zgornja enačba poenostavi v

$$
\begin{equation*}
\nabla^{2} P=\nabla \cdot \mathbf{b}-\nabla \cdot\left(\rho^{a} \nabla \cdot(\mathbf{v v})\right) \tag{2.18}
\end{equation*}
$$

Dobili smo Poissonovo tlačno enačbo. Robne pogoje dobimo preprosto z množenjem momente enačbe (2.9) z normalnim vektorjem na želenem robu

$$
\begin{gather*}
\left(\rho^{a} \frac{\partial \mathbf{v}}{\partial t}+\rho^{a} \nabla \cdot(\mathbf{v} \mathbf{v})\right) \hat{\mathbf{n}}=\left(-\nabla P+\nabla \cdot\left(\mu^{a} \nabla \mathbf{v}\right)+\mathbf{b}\right) \hat{\mathbf{n}}  \tag{2.19}\\
\frac{\partial P}{\partial n}=\left(\rho^{a} \nabla \cdot(\mathbf{v} \mathbf{v})+\nabla \cdot\left(\mu^{a} \nabla \mathbf{v}\right)+\mathbf{b}\right) \hat{\mathbf{n}} \tag{2.20}
\end{gather*}
$$

v naših obravnavah bomo zahtevali, da na robovih zrak miruje, kar dodatno poenostavi robne pogoje v

$$
\begin{equation*}
\frac{\partial P}{\partial n}=\left(\nabla \cdot\left(\mu^{a} \nabla \mathbf{v}\right)+\mathbf{b}\right) \hat{\mathbf{n}} \tag{2.21}
\end{equation*}
$$

kjer smo pri advektivnem členu upoštevali

$$
\begin{equation*}
\nabla \cdot(\mathbf{v v})=\mathbf{v}\binom{\nabla \cdot \mathbf{v}}{0}+(\mathbf{v} \nabla) \cdot \mathbf{v}=(\mathbf{v} \nabla) \cdot \mathbf{v}=0 \tag{2.22}
\end{equation*}
$$

Sedaj imamo iz stališča prenosnih enačb sistem zaprt. Potrebujemo samo še modele za generacijo toplotnega toka, sevanja in sončnega obsevanja, kar obdelamo v naslednjih dveh kratkih razdelkih.

### 2.1.3. Joulsko segrevanje

Pri električnem toku skozi prevodnik se zaradi interakcij nosilcev naboja s kristalno strukturo del energije pretvarja v toploto. Pojav se imenuje joulsko segrevanje in ga izrazimo kot

$$
\begin{equation*}
q_{j}=\frac{I^{2} R(T)}{S^{a l}}\left[\frac{\mathrm{~W}}{\mathrm{~m}^{3}}\right] \tag{2.23}
\end{equation*}
$$

kjer je $I[\mathrm{~A}]$ električni tok ter $R(T)[\Omega / \mathrm{m}]$ temperaturno odvisna upornost vrvi in $S^{a l}\left[\mathrm{~m}^{2}\right]$ presek vodnika. V prvem približku se joulsko segrevanje obravnava kot homogen toplotni vir. V natančnejših izračunih se lahko upošteva tudi geometrijo pletenice in popravke višjega reda. V CIGRE [5] obravnavo razširijo na več obročev vodnikov. Pogosto se v $q_{J}$ upošteva tudi magnetno segrevanje $q_{M}$ preko večje efektivne upornosti.

Temperaturno odvisnost upornosti zapišemo do kvadratnega člena kot

$$
\begin{equation*}
R(T)=R_{20}\left(1+\alpha_{20}\left(T-20^{\circ} \mathrm{C}\right)+\beta_{20}\left(T-20^{\circ} \mathrm{C}\right)^{2}\right)\left[\frac{\Omega}{\mathrm{m}}\right] \tag{2.24}
\end{equation*}
$$

kjer je $R_{20}$ upornost na dolžino pri $20{ }^{\circ} \mathrm{C}$ ter $\alpha_{20}\left[{ }^{\circ} \mathrm{C}^{-1}\right]$ in $\beta_{20}\left[{ }^{\circ} \mathrm{C}^{-2}\right]$ konstanti reda velikosti $10^{-3}$ in $10^{-7}$.

### 2.1.4. Sončno obsevanje

Prejeto moč na vrvi zaradi sevanja sonca zapišemo kot

$$
\begin{equation*}
q_{S}=\frac{\alpha_{S} I_{T}}{\pi}\left[\frac{\mathrm{~W}}{\mathrm{~m}^{2}}\right] \tag{2.25}
\end{equation*}
$$

kjer so $\alpha_{s}$ absorptivnost vodnika, $I_{T}\left[\mathrm{~W} / \mathrm{m}^{2}\right]$ intenziteta sončnega obsevanja. Vrv absorbira le normalno komponento vpadnega sevanja. V $I_{T}$ je vsebovana neposredna obsevanost vpadnih sončnih žarkov pravokotno na vodnik, difuzno sevanje ozračja ter odboja sevanja od tal oziroma objektov iz okolice. Intenziteto sončnega obsevanja $I_{T}$ lahko določimo preko postopka, opisanega v [54], ali preko direktne meritve sončne obsevanosti.

### 2.1.5. Sevanja površine vodnika

Skladno s Stefan-Boltzmannovim zakonom vsako črno telo seva in daljnovodna vrv seveda ni izjema. Vrv s temperaturo površine $T_{s}[\mathrm{~K}]$ v ozračju s temperaturo $T_{a}[\mathrm{~K}]$ seva z močjo

$$
\begin{equation*}
q_{R}=\sigma_{B} \epsilon\left(T_{s}^{4}-T_{a}^{4}\right)\left[\frac{\mathrm{W}}{\mathrm{~m}^{2}}\right] \tag{2.26}
\end{equation*}
$$

kjer je $\sigma_{B}=5,67\left[\mathrm{~W} / \mathrm{m}^{2} \mathrm{~K}^{4}\right]$ Stefanova konstanta in $\epsilon$ emisivnost vodnika. S časom atmosferski pojavi vrvi spreminjajo emisivnost, ki lahko doseže vrednosti do $0,8-0,9$. S $T_{s}$ in $T_{a}$ smo označili temperaturo površine vrvi in ambientalno temperature daleč od vrvi.

### 2.1.6. Snovne lastnosti zraka

DTR modeli, ki smo si jih ogledali v 1.2, upoštevajo temperaturno odvisnost snovnih lastnosti in tudi podajajo empirične relacije za izračun teh vrednosti. Nikjer pa ni zaslediti kako na rezultate vpliva vlažnost, kar je brez razmisleka težko oceniti. Zato si nekoliko podrobneje oglejmo ta pojav. V članku [55] Tsilingiris predstavi analizo snovnih lastnosti v odvisnosti od temperature in vlažnosti. Članek temelji na obravnavi zmesi suhega zraka in vodne pare. Posamezne komponente mešanice opiše preko empiričnih relacij in nato predstavi za nas zanimive snovne lastnosti, in sicer toplotno prevodnost, specifično toplotno kapacitivnost, viskoznost in gostoto kot funkcije tlaka, relativne vlažnosti in temperature in to ravno v nam zanimivem območju med 0 in $100^{\circ} \mathrm{C}$. Po nekaj iteracijah uspemo popraviti napake v članku in implementirati predstavljene relacije (Slika 9).

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-31.jpg?height=1352&width=1356&top_left_y=962&top_left_x=365)
Slika 9: Odvisnost snovnih lastnosti od temperature in relativne vlažnosti [55].

V naši obravnavi bo najnižja temperatura v območju pogojena z robno temperaturo, ali drugače, zrak se preko vrvi nikoli ne bo ohlajal, kar posledično pomeni, da na vrvi ni možna kondenzacija. Predpostavili bomo tudi, da je vrv vedno suha, tako ne bomo imeli niti izvorov niti ponorov vodne pare. Posledično lahko predpostavimo, da se mase vodne pare ohranja ter da je homogeno porazdeljena. Za nas je tako bolj uporabna zveza med snovnimi lastnostmi in absolutno vlago. Spomnimo se, da v zraku ne more biti poljubno mnogo pare, temveč nam parni tlak nasičenja $\left(e_{s}\right)$ pove, koliko vode lahko prejme zrak pri določeni temperaturi. Temperaturno odvisnost najlažje določimo preko integracije ClausiusClapeyronove enačbe [6]

$$
\begin{equation*}
e_{s}(T)=e_{s 0} e^{\left(\frac{L_{e}}{R_{v}}\left(\frac{1}{T_{0}}-\frac{1}{T}\right)\right)} \tag{2.27}
\end{equation*}
$$

kjer je $L_{e}=2,5 \mathrm{MJ} / \mathrm{kg}$ izparilna latentna toplota, $e_{s 0}=6,1 \mathrm{hPa}$ parni tlak nasičenja pri $0^{\circ} \mathrm{C}$ in $R_{v}=461 \mathrm{~J} / \mathrm{KgK}$ specifična plinska konstanta za vodo. Obstajajo tudi druge relacije, npr. Antoineova enačba [41] oziroma tabelirani podatki [56] in vpeljemo relacijo med relativno in absolutno vlago

$$
\begin{equation*}
r=\frac{e}{e_{s}(T)} \tag{2.28}
\end{equation*}
$$

ki nam pove, kakšno je razmerje parnega tlaka proti parnemu tlaku nasičenja in se izraža v odstotkih. Npr., $r=1$ pove, da zrak ne more več sprejemati vodne pare. Predpostavimo, da je največja temperatura zraka v naši obravnavi $T_{\text {max }}=40^{\circ} \mathrm{C}$, torej bo v našem območju razpon absolutno vlage $\rho^{v} \in[0,0,044]\left[\mathrm{kg} / \mathrm{m}^{3}\right]$, kjer smo gostoto izrazili s plinsko enačbo

$$
\begin{equation*}
\rho^{v}=\frac{e_{s}\left(T_{\max }\right)}{R_{v} T_{\max }} \tag{2.29}
\end{equation*}
$$

Ob dobljenih relacijah (Slika 10) narišimo še CIGRE in IEEE empirične relacije, ki smo jih zapisali v razdelku 1.2. Opazimo, da se snovne lastnosti znotraj temperaturnega intervala spremenijo za reda 30 \%, medtem ko znotraj intervala vlažnosti za okoli 5 \%. Iz relacij [55] lahko izpeljemo tudi odvisnost od nadmorske višine, saj so vse lastnosti odvisne od tlaka. Upoštevajmo, da se znak obnaša kot idealni plin [57] in zapišimo odvisnost tlaka od višine

$$
\begin{equation*}
p(h)=p_{0} e^{-h \frac{g M}{R T}} \tag{2.30}
\end{equation*}
$$

kjer je $p_{0}=101325 \mathrm{~Pa}$ tlak pri tleh. Odvisnost tudi primerjamo s CIGRE/IEEE (Slika 11).

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-33.jpg?height=1309&width=1312&top_left_y=268&top_left_x=386)
Slika 10: Odvisnost snovnih lastnosti od temperature in absolutne vlažnosti.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-33.jpg?height=631&width=1114&top_left_y=1701&top_left_x=491)
Slika 11: Odvisnost snovnih lastnosti od nadmorske višine in temperature pri absolutni vlažnosti 0,03 $\mathrm{kg} / \mathrm{m}^{3}$.

Lahko bi pokazali tudi odvisnosti specifične toplotne kapacitivnosti, toplotne prevodnosti in viskoznosti od tlaka oziroma višine, vendar so zanemarljive.

### 2.2 Implementacija rešitvenega postopka

### 2.2.1. Krajevna diskretizacija domene

Fizikalni model, ki bi ga radi rešili, smo opisali s sistemom nelinearnih parcialnih enačb v neregularni domeni, kar seveda ni analitično rešljivo. Zato bomo potrebovali numerično reševanje, in ker še ne vemo vse kakšne težave nas lahko doletijo, si pripravimo čim bolj splošno okolje. V prvem koraku si oglejmo krajevno diskretizacijo, kjer bomo uporabili, ravno zaradi splošnosti, lokalno brezmrežno metodo (ang. Meshless Local Strong Form Method (MLSM)) [58]. MLSM lahko razumemo tudi kot posplošeno metodo končnih diferenc, ki ni več omejena samo na lepe regularne domene in monomsko bazo, temveč lahko spreminjamo red aproksimacije in bazni prostor in dodajamo različne izboljšave. Čeprav podrobnosti metode morda nekoliko presegajo obseg študije, si vseeno, za lažje kasnejše razumevanje implementacije in morebitnih adaptacij numeričnih postopkov, oglejmo osnovni razmislek krajevne diskretizacije.
Jedro MLSM je lokalna aproksimacija obravnavanega polja, v našem primeru so to temperature, hitrost in tlak, in sicer preko prekrivajočih se lokalnih podpornih domen. Z drugimi besedami, v vsakem diskretizacijskem vozlišču poiščemo aproksimacijo našega polja na majhni lokalni podmnožici sosednjih $\boldsymbol{n}$ vozlišč, kar zapišemo kot

$$
\begin{equation*}
\hat{u}(\mathbf{p})=\sum_{i}^{m} \alpha_{i} b_{i}(\mathbf{p})=\mathbf{b}(\mathbf{p})^{\mathrm{T}} \boldsymbol{\alpha} \tag{2.31}
\end{equation*}
$$

pri čemer $m$ predstavlja število baznih funkcij, $\boldsymbol{\alpha}$ aproksimacijske koeficiente, $\mathbf{b}$ poljubne bazne funkcije in $\mathbf{p}\left(p_{x}, p_{y}\right)$ krajevni vektor. V posebnem primeru kadar je število baznih funkcij $m$ enako številu podpornih domen $n$, se določanje koeficientov $\boldsymbol{\alpha}$ poenostavi na reševanje sistema $n$ linearih enačb, ki ga dobimo tako, da enačbo (2.31) izrazimo za vsako podporno vozlišče posebej,

$$
\begin{equation*}
u\left(\mathbf{p}_{j}\right)=\mathbf{u}=\mathbf{b}(\mathbf{p})^{\mathrm{T}} \boldsymbol{\alpha} \tag{2.32}
\end{equation*}
$$

pri čemer so $\mathbf{p}_{j}$ položaji podpornih vozlišč, u pa tamkajšnje vrednosti obravnavanega polja. Zgornji sistem lahko zapišemo v matrični obliki, kot

$$
\begin{equation*}
\mathbf{B} \boldsymbol{\alpha}=\mathbf{u} \tag{2.33}
\end{equation*}
$$

pri čemer $\mathbf{B}$ predstavlja matriko koeficientov z elementi $B_{j i}=b_{i}\left(\mathbf{p}_{j}\right)$. Če je število podpornih vozlišč večje kot število baznih funkcij ( $n>m$ ), dobimo predoločen sistem, ki ga rešimo z minimizacijo naj-
manjših kvadratov razlik med aproksimacijo in vrednostmi polja v vozliščih (ang. Weighted Least Squares (WLS) approximation),

$$
\begin{equation*}
r^{2}=\sum_{j}^{n} W\left(\mathbf{p}_{j}\right)\left(u\left(\mathbf{p}_{j}\right)-\hat{u}\left(\mathbf{p}_{j}\right)\right)^{2}=(\mathbf{B} \boldsymbol{\alpha}-\mathbf{u})^{\mathrm{T}} \mathbf{W}(\mathbf{B} \boldsymbol{\alpha}-\mathbf{u}), \tag{2.34}
\end{equation*}
$$

pri čemer je $\mathbf{W}$ diagonalna matrika elementov $W_{j j}=W\left(\mathbf{p}_{j}\right) \mathrm{z}$

$$
\begin{equation*}
W(\mathbf{p})=\exp \left(-\left(\frac{\left\|\mathbf{p}_{0}-\mathbf{p}\right\|}{\sigma p_{\min }}\right)^{2}\right) \tag{2.35}
\end{equation*}
$$

$\sigma$ je utežni parameter, $\mathbf{p}_{0}$ središče podporne domene, $p_{\text {min }}$ pa razdalja do prvega vozlišča podporne domene. Za reševanje (2.34) obstajajo razni pristopi. Najbolj intuitiven in tudi najbolj računsko učinkovit je preprosto izračunati gradient za (2.34) glede na $\boldsymbol{\alpha}$, kar da

$$
\begin{equation*}
\mathbf{W B B}^{\mathrm{T}} \boldsymbol{\alpha}=\mathbf{W} \mathbf{B}^{\mathrm{T}} \mathbf{u} \tag{2.36}
\end{equation*}
$$

Problem gornjega pristopa je slaba pogojenost. Bolj stabilen, a dražji pristop je QR dekompozicija. Še bolj stabilna in seveda še dražja je SVD dekompozicija. Ne glede na način reševanja lahko problem zapišemo v matrični obliki kot

$$
\begin{equation*}
\boldsymbol{\alpha}=\left(\mathbf{W}^{0.5} \mathbf{B}\right)^{+} \mathbf{W}^{0.5} \mathbf{u} \tag{2.37}
\end{equation*}
$$

pri čemer je $\left(\mathbf{W}^{0.5} \mathbf{B}\right)^{+}$Moore-Penroseov psevdo inverz. Če $\boldsymbol{\alpha}$ na gornji način izrazimo v (2.32), dobimo

$$
\begin{equation*}
\hat{u}(\mathbf{p})=\mathbf{b}(\mathbf{p})^{\mathrm{T}}\left(\mathbf{W}^{0.5}(\mathbf{p}) \mathbf{B}\right)^{+} \mathbf{W}^{0.5}(\mathbf{p}) \mathbf{u}=\chi(\mathbf{p}) \mathbf{u} \tag{2.38}
\end{equation*}
$$

kjer smo vpeljali oblikovno funkcijo $\chi$. Zdaj lahko, kot je naš cilj, na našem polju uporabimo parcialni diferencialni operator,

$$
\begin{equation*}
L \hat{u}(\mathbf{p})=L \chi(\mathbf{p}) \mathbf{u} \tag{2.39}
\end{equation*}
$$

kjer $L$ predstavlja splošni diferencialni operator. V našem primeru obravnavamo Navier-Stokesovo in toplotno enačbo, torej potrebujemo oblikovne funkcije za Laplaceove operator in prve odvode, ki jih izračunamo vnaprej, kot

$$
\begin{align*}
& \boldsymbol{\chi}^{\partial x}(\mathbf{p})=\frac{\partial}{\partial x} \mathbf{b}(\mathbf{p})^{\mathrm{T}}\left(\mathbf{W}^{0.5}(\mathbf{p}) \mathbf{B}\right)^{+} \mathbf{W}^{0.5}  \tag{2.40}\\
& \boldsymbol{\chi}^{\partial y}(\mathbf{p})=\frac{\partial}{\partial y} \mathbf{b}(\mathbf{p})^{\mathrm{T}}\left(\mathbf{W}^{0.5}(\mathbf{p}) \mathbf{B}\right)^{+} \mathbf{W}^{0.5}  \tag{2.41}\\
& \boldsymbol{\chi}^{\nabla^{2}}(\mathbf{p})=\nabla^{2} \mathbf{b}(\mathbf{p})^{\mathrm{T}}\left(\mathbf{W}^{0.5}(\mathbf{p}) \mathbf{B}\right)^{+} \mathbf{W}^{0.5} \tag{2.42}
\end{align*}
$$

Predstavljena formulacija je praktična za implementacijo, saj se večina kompleksnih operacij (iskanje podpornih vozlišč in gradnja oblikovnih funkcij) izvaja samo, kadar se topologija vozlišč spremeni, kar se v našem primeru ne bo nikoli zgodilo.

### 2.2.2. Postavitev računskih točk

Naš problem je formuliran na neregularni mreži, zato moramo razmisliti tudi, kako bomo postavili računska vozlišča. Vemo, da potrebujemo za konstrukcijo stabilnih in zanesljivih oblikovnih funkcij dobro pogojeno matriko $\mathbf{B}$, za kar je predpogoj uravnotežena podporna domena.
Da bi dobili stabilno numerično rešitev, poskušamo minimizirati razdalje med točkami v podpornih domenah. Z drugimi besedami, rešujemo globalni optimizacijski problem, kjer je v vlogi cenovne funkcije skupna deformacija lokalnih podpornih domen, kar merimo kot

$$
\begin{equation*}
C=\frac{\min (\mathbf{d})}{\max (\mathbf{d})} \tag{2.43}
\end{equation*}
$$

kjer d predstavlja vektor razdalj vsakega od vozlišč do njegovega najbližjega soseda. Globalni minimum iščemo z lokalno iteracijo, kjer v vsaki iteraciji vsa vozlišča premaknemo glede na lokalni odvod utežne funkcije,

$$
\begin{equation*}
\mathbf{p} \leftarrow \mathbf{p}-\sigma_{k} \sum_{j=1}^{n} \nabla W\left(\mathbf{p}-\mathbf{p}_{j}\right) \tag{2.44}
\end{equation*}
$$

kjer je $\mathbf{p}_{j}$ pozicija $j$-tega podpornega vozlišča, in $\sigma_{k}$ relaksacijski parameter. Iterativni proces se začne s postavitvijo robnih vozlišč, kar nam predstavlja definicijo domene. Sledi pozicioniranje notranjih vozlišč v skladu z enačbo (2.44).

### 2.2.3. Časovna diskretizacija

Obravnavani model je časovno odvisen Cauchyjev problem, kar pomeni, da ob začetnem času $t_{0}$ poznamo vrednost količin $y_{0}$ (temperature, hitrosti in tlaka) ter diferencialne enačbe ((2.9), (2.10) in (2.11) ), ki opisujejo njihov časovni razvoj v obliki $\dot{y}(t)=f(t, y)$ kjer je $y$ neznana vektorska ali skalarna količina, $f$ pa podaja njen odvod. Količino y želimo simulirati do nekega izbranega časa $t_{\text {max }}$. Izračun $f$ je lahko zahtevna naloga, saj je pri parcialnih diferencialnih enačbah $f$ pogosto podan z enačbo eliptičnega tipa, kar pomeni, da moramo za izračun ene vrednosti odvoda rešiti eliptičen robni problem. Za primer toplotne enačbe (2.11) brez advekcije je $f(t, y)=-\lambda \nabla^{2} y$. Najenostavnejša in najpogosteje uporabljena metoda je eksplicitna Eulerjeva, kjer si izberemo časovni korak $\Delta t$, označimo $t_{i}=t_{0}+i \Delta t$ in $y_{i}=y\left(t_{i}\right)$ ter odvod po času diskretiziramo kot

$$
\begin{equation*}
\dot{y}\left(t_{i+1}\right)=\frac{y_{i+1}-y_{i}}{\Delta t} \tag{2.45}
\end{equation*}
$$

Tako lahko novo vrednost $y_{i+1}$ izrazimo kot

$$
\begin{equation*}
y_{i+1}=y_{i}+\Delta t \cdot f\left(t_{i}, y_{i}\right) \tag{2.46}
\end{equation*}
$$

pri čemer smo za izračun $f$ uporabili že znane vrednosti funkcije $y_{i}$ iz prejšnjega koraka. Prednost eksplicitne Eulerjeve metode je njena enostavnost in hitrost, saj za izračun enega časovnega koraka potrebujemo le en izračun $f$. Njena glavna problema sta nestabilnost in nenatančnost in je zato pogosto treba uporabiti majhne časovne korake.

Z uporabo naprednejših tehnik za reševanje diferencialnih enačb lahko obidemo problem nestabilnosti. Najbolj znan je razred metod, imenovanih Runge-Kutta, ki je posplošitev eksplicitne Eulerjeve metode. Te metode za izračun približka ob času $t_{i+1}$ uporabijo več vmesnih izračunov funkcije $f$ in s tem povečajo natančnost in stabilnost za ceno računskega časa. Najslavnejši predstavnik, RK4, naslednji približek $y_{i+1}$ izračuna s pomočjo štirih vmesnih korakov:

$$
\begin{align*}
& k_{1}=f\left(t_{i}, y_{i}\right) \\
& k_{2}=f\left(t_{i}+\Delta t / 2, y_{i}+\Delta t k_{1} / 2\right) \\
& k_{3}=f\left(t_{i}+\Delta t / 2, y_{i}+\Delta t k_{2} / 2\right)  \tag{2.47}\\
& k_{4}=f\left(t_{i}+\Delta t, y_{i}+\Delta t k_{3}\right) \\
& y_{i+1}=y_{i}+\Delta t / 6\left(k_{1}+2 k_{2}+2 k_{3}+k_{4}\right)
\end{align*}
$$

Zdravilo za visoko časovno zahtevnost RK metod so linearne veččlenske metode, ki namesto vmesnih izračunov funkcije uporabijo že izračunane vrednosti iz prejšnjih približkov in s tem nekaj prihranijo na računskem času, toda ohranjajo enak red natančnosti. Naslednji približek tako izračunamo kot linearno kombinacijo prejšnjih:

$$
\begin{equation*}
y_{i+1}=y_{i}+\Delta t \sum_{j=1}^{s} b_{j} y_{i-s+1} \tag{2.48}
\end{equation*}
$$

Najbolj znane so Adams-Bashforthove metode (AB), npr. metoda četrtega reda

$$
\begin{equation*}
y_{i+1}=y_{i}+\Delta t\left(\frac{55}{24} f\left(t_{i}, y_{i}\right)-\frac{59}{24} f\left(t_{i-1}, y_{i-1}\right)+\frac{37}{24} f\left(t_{i-2}, y_{i-2}\right)-\frac{3}{8} f\left(t_{i-3}, y_{i-3}\right)\right) \tag{2.49}
\end{equation*}
$$

Tudi te metode imajo svoje slabosti, saj pridobljeni računski čas plačajo z zmanjšano stabilnostjo postopka. Implementiramo tudi implicitno korakanje, ki je sicer precej dražje, saj je v vsakem časovnem koraku treba rešiti, sicer razpršen, sistem velikosti $N$ (število vseh vozlišč), vendar je pa tako korakanje
brezpogojno stabilno. Zavedati se moramo tudi, da je naš model nelinearen, tako v robnih pogojih kot v samih modelskih enačbah, kar nam dodatno omejuje časovni korak.

V grobem lahko modelsko dogajanje razdelimo na dva dela, in sicer na obtekanje zraka in segrevanje vrvi, torej na dogajanje v vrvi in dogajanje v okolici vrvi. Odzivni čas teh dveh pojavov je izrazito različen. Naravna konvekcija v okolici vrvi se tipično umiri v nekaj sekundah. Po drugi strani, ko po vrvi poženemo tok v brezvetrju le ta potrebuje nekaj ur, da se segreje na končno temperaturo. To so seveda zgolj okvirne ocene, vendar dovolj natančne, da pripravimo časovno integracijo v dveh korakih. V prvem koraku uporabimo fino časovno korakanje (reda ms), da pri dani temperaturi površine vrvi izračunamo temperaturno in hitrostno polje v zraku, ocenimo toplotni tok preko površine vrvi in s to oceno z veliko večjim časovnim korakom (reda 10 s) izračunamo naslednji časovni korak prenosa in generacije toplote znotraj vrvi.

### 2.2.4. Implementacija

Ena izmed glavnih prednosti predstavljene metodologije je splošna formulacija, kar lahko s pridom združimo z generičnim objektnim programiranjem, ki ga v polni meri omogoča jezik C++ od standarda 11 dalje. V program tako, sicer z veliko truda, implementiramo dejanske abstraktne matematične koncepte, kot so npr. linearni operator, bazna funkcija, MLS aproksimant in domena, kar nam omogoča, da rešitveni postopek zapišemo elegantno, po prevodu pa je koda taka, kot če bi uporabljali samo preproste programske sheme. Slika 13 prikazuje bločno shemo implementacije z označenimi glavnimi moduli, ki so med seboj ohlapno sklopljeni, kar omogoča hitro zamenjavo posameznih delov kode, recimo namesto monomske baze lahko z lahkoto uporabimo Gaussovo ali pa zamenjamo časovni integrator, .... Poleg same elegance taka koda omogoča učinkovito testiranje posameznih modulov, s čimer minimiziramo možnost napak, kar je pri razvojnih projektih izredno pomembno (Slika 12). Trenutno po vsaki spremembi kode izvedemo 242 testov za preverjanje baznih funkcij, grajenja domene, integratorjev, aproksimacije, podatkovnih tipov, reševanja sistema, operatorjev in, navsezadnje, zaključenih primerov, kot je na primer reševanje Poissonove enačbe.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-39.jpg?height=676&width=1559&top_left_y=242&top_left_x=283)
Slika 12: Izsek izpisa testov.

Za ilustracijo implementacije si oglejmo najvišji nivo rešitvenega postopka za de Vahl Davisov problem. Slednjega bomo v nadaljevanju rešili kot prvi testni primer, z eksplicitnim Eulerjevim korakanjem in ACM tlačno sklopitvijo. Najvišji nivo rešitvenega postopka je časovna zanka, pri kateri se v vsakem časovnem koraku za vsako obravnavano PDE izvede ena prostorska zanka preko vseh računskih točk. Poleg časovnega korakanja imamo zaradi tlačno-hitrostne sklopitve dodatno iteracijo med hitrostnim in tlačnim poljem. Na najnižjem nivoju, obravnavi posamezne točke, moramo za vsak diferencialni operator izvesti konvolucijo oblikovnih funkcij in vrednosti obravnavnega polja v podpornih točkah, kjer so polja lahko skalarna ali vektorska. Oglejmo si primer izračuna nove vrednosti tlaka v eni točki:

$$
\begin{equation*}
P_{i}=P_{i 0}-\varsigma \Delta t \underbrace{\left(\sum_{i=1}^{n} \boldsymbol{\chi}_{i}^{\partial x} \mathbf{v}_{i x}+\sum_{i=1}^{n} \boldsymbol{\chi}_{i}^{\partial y} \mathbf{v}_{i y}\right)}_{\nabla \cdot \mathbf{v}}+\varsigma \Delta t^{2} \underbrace{\sum_{i=1}^{n} \boldsymbol{\chi}_{i}^{\nabla^{2} \mathrm{~T}} \mathbf{P}_{i}}_{\nabla^{2} P}, \tag{2.50}
\end{equation*}
$$

Indeks $i$ nam pove, za katero točko gre, $\mathbf{v}_{i x}, \mathbf{v}_{i y}$ in $\mathbf{P}_{i}$ pa vrednosti hitrostnega oziroma tlačnega polja v podpornih točkah točke $i$. Podobno diskretiziramo tudi ostale enačbe. Bločna shema (Slika 14) prikazuje potek izračuna. Slika 15 prikazuje izsek dejanske C++ kode, ki izvede gornji algoritem.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-40.jpg?height=1673&width=1525&top_left_y=244&top_left_x=302)
Slika 13: Bločna shema implementacije.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-41.jpg?height=932&width=1297&top_left_y=242&top_left_x=399)
Slika 14: Bločna shema rešitvenega postopka.

```
v2[boundary] = vec_t{0.0, 0.0};
T2[left] = 0.T_cold;
T2[right] = 0.T_hot;
//Time stepping
for (int step = 0; step <= 0.t steps; ++step) {
    for (int i_count = 1; i_count < _MAX_ITER_; ++i_count) {
        // Navier Stokes
        for (auto c : interior) {
            v2[c] = v1[c] + 0.dt * (-1 / 0.rho * op.grad(P1, c)
                + O.mu / O.rho * op.lap(v1, c)
                - op.grad(v1, c) * vl[c]
                + O.g * (1 - O.beta * (T1[c] - O.T_ref)));
        }
        //Speed of sound
        Range<scal_t> norm = v2.map([](const vec_t& p) { return p.norm(); });
        scal_t C = O.dl * std::max(*std::max_element(norm.begin(), norm.end()), O.v_ref);
        // Mass continuity
        Range<scal_t> div_v;
        for (auto c:all) {
            div_v[c] = op.div(v2, c);
            P2[c] = P1[c] - c * c * O.dt * O.rho * div_v[c] +
                O.dl2 * C * C * O.dt * O.dt * op.lap(Pl, c);
        }
        P1.swap(P2) ;
    }
    //heat transport
    for (auto c : interior) {
        T2[c] = T1[c] + 0.dt * 0.lam / 0.rho / 0.c_p * op.lap(T1, c) -
                O.dt * vl[c].transpose() * op.grad(T1, c);
    }
    for (auto c : top) T2[c] = op.neumann(T2, c, vec_t{0, -1}, 0.0);
    for (auto c : bottom) T2[c] = op.neumann(T2, c, vec_t{0, 1}, 0.0);
}
```

Slika 15: Izsek kode za izračun de Vahl Davisovega problema z eksplicitno ACM metodo.

Več podrobnosti o sami implementaciji bi, žal, močno preseglo obseg študije, jih je pa mogoče najti na [59]. Uporabljeno knjižnico razvijamo na oddelku E6 Inštituta "Jožef Stefan" pod MIT licenco. Sama knjižnica uporablja še knjižnici Eigen (MLP2 licenca) in ANN (licenca GLPL). Vse omenjene licence so odprtokodne.

### 2.3 Verifikacija simulatorja na standardnih testih

### 2.3.1. de Vahl Davisov test

V prvih korakih preverimo implementacijo modela, in sicer preko primerjalnih testov. Dobršen del modela predstavlja sklopljen sistem prenosa toplote ter ohranitve gibalne količine in mase. Ta sklop lahko preverimo preko dobro znanega de Vahl Davisovega testa za naravno konvekcijo [19], saj v literaturi najdemo mnogo numeričnih rešitev [24, 60-65], s katerimi lahko primerjamo naše izračune.

Test obravnava prenos toplote in gibanje kapljevine v zaprti kotanji, kjer sta horizontalni steni toplotno izolirani, medtem ko vertikalni nastavimo na različni temperaturi, in sicer toplo stran na $T_{H}$ ter hladno na $T_{C}$. Obravnavamo viskozno tekočino v neprepustni ogradi, torej predpostavimo, da tekočina ob njej ne drsi in ne teče skozi steno (Slika 16). Robni pogoji se tako glasijo

$$
\begin{gather*}
\tilde{\mathbf{v}}\left(\tilde{\mathbf{p}}_{\Gamma}, \tilde{t}\right)=0,  \tag{2.51}\\
\tilde{T}\left(\tilde{p}_{x}=0, \tilde{t}\right)=1,  \tag{2.52}\\
\tilde{T}\left(\tilde{p}_{x}=1, \tilde{t}\right)=0,  \tag{2.53}\\
\frac{\partial}{\partial \tilde{p}_{y}} \tilde{T}\left(\tilde{p}_{y}=0, \tilde{t}\right)=\frac{\partial}{\partial \tilde{p}_{y}} \tilde{T}\left(\tilde{p}_{y}=1, \tilde{t}\right)=0, \tag{2.54}
\end{gather*}
$$

kjer smo z $\Gamma$ označili rob domene. Začetna pogoja zapišemo kot

$$
\begin{gather*}
\tilde{\mathbf{v}}\left(\tilde{\mathbf{p}}_{\Omega}, \tilde{t}=0\right)=0,  \tag{2.55}\\
\tilde{T}\left(\tilde{\mathbf{p}}_{\Omega}, \tilde{t}=0\right)=0.5, \tag{2.56}
\end{gather*}
$$

kjer z $\Omega$ označimo notranjost domene. Uporabili smo brezdimenzijske količine definirane kot

$$
\begin{array}{cc}
\tilde{p}_{x}=\frac{p_{x}}{\Omega_{W}} & \tilde{p}_{y}=\frac{p_{y}}{\Omega_{H}} \\
\tilde{v}_{x}=\frac{v_{x} \Omega_{W} \rho c_{p}}{\lambda} & \tilde{v}_{y}=\frac{v_{y} \Omega_{H} \rho c_{p}}{\lambda} \\
\tilde{T}=\frac{T-T_{C}}{T_{H}-T_{C}} & \tag{2.59}
\end{array}
$$

$$
\begin{equation*}
\tilde{t}=\frac{\lambda}{\rho c_{p} \Omega_{H}^{2}} t \tag{2.60}
\end{equation*}
$$

Problem karakterizirata dve brezdimenzijski števili; Rayleighjevo ( Ra ) in Prandtlovo število ( Pr ), definirani kot

$$
\begin{gather*}
\mathrm{Ra}=\frac{|\mathbf{g}| \beta_{T}\left(T_{H}-T_{C}\right) \rho^{2} c_{p}}{\lambda \mu}  \tag{2.61}\\
\operatorname{Pr}=\frac{\mu c_{p}}{\lambda} \tag{2.62}
\end{gather*}
$$

kjer je razmerje med Prandtlovim in Rayleighjevim številom poznano tudi pod imenom Grashofovo število,

$$
\begin{gather*}
\mathrm{Gr}=\frac{\mathrm{Ra}_{T}}{\mathrm{Pr}} .  \tag{2.63}\\
\begin{array}{c}
\text { zgornja stran } \\
\frac{\partial T}{\partial \vec{n}}=0 \\
\vec{v}=0 \\
\vec{v} \vec{v} \vec{v}=0 \\
T_{H} \\
\vec{v}=0 \\
\overrightarrow{\partial \vec{n}}=0 \quad \vec{v}=0 \\
\text { spodnja stran }
\end{array}
\end{gather*}
$$

Slika 16: Shema de Vahl Davisovega primera.

Originalni de Vahl Davisov članek obravnava gibanje zraka ( $\operatorname{Pr}=0.71$ ) pri pogojih do Rayleighevega števila $10^{6}$, vendar lahko v novejših publikacijah najdemo rešitve bolj agresivnih primerov, in sicer tja do $\mathrm{Ra}=10^{8}$, ki pa je v grobem tudi meja laminarnega režima, kot sta pokazala Lage and Bejan [66]. Podobno kot Lage in Bejan, ki pokažeta, da se laminaren režim konča v grobem pri $\mathrm{Gr}<10^{9}$, v [67, $68]$ avtorji pokažejo, da problem nima več stacionarne rešitve pri $\mathrm{Ra}=2 \cdot 10^{8}$. V nadaljevanju tako preverimo naš rešitveni postopek do $\mathrm{Ra}=10^{8}$, kjer rešitve primerjamo z [19] (a), [62] (b), [24] (c) [65] (d) in [25] (e).

Najprej si oglejmo temperaturno polje in magnitudo hitrostnega polja v stacionarnem stanju za zadnji primer (Slika 17). Iz slik polj lahko hitro opazimo, da je obnašanje po pričakovanjih. Na topli strani kotanje je zrak lažji in zato sili navzgor in obratno na hladni strani, kar privede do kroženja zraka. Slike
polj nam sicer predstavijo kvalitativno obnašanje, vendar žal povedo le malo o kvaliteti rešitve. Ta podatek lažje razberemo iz konvergenčne analize (Slika 18), kjer si ogledamo povprečno Nusseltovo število na ogrevanih robovih in največjo vertikalno hitrost v horizontalnem preseku. Te podatke najdemo tudi v objavljenih člankih, tako da slike opremimo s primerjalnimi vrednostmi. Opozoriti velja, da za referenčne podatke ne poznamo cele konvergenčne slike, temveč le vrednost za vsak primer, kar je predstavljeno s konstantno vrednostjo na konvergenčnih slikah. Rezultatov se razveselimo, saj naša rešitev lepo konvergira k referenčnim vrednostim, kjer se seveda zavedamo razhajanja danih podatkov.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-44.jpg?height=714&width=1439&top_left_y=726&top_left_x=343)
Slika 17: Temperaturno polje (levo) in magnituda hitrostnega polja (desno) v stacionarnem stanju za primer $\mathrm{Ra}=10^{8}$.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-44.jpg?height=731&width=1384&top_left_y=1609&top_left_x=350)
Slika 18: Odvisnost povprečnega Nusseltovega števila (levo) in maksimalne vertikalne hitrosti (desno) od števila računskih vozlišč za $\mathrm{Ra}=10^{8}$.

Časovni korak $\Delta t=10^{-5}$ je mejni, do koder Eulerjeva metoda še konvergira. Pri RK4 pa lahko korak povečamo do 8 -krat in še vedno dobimo smiselno rešitev. Če uporabimo korak $\Delta t=8 \cdot 10^{-5}$, dosežemo računski čas $\sim 283$ s in prehitimo Eulerjevo metodo. Vse izračune smo izvedli z MLSM z 9 Gaussovimi funkcijami na podpornih domenah velikosti 9, torej z interpolacijo.

### 2.3.2. Naravna konvekcija okoli cilindra

Med pregledom literature smo naleteli na objavljene izračune problema naravne konvekcije okoli segretega valja [27], ki je že kar spodoben približek našega problema (Slika 19). Primer je podoben de Vahl Davisovemu testu, le da to pot domena vsebuje ekscentrično postavljen krog premera $40 \%$ širine celotne domene. Primerjajmo izračun pri $\operatorname{Pr}=10$ in $\mathrm{Ra}=1 \mathrm{e} 6$, ki je že precej intenziven primer. Poleg same intenzitete je primer, iz numeričnega vidika, precej težji, kot bodo naše simulacije, in sicer zaradi relativno velikega razmerja med velikostjo valja in celotne zaprte domene. Pri naših simulacijah pričakujemo bolj umrijeno gibanje, tako da je iz stališča simulacije mehanike fluida ta test primeren. Torej, preverimo našo MLSM rešitev še na tem primeru. Ponovno si najprej oglejmo temperaturno in hitrostno polje (Slika 20).

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-45.jpg?height=586&width=601&top_left_y=1228&top_left_x=762)
Slika 19: Shema izračuna naravne konvekcije okoli segretega valja.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-46.jpg?height=680&width=1541&top_left_y=292&top_left_x=296)
Slika 20: Temperaturno polje (levo) in magnituda hitrostnega polja (desno) v stacionarnem stanju za primer obtekanja toplega cilindra pri $\mathrm{Ra}=10^{6}, \operatorname{Pr}=10$.

V naslednjem koraku primerjamo izoterme izračunane z MLSM (rdeče krivulje) in sliko 19 iz [27] (slika v ozadju). V članku lahko najdemo tudi vrendnosti Nusseltovege števila na hladni steni, kar tudi primerjamo (Slika 21). Primerjave nam dodatno utrdijo zaupanje v našo rešitev.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-46.jpg?height=706&width=1395&top_left_y=1368&top_left_x=345)
Slika 21: Primerjava izoterm (levo) in Nusseltovega števila na hladni steni (desno).

### 2.3.3. Prenos toplote iz ogrevane vrvi na okolico brez naravne konvekcije

V naslednjem koraku preverim pravilno delovanje sklopljenih domen. Rešimo najprej primer z znano analitično rešitvijo, in sicer ogrevan cilinder znotraj večjega cilindra, ki je v termostatu z okolico. Zapišimo problem eksaktno

$$
\begin{array}{ll}
\lambda_{1} \nabla^{2} T_{1}(r) & =q_{0} ; 0 \leq r<R_{1}, \\
T_{1}\left(R_{2}\right) & =T_{2}\left(R_{1}\right), \\
\left.\lambda_{1} \frac{\partial}{\partial n} T_{1}\right|_{R_{1}} & =-\left.\lambda_{2} \frac{\partial}{\partial n} T_{2}\right|_{R_{2}},  \tag{2.64}\\
\lambda_{2} \nabla^{2} T_{2}(r) & =0 ; R_{1} \leq r<R_{2}, \\
T_{2}\left(R_{2}\right) & =0,
\end{array}
$$

kjer smo z indeksom 1 označili notranji cilinder in z indeksom 2 zuanji cilinder. Analitično rešitev zapišemo kot

$$
T(r)=\left\{\begin{array}{cl}
\frac{q_{0}}{4 \lambda_{1} \lambda_{2}}\left(\lambda_{2}\left(R_{1}^{2}-r^{2}\right)+2 \lambda_{1} R_{1}^{2} \log \left(\frac{R_{2}}{R_{1}}\right)\right) & ; 0 \leq r<R_{1}  \tag{2.65}\\
R_{1} \frac{q_{0} R_{1}^{2}}{2 \lambda_{2}} \log \left(\frac{R_{2}}{r}\right) & ; R_{1} \leq r \leq R_{2}
\end{array} .\right.
$$

Rešitev našega simulacijskega okolja zlahka nastavimo na iste pogoje, in sicer tako, da izberemo enake snovne lastnosti za prevodnik in nosilno vrv ter prepovemo gibanje zraka in sevanje (Slika 22). Izračune predstavimo preko primerjave horizontalnega preseka analitične in MLSM rešitve ter izoterm (Slika 23). MLSM rešitev se popolnoma ujema z analitično. Na sliki z izotermami rešitve je mogoče videti tudi postavitev računskih točk, kjer smo distribucijo zgostili na meji med notranjim cilindrom in okolico. To bomo uporabili tudi kasneje pri izračunih pri realnih pogojih.

```
<params>
    <mls m="3" n="9" sigmaW="1.00" sigmaB="400" />
    <num dt="1" dl="0.75" dl2="0" v_ref ="0.01" max_div="150"/>
    <const time="3" g_0 = "0" sigma="5.670e-8"/>
    <domain d_ste="0.05" d_alu="0.05" d_air="0.05" strands="0" fill_proximity="0.85"/>
    <relax initial_heat="1.5" final_heat="0.5" iter_num="50" projection="1" proj_eps="1"/>
    <air r="2" rho="1" mu="1" lam="1" c_p="1" beta="1" T_ref="0"/>
    <alu r_c="0.00" r_0="1" n_s="2" N_s="1" rho="1" lam="5" c_p="1" R="1" alpha="0" sef="1" eps="0.1"/>
    <ste r="0.5" r_0="1" N_s="1" rho="1" lam="5" c_p="1" R="1" alpha="0"/>
    <case current="5" T_amb="0.0"/>
    <io out_num="20" on_screen_num="1" load_from_file="" load_from_step="50"/>
    <sys num_threads="4"/>
</params>
```

Slika 22: Točna nastavitev testnega primera.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-48.jpg?height=704&width=1398&top_left_y=315&top_left_x=343)
Slika 23: Primerjava analitične in MLSM rešitve prenosa toplote iz ogrevane vrvi (levo) in prikaz izoterm (desno)

V zadnjem testu pred bolj resnimi izračuni bomo preverili pravilnost implementacije konstitutivnih relacij in snovnih lastnosti. Spomnimo se, da smo se v študiji »Analiza preprečevanja nastajanja žleda z obratovalnimi ukrepi« [69] ukvarjali z enodimenzionalnim termičnim modelom vrvi. Modela lahko preko nastavitev prisilimo v podobno delovanje, in sicer ponovno v obeh modelih prepovemo konvekcijo in v MLSM modelu nastavimo toploto prevodnost zraka na nič. Rešitev doseže stacionarno stanje, ko je generacija toplote zaradi joulskih izgub enaka sevanju površine. Oglejmo si termično sliko vrvi AlFe490/65 skozi katero teče 400 A toka pri zunanji temperaturi $0^{\circ} \mathrm{C}$ (Slika 24). Primerjava obeh izračunov poveča zaupanje v delovanje našega simulatorja.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-48.jpg?height=613&width=1235&top_left_y=1729&top_left_x=431)
Slika 24: Primerjava MLSM in DTR izračunov

## 3. Vzpostavitev eksperimentalnega poligona in izvedba preskusov

### 3.1 Priprava eksperimentalnega okolja za merjenje temperature vrvi v kontroliranih pogojih

### 3.1.1. Zgradba merilnega eksperimenta

Z merilnim eksperimentom želimo posnemati daljnovod med obratovanjem v brezvetrju. V kontroliranih laboratorijskih pogojih je potrebno vzpostaviti merilni sistem, s katerim je možno izvajati meritve v brezvetrju. Zgradbo merilnega eksperimenta lahko v grobem razdelimo na pet podsklopov, kot to prikazuje Slika 25:

- Napajalni močnostni del namenjen napajanju tokovne zanke
- DTR merilni del namenjen merjenju toka v vodniku
- DTR_0.6 merilni del namenjen merjenju temperature vodnika in okoljskih parametrov
- DTR regulator namenjen regulaciji toka v vodniku, vzdrževanju temperature jedra vodnika in regulacije toka po profilu
- Informacijski sistem namenjen shranjevanju vseh merjenih veličin, reguliranih veličin in izmerjenih podatkov med podsklopi

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-49.jpg?height=852&width=1245&top_left_y=1443&top_left_x=446)
Slika 25: Shematski prikaz eksperimenta za merjenje temperature vodnika v kontroliranih pogojih.

Konfiguracija merilnega eksperimenta je zasnovana na osnovi dveh tipov vodnikov, ki se uporabljajo v slovenskem prenosnem omrežju. Za 400 kV in 220 kV napetostni nivo prenosnega omrežja je bil izbran vodnik AlFe-490/65, ki ima določen statični termični tok 960 A pri temperaturi jedra $80^{\circ} \mathrm{C}$, za 110 kV napetostni nivo pa vodnik AlFe-240/40 s statičnim termičnim tokom 645 A pri isti temperaturi jedra vodnika. Merilni del eksperimenta prikazujeta spodnji sliki (Slika 26 in Slika 27) v stranskem in tlorisnem pogledu.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-50.jpg?height=650&width=1575&top_left_y=655&top_left_x=278)
Slika 26: Stranski pogled merilnega dela eksperimenta v VN laboratoriju.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-50.jpg?height=905&width=1565&top_left_y=1394&top_left_x=283)
Slika 27: Tloris merilnega dela eksperimenta v VN laboratoriju.

### 3.1.2. Namestitev TC senzorjev temperature

Validacija fizikalnega modela naravne konvekcije zahteva kvalitetne meritve temperature na površini in jedru vodnika. Predvsem je pomembno, da se meritve izvajajo neposredno na površini vodnika in pri tem ne povzročajo dodatnih motenj v gibanju zraka, ki bi lahko vplivale na obtekanje zraka okrog vodnika. Aluminijasta pletenica vodnika je sestavljena iz več posameznih tankih žic, zato morajo biti senzorji temperature izredno majhnih dimenzij, da se jih lahko ustrezno namesti na posamezno žico. Kot primeren senzor temperature bil izbran termočlen (TC) velikosti $0,2 \mathrm{~mm}$, ki ga je možno namestiti tik pod površino posamezne žice vodnika.

Par TC senzorjev temperature je postavljenih tudi v jedru vodnika. Senzorji temperature so praviloma z žicami povezani do merilnika temperature, kjer se izvaja vzorčenje in pretvarjanje merjenih veličin. Žice bi lahko, podobno kot senzorji temperature, povzročale dodatne turbulence zraka okrog vodnika, kar je nezaželeno. Da se temu izognemo, je v merilnem delu eksperimenta vsak posamezni TC senzor temperature postavljen v svojem merilnem območju, kot to prikazuje Slika 28. Medsebojni vpliv, ki ga povzročajo povezave med senzorjem in merilnikom temperature, je tako minimalen.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-51.jpg?height=687&width=1146&top_left_y=1241&top_left_x=485)
Slika 28: Ustrezna razporeditev TC senzorjev vzdolž vodnika z minimalnim medsebojnim vplivom delovanja.

### 3.1.3. Zajem, digitalna pretvorba in obdelava meritev

Merilnik temperature, ki temelji na principu termočlena, je načeloma sestavljen iz TC senzorja in merilnega pretvornika. V pretvorniku se izvaja analogno digitalna pretvorba napetosti termočlena, kompenzacija temperature hladnega spoja termočlena in linearizacija signala. TC senzorji so na površini vodnika nameščeni kontaktno, da zagotavljajo najboljšo toplotno prevodnost, vendar hkrati tudi elek-
trično prevodnost med senzorji in vodnikom. Vodnik se v tokovni zanki eksperimenta napaja prek tokovnega transformatorja z izmeničnim tokom. Zaradi tega je električni potencial na vodniku, in posledično na TC senzorjih, izmenične sinusne oblike s frekvenco 50 Hz in vsemi harmoniki, ki pri tem nastanejo. Električni potencial na vodniku je tudi odvisen od toka, ki teče skozi vodnik. Ker je merilni pretvornik temperature na stalnem določenem električnem potencialu, TC senzorji pa so na plavajočem električnem potencialu, se pri pretvorbi uporablja izolacijsko SPI in I ${ }^{2} \mathrm{C}$ vodilo (Slika 29), ki izniči morebiten vliv razlike električnih potencialov.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-52.jpg?height=706&width=1155&top_left_y=732&top_left_x=489)
Slika 29: Zajem, digitalna pretvorba in digitalna obdelava temperature vodnika ter temperature in relativne vlažnosti zraka.

Merilni eksperiment je izdelan na modularni konstrukciji dimenzij $6 \mathrm{~m} \times 1,5 \mathrm{~m} \times 2 \mathrm{~m}$. Merilna višina je postavljena na $1,5 \mathrm{~m}$. Na eksperimentu sta hkrati postavljeni dve tokovni zanki sestavljeni iz vodnikov AlFe490/65 in AlFe240/40 (Slika 30).

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-53.jpg?height=742&width=1283&top_left_y=279&top_left_x=378)
Slika 30: Postavitev merilnega eksperimenta v visokonapetostnem laboratoriju EIMV.

Tokovni zanki merilnega eksperimenta si delita povratni krak, ki je sestavljen iz dvojnega vodnika AlFe490/65. Temperatura povratnega kraka tokovne zanke je zaradi podvojenega preseka vodnika nižja saj se tok v zanki porazdeli. Povratni krak tokovnih zank je postavljen na sredini merilnega eksperimenta (Slika 31).

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-53.jpg?height=897&width=1000&top_left_y=1435&top_left_x=661)
Slika 31: Namestitev vodnikov tokovne zanke merilnega eksperimenta.

Priključitev posameznik vodnikov v zanke je izvedeno s pomočjo ustreznih nizko izgubnih tokovnih priključnih sponk posebej zasnovanih za merilni eksperiment (Slika 32)

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-54.jpg?height=721&width=959&top_left_y=412&top_left_x=584)
Slika 32: Priklop vodnikov v tokovno zanko preko tokovnih priključnih sponk.

Tokovni zanki merilnega eksperimenta sta zaključeni s pomočjo bakrenega mostiča dimezij 100 mm x 10 mm (Slika 33). S tem dosežemo majhne izgube in fleksibilnost pri montaži ni izvajanju meritev.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-54.jpg?height=738&width=1529&top_left_y=1396&top_left_x=298)
Slika 33: Kratkostičenje tokovnih zank s pomočjo bakrenega mostiča dimenzij $100 \mathrm{~mm} \times 10 \mathrm{~mm}$ (levo) in izvedba izolacije tokovne zanke na merilnem eksperimentu (desno).

Nosilni elementi tokovnih zank so postavljeni na ustreznih visokonapetostnih izolatorjih, ki zagotavljajo galvansko ločitev merilnega tokovnega tokokroga od merilnega eksperimenta. Končni priključki
tokovnih zank so zaključeni s posebnimi modularnimi bakrenimi nosilci za lažji priklop na napajalni vir (Slika 34 levo). Potrebno je izpostavit, da je v merilnem eksperimentu potrebno zagotoviti minimalno vplivanje napajalnega vira na merjenec. Prehod povratnega kraka tokovnih zank je še posebej izdelan z namenov zmanjšanje toplotnega vliva napajalnega vira na merjenec (Slika 34 desno).

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-55.jpg?height=740&width=1529&top_left_y=597&top_left_x=298)
Slika 34: Zaključni priklop tokovnih zank na napajalni vir (levo) in prehod nevtralnega kraka tokovne zanke na napajalni vir (desno).

Merjenje robnih vremenskih pogojev merilnega eksperimenta je izvedeno z nosilnimi elementi merilne opreme, ki je sestavljena iz štirih nosilcev (Slika 35). Ker so pri fizikalnem modelu obtekanja okrog daljnovodne vrvi robni pogoji pomembni, so nosilni elementi za merjenje robnih pogojev modularni, da se lahko zagotovi ustrezna merilna natančnost.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-56.jpg?height=1345&width=1017&top_left_y=247&top_left_x=554)
Slika 35: Nosilni elementi merilne opreme robnih pogojev merilnega eksperimenta.

### 3.2 Priprava eksperimentalnega okolja za opazovanje gibanja zraka ob segrevanju vodnika

Relativno enostaven prikaz gibanja zračnih tokov v okolici segretega vodnika nam omogoča fotografska tehnika imenovana schlieren fotografija, ki temelji na odvisnosti lomnega količnika zraka od temperature. Svetloba se namreč lomi drugače v gostejšem (hladnejšem) zraku, kot v redkejšem (toplejšem) zraku. To lastnost lahko izkoristimo za prikaz zračnih tokov. Poligon za izdelavo schlieren fotografij je sestavljen iz točkastega svetlobnega vira, konkavnega zrcala in fotoaparata s teleobjektivom. Za opazovanje loma svetlobe, potrebujemo točkast izvor kolimilirane svetlobe (svetlobe z vzporednimi žarki) pred ali za predmetom, ki ga opazujemo. To dosežemo tako, da pred konkavno zrcalo, na dvakratno dolžino goriščne razdalje zrcala (2f), postavimo točkast svetlobni vir.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-57.jpg?height=800&width=1415&top_left_y=262&top_left_x=354)
Slika 36: Nosilni elementi merilne opreme robnih pogojev merilnega eksperimenta

Ob izvor svetlobe postavimo fotoaparat s teleobjektivom. Opazovani predmet postavimo neposredno pred zrcalo, ki deluje kot vir kolimilirane svetlobe. Pred fotoaparat postavimo še barvni filter, ki lomljeno svetlobo obarva. Na ta način na sliki vidimo zračni tok okoli opazovanega predmeta. Na spodnji sliki (Slika 37) je predstavljen testni poligon, postavljen z namenom potrditve koncepta izdelave Schlieren fotografij in nastavljanja parametrov za kasnejšo vgradnjo na sam merilni poligon, s čimer bomo lahko kvalitativno ocenili veljavnost modelskih predpostavk in ali res merimo samo naravno konvekcijo zaradi segrevanja vrvi ali imamo prisotno tudi kakšno drugo gibanje zraka.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-57.jpg?height=600&width=1582&top_left_y=1622&top_left_x=270)
Slika 37: Poskusna postavitev za Schlieren fotografijo (levo) in segret objekt fotografiran na testnem poligonu (desno).

### 3.3 Izvedba meritev za validacijo numerična okolja

Po dokončni postavitvi merilnega eksponata sledi priklop merilnikov temperature. Z namenom minimaliziranja toplotnih vplivov transformatorja in ostalih elementov v okolici merilnega eksponata je merilno območje vmeščeno v sredino merilnega eksponata.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-58.jpg?height=538&width=1571&top_left_y=595&top_left_x=279)
Slika 38: Shema merilnega območja testnega poligona

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-58.jpg?height=899&width=1290&top_left_y=1226&top_left_x=416)
Slika 39: Prikaz merilnega območja testnega poligona

Za merjenje temperature sta bili uporabljeni dve skupine merilnikov temperature. Prva skupina merilnikov temperature je bila nameščena v sredini in na površini vodnika na različnih pozicijah. Ti merilniki so na spodnjih slikah označeni s TC. Druga skupina merilnikov je namenjena merjenju ambientalne
temperature. Merilniki so bili razporejeni v okolici vodnika na različnih pozicijah in oddaljenosti od vodnika. Na spodnjih slikah so označeni z oznako CJ.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-59.jpg?height=647&width=944&top_left_y=391&top_left_x=588)
Slika 40: Merilnik ambientalne temperature CJ (levo) in merilnik temperature površine vodnika TC (desno).

Shematski prikaz postavitve merilnikov temperature prikazujejo spodnje slike, kjer so z rdečo barvo označeni merilniki temperature, ki so nameščeni na površini vodnika, z vijolično barvo so obarvani merilniki temperature, ki so nameščeni v sredini vodnika, z modro in zeleno barvo pa merilniki temperature, ki so bili namenjeni merjenju temperature v okolici vodnika.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-59.jpg?height=695&width=1211&top_left_y=1460&top_left_x=455)
Slika 41: Postavitev merilnikov temperature na eksperimentu.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-60.jpg?height=849&width=1212&top_left_y=247&top_left_x=451)
Slika 42: Postavitev merilnikov temperature: pogled s sprednje strani vodnika.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-60.jpg?height=845&width=1301&top_left_y=1282&top_left_x=412)
Slika 43: Postavitev merilnikov temperature: pogled s sprednje strani vodnika.

Merilniki temperature vsake skupine so preko podatkovnega vodila povezani z osebnim računalnikom, kjer se podatki v realnem času prikazujejo ter shranjujejo.

## 4. Analiza rezultatov

### 4.1 Analiza numeričnih izračunov

V razdelku 2 smo pripravili fizikalni model in vsa potrebna numerična orodja za njegovo reševanje. Sedaj se osredotočimo na analize izračunov dogajanja okoli daljnovodne vrvi. Za ogrevanje si oglejmo ustaljeno stanje pri dani temperaturni razliki med površino vrvi in okolico za vrv AlFe490/65, in sicer za $\Delta T=T_{s}-T_{a}=10^{\circ}$ (Slika 44), $\Delta T=40^{\circ}$ (Slika 45) in $\Delta T=80^{\circ}$ (Slika 46).

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-61.jpg?height=570&width=1515&top_left_y=799&top_left_x=294)
Slika 44: Temperaturno polje (levo) in polje magnitude hitrosti (desno) v umirjenem stanju pri $\Delta T=10^{\circ}$.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-61.jpg?height=558&width=1499&top_left_y=1531&top_left_x=300)
Slika 45: Temperaturno polje (levo) in polje magnitude hitrosti (desno) v umirjenem stanju pri $\Delta T=40^{\circ}$.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-62.jpg?height=551&width=1495&top_left_y=270&top_left_x=302)
Slika 46: Temperaturno polje (levo) in polje magnitude hitrosti (desno) v umirjenem stanju pri

$$
\Delta T=80^{\circ} .
$$

Po pričakovanjih se nad vrvjo ustvari ozek curek toplega zraka, ki se zaradi vzgona dviguje. Posledično vrv od spodaj obteka relativno hladen zrak, kar je tudi glavni mehanizem hlajenja. V primeru, ko bi bila vrv hladnejša od okolice, bi imeli točno obraten primer, zrak bi se ob vrvi ohlajal in padal proti tlom. Oglejmo si temperaturne preseke $T(x, \mathrm{y}=0) / \Delta T$ za vse tri primere (Slika 47).

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-62.jpg?height=691&width=1337&top_left_y=1299&top_left_x=384)
Slika 47: Temperaturni profil $T(x, y=0)$ pri različnih $\Delta T$.

Takoj opazimo, da je robni sloj naravne konvekcije relativno majhen, reda le 1 cm , kar je tudi v skladu s pričakovanji [9].

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-63.jpg?height=697&width=1340&top_left_y=281&top_left_x=386)
Slika 48: Odvisnost moči hlajenja od širine računske domene.

Čeprav se na primerjavi temperaturnih profilov (Slika 47) lepo vidi, da je mejna plast naravne konvekcije široka reda nekaj cm, si vseeno oglejmo odvisnost rezultatov od te modelske predpostavke (Slika 48, Slika 49 in Slika 50).

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-63.jpg?height=699&width=1333&top_left_y=1336&top_left_x=391)
Slika 49: Odvisnost moči hlajenja od višine računske domene.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-64.jpg?height=691&width=1322&top_left_y=283&top_left_x=395)
Slika 50: Odvisnost moči hlajenja od globine računske domene.

Na podlagi dobljenih rezultatov lahko z mirno vestjo računsko območje omejimo na kvadrat s stranico 5 cm . V nadaljevanju si oglejmo časovni razvoj moči hlajenja zaradi naravne konvekcije pri konstanti temperaturi površine (vrvi Slika 51) iz katerega vidimo, da se naravna konvekcija v nam zanimivih režimih res umiri v nekaj sekundah.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-64.jpg?height=691&width=1318&top_left_y=1402&top_left_x=395)
Slika 51: Časovni razvoj moči hlajenja zaradi naravne konvekcije pri konstanti temperaturi površine vrvi.

Seveda moramo preveriti še obnašanje rešitve v odvisnosti od krajevne in časovne diskretizacije. Poglejmo najbolj agresiven primer pri temperaturni razliki $\Delta T=80^{\circ}$ in konstantnih snovnih lastnostih (Slika 52). Na grafu se vidijo vsa pričakovana obnašanja; rešitev lepo konvergira in je nestabilna pri
gostih krajevnih diskretizacijah za velike časovne korake. Pri približno $N=7 \cdot 10^{4}$, kar v grobem pomeni razdaljo reda $0,1 \mathrm{~mm}$ med diskretizacijskimi točkami, se rešitev umiri.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-65.jpg?height=658&width=1271&top_left_y=451&top_left_x=416)
Slika 52: Odvisnost moči hlajenja od števila računskih točk in časovnega koraka.

Vsebinsko zgovorna je Slika 53, ki kaže odziv moči hlajenja na spremembo snovnih lastnosti zraka. Takoj opazimo, da ima največji vpliv toplotna prevodnost, kjer je relativni odziv simulacije nekoliko manjši kot relativna sprememba te količine, sledi gostota ter viskoznost. Specifična kapacitivnost in koeficient razteznosti imata najmanjši vpliv. Spomnimo se analize iz začetka študije, kjer smo pogledali razpone vrednosti snovnih lastnosti v odvisnosti od temperature (2). Te podatke združimo z odzivom moči hlajenja in postane hitro očitno, da je potrebno upoštevati temperaturno odvisnost toplotne prevodnosti in viskoznosti, kar bomo v nadaljevanju upoštevali preko (1.17) in (1.18).

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-65.jpg?height=652&width=1282&top_left_y=1727&top_left_x=399)
Slika 53: Odvisnost moči hlajenja od snovnih lastnosti zraka.

Z dosedanjimi analizami smo popolnoma določili računski postopek, zato si lahko ogledamo prvi rezultat, in sicer primerjavo moči hlajenja zaradi naravne konvekcije v odvisnosti od razlike temperature površine vrvi ter ambientalne temperature MLSM rešitve ter IEEE, IEC in CIGRE standardov (Slika 54). Takoj je očitno, da IEC model popolnoma odpove, saj predpostavi, da naravne konvekcije ni, medtem ko modela IEEE in CIGRE ter MLSM model vrnejo podobno obnašanje (Slika 52). Na tem mestu se spomnimo, da MLSM model ne potrebuje empirično določenih parametrov, kot to potrebujeta IEEE in CIGRE standarda.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-66.jpg?height=654&width=1294&top_left_y=758&top_left_x=395)
Slika 54: Odvisnost moči hlajenja naravne konvekcije od temperaturne razlike med površino vrvi in okolico.

Nekoliko manj relevanten a vseeno zanimiv podatek je, da smo za pripravo analiz izvedli reda 2500 izračunov, kjer je tipični računski čas ene simulacije trajal reda nekaj minut. Skupno je bilo torej za zgornje grafe potrebnih približno 150 ur računanja, katerega smo izvedli na našem testnem skupku 36 računalnikov s skupno 144 jedri. V ta čas seveda ni všteto testiranje in vse ostale analize. Precej bolj zajeten zalogaj bo serija izračunov potrebna za analizo meritev o katerih bomo razpravljali v naslednjem poglavju.

### 4.2 Primerjava numeričnih in eksperimentalnih meritev

### 4.2.1. Ocena merilnega pogreška

Pred samo primerjavo izračunanih rezultatov temperatur z izmerjenimi vrednostmi moramo poznati oziroma vsaj oceniti velikostni razred napake samih meritev. Zavedati se moramo, da k napaki lahko prispeva vsak od merilnih členov. Meritev temperature opravimo s termočlenom in integriranim vezjem MAX31856. Za slednjega je deklariran merilni pogrešek pri branju napetosti termočlena $\pm 0,15 \% \mathrm{v}$
območju od -20 do $85^{\circ} \mathrm{C}$. Naše opravljene meritve so znotraj tega temperaturnega območja, zato lahko ocenimo, da npr. največji pogrešek pri $\mathrm{T}=85^{\circ} \mathrm{C}$ znaša $\pm 0,1275^{\circ} \mathrm{C}$. Dodaten pogrešek nastane zaradi kompenzacije t.i. »cold junction«« oz. hladnega stika, ki je nujen za ločitev visokih temperatur termočlena do merilne elektronike. Po specifikacijah uporabljenega termočlena znaša pogrešek »cold junction« $\pm 0,7^{\circ} \mathrm{C}$ v območju temperatur -20 do $80^{\circ} \mathrm{C}$. Skupen pogrešek torej znaša reda $\pm 1,0{ }^{\circ} \mathrm{C}$. Dodatno k pogrešku prispevajo tudi ostali faktorji, ki pa jih težje določiti, in sicer pogrešek pri mehanski namestitvi merilnikov ter pogrešek zaradi sprememb v merilnem okolju.

Zavedati se moramo, da vsak mehanski poseg v vodnik spreminja njegove mehanske in električne lastnosti. Ker pa je površina takšnega senzorja proti celotni površini vodnika minimalna, to ne bi smelo opazno vplivati na kakovost meritev. Dodatno takšen merilni člen rahlo spreminja obtekanje segretega zraka v okolici vodnika, vendar je z razporeditvijo merilnikov na dovolj oddaljenih lokacijah vzdolž dolžine vodnika tudi takšen pogrešek minimiziran. Pri meritvah smo tudi predpostavili, da postavitev merilnikov vzdolž dolžine vodnika (na isti lokaciji na obodu) ne bi smela vplivati na meritve. Vse takšne predpostavke so še vedno predpostavke. Da bi kompenzirali oz. kar se da zmanjšali vpliv takšnih napak na kakovost meritev, bi bilo treba opraviti množico preizkusov, kjer bi na podlagi statističnih rezultatov meritev lahko ugotovili vpliv načina in lokacije postavitve merilnikov na napako.

Dodatno je vsako realno merilno okolje podvrženo spremembam v okolici (npr. nihanju zraka v okolici senzorjev, ki odvisno od mikrolokacije teh sprememb različno vpliva na posamezne merilnike in meritve). Pri našem eksperimentu so bile meritve opravljene v nadzorovano zaprtem okolju laboratorija, tako da so takšni okoljski faktorji bili minimizirani. Posledično lahko trdimo, da je vpliv takšnega pogreška zanemarljiv.

### 4.2.2. Določitev velikosti odstopanja temperature pri meritvah

V nadaljevanju poglejmo izmerjene ambientalne temperature, ki so se sočasno merile na različnih lokacijah v okolici vodnika z merilniki CJ (pozicije merilnikov se niso spreminjale). Vse temperature so povprečene z eno minutnim oknom. Opazimo, da:

- odstopanja med senzorji, ki kažejo največje in najmanjše temperature, ne presegajo $0,4^{\circ} \mathrm{C}$ (odstopanja od povprečne temperature pa največ $\pm 0,2^{\circ} \mathrm{C}$ ),
- ta odstopanja so približno konstantna v vseh treh merilnih ciklih,
- vrstni red senzorjev, ki izmerijo od najmanjših do največjih temperatur, se ne spreminja v vseh treh merilnih ciklih,
- časovna dinamika spreminjanja temperatur je pri vseh merilnikih približno enaka, meritve so le zamaknjene za enosmerno (offset) vrednost temperature.

Vse te ugotovitve nam dajo slutiti, da vzrok za odstopanja izmerjenih temperatur ni različna mikroklima v okolici vodnika, temveč pogreški samega merilnega sistema. Ti pogreški so znotraj odstopanja $\pm 0,8 { }^{\circ} \mathrm{C}$.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-68.jpg?height=609&width=1531&top_left_y=625&top_left_x=294)
Slika 55: Ambientalne temperature izmerjene 22. 3. 2018 (levo) in 29. 3. 2018 (desno)

V nadaljevanju poglejmo še meritev na površini vodnika, in sicer na zgornjem in spodnjem delu vodnika. Slike prikazujejo čas pred samim začetkom meritev, preden spustimo tok skozi vodnik in ko je vodnik segret na temperaturo okolice (na koncu je prikazan še krajši interval, ko tok povečamo in začne temperatura strmo naraščati). Dejanska temperatura vodnika na začetku bi morala biti enaka temperaturi okolice. Rezultati na treh spodnjih slikah pa kažejo, da temu ni tako, in sicer pri meritvah dne 8. 3. in 22. 3. je temperatura vodnika manjša od temperature okolice, 29. 3. pa ravno obratno (Slika 56). Ta odstopanja med meritvami na površini in meritvami okolice so reda $1^{\circ} \mathrm{C}$, večinoma pa pod deklariranim pogreškom $\pm 0,8^{\circ} \mathrm{C}$.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-69.jpg?height=628&width=1567&top_left_y=251&top_left_x=266)
Slika 56: Ambientalne in temperature izmerjene na površini vodnika 22. 3. 2018 (levo) in 29. 3. 2018 (desno).

Primerjamo še meritve v simetrično postavljenih senzorjev TC1 in TC2 (Slika 57) v sredici vodnika Al/Fe-490/65 (Slika 58) izmerjene 22. 3. 2018.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-69.jpg?height=497&width=1056&top_left_y=1190&top_left_x=534)
Slika 57: Postavitev senzorjev pri meritvi opravljeni 22. 3. 2018 in meritvi opravljeni 29. 3. 2018.

Iz obeh grafov je razvidno, da se z naraščanjem temperature vodnika povečuje tudi izmerjena razlika temperatur med obema senzorjema, in sicer temperatura TC2 narašča hitreje (razlika TC1-TC2 je vedno bolj negativna). Srednje odstopanje izmerjenih temperatur med merilnikoma znaša približno $1 \%$.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-70.jpg?height=680&width=1545&top_left_y=253&top_left_x=292)
Slika 58: Primerjava meritev simetrično postavljenih senzorjev v jedru vodnika.

Primerjamo temperaturo simetrično merjeno na površini vodnika Al/Fe-490/65 s senzorjema TC0 in TC3 izmerjene 29. 3. 2018. Slika 59 prikazuje časovni potek razlike temperatur obeh senzorjev in korelacijo razlike temperatur in povprečne temperature obeh senzorjev. Tokrat je opazno večje začetno enosmerno odstopanje (približno $0,2^{\circ} \mathrm{C}$ ) v temperaturah med obema senzorjema, odstopanje temperatur pa, za razliko od rezultatov TC1 in TC2 zgoraj, tokrat ne kaže odvisnosti od temperature vodnika in je približno konstantno.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-70.jpg?height=693&width=1575&top_left_y=1486&top_left_x=275)
Slika 59: Primerjava meritev simetrično postavljenih senzorjev v jedru vodnika.

### 4.2.3. Primerjava modelskih izračunov in meritev

V prvem koraku pogledamo ali na poligonu res merimo samo konvektivno hlajenje zaradi naravne konvekcije. To naredimo s pomočjo Schlieren fotografije iz katere sicer ne moremo razbrati absolutnih vrednosti temperature, saj je rezultat odvisen od konfiguracije samega poligona, moči točkastega izvora, nastavitve zrcala, nastavitve barvnih filtrov, nastavitve fokusa objektiva ter časa odprtosti zaslonke ob fotografiranju. Z nastavitvijo teh parametrov lahko dobimo različne fotografije za enako segret vodnik v enakih pogojih. Lahko pa ocenimo obliko temperaturnega polja, kar je dovolj, da lahko sklepamo ali je bila med meritvijo res prisotna samo naravna konvekcija, kar nam potrdi primerjava fotografije in simuliranega polja (Slika 60).

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-71.jpg?height=493&width=1327&top_left_y=872&top_left_x=399)
Slika 60: Rezultat Schlieren fotografije segretega vodnika z uporabo barvnega filtra (levo) in temperaturno polje izračunano z MLSM (desno) .

V nadaljevanju si oglejmo bolj kvantitativno primerjavo izračunov z meritvami. Merili smo potek temperature na vrveh AlFe240/40 in AlFe490/65, kjer smo meritev vedno pričeli v umirjenem stanju, s temperaturo vodnika enako okolici. Po kratkem času smo po vodniku pognali tok, počakali, da se stanje umiri, pognali nekoliko večji tok, ponovno počakali, da se stanje umiri, .... Postopek smo za vrvi AlFe240/40 pri vsaki meritvi ponovili štirikrat in nato ugasnili tok ter počakali, da se vrv ohladi nazaj na temperaturo okolice. Zaradi počasnejše dinamike smo pri AlFe490/65 na eno meritev izmerili samo dva skoka. Izvedli smo pet meritev za vrv AlFe490/65 in dve za AlFe240/40. Razpon toka pri AlFe240/40 je bil med 50 in 700 A , kjer je vrv dosegala temperature jedra med $25{ }^{\circ} \mathrm{C}$ in $80^{\circ} \mathrm{C}$ in pri vrvi AlFe490/65 300 do 1000 A , kjer je vrv dosegala temperature jedra med $35^{\circ} \mathrm{C}$ in $95^{\circ} \mathrm{C}$.

Meritve so bile izvedene v zgodnji pomladi (skupno 26,3 ur meritev na vodniku Al/Fe 490/65 v marcu), poleti ( 24,9 ur meritev na vodniku Al/Fe 490/65 v avgustu) in jeseni ( 13 ur meritev na vodniku Al/Fe 490/65 in 28,9 ur meritev na vodniku Al/Fe 240/40 v septembru in oktobru), vse v letu 2018 (Tabela 1 in Tabela 2).

| Obdobje |  | marec | marec | avgust | avgust | september | september | september |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $T_{a}$ |  | Al/Fe | Al/Fe | Al/Fe | Al/Fe | Al/Fe | Al/Fe | Al/Fe |
|  | vodnik | 490/65 | 490/65 | 490/65 | 490/65 | 490/65 | 240/40 | 240/40 |
| $10^{\circ} \mathrm{C}-15^{\circ} \mathrm{C}$ |  | 13,7 |  |  |  |  |  |  |
| $15^{\circ} \mathrm{C}-20^{\circ} \mathrm{C}$ |  |  | 12,6 |  |  |  |  |  |
| $20^{\circ} \mathrm{C}-25^{\circ} \mathrm{C}$ |  |  |  |  | 12,5 | 13,0 | 5,0 | 3,9 |
| $25^{\circ} \mathrm{C}-30^{\circ} \mathrm{C}$ |  |  |  | 12,4 |  |  | 9,1 | 10,9 |

Tabela 1: Čas meritev na posameznih vodnikih po posameznih meritvah glede na temperaturni razpon temperature okolice v urah.

| $T_{a}$ | Al/Fe 240/40 | Al/Fe 490/65 | Skupno |
| :--- | :--- | :--- | :--- |
| $10^{\circ} \mathrm{C}-15^{\circ} \mathrm{C}$ |  | 13,7 | 13,7 |
| $15^{\circ} \mathrm{C}-20^{\circ} \mathrm{C}$ |  | 12,6 | 12,6 |
| $20^{\circ} \mathrm{C}-25^{\circ} \mathrm{C}$ | 8,9 | 25,5 | 34,4 |
| $25^{\circ} \mathrm{C}-30^{\circ} \mathrm{C}$ | 20 | 12,4 | 32,4 |
|  | 28,9 | 64,2 | 93,1 |

Tabela 2: Čas meritev na posameznih vodnikih glede na temperaturni razpon temperature okolice v urah.

V nadaljevanju primerjajmo izračunane temperature jedra z MLSM in CIGRE algoritmom ter meritvami. Opazimo, da MLSM in CIGRE algoritma vračata podobno obnašanje. To smo pričakovali, saj je edina resna razlika le v izračunu toplotnega toka skozi površino vrvi, za katerega smo pa že pokazali, da z MLSM dobimo podobne napovedi kot s CIGRE. Predvsem je pomembno, da oba modela relativno dobro sledita meritvam. Opazno odstopanje opazimo le pri nekaterih časovnih potekih. V splošnem lahko ugotovimo, da oba numerična izračuna nekoliko prehitevata meritve, kar se najlepše vidi pri končnih ohlajanjih. Je pa nekatera odstopanja mogoče tudi komentirati. Pri meritvi 1 (Slika 61) opazimo izrazito razliko v dinamiki pri drugem skoku, kar je lahko posledica slabe meritve, saj pri podobnih pogojih (meritev 2, prvi skok) ne opazimo tako velikega odstopanja. Podoben razmislek velja tudi za odstopanje pri ohlajanju pri meritvi 2, saj pri podobnih pogojih pri meritvi 1 ni tako velikih odstopanj. Pri meritvi 3 (Slika 63) so bile med meritvijo očitno prisotne motnje in so zato odstopanja najverjetneje posledica teh motenj. Konsistentno prehitevanje pri ohlajanju opazimo le pri obeh meritvah AlFe240/40 (Slika 67 in Slika 66). Na časovni potek pojava vpliva moč izgub v okolico, gostota in specifična toplotna kapacitivnost pletenice. Če zaupamo modelu za joulske izgube potem lahko izključimo napako v moči izgub v okolico, saj dobimo dobro ujemanje v stacionarnem stanju in tako lahko razlog za prehi-
tevanje iščemo v modelu gostote in specifične toplotne kapacitivnosti pletenice. Ta diskusija že presega okvir te študije, saj, kot bomo videli v nadaljevanju, razlika v časovni dinamiki obeh modelov in meritvami ne vpliva na naše zaključke.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-73.jpg?height=712&width=1417&top_left_y=489&top_left_x=386)
Slika 61: Primerjava izračunane temperature jedra z MLSM in CIGRE algoritmom ter meritvami (M) za meritev 1.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-73.jpg?height=714&width=1415&top_left_y=1362&top_left_x=388)
Slika 62: Primerjava izračunane temperature jedra z MLSM in CIGRE algoritmom ter meritvami (M) za meritev 2.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-74.jpg?height=717&width=1415&top_left_y=259&top_left_x=388)
Slika 63: Primerjava izračunane temperature jedra z MLSM in CIGRE algoritmom ter meritvami (M) za meritev 3.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-74.jpg?height=714&width=1412&top_left_y=1130&top_left_x=391)
Slika 64: Primerjava izračunane temperature jedra z MLSM in CIGRE DTR algoritmom ter meritvami (M) za meritev 4.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-75.jpg?height=712&width=1440&top_left_y=262&top_left_x=378)
Slika 65: Primerjava izračunane temperature jedra z MLSM in CIGRE DTR algoritmom ter meritvami (M) za meritev 5 .

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-75.jpg?height=710&width=1412&top_left_y=1134&top_left_x=391)
Slika 66: Primerjava izračunane temperature jedra z MLSM in CIGRE algoritmom ter meritvami (M) za meritev 6.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-76.jpg?height=719&width=1419&top_left_y=257&top_left_x=384)
Slika 67: Primerjava izračunane temperature jedra z MLSM in CIGRE algoritmom ter meritvami (M) za meritev 7.

Pri zgornjih grafih smo potiho predpostavili, da poznamo toplotno prevodnost in emisivnost vrvi, kar pa ni res. Ti podatki niso znani. Res da poznamo toplotno prevodnost aluminija, ki se giblje okoli $\lambda_{\text {Al }}=200[\mathrm{~W} / \mathrm{mK}]$, vendar se večina radialnega prenosa toplote skozi vrv dogaja v zračnih kanalih med posameznimi vodniki [49], poleg tega pa spoji med vodniki niso idealni, kar pomeni, da je efektivna radialna toplotna prevodnost reda $\lambda \in[0.5,7][\mathrm{W} / \mathrm{mK}]$, in je močno odvisno od napetosti vrvi, ki vpliva na pritisk med posameznimi prameni v vrvi [5]. Spomnimo se diskusije iz študije »Analiza preprečevanja nastajanja žleda z obratovalnimi ukrepi« [69], kjer smo pri analitični obravnavi ogrevane vrvi pokazali, da v stacionarnem stanju velja

$$
\begin{equation*}
\Delta T=T_{C}-T_{S}=\frac{P_{j}}{2 \lambda \pi}\left[\frac{1}{2}-\frac{D_{1}^{2}}{D^{2}-D_{1}^{2}} \ln \left(\frac{D}{D_{1}}\right)\right], \tag{3.1}
\end{equation*}
$$

kjer so $D, D_{1}, P_{j}$ premer vrvi, premer nosilne vrvi in moč joulskih izgub. Iz preprostega modela vidimo, da je edini prosti parameter, ki vpliva na razliko med temperaturo jedra in površine vrvi njena toplotna prevodnost, kar pomeni, da jo lahko ocenimo iz meritev. Iz vseh meritev izluščimo stacionarna stanja in narišimo odvisnost $\Delta T$ od moči joulskih izgub za napoved (3.1), meritve ter CIGRE in MLSM izračun, kjer smo ocenili $\lambda=2 \mathrm{~W} / \mathrm{mK}$ za AlFe490/65 in $\lambda=3.5 \mathrm{~W} / \mathrm{mK}$ za AlFe240/40 (Slika 68).

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-77.jpg?height=802&width=1559&top_left_y=253&top_left_x=257)
Slika 68: Primerjava razlike temperature površine in jedre izračunane z MLSM in CIGRE algoritmom, meritvami (M) ter analitično napovedjo (A) v odvisnosti od joulskih izgub v vrvi.

Precej bolj nadležno je nepoznavanje emisivnosti, ki ima zelo močan vpliv na rezultate, zlasti pri visokih temperaturah. Ponovno bomo morali ta podatek reproducirati iz meritev in se zanesti na priporočila standardov. Oglejmo si odziv modela na spremembo emisivnosti znotraj priporočil CIGRE (Slika 69). Odziv je zelo velik. Razlika modelske napovedi med skrajnimi izbirami emisivnosti je reda $20{ }^{\circ} \mathrm{C}$. Glede na izračune in meritev je smiselna izbira $\epsilon=0,85$ za AlFe240/40 in $\epsilon=0,25$ za AlFe490/65, kar je je tudi v skladu s priporočili CIGRE. Pri meritvah smo namreč uporabili popolnoma novo AlFe490/65 vrv, kjer standard priporoča uporabo emisivnosti znotraj 0,2-0,3, medtem, ko je bil za meritve uporabljena stara AlFe240/40 vrv, za kar pa standard priporoča emisivnosti med 0,8-0, 9 (»Emissivities of energized conductors increase rapidly with age from about $0.2-0.3$ when new to about 0.8-0.9 within one or two years of high voltage operation in industrial or heavy agricultural environments« [5]). Zaupanje v model bi bilo seveda veliko višje, če bi poznali prave vrednosti emisivnosti, a vseeno smo z rezultati zadovoljni, saj smo pokazali, da je mogoče s simulacijo in CIGRE modelom relativno dobro popisati hlajenje vrvi zaradi naravne konvekcije.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-78.jpg?height=602&width=1541&top_left_y=249&top_left_x=262)
Slika 69: Odziv izračunane temperature z uporabo različnih emisivnosti.

### 4.2.4. Določitev meje med prevladujočo naravno konvekcijo in prisilno konvekcijo

Ob brezvetrju je prevladujoč mehanizem hlajenja naravna konvekcija, ki pa ob pojavu vetra hitro postane zanemarljiv in prevlada prisilna konvekcija. Eno izmed glavnih vprašanj študije je pri kateri jakosti vetra se to zgodi. Do sedaj smo se v študiji ukvarjali z vzpostavitvijo zaupanja računskih modelov za napovedovanje termičnega stanja vrvi, sedaj bomo ta orodja uporabili za vpogled v dogajanje pri prehodu iz popolne naravne konvekcije v prevladujočo prisilno konvekcijo, saj nam, poleg obravnave čiste naravne konvekcije, omogočajo vpeljati tudi prisilno gibanje zraka. V primeru CIGRE izračuna v ta namen uporabimo predlagane empirične relacije in v primeru MLSM simulatorja primerno spremenimo hitrostne in tlačne robne pogoje.

CIGRE standard obravnavo konvektivnega hlajenje razdeli na dve območji, ki jih razmeji pri hitrosti vetra $0,5 \mathrm{~m} / \mathrm{s}$. Delitev sloni na predpostavki, da pod $0,5 \mathrm{~m} / \mathrm{s}$ smer vetra ni več dobro definirana in jo zato nastavijo na nevtralnih $45^{\circ}$. Za končni rezultat CIGRE predlaga, da se v režimu pod $0,5 \mathrm{~m} / \mathrm{s}$ izračuna tako moč hlajenja zaradi prisilne konvekcije pri kotu $45^{\circ}$ preko enačbe (1.9) kot tudi popolne naravne konvekcije preko enačbe (1.10) ter se upošteva višja vrednost, medtem ko se nad hitrostjo vetra $0,5 \mathrm{~m} / \mathrm{s}$ upošteva izračun (1.9) pri podanem kotu. Tak pristop ima nekoliko neokusno implikacijo, in sicer razen pri kotih $45^{\circ}$ moč hlajenja doživi skok pri prehodu meje $0,5 \mathrm{~m} / \mathrm{s}$, kar ni ravno v skladu z našimi predstavami o naravi. Raziskovalci predlagajo različna zdravila za ta pojav, od linearne prehoda moči hlajenja med $0,5 \mathrm{~m} / \mathrm{s}$ in $0 \mathrm{~m} / \mathrm{s}$ do naključne izbire kota vetra v območju pod $0,5 \mathrm{~m} / \mathrm{s}$ [5]. Standard CIGRE diskusijo zaključi z mislijo »Some of the convection models for low wind speeds are described in Annex C, but their practical application for dynamic thermal ratings would need an accurate assessment of the wind speed and direction all along the line at any time, which is not possible in practice for normal situations«.

V naši obravnavi si oglejmo kakšno je obnašanje pri kotu vetra $90^{\circ}$ pri pogojih, ki jih narekuje SIST EN 50182:2001. Za razliko od CIGRE z MLSM lahko simuliramo zmes naravne in prisilne konvekcije ( $P_{C}^{\text {MLSM }}$ ), saj izračunavamo temperaturno in hitrostno polje. Prav tako lahko izračunamo samo prisilno konvekcijo, tako da preprosto izklopimo gravitacijsko polje ( $P_{F}^{M L S M}$ ), kar bi bilo pri meritvah precej težje doseči. Poleg MLSM izračunov narišemo še moč hlajenja zaradi naravne konvekcije po CIGRE ( $P_{\text {NC }}^{\text {CIGRE }}$ ), prisilne konvekcije ( $P_{F}^{\text {CIGRE }}$ ) in prisilne konvekcije pri $45^{\circ}$ ( $P_{F 45}^{\text {CIGRE }}$ ) (Slika 70). Ujemanje med MLSM in CIGRE prisilno konvekcijo je solidno, s čimer dodatno povečamo zaupanje v oba modela.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-79.jpg?height=801&width=1535&top_left_y=852&top_left_x=262)
Slika 70: Moč hlajenja naravne in prisilne konvekcije v odvisnosti od hitrosti vetra pri temperaturi vodnika $80^{\circ} \mathrm{C}$ in temperaturi zraka $35^{\circ} \mathrm{C}$ za vodnik AlFe240/40 (levo) in AlFe490/65 (desno).

Takoj opazimo, da v danem primeru prisilna konvekcija nadvlada naravno dokaj hitro, približno pri 0.1 $\mathrm{m} / \mathrm{s}$. CIGRE priporočilo je sicer nekoliko bolj konzervativno s predpostavko, da je smer vetra pod 0.5 $\mathrm{m} / \mathrm{s}$ vedno $45^{\circ}$ in zato »prisilna<< konvekcija nekoliko kasneje nadvlada naravno konvekcij, in sicer pri približno $0.15-0.16 \mathrm{~m} / \mathrm{s}$, odvisno od tipa vrvi. Zanimiv je minimum moči hlajenja izračunane z MLSM, ki se nahaja pri približno $0.05 \mathrm{~m} / \mathrm{s}$. Poglejmo si temperaturna polja okoli vrvi pri $0 \mathrm{~m} / \mathrm{s}, 0.5 \mathrm{~m} / \mathrm{s}$ in 0.1 $\mathrm{m} / \mathrm{s}$ prisilnega vetra (Slika 71). Lepo se vidi, da pri približno pri $0.05 \mathrm{~m} / \mathrm{s}$ prisilnega vetra, le ta zmoti tok naravne konvekcije, kar povzroči slabše hlajenje. Pri $0.1 \mathrm{~m} / \mathrm{s}$ postane prisilna konvekcija dominantna in obnašanje postane spet pričakovano. Tega pojava CIGRE seveda ne more popisati, saj ne obravnava mešane konvekcije, temveč samo preklaplja med empiričnima relacijama za opis prisilne in naravna konvekcije. Podobno obnašanje so opazili tudi avtorji članka [43], ki so problem analizirali s
pomočjo komercialnega paketa za reševanje prenosnih pojavov. Čeprav je pojav zanimiv iz operativnega stališča nima prav velike uporabne vrednosti, saj so meritve vetra pri tako nizkih vrednostih zelo nepredvidljive in posledično je tudi sama napoved moči hlajenje zaradi konvekcije vprašljiva. Vsekakor podrobnost kot je minimum hlajenje pri prehodu iz naravne v prisilno konvekcijo ne spremeni operativnega pogleda na model.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-80.jpg?height=720&width=1477&top_left_y=608&top_left_x=343)
Slika 71: Temperaturna polje okoli vrvi pri $0 \mathrm{~m} / \mathrm{s}, 0.5 \mathrm{~m} / \mathrm{s}$ in $0.1 \mathrm{~m} / \mathrm{s}$ zunanjega vetra.

Motor naravne konvekcije je razlika v temperaturi med površino vodnika in okoliškega zraka. Zato si oglejmo še odvisnost hitrosti pri kateri pride do prehoda med naravno in prisilno konvekcijo od temperature vrvi pri temperaturi okoliškega zraka $35^{\circ} \mathrm{C}$ (Slika 72), kjer narišemo mejno hitrost pri predpostavki, da veter piha pod kotom $45^{\circ}\left(\hat{u}_{F 45}\right)$ ali $90^{\circ}\left(\hat{u}_{F}\right)$.

Sedaj lahko odgovorimo še na drugo vprašanje študije, in sicer »Ali je pri hitrostih vetra pod 0,6 m/s moč hlajenja zaradi naravne konvekcije dovolj velika, da je, pri temperaturi okolice $35{ }^{\circ} \mathrm{C}$, sončnem sevanju $900 \mathrm{~W} / \mathrm{m}^{2}$, koeficientu absorpcije 0,5 in emisivnosti 0,5 , dopustni tok daljnovodne vrvi vedno višji ali enak statičnemu termični toku določenemu s standardom SIST EN 50182:2001?«. Odgovor je ne, samo hlajenje preko naravne konvekcije ni dovolj za ohranjanje temperature vodnika pod kritično vrednostjo pri danih pogojih. Za dodatno potrditev te izjave poglejmo še s CIGRE algoritmom izračunan dinamični termični tok za obe vrvi (Slika 73). Vidimo, da je za obe vrvi dinamični termični tok pod $0,6 \mathrm{~m} / \mathrm{s}$ nižji od statične meje. Na sliki se tudi lepo vidi skok pri $0.5 \mathrm{~m} / \mathrm{s}$ o katerem smo diskutirali na začetku tega poglavja.

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-81.jpg?height=802&width=1535&top_left_y=249&top_left_x=259)
Slika 72: Odvisnost hitrosti pri kateri pride do prehoda med naravno in prisilno konvekcijo od temperature vrvi pri temperaturi zraka $35{ }^{\circ} \mathrm{C}$ za vodnik AlFe240/40 (levo) in AlFe490/65 (desno).

![](https://cdn.mathpix.com/cropped/91a23e1b-1ae5-4416-a29d-cf05364215c5-81.jpg?height=811&width=1559&top_left_y=1179&top_left_x=257)
Slika 73: Dinamični in statični termični tok pri temperaturi zraka $35{ }^{\circ} \mathrm{C}$ za vodnik AlFe240/40 (levo) in AlFe490/65 (desno) v odvisnosti od hitrosti vetra izračunan s CIGRE priporočili.

## 5. Zaključki študije

V študiji smo pod drobnogled vzeli obravnavo konvektivnega hlajenja vrvi pri pogojih, ko naravna konvekcija igra glavno vlogo, torej pri nizkih vrednostih hitrosti vetra. Implementirali smo priporočila treh glavnih standardov (CIGRE, IEEE, IEC), ki slonijo na preprostih skalarnih modelih in se zanašajo predvsem na empirične relacije in originalno rešitev dvodimenzionalnega fizikalnega modela (MLSM). Modele smo primerjali med seboj in pokazali, da IEC ni primeren za našo obravnavo, saj ne upošteva naravne konvekcije in da MLSM, IEEE in CIGRE napovedujejo podobne rezultate. Napovedi modelov smo nadaljnje primerjali z meritvami na poligonu, ki smo ga v sklopu študije pripravili za posnemanje vodnika med »obratovanjem« v brezvetrju in pokazali, da se MLSM ter CIGRE izračuna dobro ujemajo z meritvami. V nadaljevanju smo primerjali še MLSM in CIGRE pri šibkih vetrovih, ponovno z dobrim ujemanjem, in pokazali, da prisilna konvekcija relativno hitro nadvlada naravno konvekcijo, in sicer precej pod $0,6 \mathrm{~m} / \mathrm{s}$, kar pomeni, da samo hlajenje zaradi naravne konvekcije ne zadošča, da bi zagotavljalo dopustni tok daljnovodne vrvi višji ali enak statičnemu termični toku določenemu s standardom SIST EN 50182:2001 pri hitrostih vetra pod $0,6 \mathrm{~m} / \mathrm{s}$, temperaturi okolice $35^{\circ} \mathrm{C}$, sončnem sevanju 900 $\mathrm{W} / \mathrm{m}^{2}$, koeficientu absorpcije 0,5 in emisivnosti 0,5 .

### 5.1 Povzetek glavnih prispevkov študije

- Pregled znanstvene in strokovne literature iz področja naravne konvekcije, kjer so zajete objave iz teoretičnih, numeričnih in eksperimentalnih del.
- Pregled literature iz področja obravnave konvektivnega prenosa toplote v DTR modelih, kjer identificiramo prvo pojavljanje vrednosti $0,6 \mathrm{~m} / \mathrm{s}$ v kontekstu termične obravnave daljnovodnih vrvi, kar je prvo vprašanje študije.
- Neposredna primerjava konvektivnega hlajenja CIGRE, IEEE, in IEC standardov.
- Pregled pogostosti stanj glede na hitrost vetra in temperaturo zraka na podlagi podatkov iz ELESovih merilnih postaj.
- Verificirana numerična rešitev razvitega dvodimenzionalnega fizikalnega modela, ki lahko opiše konvektivno hlajenje vrvi.
- Vzpostavitev eksperimentalnega poligona za posnemanje daljnovoda med obratovanjem v brezvetrju in izvedba preskusov s skočno spremembo toka.
- Analiza naravne konvekcije okoli daljnovodnih vrvi AlFe240/40 in AlFe490/65 pri različnih obratovalnih pogojih.
- Primerjava modelskih izračunov in meritev z razponom toka pri AlFe240/40 50 do 700 A , kjer je vrv dosegala temperature jedra med $25{ }^{\circ} \mathrm{C}$ in $80^{\circ} \mathrm{C}$ in pri vrvi AlFe490/65 300 do 1000 A , kjer je
vrv dosegala temperature jedra med $35{ }^{\circ} \mathrm{C}$ in $95{ }^{\circ} \mathrm{C}$. V vseh primerih CIGRE algoritem in MLSM rešitev dobro sledita meritvam.
- Določitev meje med prevladujočo naravno konvekcijo in prisilno konvekcijo v odvisnosti od temperature vrvi pri temperaturi zraka $35{ }^{\circ} \mathrm{C}$.
- Analiza prehoda med prevladujočo naravno in prevladujočo prisilno konvekcijo.
- Enoličen odgovor na drugo vprašanje študije »Ali je pri hitrostih vetra pod $0,6 \mathrm{~m} / \mathrm{s}$ moč hlajenja zaradi naravne konvekcije dovolj velika, da je, pri temperaturi okolice $35{ }^{\circ} \mathrm{C}$, sončnem sevanju 900 $\mathrm{W} / \mathrm{m}^{2}$, koeficientu absorpcije 0,5 in emisivnosti 0,5 , dopustni tok daljnovodne vrvi vedno višji ali enak statičnemu termični toku določenemu s standardom SIST EN 50182:2001?«, in sicer »ne, moč hlajenja naravne konvekcije ni dovolj velika, da bi bil v danih razmerah dopustni tok daljnovodne vrvi vedno višji ali enak statičnemu termični toku določenemu s standardom SIST EN 50182:2001«.


### 5.2 Možnosti za nadgradnje

Nadaljnje delo je mogoče na vseh delih študije.

- Fizikalni model in njegovo numerično rešitev bi bilo mogoče nadgraditi v tri dimenzije in analizirati hitrostno polje pri različnih vpadnih kotih vetra, ki je, kot je razvidno iz CIGRE razprav, zanimivo vprašanje.
- Numerično rešitev bi bilo mogoče nadgraditi z algoritmi za stabilizacijo advektivnega člena, kar bi omogočilo analizo prisilne konvekcije tudi za večje hitrosti vetra. V prvem koraku bi bilo smotrno implementirati adaptivno privetrno shemo.
- Iz eksperimentalnega stališča je zagotovo naslednji korak točno izmeriti snovne lastnosti vrvi. Predvsem emisivnost in toplotno prevodnost.
- Emisivnost se glede na priporočila standardov s časom spreminja in, kot smo videli, ima močan vpliv na izračune, zato bi bil iz stališča modela naslednji smiseln korak razviti model staranja vrvi.


## 6. Viri

[1] S. W. Churchill MB. A Correlating Equation for Forced Convection From Gases and Liquids to a Circular Cylinder in Crossflow. J Heat Transfer. 1977;99(2):300-6.
[2] McAdams WH. Heat Transmission. New York: McGraw-Hill Book Company Inc.; 1959.
[3] Zhukauskas A, Žiugžda J. Heat transfer of a cylinder in crossflow: Hemisphere Pub.; 1985.
[4] Morgan VT. The heat transfer from bare stranded conductors by natural and forced convection in air. International Journal of Heat and Mass Transfer 1973;16(11):2023-34.
[5] CIGRE. Guide for Thermal Rating Calculations of Overhead Lines. CIGRE; 2014.
[6] Rakovec J, Vrhovec T. Osnove Meteorologije: Društvo Matematikov Fizikov in Astronomov Slovenije; 2000.
[7] Dantzig J, Rappaz M. Solidification. Laussane: EPFL Press; 2009.
[8] Kosec G, Šarler B. Simulation of macrosegregation with mesosegregates in binary metallic casts by a meshless method. Eng Anal Bound Elem. 2014;45:36-44.
[9] Bejan A. Convection Heat Transfer New Jersey: John Wiley \& Sons; 2004.
[10] Jany P, Bejan A. Scaling theory of melting with natural convection in an enclosure. Int J Heat Mass Tran. 1987;31:1221-35.
[11] Yogesh J. Natural Convection: Heat and Mass Transfer: Elsevier Science Limited; 1980.
[12] Ingham D, Pop I. Transport Phenomena in Porous Media: Pergamon; 1998.
[13] Giangi M, Kowalewski TA, Stella F, Leonardi E. Natural convecrion during ice formation: numerical simulation vs. experimental results. Comp Assist Mech Eng Sc. 2000;7:321-42.
[14] Quillet G, Ciobanas A, Lehmann P, Fautrelle Y. A benchmark solidification experiment on an Sn-10\% wtBi alloy. Int J Heat Mass Tran. 2007;50:654-66
[15] Ahmad N, Combeau H, Desbiolles JL, Jalanti T, Lesoult G, Rappaz J, et al. Numerical simulation of macrosegreation: a comparison between finite volume method and finite element method predictions and a confrontation with experiments. Metall Mater Trans A. 1998;A29:617.
[16] Ferziger JH, Perić M. Computational Methods for Fluid Dynamics. Berlin: Springer; 2002.
[17] Kosec G, Šarler B. Numerical solution of natural convection problems. In: Kazi S, editor. Convection and Conduction Heat Transfer. Rijeka: InTech; 2011.
[18] Zienkiewicz OC, Taylor RL. The Finite Element Method: Fluid Dynamics. Boston: Elsevier Butterworth-Heinemann; 2005.
[19] de Vahl Davis G. Natural convection of air in a square cavity: a bench mark numerical solution. Int J Numer Meth Fl. 1983;3:249-64.
[20] Boetcher SKS. Natural Convection from Circular Cylinders. Daytona Beach: Springer; 2014.
[21] Morgan V. The overall convective heat transfer from smooth circular cylinders. Adv Heat Transf. 1975;1:199-264.
[22] Atmane MA, Chan VSS, Murray DB. Natural convection around a horizontal heated cylinder: The effects of vertical confinement. Int J Heat Mass Tran. 2003;46:3661-72. 10.1016/S0017-9310(03)00154-6.
[23] Cesinia G, Paroncinia M, Cortellab G., Manzanb M. Natural convection from a horizontal cylinder in a rectangular cavity. Int J Heat Mass Tran. 1999;42:1801-11.
[24] Wan DC, Patnaik BSV, Wei GW. A new benchmark quality solution for the buoyancy-driven cavity by discrete singular convolution. Numer Heat Transfer. 2001;B40:199-228.
[25] Kosec G, Šarler B. Solution of thermo-fluid problems by collocation with local pressure correction. Int J Numer Method H. 2008;18:868-82.
[26] Ni J, Beckermann C. Natural convection in a vertical enclosure filled with anisotropic porous media. JHT. 1991;113:1033-7.
[27] Demirdžić I, Lilek Ž, Perić M. Fluid flow and heat transfer test problems for non-orthogonal grids: Bench-mark solutions. Int J Numer Meth Fl. 1992;15:329-54.
[28] Roychowdhury DG, Das SK, Sundararajan T. Numerical simulation of natural convective heat transfer and fluid flow around a heated cylinder inside an enclosure. Heat and Mass Transfer. 2002;38:565-76. 10.1007/s002310100210.
[29] Mamun Molla M, Paul SC, Anwar Hossain M. Natural convection flow from a horizontal circular cylinder with uniform heat flux in presence of heat generation. Appl Math Model. 2009;33:3226-36. 10.1016/j.apm.2008.10.039.
[30] Elsherbiny SM, Teamah MA, Moussa AR. Natural convection heat transfer from an isothermal horizontal square cylinder. Alexandria Engineering Journal. 2017;56:181-7. 10.1016/j.aej.2016.09.020.
[31] Kumar De A, Dalal A. A numerical study of natural convection around a square, horizontal, heated cylinder placed in an enclosure. Int J Heat Mass Tran. 2006;49:4608-23. 10.1016/j.ijheatmasstransfer.2006.04.020.
[32] Wang P, Kahawita R, Nguyen TH. Numerical Computation Of The Natural Convection Flow About A Horizontal Cylinder Using Splines. Numerical Heat Transfer, Part A: Applications. 1990;17:191-215. 10.1080/10407789008944739.
[33] Golani R, Dhiman AK. Fluid flow and heat transfer across a circular cylinder in the unsteady flow regime. Int J Eng Sci. 2004;3:8-19.
[34] Bharti RP, Chhabra RP, Eswaran V. A numerical study of the steady forced convection heat transfer from an unconfined circular cylinder. Heat and Mass Transfer. 2007;43:639-48. 10.1007/s00231-006-0155-1.
[35] Berizzi A. The Italian 2003 blackout. IEEE Power Engineering Society General Meeting, 20042004. p. 1673-9 Vol.2.
[36] Schurig OR, Frick CW. Heating and Current-Carrying Capacity of Conductors for Outdoor service. General Electric Review. 1930;33:141-57.
[37] House HE, Tuttle PD. Current-Carrying Capacity of ACSR. AIEE Transactions on Power Apparatus and Systems. 1958:1169-78.
[38] McAdams WH. Heat Transmission: McGraw-Hill Inc.; 1954.
[39] Howington BS, Ramon GJ. Dynamic Thermal Line Rating Summary and Status of the State-of-the-Art Technology. IEEE Trans on power delivery. 1987;2:851-8.
[40] Morgan VT. The Thermal Rating of Overhead-Line Conductors. Electric Power Systems Research. 1981;5:119-39.
[41] Pytlak P, Musilek P, Lozowski E, Toth J. Modelling precipitation cooling of overhead conductors. Electric Power Systems Research. 2011;81:2147-54.
[42] Kosec G, Maksić M, Djurica V. Dynamic thermal rating of power lines - Model and measurements in rainy conditions. International Journal of Electrical Power \& Energy Systems. 2017;91:222-9. 10.1016/j.ijepes.2017.04.001.
[43] Rahman SA, Kopsidas K. Modelling of Convective Cooling on Conductor Thermal Rating Methods. The University of Manchester.
[44] IEEE Standard for Calculating the Current-Temperature Relationship of Bare Overhead Conductors. IEEE Std. 738-2012; 2014.
[45] Commission IE. Technical Committee 20 - Overhead Electrical Conductors. International Electrotechnical Commission; 2016.
[46] Arroyo A, Castro P, Martinez R, Manana M, Madrazo A, Lecuna R, et al. Comparison between IEEE and CIGRE Thermal Behaviour Standards and Measured Temperature on a $132-\mathrm{kV}$ Overhead Power Line. Energies. 2015;8:13660-71. 10.3390/en81212391.
[47] Makkonen L. Modeling power line icing in freezing precipitation. Atmospheric Research. 1998;46:131-42.
[48] Kosec G, Šarler B. Meshless aproach to solving freezing driven by a natural convection. Mater Sci Forum. 2008;649:205-10.
[49] Morgan VT. The radial temperature distribution and effective radial thermal conductivity in bare solid and stranded conductors. IEEE Transactions on Power Delivery 1990;5:1443-52.
[50] Faber TE. Fluid Dynamics for Physicists: Cambridge, University Press; 1995.
[51] Rahman MM, Siikonen T. An artificial compressibility method for viscous incompressible and low Mach number flows. Int J Numer Meth Eng. 2008;75:1320-40.
[52] Arpino F, Massarotti N, Mauro A, Nithiarasu P. Artificial compressibility based CBS solutions for double diffusive natural convection in cavities. Int J Numer Method H. 2013;23:205-25.
[53] Kosec G. A local numerical solution of a fluid-flow problem on an irregular domain. Adv Eng Softw. 2018;120:36-44. 10.1016/j.advengsoft.2016.05.010.
[54] Iglesias J, Watt G, Douglass D, Morgan V, Stephen R, Bertinat M, et al. Guide for Thermal Rating Calculations of Overhead Lines. In: CIGRE, editor.2014.
[55] Tsilingiris PT. Thermophysical and transport properties of humid air at temperature range between 0 and $100^{\circ} \mathrm{C}$. Energ Convers Manage. 2008;49:1098-110. 10.1016/j.enconman.2007.09.015.
[56] Ražnjević. Handbook of Thermodynamic Tables and Charts Bristol, PA: Hemisphere; 1976.
[57] Kuščer I, Žumer S. Toplota: termodinamika, statistična mehanika, transportni pojavi. Ljubljana: Društvo matematikov, fizikov in astronomov SR Slovenije; 1987.
[58] Trobec R, Kosec G. Parallel scientific computing : theory, algorithms, and applications of mesh based and meshless methods: Springer; 2015.
[59] Kosec G, Kolman M, Slak J. Utilities for solving PDEs with meshless methods. http://wwwe6.ijs.si/ParallelAndDistributedSystems/PDE_solver_utils/html/index.html.
[60] Hortmann M, Perić M, Scheuerer G. Finite volume multigrid prediction of laminar natural convection - bench-mark solutions. Int J Numer Meth Fl. 1990;11:189-207.
[61] Prax C, Sadat H, Salagnac P. Diffuse approximation method for solving natural convection in porous Media. Theor App T. 1996;22:215-23.
[62] Sadat H, Couturier S. Performance and accuracy of a meshless method for laminar natural convection. Numer Heat Transfer. 2000;B37:455-67.
[63] Divo E, Kassab AJ. Localized meshless modeling of natural-convective viscous flows. Numer Heat Transfer. 2007;B129:486-509.
[64] Manzari MT. An explicit finite element algorithm for convection heat transfer problems. International Journal of Numerical Methods for Heat and Fluid Flow. 1999;9:860-77.
[65] Šarler B. A radial basis function collocation approach in computational fluid dynamics. CMESComp Model Eng. 2005;7:185-93.
[66] Lage JL, Bejan A. The Ra-Pr domain of laminar natural convection in an enclosure heated from the side. Numer Heat Transfer. 1991;A19:21-41.
[67] Janssen RJA, Henkes RAWM. Accuracy of finite-volume disretizations for the bifurcating natural-convection flow in a square cavity. Numer Heat Transfer. 1993;B24:191-207.
[68] Nobile E. Simulation of time-dependent flow in cavities with the additive-correction multigrid method, part II: Apllications. Numer Heat Transfer. 1996;B30:341-50.
[69] Kosec G, Trobec R, Depolli M, Avbelj V, Krištofelc T, Souvent A, et al. Analiza preprečevanja nastajanja žleda z obratovalnimi ukrepi. 2016.

