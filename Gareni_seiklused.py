import time
import random

print("Tere tulemast mängu Gareni seiklused")
nimi = input("Sisesta nimi: ")

hp=100
mana=8
hõbe=500
potion=0

def esimene(x): #kodu juures
    global hp
    global hõbe
    if x.lower() == "jah":
        time.sleep(1)
        print("Andsid talle 5 hõbedat ja liigud rahulikult edasi.")
        hõbe-=5
    elif x.lower() == "ei":
        time.sleep(1)
        hp = hp - 5
        print("Kodutu viskas sind pudeliga selga ja sa kaotasid 5 elupunkti. Sul on alles " + str(hp) + " elupunkti.")
        
    
def teine(x): #mets
    global hp
    if x.lower() == "liigun edasi":
        time.sleep(1)
        print("Liikudes jälgid pingsalt oma ümbrust, aga sa ei näe kedagi")
    elif x.lower() == "jooksen":
        time.sleep(2)
        print("Jooksed paarsada meetrit edasi ja peidad ennast põõsa taha")
        time.sleep(2)
        print("Põõsas on vaablasepesa ja nad nõelavad sind mitu korda.")
        time.sleep(2)
        print("Jooksed ruttu eemale ja jääd istuma.")
        põõsas = input("Kas kaotad elupunkte või valmistad endale salvi 2 tegevuspunktiga? (elupunktid/salv)")
        while põõsas.lower()!= "elupunktid" and põõsas.lower()!="salv":
            print("Sellist vastust ei saa anda. Proovi uuesti.")
            põõsas=input("Kas kasutad salvi või kaotad elupunkte? (elupunktid/salv)")
        if põõsas.lower() == "salv":
            time.sleep(1)
            print("Pärast salvi pealemäärimist tunned end hästi ja liigud edasi.")
            global mana
            mana-=2  
        elif põõsas.lower() == "elupunktid":
            print("Liigud vaikselt edasi aga ei tunne ennast väga hästi.")
            time.sleep(2)
            vaablane = random.randint(4, 15)
            hp-=vaablane
            print("Kaotasid "+ str(vaablane) + " elupunkti. Sul on alles " + str(hp) + " elupunkti.")

def kolmas(x): #magamine
    global hp
    global mana
    global hõbe
    global puud
    global kalad
    global teene
    teene=0
    if x.lower()=="magan":
        time.sleep(1)
        print("Hakkad otsima endale head kohta, kus laager püsti panna.")
        time.sleep(1)
        print("Leiad kaks head kohta: \n"
        "1)Puualune tihnik, mis väikse hõrendamise järel kaitseks tuule ja vihma eest. Ühtlasi saaks sealt lõkkemateriali ka järgmisteks kordadeks korjata. \n"
        "2)Jõeäärne liivarand, kus saaksid endale õhtuks pisut kala püüda ja oleks kindel, et mõni metsloom sind öösel segama ei tule.")
        time.sleep(1)
        valik1=input("Kumma valid? (tihnik/liivarand) ")
        while valik1.lower()!= "tihnik" and valik1.lower()!="liivarand":
            print("Sellist vastust ei saa anda. Proovi uuesti.")
            valik1=input("Kumma valid? (tihnik/liivarand) ")
        if valik1.lower()=="tihnik":
            kalad=0
            print("Hakkad tihnikus puid lõhkuma, kuni oled kogunud endale ka järgnevateks kordadeks 10 küttepuud. Jääd mõnusalt magama. \n")
            global puud
            puud=10
            time.sleep(10)
            print("Hommikul ärgates näed, et telk on ümbritsetud samasuguse tihnikuga nagu enne. Puude vahelt ilmub välja Ivern, metsade valvaja. \n"
                "Ivern laidab sind puude ilma loata lõhkumise eest ning annab sulle 2 valikut:")     
            print("1) Annad lahked puud tagasi, mistõttu kaotad oma 10 varu küttepuud. \n"
            "2) Maksad Ivernile 100 hõbedat trahvi. \n"
            "Salajase 3. võimalusena on sul ka Iverniga kaklema minna.")
            time.sleep(1)
            valik2=input("Mida otsustad teha? (puud/hõbe/kaklus) ")
            while valik2.lower()!= "puud" and valik2.lower()!="hõbe" and valik2.lower()!="kaklus":
                print("Sellist vastust ei saa anda. Proovi uuesti.")
                valik2=input("Mida otsustad teha? (puud/hõbe/kaklus) ")
            if valik2.lower()=="puud":
                puud=0
                print("Andsid Ivernile puud tagasi ja jätkad teekonda.")
            elif valik2.lower()=="hõbe":
                hõbe-=100
                print("Liigud muretult edasi, kuid su rahakott kergendus 100 hõbeda võrra. Sul on alles " + str(hõbe) + " hõbedat.")
            elif valik2.lower()=="kaklus":
                print("Hakkad oma mõõgaga Ivernit lööma. Ivern on aga väga osav kakleja ning lööb sind oma puiste oksadega vastu. \n "
                "Ja kestab...")
                Iverni_dämm=random.randint(5,10)
                time.sleep(3)
                print("Ja kestab...")
                Iverni_dämm+=random.randint(5,10)
                time.sleep(3)
                print("Ja kestab")
                Iverni_dämm+=random.randint(5,10)
                time.sleep(3)
                mana-=3
                hp-=Iverni_dämm
                print("Lõpuks on Ivern nõrgestatud ja ta pageb läbi põõsaste metsa tagasi. \n"
                "Võitlus oli aga väga väsitav ning kaotasid 3 mana. Lisaks sellele kaotasid ka " + str(Iverni_dämm) + " elu. \n"
                "Liigud edasi, kuid nüüd on sul alles "+ str(mana) + " tegevuspunkti ja " + str(hp) + " elu.")
        elif valik1.lower()=="liivarand":
            puud=0
            kalapüük=input("Sead liivaranda oma telgi püsti. Kas soovid enne magamaminekut ka kala püüda? (jah/ei) ")
            while kalapüük.lower()!= "jah" and kalapüük.lower()!="ei":
                print("Sellist vastust ei saa anda. Proovi uuesti.")
                kalapüük=input("Kas soovid kala püüda? (jah/ei) ")
            time.sleep(2)
            if kalapüük.lower()=="jah":
                print("Viskad konksu sisse ja hakkad kala püüdma.")
                time.sleep(1)
                kalad=0
                while kalapüük.lower()=="jah":
                    a=random.randint(0,2)
                    if a==2:
                        kalad+=1
                        print("Ohoo, saidki kala!")
                    else:
                        print("Kahjuks tuli konks tühjana veest välja.")
                    kalapüük=input("Kas soovid veel kala püüda? (jah/ei) ")
                    while kalapüük.lower()!= "jah" and kalapüük.lower()!="ei":
                        print("Sellist vastust ei saa anda. Proovi uuesti.")
                        kalapüük=input("Kas soovid veel kala püüda? (jah/ei) ")
            else:
                kalad=0
            print("Otsustad magama jääda.")
            time.sleep(5)
            print("Ohoh! Mis see veel on? Öösel kuuled rannas veidraid hääli. Piilud telgist välja ja näed, et seal seisab kahel jalal suur paks kala. \n"
            "Ka kala märkab sind ja kutsub sind telgist välja.")
            time.sleep(3)
            telgist_välja=input("Kas vastad müstilise kala kutsele? (jah/ei) ")
            while telgist_välja.lower()!= "jah" and telgist_välja.lower()!="ei":
                print("Sellist vastust ei saa anda. Proovi uuesti.")
                telgist_välja=input("Kas lähed telgist välja? (jah/ei) ")
            if telgist_välja.lower()=="jah":
                print("Lähened kalale ja see hakkab ennast tutvustama.")
                time.sleep(3)
                print("Oi, jälle üks ekslev inimeseloom! Mina olen Tahm Kench, jõgede kuningas. Kuidas oleks ühe mõistatusega? Kui sa võidad, jään ma sulle ühe teene võlgu. Kui sa aga kaotad, siis võtan ma su vete sügavustesse kaasa ja söön oma õhtusöögiks.")
                mäng=input("Kas mängid Tahm Kenchiga? (jah/ei)")
                while mäng.lower()!= "jah" and mäng.lower()!="ei":
                    print("Sellist vastust ei saa anda. Proovi uuesti.")
                    mäng=input("Kas mängid Tahm Kenchiga? (jah/ei) ")
                if mäng.lower()=="jah":
                    print("Hehee, suurepärane. Nonii, siit see tuleb: ")
                    mõistatus=random.randint(1,3)
                    if mõistatus==1:
                        vastus=input("Mis on kaelaga, kuid millel pole pead? ")
                        if vastus.lower()=="pudel":
                            print("Nojah, tundub, et täna jääb mul söömata! Jään sulle teene võlgu. Usu mind, tulen siis, kui sul mind kõige rohkem vaja.")
                            teene=1
                        else: 
                            print("Hehe, võid mulle head isu soovida. Siin sinu seiklus kahjuks katkeb.")
                            hp-=100
                            return
                    elif mõistatus==2:
                        vastus=input("Millel on palju hambaid, kuid kindlasti ei hammusta? ")
                        if vastus.lower()=="kamm":
                            print("Nojah, tundub, et täna jääb mul söömata! Jään sulle teene võlgu. Usu mind, tulen siis, kui sul mind kõige rohkem vaja.")
                            teene=1                        
                        else: 
                            print("Hehe, võid mulle head isu soovida. Siin sinu seiklus kahjuks katkeb.")
                            hp-=100
                            return
                    elif mõistatus==3:
                        vastus=input("Kes/mis on mees kaheteistkümne näoga?")
                        if vastus.lower()=="aasta":
                            print("Nojah, tundub, et täna jääb mul söömata! Jään sulle teene võlgu. Usu mind, tulen siis, kui sul mind kõige rohkem vaja.")
                            teene=1
                        else: 
                            print("Hehe, võid mulle head isu soovida. Siin sinu seiklus kahjuks katkeb.")
                            hp-=100
                            return
                else:
                    print("Hmm, võtan seda kui solvangut. Ega midagi, siis pean ma su ära neama. \n"
                    "Kry 'n moeiliker tyd op die volgende reis en maak die pyn pynliker as ooit!")
                    print("Tahm Kenchi needus hakkab sind räsima ja sa kaotad 30 elupunkti.")
                    hp-=30
                    time.sleep(1)
                    print("Lähed telki tagasi magama.")
                    time.sleep(10)
                    print("Oeh, oli ikka raju öö! Kas hakkad kohe edasi minema või proovid öösel kaotatud elupunkte tasa teha ja kala süüa. Kui kala on söödav, saad endale lisaks 5 elu, kui mürgine, kaotad 3.")
                    söö_kala=input("Kas sööd kala või lähed edasi? (kala/edasi) ")
                    while söö_kala.lower()!= "kala" and söö_kala.lower()!="edasi":
                        print("Sellist vastust ei saa anda. Proovi uuesti.")
                        söö_kala=input("Kas sööd kala või lähed edasi? (kala/edasi) ")
                    if söö_kala.lower()=="edasi":
                        print("Pakid oma asjad kokku ja jätkad oma teekonda " + str(hp) + " elu ja " + str(mana) + " tegevuspunktiga.")
                        return
                    else:
                        print("Püüdsid eile " + str(kalad)+ " kala.")
                        if kalad==0:
                            print("Kahjuks pole sul kotis ühtegi kala ja sa jätkad " + str(hp) + " elu ja " + str(mana) + " tegevuspunktiga.")
                        else:
                            for i in range(kalad):
                                kala_dämm=random.randint(1,3)
                                if kala_dämm==2:
                                    print("Kahjuks osutus antud kala mürgiseks ja sa kaotasid 3 elu.")
                                    hp-=3
                                else:
                                    print("Kala oli maitsev ning andis sulle juurde 5 elu!")
                                    hp+=5
                            print("Kala sai otsa ja sa jätkad teekonda " + str(hp) + " elu ja " + str(mana) + " tegevuspunktiga.")
            else:
                print("Lähed pisut hämmingus telki tagasi ja jääd uuesti magama.")
                time.sleep(10)
                print("Hommikul üles ärgates märkad sa, et sult on varastatud ära kõik kala ja 100 hõbedat! Vaadates unise peaga telgist välja, näed, et telgi ette on miskit liiva sisse kirjutatud. \n"
                "Su ees seisab: SEE ON TASU MINUGA MITTE MÄNGIMA TULEMISE EEST \n "
                "                                                  -Tahm Kench")
                time.sleep(4)
                kala=0
                hõbe-=100
                print("Vaatad veel ringi, lootes, et leiad öösel nähtud kala, kuid liivarannas oled vaid sina.")
                time.sleep(2)
                print("Pakid oma asjad kokku ja jätkad oma teekonda " + str(hp) + " elu ja " + str(mana) + " tegevuspunktiga. Peale vargust on sul on alles " + str(hõbe) + " hõbedat.")
                time.sleep(2)
            
    elif x.lower()=="jätkan":
        kalad=0
        puud=0
        print("Kõnnid edasi, kuid tunned juba suurt väsimust. Silmalaud hakkavad järjest raskemaks muutuma ning tasakaal hakkab kõikuma.")
        time.sleep(3)
        print("Hakkad pimeduses nägema mingit naiselikku kuju. Lähenedes paraneb silmanägemine ja sa näed naist juba üsna selgelt. \n"
        "Tal on blondid juuksed, millesse on seatud 3 roosi, lõõmavad oranžid silmad, mis sind võpatama panevad, seljas punane kleit, mis ilusam kui ükski teine kleit mida sa kunagi varem näinud oled.")
        time.sleep(3)
        print("Oled jõudnud naisele juba väga lähedale ja sa armud temasse esimesest silmapilgust. \n"
        "'Hei, kallis, ma olen Evelynn. Mida sa nii hilja üksi metsas teed? Ma tean siin lähedal ühte kohta, kus me saaksime turvaliselt kahekesi aega veeta ja ennast välja puhata ;)'")
        time.sleep(3)
        evelynn=input("Kas lähed Evelynniga kaasa? (jah/ei) ")
        while evelynn.lower()!= "jah" and evelynn.lower()!="ei":
                print("Sellist vastust ei saa anda. Proovi uuesti.")
                evelynn=input("Kas lähed Evelynniga kaasa? (jah/ei) ")
        if evelynn.lower()=="jah":
            print("'Oii, kallikene, ma ei jõua ära meie koosveedetud ööd ära oodata. Tule, las ma näitan teed.', sõnab Evelynn sulle võrgutavalt.")
            time.sleep(2)
            print("Peale üürikest jalutuskäiku ilmneb metsa tukast üks majakene. Maja näib küll mahajäätud välja, kuid iha Evelynni järele on jalutuskäiguga nii suureks kasvanud, et sa ei jõua oodata, et majja sisse astuda. \n"
            "Majja sisse astudes avaneb sulle aga verdtarretav vaatepilt: kümneid, kui mitte sadu verest tühjaks imetud surnukehi!")
            time.sleep(4)
            print("Sinu selja taga läheb uks pauguga kinni ja su ees ei seisa enam mitte veetlev punases kleidis preili, vaid suurte küüniste ja kihvadega (kuid siiski kurvikas ;)), deemon. \n"
            "'Oh teid mehi, te allute mulle nii kergesti, te igavesed SIMPid!' ütleb Evelynn samal hetkel kui ta sulle oma küünised sisse lööb.")
            time.sleep(4)
            print("Siin sinu seiklus kahjuks lõppeb.")
            hp-=100
            return
        else:
            kindel=input("Evelynn käib veel peale: 'Ma ju näen, et sa oled väsinud ja vajad pisut virgutust. Oled sa ikka oma valikus kindel? (jah/ei) ")
            while kindel.lower()!= "jah" and kindel.lower()!="ei":
                print("Sellist vastust ei saa anda. Proovi uuesti.")
                kindel=input("Kas oled ikka kindel? (jah/ei) ")
            if kindel.lower()=="ei":
                print("'Oii, kallikene, ma ei jõua ära meie koosveedetud ööd ära oodata. Tule, las ma näitan teed.', sõnab Evelynn sulle võrgutavalt.")
                time.sleep(2)
                print("Peale üürikest jalutuskäiku ilmneb metsa tukast üks majakene. Maja näib küll mahajäätud välja, kuid iha Evelynni järele on jalutuskäiguga nii suureks kasvanud, et sa ei jõua oodata, et majja sisse astuda. \n"
                "Majja sisse astudes avaneb sulle aga verdtarretav vaatepilt: kümneid, kui mitte sadu verest tühjaks imetud surnukehi!")
                time.sleep(4)
                print("Sinu selja taga läheb uks pauguga kinni ja su ees ei seisa enam mitte veetlev punases kleidis preili, vaid suurte küüniste ja kihvadega (kuid siiski kurvikas ;)), deemon. \n"
                "'Oh teid mehi, te allute mulle nii kergesti, te igavesed SIMPid!' ütleb Evelynn samal hetkel kui ta sulle oma küünised sisse lööb.")
                time.sleep(4)
                print("Siin sinu seiklus kahjuks lõppeb.")
                hp-=100
                return
            else:
                print("'No ise tead, rumaluke!' ütleb Evelynn. Hakkad veetlevast kaunitarist mööda astuma, kuid samal hetkel tunned mingi torget kõhus.")
                time.sleep(3)
                print("Sa vaatad selja taha ning su ees ei seisa enam mitte veetlev punases kleidis preili, vaid suurte küüniste ja kihvadega naisdeemon ning ta on sind just ühe oma pika küünisega pussitanud.")
                time.sleep(3)
                print("Asud vastulöögile, kuid Evelynn on tohutult väle, põikab su löögist kõrvale ning pussitab sind veelkord.")
                time.sleep(3)
                relv=input("Hakkad oma vööl olevaid asju kompama ning leiad sealt mõõga ja laterna. Kumma valid? (mõõk/latern)")
                while relv.lower()!= "latern" and relv.lower()!="mõõk":
                    print("Sellist vastust ei saa anda. Proovi uuesti.")
                    relv=input("Kumma võtad? (latern/mõõk)) ")
                time.sleep(1)
                if relv.lower()=="latern":
                    print("Paned laterna kiirelt põlema ning näed, kuidas Evelynn selle peale koheselt eemale tõmbub. Hakkad laternaga vehkima ning Evelynn kiljatab ning taganeb veelgi. Teed seda veel paar korda ning Evelynn kaob jäljetult pimedusse. \n"
                    "Olgugi et said Evelynnist jagu, kaotasid sa kahest torkest 30 elu.")
                    time.sleep(3)
                    hp-=30
                    print("Jätkad oma teekonda läbi pimeduse " + str(hp) + " elu ja " + str(mana) + " tegevuspunktiga. Õnneks hakkab vaikselt koitma ka juba hommikuvalgus.")
                else:
                    print("Hakkad mõõgaga vehkima, kuid Evelynn osutub taaskord liiga väledaks ning puikleb sinu hoopide eest. \n"
                    "Kaklus kestab pikalt ning sa üritad erinevatel viisidel Evelynni alistada, kuid lõpuks langed sa väsimuse ja võitluses saadud vigastuste tagajärjel.")
                    time.sleep(3)
                    print("Siin sinu seiklus kahjuks lõppeb.")
                    hp-=100
                    return
def neljas(): #Noxuse turul
    global mürk
    global potion
    global rüü
    global viiking
    global hõbe
    global puud
    global kalad
    if kalad>1:
        print("Müüd maha oma ülejäänud järelejäänud kalad ning saad selle eest ", kalad*5, " hõbedat.")
        hõbe+=kalad*5
    if puud>0:
        print("Müüd maha oma kogutud küttepuud ning saad selle eest ", puud*10, " hõbedat.")
        hõbe+=puud*10
    print("Kõnnid turul ringi ning sinu juurde tuleb mees, kellel on suu ette seotud valge mask ning seljal veider balloon rohelise vedelikuga. Ta pakub sulle mürki, mis enda mõõga peale tilgutades, muudab su \n"
    "löögid 1.5x tugevamaks. Selle mürgi hind on 300 hõbedat.")
    time.sleep(5)
    print("Seejärel satud sa putka juurde, kus pakutakse ravimtaimi, mis annavad sulle 10 elupunkti. Ühe annuse hind on 100 hõbedat.")
    time.sleep(3)
    print("Kõnnid veel edasi ning märkad relvaärimeest, kes müüb kõige kõvemast terasest rüüd. Kui keegi sulle pihta peaks saama, teevad vastase löögid 50% vähem kahju. Rüü hind on 100 hõbedat.")
    time.sleep(4)
    print("Viimaks tuleb sinu juurde viiking, kes ütleb, et on valmis igaks võitluseks ja loodab lihtsalt Valhallasse pääseda. Et ta sind aitaks, pead talle maksma 500 hõbedat.")
    time.sleep(4)
    print("Sul on alles ", hõbe, " hõbedat.")
    mürk=input("Kas ostad endale maskiga mehelt mürgi? (jah/ei) ")
    while mürk.lower()!= "jah" and mürk.lower()!="ei":
        print("Sellist vastust ei saa anda. Proovi uuesti.")
        mürk=input("Kas ostad endale maskiga mehelt mürgi? (jah/ei) ")
    if mürk.lower()=="jah":
        if hõbe<300:
            print("Sul pole selleks piisavalt raha.")
            mürk=1
        else:
            hõbe-=300
            mürk=1.5
    else:
        mürk=1
    print("Sul on alles ", hõbe, " hõbedat.")
    vpotion=input("Kas soovid ravimtaimi osta? (jah/ei)")
    while vpotion.lower()!= "jah" and vpotion.lower()!="ei":
        print("Sellist vastust ei saa anda. Proovi uuesti.")
        vpotion=input("Kas soovid ravimtaimi osta? (jah/ei)")
    while vpotion.lower()=="jah":
        potion=0
        if hõbe<100:
            print("Sul pole piisavalt raha.")
            break
        else:
            print("Ostsid ühe annuse ravimtaimi.")
            hõbe-=100
            potion+=1
            vpotion=input("Kas soovid veel ravimtaimi osta? (jah/ei)")
    print("Sul on alles ", hõbe, " hõbedat.")
    rüü=input("Kas soovid relvaärikalt rüüd osta? (jah/ei)")
    while rüü.lower()!= "jah" and rüü.lower()!="ei":
        print("Sellist vastust ei saa anda. Proovi uuesti.")
        rüü=input("Kas soovid rüü osta? (jah/ei)")
    if rüü.lower()=="jah":
        if hõbe<100:
            print("Sul pole piisavalt raha!")
            rüü=1
        else:
            print("Ostsid endale rüü!")
            rüü=0.5
            hõbe-=100
    else:
        rüü=1
    viiking=input("Kas palkad viikingi endale appi lumelindu päästma? (jah/ei) ")
    while viiking.lower()!= "jah" and viiking.lower()!="ei":
        print("Sellist vastust ei saa anda. Proovi uuesti.")
        viiking=input("Kas palkad viikingi endale appi lumelindu päästma? (jah/ei) ")
    if viiking.lower()=="jah":
        if hõbe<500:
            print("Sul pole piisavalt raha!")
        else:
            print("Viiking järgneb sulle kuhuiganes ja on valmis täitma igat käsku.")
            viiking=1
            hõbe-=500
def bossfight(): #Kaklus Dariusega
    global potion
    global hp
    dariuse_hp=100
    while dariuse_hp>0 or hp>0:
        if hp<30 and potion>0:
            joo_potioneid=input("Sul alles vähem, kui 30 elu! Kas soovid oma ravimtaimi kasutada, et 10 elu juurde saada? (jah/ei)")
            while joo_potioneid.lower()!= "jah" and joo_potioneid.lower()!="ei":
                print("Sellist vastust ei saa anda. Proovi uuesti.")
                joo_potioneid=input("Kas soovid ravimtaimi tarvitada? (jah/ei) ")
            if joo_potioneid.lower()=="jah":
                hp+=10
                potion-=1
                print("Tarvitasid ravimtaimi ning sul on nüüd ", hp, " elu alles.")
                time.sleep(2)
        dämm=random.randint(5,15)*mürk
        if viiking==1:
            viikingi_dämm=random.randint(0,10)
            dariuse_hp-=(dämm+viikingi_dämm)
        else:
            dariuse_hp-=dämm
        if dariuse_hp<=0:
            break
        if viiking==1:
                print("Tegid Dariusele ", dämm, " dmg ja viiking Olaf omalt poolt ", viikingi_dämm, " dmg! Tal on alles ", dariuse_hp, " elu.")
        else:
            print("Tegid Dariusele ", dämm, " dmg! Tal on alles ", dariuse_hp, " elu.")
        time.sleep(3)
        dariuse_dämm=random.randint(5,15)*rüü
        hp-=dariuse_dämm
        if hp<=0:
            break
        print("Darius tegi sulle vastu ", dariuse_dämm, " dmg! Sul on alles ", hp, " elu.")
        time.sleep(3)
    if hp<=0:
        print("Kahjuks osutus Darius sulle liiga raskeks vastaseks ning sa surid!")
        return
    else: 
        print("Juhuu!!! Oled Dariuse alistanud ning lähed katakombidesse lumelindu otsima.")


                     
while True:
    #--------------Esimese algus--------------#
    print(nimi + ", oled sattunud Zauni. Sul on 100 elupunkti ja 8 tegevuspunkti.")
    time.sleep(2)
    print("Mängu võitmiseks on sul vaja jõuda lumelinnu Aniviani, kelle Darius varastas, ning ta Zauni tagasi eskortima.")
    time.sleep(2)
    print("Kodust lahkudes tõmbas su tähelepanu endale kodutu, kes küsis sult 5 hõbedat, et süüa osta.")
    time.sleep(2)
    takistus1 = input("Kas annad talle 5 hõbedat? (jah/ei)")
    while takistus1.lower()!= "jah" and takistus1.lower()!="ei":
        print("Sellist vastust ei saa anda. Proovi uuesti.")
        takistus1=input("Kas annad kodutule 5 hõbedat? (jah/ei)")
    esimene(takistus1)
    if hp <= 0:
        break
    #--------------Teise algus--------------#
    time.sleep(1)
    print("Jõudsid matkarajale ning tunned nagu keegi jälitaks sind.")
    time.sleep(1)
    takistus2 = input("Kas liigud rahulikult edasi või hakkad jooksma ja peidad end? (liigun edasi/jooksen)")
    while takistus2.lower()!= "liigun edasi" and takistus2.lower()!="jooksen":
        print("Sellist vastust ei saa anda. Proovi uuesti.")
        takistus2=input("Kas liigud rahulikult edasi või hakkad jooksma? (liigun edasi/jooksen)")
    teine(takistus2)
    if hp <= 0:
        break
    #--------------Kolmanda algus--------------#
    time.sleep(1)
    print("Huh, jõudsidki metsast välja!")
    time.sleep(1)
    takistus3=input("Päike on juba aga loojunud ning sa tunned ennast senisisest teekonnast üpris väsinuna. Kas paned telgi püsti ja magad või otsustad väsimusest hoolimata teekonda jätkata? (magan/jätkan)")
    while takistus3.lower()!= "magan" and takistus3.lower()!="jätkan":
        print("Sellist vastust ei saa anda. Proovi uuesti.")
        takistus3=input("Kas jääd magama või jätkad teekonda hoolimata väsimusest? (magan/jätkan)")
    kolmas(takistus3)
    if hp<=0:
        break
    #-----------Neljanda algus-------------#
    time.sleep(1)
    print("Pärast sündmusterikast ööd hakkab taas päike koitma ning kaugelt paistavad müürid sama kõrged kui puud. Lähemale minnes näed juba kindluse keskel hiigelsuurt paleed.")
    time.sleep(3)
    print("On ilmselge, et oled jõudnud Noxusesse, Dariuse kodukuningriiki.")
    time.sleep(3)
    print("Astud peagi kindluse peaväravast läbi ja satud Noxuse turule. Siit leiad kõike meelepärast.")
    time.sleep(3)
    neljas()
    #------------Viienda algus---------------#
    time.sleep(3)
    print("Pärast turgu sead sammud otse Dariuse paleesse.")
    time.sleep(3)
    print("Astud palee ustest sisse ja pika aatriumi lõpus näed sa Dariust.")
    time.sleep(3)
    print("'Kuhu panid sa lumelinnu!?', küsid sa Dariuselt.")
    time.sleep(3)
    print("'Ta on katakombides ahelates, aga sinna saad sa ainult üle minu laiba!', vastab Darius.")
    time.sleep(3)
    print("Algab võitlus elu ja surma nimel.")
    time.sleep(2)
    bossfight()
    if hp<=0:
        break
    #------------Kuuenda algus---------------#
    time.sleep(3)
    print("Sisened hämaratesse katakombidesse. Käid mööda pikki koridore kuni kuuled kaugusest kettide kõlinat.")
    time.sleep(3)
    print("Hakkad hääle poole jooksma, kuni jõuad ukseni, mille tagant heli tuleb. Uks on aga lukus ja sellel on 3-numbriline kood ning ukse avamiseks pead selle ära arvama.")
    ukse_kood=random.randint(100,999)
    time.sleep(4)
    if teene==1:
        print("Kusagilt kostub tuttav hääl. Sulle meenub Tahm Kenchiga öine juhtum ning tunned ta hääle ära. Ta lausub sulle: 'Uksekood on", ukse_kood, ".'")
        time.sleep(4)
    pakkumine=int(input("Sisesta uksekood: "))
    while pakkumine!=ukse_kood:
        if pakkumine>ukse_kood:
            vahe=pakkumine-ukse_kood
            pakkumine=int(input("Vale vastus! See vastus on " + str(vahe) + " võrra liiga suur. Proovi uuesti: "))
        else:
            vahe=ukse_kood-pakkumine
            pakkumine=int(input("Vale vastus! See vastus on " +  str(vahe)+ " võrra liiga väike. Proovi uuesti: "))
    print("Lukk kõlksatab ja sa lükkad ukse lahti. Seal ta ongi! Anivia!")
    time.sleep(3)
    print("Sa vabastad Anivia ahelatest ja aitad ta katakombidest välja.")
    time.sleep(4)
    print("Jõuate paleest välja ning Anivia muutub kohe hiigelsuureks lumelinnuks ning lausub võidurõõmsalt: 'Hüppa peale! Lendame koju!'")
    break
if hp<=0:
    print("Elupuktid said otsa. Mäng läbi!")
else:
    print("PALJU ÕNNE, ", nimi.upper(), "! Oled mängu edukalt läbinud!")
exit()