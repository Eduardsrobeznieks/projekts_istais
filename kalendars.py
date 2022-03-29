from math import*
m = int(input('ievadiet mēneša numuru  - '))
M=m
d = int(input('ievadiet datumu - '))
Y = int(input('ievadiet gadu - '))

#nosaka gada dienu
s=0
DOY=0
while M>1:
    M=M-1
    if M==1: t=31
    elif M==2: t=29
    elif M==3: t=31
    elif M==4: t=30 
    elif M==5: t=31
    elif M==6: t=30
    elif M==7: t=31 
    elif M==8: t=31 
    elif M==9: t=30 
    elif M==10: t=31
    elif M==11: t=30
    elif M==12: t=31 
    s+=t
DOY=s+d

#katram menesim savs dienu skaits un b vajag algoritmam talak
if m==1: b=36 ; n=31 ; menesis='Janvāris'
elif m==2: 
    b=39 ; menesis='Februāris'
    if (Y % 100) % 4==0: n=29
    else: n=28
elif m==3: b=10 ; n=31 ; menesis='Marts'
elif m==4: b=13 ; n=30 ; menesis='Aprīlis'
elif m==5: b=15 ; n=31 ; menesis='Maijs'
elif m==6: b=18 ; n=30 ; menesis='Jūnijs'
elif m==7: b=20 ; n=31 ; menesis='Jūlijs'
elif m==8: b=23 ; n=31 ; menesis='Augusts'
elif m==9: b=26 ; n=30 ; menesis='Septembris'
elif m==10: b=28 ; n=31 ; menesis='Oktobis'
elif m==11: b=31 ; n=30 ; menesis='Novembris'
elif m==12: b=33 ; n=31 ; menesis='Decembris'
else: print('FATAL ERROR 404 ')

print('')
print('        ',menesis,Y)

#algoritms atrod nedelas dienu datumam, magija
if m==1 or m==2:
    Y=Y-1
y = Y % 100
c = (Y-y)/100
w = (b + floor(y/4) + floor(c/4) + d + y -2*c) % 7 
d0 = int((b + floor(y/4) + floor(c/4) + 1 + y -2*c) % 7 - 1) #menesa 1.diena
if d0==-1: d0=6
elif d0==0: d0=7

#izprinte vizualu kalendaru
print('Mo  Tu  We  Th  Fr  Sa  Su')
for k in range(0,36,7):
    for i in range(1,8):
        Q=i-d0+1+k
        if Q == d:
            print('{:^4}'.format('XX'), end=(''))
        else:
            if Q<=0 or Q>n :
                print('    ', end=(''))
            else:
                print('{:^4}'.format(Q), end=(''))
    print(' ')
    
if w==2: print('pirmdiena')
if w==3: print('otrdiena')
if w==4: print('trešdiena')
if w==5: print('ceturtdiena')
if w==6: print('piektdiena')
if w==0: print('sestdiena')
if w==1: print('svētdiena')

vardadienas = {"Laimnesis, Solvita, Solvija": 1, "Indulis, Ivo, Iva, Ivis": 2, "Miervaldis, Miervalda, Ringolds": 3, "Spodra, Ilva, Ilvita": 4, "Sīmanis, Zintis": 5, "Spulga, Arnita": 6, "Rota, Zigmārs, Juliāns, Digmārs": 7, "Gatis, Ivanda": 8, "Kaspars, Aksels, Alta": 9, "Tatjana, Dorisa": 10, "Smaida, Franciska": 11, "Reinis, Reina, Reinholds, Ren?ts": 12, "Harijs, ?rijs, ?ris, Aira": 13, "Roberts, Roberta, Raitis, Raits": 14, "F?likss, Felicita": 15, "Lidija, Lida": 16, "Tenis, Dravis": 17, "Antons, Antis, Antonijs": 18, "Andulis, Alnis": 19, "O??erts, Orests, A??irds, A??is": 20, "Agnese, Agnija, Agne": 21, 'Austris': 22, "Grieta, Strauta, Rebeka": 23, "Krišs, Ksenija, Eglons, Egle": 24, "Zigurds, Sigurds, Sigvards": 25, "Ansis, Agnis, Agneta": 26, "Ilze, Ildze, Izolde": 27, "K?rlis, Spodris": 28, "Aivars, Val?rijs, Bille": 29, "T?na, Valent?na, P?rsla": 30, "Tekla, Violeta": 31, "Brigita, Indra, Indars, Indris": 32, "Sp?dola, Sonora": 33, "A?da, Ida, Vida": 34, "Daila, Veronika, Dominiks": 35, "Agate, Selga, Silga, Sinilga": 36, "Dace, D?rta, Dora": 37, "Nelda, Rihards, Ri?ards, Rišards": 38, "Aldona, ?eslavs": 39, "Simona, Apolonija": 40, "Paul?ne, Paula, Jasm?na": 41, "Laima, Laimdota": 42, "Karl?na, L?na": 43, "Malda, Melita": 44, "Valent?ns": 45, "Alvils, Olafs, Aloizs, Olavs": 46, "J?lija, Džuljeta": 47, "Donats, Konstance": 48, "Kora, Kintija": 49, "Zane, Zuzanna": 50, "Vitauts, Smuidra, Smuidris": 51, "Eleonora, Ariadne": 52, "?rija, Rigonda, Adrians, Adri?na, Adrija": 53, "Haralds, Almants": 54, "Di?na, Dina, Dins": 55, "Alma, Annemarija": 56, "Evel?na, Aur?lija, M?tra": 57, "L?vija, L?va, Andra": 58, "Skaidr?te, Justs, Skaidra": 59, " ": 60, "Ivars, Ilgvars": 61, "Lav?ze, Lu?ze, Laila": 62, "T?lis, T?lavs, Marts": 63, "Alise, Auce, Enija": 64, "Austra, Aurora": 65, "Vents, Centis, Gotfr?ds": 66, "Ella, Elm?ra": 67, "Dagm?ra, Marga, Margita": 68, 'Ēvalds': 69, "Silvija, Laimrota, Lili?na": 70, "Konstant?ns, Agita": 71, "Aija, Aiva, Aivis": 72, "Ernests, Balvis": 73, "Matilde, Ulrika": 74, "Amilda, Amalda, Imalda": 75, "Guntis, Guntars, Guntris": 76, "?ertr?de, Gerda": 77, "Ilona, Adel?na": 78, "J?zeps, Juzefa": 79, "Made, Irbe": 80, "Una, Unigunde, Dzelme, Benedikts, Benedikta": 81, "Tam?ra, Dziedra, Gabriels, Gabriela": 82, "Mirdza, Žanete, Žanna": 83, "Kazimirs, Izidors": 84, "M?ra, M?r?te, Marita, Mare, ?edimins": 85, "Eiženija, Ženija": 86, "Gustavs, Gusts, T?lr?ts, Saulis": 87, "Gunta, Ginta, Gunda": 88, "Aldonis, Agija": 89, "Nanija, Ilgm?rs": 90, "Gvido, Atvars": 91, "Dagnis, Dagne": 92, "Irmgarde": 93, "Daira, Dairis, Daiva, Daivis": 94, "Valda, Herta, ?rvalda, ?rvalds, ?rvaldis": 95, "Vija, Vidaga, Aivija": 96, "Zinta, V?lips, Filips, Dzinta": 97, "Zina, Zina?da, Helmuts": 98, "Edgars, Danute, Dana, Dans": 99, "Val?rija, Žub?te, Alla": 100, "Anita, Anitra, Z?le, Annika": 101, "Hermanis, Vilm?rs": 102, "J?lijs, Ainis": 103, "Egils, Eg?ls, Nauris": 104, "Strauja, Gudr?te": 105, "Aelita, Gastons": 106, "Mintauts, Alfs, Bernadeta": 107, "R?dolfs, Vivi?na, R?dis": 108, "Laura, Jadviga": 109, "V?sma, Fanija": 110, "Mirta, Zied?te": 111, "Mar?ers, Anastasija": 112, "Armands, Armanda": 113, "Jur?is, Juris, Georgs": 114, "Visvaldis, Nameda, Ritvaldis, Ritums": 115, "L?ksma, B?rbala": 116, "Al?na, Sandris, R?si?š": 117, "T?le, Raimonda, Raina, Klement?ne": 118, "Gundega, Ter?ze": 119, "Vilnis, Raimonds, Laine": 120, "Lilija, Li?na": 121, 'Ziedonis': 122, "Zigmunds, Sigmunds, Zigismunds": 123, "Gints, Uvis": 124, "Vizbul?te, Viola, Vijol?te": 125, "?irts, ?ederts": 126, "Gaidis, Didzis": 127, "Henriete, Henrijs, Jete, Enriko": 128, "Sta?islavs, Sta?islava, Stef?nija": 129, "Kl?vs, Ein?rs, Erv?ns": 130, "Maija, Paija": 131, "Milda, Karmena, Manfreds": 132, "Valija, In?ra, Ina, In?rs": 133, "Ir?na, Ir?na, Ira, Ira?da": 134, "Krišj?nis, Elfa, Aivita, Elvita": 135, "Sofija, Taiga, Airita, Arita": 136, "Edv?ns, Edijs": 137, "Herberts, Dailis, Umberts": 138, "Inese, Inesis, ?riks": 139, "Lita, Sibilla, Teika": 140, "Venta, Salvis, Selva": 141, "Ernest?ne, Ingm?rs, Akvel?na": 142, 'Emīlija. Visu neparasto un kalend?ros neierakstīto vārdu diena': 143, "Leont?ne, Leok?dija, Lonija, Ligija": 144, "Ilvija, Marl?na, Ziedone": 145, "Anšlavs, Junora": 146, "Edvards, Edvarts, Eduards, Varis": 147, "Dzidra, Gunita, Loreta, Dzidris": 148, "Vilis, Vilhelms": 149, "Maksis, Maksims, Raivis, Raivo": 150, "Vitolds, Lolita, Let?cija": 151, "Al?da, J?sma": 152, "Biruta, Mairita, Berned?ne": 153, "L?ba, Emma": 154, "Inta, Ineta, Intra": 155, "Elfr?da, Sintija, Sindija": 156, "Igors, Margots, Ingvars": 157, "Ingr?da, Ardis": 158, "Gaida, Arnis, Arno": 159, "Fr?dis, Fr?da, Mundra": 160, "Ligita, Gita": 161, "Malva, Anatols, Anatolijs": 162, "Ingus, Mairis, Vidvuds": 163, "Nora, Lenora, Ija": 164, "Zigfr?ds, Ain?rs, Uva": 165, "Tija, Saiva, Sentis, Santis, Saivis": 166, "Ba?uta, Žerm?na, Vilija, Vits": 167, "Just?ne, Juta": 168, "Art?rs, Artis": 169, "Alberts, Madis": 170, "Viktors, Nils": 171, "Rasma, Rasa, Maira": 172, "Em?ls, Egita, Monv?ds": 173, "Ludmila, Laimdots, Laimi?š": 174, 'Līga': 175, 'Jānis': 176, "Milija, Maiga": 177, "Ausma, Inguna, Ing?na, Inguns, Ausmis": 178, "Malv?ne, Malvis": 179, "Viesturs, Kitija, Viestards": 180, "P?teris, P?vils, Pauls, Paulis": 181, "T?livaldis, Mareks": 182, "Imants, Rimants, Ingars, Intars": 183, "Lauma, Ilvars, Halina": 184, "Benita, Everita, Verita, Emerita": 185, "Ulvis, Uldis, Sandis, Sandijs": 186, "Andžs, Andžejs, Ed?te, Esmeralda": 187, "Anrijs, Ark?dijs": 188, "Alda, Maruta": 189, "Antra, Adele, Ada": 190, "Zaiga, Asne, Asna": 191, "Lija, Ol?vija, Olivers, Odrija": 192, "Leonora, Svens": 193, "Indri?is, Ints, Namejs": 194, "Margrieta, Margarita": 195, "Oskars, Ritvars, Anvars": 196, "Egons, Egmonts, Egija, Henriks, Heinrihs": 197, "Herm?ne, Estere, Liepa": 198, "Aleksis, Aleksejs, Alekss": 199, "Roz?lija, Roze": 200, "Jautr?te, Kamila, Digna, S?ra": 201, "Ritma, Ramona": 202, "Meldra, Meldris, Melisa": 203, "Marija, Marika, Marina": 204, "Magda, Magone, M?rija, Magdal?na": 205, "Krist?ne, Krist?na, Krista, Kristi?na, Kristi?ns": 206, "J?kabs, Žakl?na": 207, "Anna, Ance, Annija": 208, "Marta, Dita, Dite": 209, "Cec?lija, Cilda": 210, "Edmunds, Edžus, Vidmants": 211, "Valters, Ren?rs, Regn?rs": 212, "R?ta, Ruta, Angelika, Sigita": 213, "Alb?ns, Alb?na": 214, "Normunds, Stefans": 215, 'Augusts': 216, "Rom?ns, Romualds, Romualda": 217, "Osvalds, Arvils": 218, "Askolds, Aisma": 219, "Alfr?ds, Madars, Fredis": 220, "Mud?te, Vladislavs, Vladislava": 221, "Madara, Genoveva, Genovefa": 222, "Brencis, Audris, Inuta, Audra": 223, "Olga, Zita, Liega, Zigita": 224, "Vizma, Kl?ra": 225, "Elv?ra, Velga, R?zija": 226, "Zelma, Zemgus, Virma": 227, "Zenta, Dzelde, Zelda": 228, "Astra, Astr?da": 229, "Vineta, O?egs": 230, "Liene, Hel?na, Elena, Ellena, Liena": 231, "Mel?nija, Imanta": 232, "Bernhards, Boriss, Rojs": 233, "Jan?na, Linda": 234, "Rud?te, Everts": 235, "Vit?lijs, Ralfs, Valgudis": 236, "B?rtulis, Bo?eslavs": 237, "Ludvigs, Ludis, Ivonna, Patr?cija, Patriks": 238, "Nat?lija, T?lija, Bro?islavs, Bro?islava": 239, "Žanis, Jorens, Alens": 240, "Auguste, Guste": 241, "Arm?ns, Vismants, Aiga": 242, "Alvis, Jolanta, Samanta": 243, "Vilma, Aigars": 244, "Ilm?rs, Iluta, Austrums": 245, "El?za, Lizete, Zete": 246, "Berta, Bella": 247, "Dzintra, Dzintara, Dzintars": 248, "Klaudija, Persijs, Vaida": 249, "Maigonis, Magnuss, Mariuss": 250, "Reg?na, Erm?ns": 251, 'Ilga': 252, "Bruno, Telma": 253, "Jausma, Albert?ne": 254, "Signe, Signija": 255, "Erna, Evita, Eva": 256, "Iza, Izabella": 257, "Sanita, Santa, Sanda, Sanija, Sandija": 258, "Sandra, Gunvaldis, Gunvaris, Sondra": 259, "Asja, Asnate, D?gs": 260, "Vera, Vaira, Vairis": 261, "Liesma, Elita, Alita": 262, "Verners, Muntis": 263, "Guntra, Ginters, Marianna": 264, "Modris, Mat?ss, Mariss": 265, "M?ris, M?rica, Maigurs": 266, "Vanda, Veneranda, Venija": 267, "Agris, Agrita": 268, "Rodrigo, Rauls": 269, "Gundars, Kurts, Knuts": 270, "?dolfs, Ilgonis": 271, "Sergejs, Svetlana, Lana": 272, "Mi?elis, Mikus, Miks, Mihails": 273, "Elma, Menarda, Elna": 274, "Zanda, L?sma, Zandis": 275, "Ilma, Skaidris": 276, "Elza, Ilizana": 277, "Modra, Francis, Dmitrijs": 278, "Am?lija, Am?lija": 279, "Monika, Zilgma, Zilga": 280, "Daumants, Druvvaldis": 281, "Aina, Anete": 282, "Elga, Helga, Elgars": 283, "Arv?ds, Arvis, Druvis": 284, "Monta, Tince, Silva": 285, "Valfr?ds, Kira": 286, "Irma, Mirga": 287, "Vilhelm?ne, Minna": 288, "Eda, Hedviga, Helvijs": 289, "Daiga, Dinija, Din?rs": 290, "Gaits, Kar?na, Gaitis": 291, "Rolands, Rolanda, Ronalds, Erlends, L?kass": 292, "El?na, Drosma, Drosmis": 293, "Leon?ds, Leon?da": 294, "Urzula, Sever?ns": 295, "?risa, Ir?da, Airisa": 296, "Daina, Dainis, Dainida": 297, "Ren?te, Modr?te, Mudr?te": 298, "Be?te, Beatrise": 299, "Amanda, Kaiva, Amanta": 300, "Lilita, Irita, Ita": 301, "?ina, Ninona, Anto?ina, Oksana": 302, "Laimonis, Elvijs, Elva, Elvis, Laimis": 303, "Nad?na, Ulla, Ad?na": 304, "Valts, Rinalds, Rinalda": 305, 'Ikars': 306, "Vivita, Dz?le, Viva": 307, "?rika, Dagnija": 308, "Atis, Otom?rs, Oto": 309, "Šarlote, Lote": 310, "Linards, Leons, Leo, Leonards, Leonarda": 311, "Helma, Lot?rs": 312, "Aleksandra, Agra": 313, 'Teodors': 314, "M?rti?š, M?rcis, Markuss, Marks": 315, "Oj?rs, Rainers, Nellija": 316, "Kaija, Korn?lija": 317, "Eižens, Jevge?ijs, Jevge?ija": 318, "Fricis, Vikentijs, Vincents": 319, "Leopolds, Und?ne, Unda": 320, "Banga, Glorija": 321, "Hugo, Uga, U?is": 322, "Aleksandrs, Doloresa, Br?ve": 323, "Elizabete, Liza, L?ze, Betija": 324, "Anda, And?na, Vigo": 325, "Zelt?te, Andis": 326, "Aldis, Alfons, Aldris": 327, "Zigr?da, Zigfr?da, Zigr?ds": 328, "Velta, Velda": 329, "Katr?na, Kate, Kadrija, Tr?ne, Katr?ne": 330, "Konr?ds, Sebastians": 331, "Lauris, Norberts": 332, "Rita, Vita, Olita": 333, "Ignats, Virg?nija": 334, "Andrievs, Andrejs, Andris": 335, "Arnolds, Emanuels": 336, "Meta, Sniedze": 337, "Evija, Raita, Jogita": 338, "Baiba, Barbara, Barba": 339, "Sab?ne, Sarma, Klaudijs": 340, "Nikolajs, Nikl?vs, Niks, Nikola": 341, "Antonija, Anta, Dzirkst?te": 342, "Gun?rs, Vladimirs, Gunis": 343, "Tabita, Sarm?te": 344, "Guna, Jud?te": 345, "Voldem?rs, Valdem?rs, Valdis": 346, "Ot?lija, Iveta": 347, "L?cija, Veldze": 348, "Auseklis, Gaisma": 349, "Johanna, Hanna, Jana": 350, 'Alvīne': 351, "Hilda, Teiksma": 352, "Kristaps, Kristofers, Krists, Klinta, Kristers": 353, "Lelde, Sarmis": 354, "Arta, Minjona": 355, "Toms, Tomass, Saulcer?te": 356, "Saulvedis, Saule": 357, "Viktorija, Balva": 358, "?dams, Ieva": 359, "Stella, Larisa": 360, "Dainuv?te, Gija, Megija": 361, "Elm?rs, Inita, Helm?rs": 362, "Inga, Ivita, Irvita, Ingeborga": 363, "Solveiga, Ilgona": 364, "D?vids, D?vis, D?niels, Daniela, Daniels": 365, "Silvestrs, Silvis, Kalvis": 366}
def atrast(l):
    for key, value in vardadienas.items():
        if l == value:
            return key
print('vārda dienas svin - ', atrast(DOY))