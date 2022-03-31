from math import*
vardadienas = {"Laimnesis, Solvita, Solvija": 1, "Indulis, Ivo, Iva, Ivis": 2, "Miervaldis, Miervalda, Ringolds": 3, "Spodra, Ilva, Ilvita": 4, "Sīmanis, Zintis": 5, "Spulga, Arnita": 6, "Rota, Zigmārs, Juliāns, Digmārs": 7, "Gatis, Ivanda": 8, "Kaspars, Aksels, Alta": 9, "Tatjana, Dorisa": 10, "Smaida, Franciska": 11, "Reinis, Reina, Reinholds, Renāts": 12, "Harijs, Ārijs, Āris, Aira": 13, "Roberts, Roberta, Raitis, Raits": 14, "Fēlikss, Felicita": 15, "Lidija, Lida": 16, "Tenis, Dravis": 17, "Antons, Antis, Antonijs": 18, "Andulis, Alnis": 19, "Oļģerts, Orests, Aļģirds, Aļģis": 20, "Agnese, Agnija, Agne": 21, 'Austris': 22, "Grieta, Strauta, Rebeka": 23, "Krišs, Ksenija, Eglons, Egle": 24, "Zigurds, Sigurds, Sigvards": 25, "Ansis, Agnis, Agneta": 26, "Ilze, Ildze, Izolde": 27, "Kārlis, Spodris": 28, "Aivars, Valērijs, Bille": 29, "Tīna, Valentīna, Pārsla": 30, "Tekla, Violeta": 31, "Brigita, Indra, Indars, Indris": 32, "Spīdola, Sonora": 33, "Aīda, Ida, Vida": 34, "Daila, Veronika, Dominiks": 35, "Agate, Selga, Silga, Sinilga": 36, "Dace, Dārta, Dora": 37, "Nelda, Rihards, Ričards, Rišards": 38, "Aldona, Česlavs": 39, "Simona, Apolonija": 40, "Paulīne, Paula, Jasmīna": 41, "Laima, Laimdota": 42, "Karlīna, Līna": 43, "Malda, Melita": 44, 'Valentīns': 45, "Alvils, Olafs, Aloizs, Olavs": 46, "Jūlija, Džuljeta": 47, "Donats, Konstance": 48, "Kora, Kintija": 49, "Zane, Zuzanna": 50, "Vitauts, Smuidra, Smuidris": 51, "Eleonora, Ariadne": 52, "Ārija, Rigonda, Adrians, Adriāna, Adrija": 53, "Haralds, Almants": 54, "Diāna, Dina, Dins": 55, "Alma, Annemarija": 56, "Evelīna, Aurēlija, Mētra": 57, "Līvija, Līva, Andra": 58, "Skaidrīte, Justs, Skaidra": 59, '–': 60, "Ivars, Ilgvars": 61, "Lavīze, Luīze, Laila": 62, "Tālis, Tālavs, Marts": 63, "Alise, Auce, Enija": 64, "Austra, Aurora": 65, "Vents, Centis, Gotfrīds": 66, "Ella, Elmīra": 67, "Dagmāra, Marga, Margita": 68, 'Ēvalds': 69, "Silvija, Laimrota, Liliāna": 70, "Konstantīns, Agita": 71, "Aija, Aiva, Aivis": 72, "Ernests, Balvis": 73, "Matilde, Ulrika": 74, "Amilda, Amalda, Imalda": 75, "Guntis, Guntars, Guntris": 76, "Ģertrūde, Gerda": 77, "Ilona, Adelīna": 78, "Jāzeps, Juzefa": 79, "Made, Irbe": 80, "Una, Unigunde, Dzelme, Benedikts, Benedikta": 81, "Tamāra, Dziedra, Gabriels, Gabriela": 82, "Mirdza, Žanete, Žanna": 83, "Kazimirs, Izidors": 84, "Māra, Mārīte, Marita, Mare, Ģedimins": 85, "Eiženija, Ženija": 86, "Gustavs, Gusts, Tālrīts, Saulis": 87, "Gunta, Ginta, Gunda": 88, "Aldonis, Agija": 89, "Nanija, Ilgmārs": 90, "Gvido, Atvars": 91, "Dagnis, Dagne": 92, 'Irmgarde': 93, "Daira, Dairis, Daiva, Daivis": 94, "Valda, Herta, Ārvalda, Ārvalds, Ārvaldis": 95, "Vija, Vidaga, Aivija": 96, "Zinta, Vīlips, Filips, Dzinta": 97, "Zina, Zinaīda, Helmuts": 98, "Edgars, Danute, Dana, Dans": 99, "Valērija, Žubīte, Alla": 100, "Anita, Anitra, Zīle, Annika": 101, "Hermanis, Vilmārs": 102, "Jūlijs, Ainis": 103, "Egils, Egīls, Nauris": 104, "Strauja, Gudrīte": 105, "Aelita, Gastons": 106, "Mintauts, Alfs, Bernadeta": 107, "Rūdolfs, Viviāna, Rūdis": 108, "Laura, Jadviga": 109, "Vēsma, Fanija": 110, "Mirta, Ziedīte": 111, "Marģers, Anastasija": 112, "Armands, Armanda": 113, "Jurģis, Juris, Georgs": 114, "Visvaldis, Nameda, Ritvaldis, Ritums": 115, "Līksma, Bārbala": 116, "Alīna, Sandris, Rūsiņš": 117, "Tāle, Raimonda, Raina, Klementīne": 118, "Gundega, Terēze": 119, "Vilnis, Raimonds, Laine": 120, "Lilija, Liāna": 121, 'Ziedonis': 122, "Zigmunds, Sigmunds, Zigismunds": 123, "Gints, Uvis": 124, "Vizbulīte, Viola, Vijolīte": 125, "Ģirts, Ģederts": 126, "Gaidis, Didzis": 127, "Henriete, Henrijs, Jete, Enriko": 128, "Staņislavs, Staņislava, Stefānija": 129, "Klāvs, Einārs, Ervīns": 130, "Maija, Paija": 131, "Milda, Karmena, Manfreds": 132, "Valija, Ināra, Ina, Inārs": 133, "Irēna, Irīna, Ira, Iraīda": 134, "Krišjānis, Elfa, Aivita, Elvita": 135, "Sofija, Taiga, Airita, Arita": 136, "Edvīns, Edijs": 137, "Herberts, Dailis, Umberts": 138, "Inese, Inesis, Ēriks": 139, "Lita, Sibilla, Teika": 140, "Venta, Salvis, Selva": 141, "Ernestīne, Ingmārs, Akvelīna": 142, 'Emīlija. Visu neparasto un kalendāros neierakstīto vārdu diena': 143, "Leontīne, Leokādija, Lonija, Ligija": 144, "Ilvija, Marlēna, Ziedone": 145, "Anšlavs, Junora": 146, "Edvards, Edvarts, Eduards, Varis": 147, "Dzidra, Gunita, Loreta, Dzidris": 148, "Vilis, Vilhelms": 149, "Maksis, Maksims, Raivis, Raivo": 150, "Vitolds, Lolita, Letīcija": 151, "Alīda, Jūsma": 152, "Biruta, Mairita, Bernedīne": 153, "Lība, Emma": 154, "Inta, Ineta, Intra": 155, "Elfrīda, Sintija, Sindija": 156, "Igors, Margots, Ingvars": 157, "Ingrīda, Ardis": 158, "Gaida, Arnis, Arno": 159, "Frīdis, Frīda, Mundra": 160, "Ligita, Gita": 161, "Malva, Anatols, Anatolijs": 162, "Ingus, Mairis, Vidvuds": 163, "Nora, Lenora, Ija": 164, "Zigfrīds, Ainārs, Uva": 165, "Tija, Saiva, Sentis, Santis, Saivis": 166, "Baņuta, Žermēna, Vilija, Vits": 167, "Justīne, Juta": 168, "Artūrs, Artis": 169, "Alberts, Madis": 170, "Viktors, Nils": 171, "Rasma, Rasa, Maira": 172, "Emīls, Egita, Monvīds": 173, "Ludmila, Laimdots, Laimiņš": 174, 'Līga': 175, 'Jānis': 176, "Milija, Maiga": 177, "Ausma, Inguna, Ingūna, Inguns, Ausmis": 178, "Malvīne, Malvis": 179, "Viesturs, Kitija, Viestards": 180, "Pēteris, Pāvils, Pauls, Paulis": 181, "Tālivaldis, Mareks": 182, "Imants, Rimants, Ingars, Intars": 183, "Lauma, Ilvars, Halina": 184, "Benita, Everita, Verita, Emerita": 185, "Ulvis, Uldis, Sandis, Sandijs": 186, "Andžs, Andžejs, Edīte, Esmeralda": 187, "Anrijs, Arkādijs": 188, "Alda, Maruta": 189, "Antra, Adele, Ada": 190, "Zaiga, Asne, Asna": 191, "Lija, Olīvija, Olivers, Odrija": 192, "Leonora, Svens": 193, "Indriķis, Ints, Namejs": 194, "Margrieta, Margarita": 195, "Oskars, Ritvars, Anvars": 196, "Egons, Egmonts, Egija, Henriks, Heinrihs": 197, "Hermīne, Estere, Liepa": 198, "Aleksis, Aleksejs, Alekss": 199, "Rozālija, Roze": 200, "Jautrīte, Kamila, Digna, Sāra": 201, "Ritma, Ramona": 202, "Meldra, Meldris, Melisa": 203, "Marija, Marika, Marina": 204, "Magda, Magone, Mērija, Magdalēna": 205, "Kristīne, Kristīna, Krista, Kristiāna, Kristiāns": 206, "Jēkabs, Žaklīna": 207, "Anna, Ance, Annija": 208, "Marta, Dita, Dite": 209, "Cecīlija, Cilda": 210, "Edmunds, Edžus, Vidmants": 211, "Valters, Renārs, Regnārs": 212, "Rūta, Ruta, Angelika, Sigita": 213, "Albīns, Albīna": 214, "Normunds, Stefans": 215, 'Augusts': 216, "Romāns, Romualds, Romualda": 217, "Osvalds, Arvils": 218, "Askolds, Aisma": 219, "Alfrēds, Madars, Fredis": 220, "Mudīte, Vladislavs, Vladislava": 221, "Madara, Genoveva, Genovefa": 222, "Brencis, Audris, Inuta, Audra": 223, "Olga, Zita, Liega, Zigita": 224, "Vizma, Klāra": 225, "Elvīra, Velga, Rēzija": 226, "Zelma, Zemgus, Virma": 227, "Zenta, Dzelde, Zelda": 228, "Astra, Astrīda": 229, "Vineta, Oļegs": 230, "Liene, Helēna, Elena, Ellena, Liena": 231, "Melānija, Imanta": 232, "Bernhards, Boriss, Rojs": 233, "Janīna, Linda": 234, "Rudīte, Everts": 235, "Vitālijs, Ralfs, Valgudis": 236, "Bērtulis, Boļeslavs": 237, "Ludvigs, Ludis, Ivonna, Patrīcija, Patriks": 238, "Natālija, Tālija, Broņislavs, Broņislava": 239, "Žanis, Jorens, Alens": 240, "Auguste, Guste": 241, "Armīns, Vismants, Aiga": 242, "Alvis, Jolanta, Samanta": 243, "Vilma, Aigars": 244, "Ilmārs, Iluta, Austrums": 245, "Elīza, Lizete, Zete": 246, "Berta, Bella": 247, "Dzintra, Dzintara, Dzintars": 248, "Klaudija, Persijs, Vaida": 249, "Maigonis, Magnuss, Mariuss": 250, "Regīna, Ermīns": 251, 'Ilga': 252, "Bruno, Telma": 253, "Jausma, Albertīne": 254, "Signe, Signija": 255, "Erna, Evita, Eva": 256, "Iza, Izabella": 257, "Sanita, Santa, Sanda, Sanija, Sandija": 258, "Sandra, Gunvaldis, Gunvaris, Sondra": 259, "Asja, Asnate, Dāgs": 260, "Vera, Vaira, Vairis": 261, "Liesma, Elita, Alita": 262, "Verners, Muntis": 263, "Guntra, Ginters, Marianna": 264, "Modris, Matīss, Mariss": 265, "Māris, Mārica, Maigurs": 266, "Vanda, Veneranda, Venija": 267, "Agris, Agrita": 268, "Rodrigo, Rauls": 269, "Gundars, Kurts, Knuts": 270, "Ādolfs, Ilgonis": 271, "Sergejs, Svetlana, Lana": 272, "Miķelis, Mikus, Miks, Mihails": 273, "Elma, Menarda, Elna": 274, "Zanda, Lāsma, Zandis": 275, "Ilma, Skaidris": 276, "Elza, Ilizana": 277, "Modra, Francis, Dmitrijs": 278, "Amālija, Amēlija": 279, "Monika, Zilgma, Zilga": 280, "Daumants, Druvvaldis": 281, "Aina, Anete": 282, "Elga, Helga, Elgars": 283, "Arvīds, Arvis, Druvis": 284, "Monta, Tince, Silva": 285, "Valfrīds, Kira": 286, "Irma, Mirga": 287, "Vilhelmīne, Minna": 288, "Eda, Hedviga, Helvijs": 289, "Daiga, Dinija, Dinārs": 290, "Gaits, Karīna, Gaitis": 291, "Rolands, Rolanda, Ronalds, Erlends, Lūkass": 292, "Elīna, Drosma, Drosmis": 293, "Leonīds, Leonīda": 294, "Urzula, Severīns": 295, "Īrisa, Irīda, Airisa": 296, "Daina, Dainis, Dainida": 297, "Renāte, Modrīte, Mudrīte": 298, "Beāte, Beatrise": 299, "Amanda, Kaiva, Amanta": 300, "Lilita, Irita, Ita": 301, "Ņina, Ninona, Antoņina, Oksana": 302, "Laimonis, Elvijs, Elva, Elvis, Laimis": 303, "Nadīna, Ulla, Adīna": 304, "Valts, Rinalds, Rinalda": 305, 'Ikars': 306, "Vivita, Dzīle, Viva": 307, "Ērika, Dagnija": 308, "Atis, Otomārs, Oto, Otto": 309, "Šarlote, Lote": 310, "Linards, Leons, Leo, Leonards, Leonarda": 311, "Helma, Lotārs": 312, "Aleksandra, Agra": 313, 'Teodors': 314, "Mārtiņš, Mārcis, Markuss, Marks": 315, "Ojārs, Rainers, Nellija": 316, "Kaija, Kornēlija": 317, "Eižens, Jevgeņijs, Jevgeņija": 318, "Fricis, Vikentijs, Vincents": 319, "Leopolds, Undīne, Unda": 320, "Banga, Glorija": 321, "Hugo, Uga, Uģis": 322, "Aleksandrs, Doloresa, Brīve": 323, "Elizabete, Liza, Līze, Betija": 324, "Anda, Andīna, Vigo": 325, "Zeltīte, Andis": 326, "Aldis, Alfons, Aldris": 327, "Zigrīda, Zigfrīda, Zigrīds": 328, "Velta, Velda": 329, "Katrīna, Kate, Kadrija, Trīne, Katrīne": 330, "Konrāds, Sebastians": 331, "Lauris, Norberts": 332, "Rita, Vita, Olita": 333, "Ignats, Virgīnija": 334, "Andrievs, Andrejs, Andris": 335, "Arnolds, Emanuels": 336, "Meta, Sniedze": 337, "Evija, Raita, Jogita": 338, "Baiba, Barbara, Barba": 339, "Sabīne, Sarma, Klaudijs": 340, "Nikolajs, Niklāvs, Niks, Nikola": 341, "Antonija, Anta, Dzirkstīte": 342, "Gunārs, Vladimirs, Gunis": 343, "Tabita, Sarmīte": 344, "Guna, Judīte": 345, "Voldemārs, Valdemārs, Valdis": 346, "Otīlija, Iveta": 347, "Lūcija, Veldze": 348, "Auseklis, Gaisma": 349, "Johanna, Hanna, Jana": 350, 'Alvīne': 351, "Hilda, Teiksma": 352, "Kristaps, Kristofers, Krists, Klinta, Kristers": 353, "Lelde, Sarmis": 354, "Arta, Minjona": 355, "Toms, Tomass, Saulcerīte": 356, "Saulvedis, Saule": 357, "Viktorija, Balva": 358, "Ādams, Ieva": 359, "Stella, Larisa": 360, "Dainuvīte, Gija, Megija": 361, "Elmārs, Inita, Helmārs": 362, "Inga, Ivita, Irvita, Ingeborga": 363, "Solveiga, Ilgona": 364, "Dāvids, Dāvis, Dāniels, Daniela, Daniels": 365, "Silvestrs, Silvis, Kalvis": 366}
def atrast_vardus(l):
    for key, value in vardadienas.items():
        if l == value:
            return key
    
izvele = int(input('Lai izmantotu kalendāru ievadiet 1, lai meklētu vārda dienas, nospiediet 2 - '))
if izvele == 1:
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
    print('vārda dienas svin - ', atrast_vardus(DOY))

elif izvele == 2:
    
    def atrast_datumu(l):
        for key, value in vardadienas.items():
            if l in key:
                return value              
    vards = input('ievadiet vārdu, kuru vēlaties meklēt - ')
    DOY = atrast_datumu(vards)
    if DOY == None:
        print('Vārds netika atrasts :(')
    i = 0
    while DOY >=0:
        i+=1
        if i==1: t=31
        elif i==2: t=29
        elif i==3: t=31
        elif i==4: t=30 
        elif i==5: t=31
        elif i==6: t=30
        elif i==7: t=31 
        elif i==8: t=31 
        elif i==9: t=30 
        elif i==10: t=31
        elif i==11: t=30
        elif i==12: t=31 
        DOY = DOY-t
    M=(DOY+t)
    print(vards, ' vārda dienu svin - ',str(M).zfill(2), '.' ,str(i).zfill(2),'.',sep='')