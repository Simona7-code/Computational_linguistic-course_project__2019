# -*- coding: utf-8 -*-
import sys
import codecs
import nltk
from nltk import bigrams
from nltk import trigrams
import math

#funzione che estrae i 20 token più frequenti escludendo la punteggiatura
def tok20piufreq(listatokenordinata):
    tokensNPun=[] #lista che conterrà la lista dei token con relativa POS e frequenza che non sono segni di punteggiatura (definito nella condizione dell'if, dove tok[0][1] è il POS del token)
    for tok in listatokenordinata:
        if tok[0][1]!="." and tok[0][1]!="," and tok[0][1]!=":" and tok[0][1]!="(" and tok[0][1]!=")":
            #appende il token (diverso da un segno di punteggiatura) alla lista tokensNPun
            tokensNPun.append(tok)
    #seleziona solo i primi venti token della lista
    TokNoPun20=tokensNPun[0:20]
    #il ciclo for permette la stampa del token (elem[0][0]) e della frequenza (elem[1]) dal momento che la lista è così strutturata: ((token,POS),frequenza)
    for elem in TokNoPun20:
    	print elem[0][0], "--> frequenza", elem[1]

#funzione che estrae i 20 Sostantivi più frequenti
def SOST20piufreq(listatokenordinata):
    tokenS=[] #lista che conterrà la lista dei token con relativa POS e frequenza che sono sostantivi(definito nella condizione dell'if, dove tok[0][1] è il POS del token)
    for tok in listatokenordinata:
        if tok[0][1] == "NNS" or tok[0][1]=="NN" or tok[0][1]=="NNP" or tok[0][1]=="NNPS":
            #appende il token (che è un sostantivo) alla lista tokensNPun
            tokenS.append(tok)
    #seleziona solo i primi venti token della lista
    TokSost20=tokenS[0:20]
    #il ciclo for permette la stampa del token (elem[0][0]) e della frequenza (elem[1]) dal momento che la lista è così strutturata: ((token,POS),frequenza)
    for elem in TokSost20:
    	print elem[0][0], "--> frequenza", elem[1]

#funzione che estrae i 20 Aggettivi più frequenti
def AGG20piufreq(listatokenordinata):
    tokenA=[] #lista che conterrà la lista dei token con relativa POS e frequenza che sono aggettivi (definito nella condizione dell'if, dove tok[0][1] è il POS del token)
    for tok in listatokenordinata:
        if tok[0][1]=="JJ" or tok[0][1] =="JJR" or tok[0][1]=="JJS":
            #appende il token (che è un aggettivo) alla lista tokensNPun
            tokenA.append(tok)
    #seleziona solo i primi venti token della lista
    TokAgg20=tokenA[0:20]
    #il ciclo for permette la stampa del token (elem[0][0]) e della frequenza (elem[1]) dal momento che la lista è così strutturata: ((token,POS),frequenza)
    for elem in TokAgg20:
    	print elem[0][0], "--> frequenza", elem[1]

#funzione che estrae i 20 bigrammi di token più frequenti che non contengono punteggiatura, articoli e congiunzioni
def bigrNoPunArtCong(listabigrammiordinata):
	BigrNo=[] #lista che dopo il ciclo conterrà i bigrammi che non contengono le POS da escludere
	for tok in listabigrammiordinata: #ciclo controlla per ogni bigramma i POS dei due token, rispettivamente tok[0][0][1] è il POS del primo token del bigramma e tok[0][1][1] del secondo token del bigramma
		if tok[0][0][1]!="." and tok[0][0][1]!="," and tok[0][0][1]!=":" and tok[0][0][1]!="(" and tok[0][0][1]!=")" and tok[0][0][1]!="DT" and tok[0][0][1]!="CC" and tok[0][0][1]!="IN" and tok[0][1][1]!="." and tok[0][1][1]!="," and tok[0][1][1]!=":" and tok[0][1][1]!="(" and tok[0][1][1]!=")" and tok[0][1][1]!="DT" and tok[0][1][1]!="CC" and tok[0][1][1]!="IN":
			BigrNo.append(tok) #se i bigrammi non hanno POS delle categorie specificate, vengono inseriti nella lista BigrNo
	BigrNo20=BigrNo[0:20] #assegna a BIgrNo20 i primi 20 bigrammi presenti nella lista risultante dal precedente ciclo
	for elem in BigrNo20:
		print elem[0][0][0], elem[0][1][0],"-->frequenza", elem[1] #stamperà i due token che compongono i bigrammi, seguiti dalle rispettive frequenze

#funzione che estrae le 10 POS più frequenti attraverso un ciclo che prende i primi 10 elementi della lista di token postaggati in ordine decrescente di frequenza e ne stampa il POS con la relativa frequenza
def POSfreq10(POSTokOrd):
	for token in POSTokOrd[0:10]:
	    print token[0][1],"--> frequenza", token[1]

#funzione che estrae i primi 10 bigrammi di POS più frequenti attraverso un ciclo che prende i primi 10 elementi della lista dei bigrammi postaggati in ordine decrescente di frequenza e stampa i 2 POS che compongono il bigramma con la relativa frequenza
def POSBigrfreq10(POSBigrOrd):
	for token in POSBigrOrd[0:10]:
	    print token[0][0][1], token[0][1][1],"--> frequenza", token[1]

#funzione che estrae i primi 10 trigrammi di POS più frequenti attraverso un ciclo che prende i primi 10 elementi della lista dei trigrammi postaggati in ordine decrescente di frequenza e stampa i 3 POS che compongono il trigramma con la relativa frequenza
def POSTrigrfreq10(POSTrigOrd):
	for token in POSTrigOrd[0:10]:
	    print token[0][0][1], token[0][1][1], token[0][2][1], "--> frequenza", token[1]

#funzione che estrae tutti i bigrammi Aggettivo-sostantivo con le frequenze dei singoli token che li compongono maggiore di 2
def BigrSostAGG(listabig,TokTot):
	BigAggSogg=[]
	BigAggSoggF2=[]
	for token in listabig: #per ogni bigramma in lista totale dei bigrammi del testo postaggati
		if (token[0][1]=="JJ" or token[0][1]=="JJR" or token[0][1]=="JJS") and (token[1][1]=="NN" or token[1][1]=="NNS" or token[1][1]=="NNP" or token[1][1]=="NNPS"):
			BigAggSogg.append(token) #appende alla lista tutti i bigrammi il cui primo token è un aggettivo e il secondo è un sostantivo
	for tok in BigAggSogg: #per ogni bigramma Aggettivo-Sostantivo nella lista appena calcolata
		if TokTot.count(tok[0][0])>2 and TokTot.count(tok[1][0])>2: #controlliamo che i singoli token che li compongono abbiano frequenza > 2, contando quante volte essi si presentano nella lista che contiene il corpus 
			BigAggSoggF2.append(tok) #se il bigramma soddisfa la condizione dell'if, viene appeso a questa nuova lista, che viene poi restituita dalla funzione
	return BigAggSoggF2

#funzione che estrae i 20 bigrammi aggettivo-sostantivo con frequenza massima e li stampa a schermo
def FreqMaxSogAgg(BigAggSoggF2,TokTot):
	Freq=nltk.FreqDist(BigAggSoggF2) #calcola le frequenze di tutti i bigrammi aggettivo-sostantivo
	ListaFreqOrd=Freq.most_common(20) #estrae i primi venti bigrammi (quelli con le frequenze più alte) dalla lista dei bigrammi aggettivo-sostantivo
	for elem in ListaFreqOrd: #per ognuno di questi 20
		print "Il bigramma \"", elem[0][0][0], elem[0][1][0],"\" ha frequenza", elem[1] #stampa il bigramma (i due token che lo compongono) e la frequenza di esso
		print "La frequenza di", elem[0][0][0],"è",TokTot.count(elem[0][0][0]) #stampa il primo token del bigramma con la sua frequenza, calcolata contando quante volte il token compare nel corpus
		print "La frequenza di", elem[0][1][0],"è",TokTot.count(elem[0][1][0]) #stampa il secondo token del bigramma con la sua frequenza, calcolata contando quante volte il token compare nel corpus
		print 
	return ListaFreqOrd #restituisce alla funzione principale i 20 bigrammi aggettivo-sostantivo dalle frequenze più alte

#funzione che calcola e stampa il valore delle venti probabilità congiunte massime, assieme ai rispettivi bigrammi
def ProbCong20(TokTot, BigAggSoggF2, ListaFreqOrd): 
	Corpus=len(TokTot) #cardinalità del Corpus
	for bigramma in ListaFreqOrd:  
		FreqBig=BigAggSoggF2.count(bigramma[0]) #conta le frequenze dei bigrammi (escludendo la frequenza) che ci interessano all'interno della lista che contiene tutti i bigrammi aggettivo-sostantivo
		ProbCong= FreqBig*1.0/Corpus #la probabilità condizionata viene calcolata dividendo la frequenza del bigramma (dal valore decimale per una maggior precisione) con Corpus
		print "Il bigramma \"", bigramma[0][0][0], bigramma[0][1][0],"\" ha probabilità congiunta di", ProbCong #stampa il bigramma seguito dalla rispettiva probabilità congiunta 
        print

#funzione che calcola e stampa il valore delle venti forze associative massime, assieme ai rispettivi bigrammi
def LMI20(TokTot,BigAggSoggF2,ListaFreqOrd):
	Corpus=len(TokTot) #cardinalità del Corpus
	for bigramma in ListaFreqOrd: #per ogni bigramma dei venti presenti
		FreqBig=BigAggSoggF2.count(bigramma[0]) #conta le occorrenze del bigramma (escludendo la frequenza) che ci interessa all'interno della lista che contiene tutti i bigrammi aggettivo-sostantivo
		FreqTok1=TokTot.count(bigramma[0][0][0]) #conta le occorrenze del primo token che compone il bigramma all'interno del corpus
		FreqTok2=TokTot.count(bigramma[0][1][0])#conta le occorrenze del secondo token che compone il bigramma all'interno del corpus
		LMI=FreqBig* math.log(((FreqBig*Corpus)/(FreqTok1*FreqTok2)),2) #la LMI di un bigramma viene calcolatta moltiplicando la frequenza del bigramma con il logaritmo in base due della frequenza del bigramma moltiplicata alla cardinalità del corpus diviso il prodotto delle frequenze dei due token che lo compongono
		print "Il bigramma\"", bigramma[0][0][0], bigramma[0][1][0],"\"ha una forza associativa di valore", LMI #stampa il bigramma seguito dalla rispettiva forza associativa
        print

#funzione che restituisce, date tutte le frasi di un corpus, la lista contenente le frasi con le caratteristiche idonee a quelle richieste
def frasiPerMarkov(frasi,TokTot):
    frasilung=[] 
    frasiperM=[]
    for frase in frasi: #per ogni frase in tutte le frasi del corpus
        tokens = nltk.word_tokenize(frase) #tokenizza la frase
        if (len(tokens) > 5) and (len(tokens) < 9): #se le frasi contengono un numero di tokens maggiore di 5 e minore di 9
            frasilung.append(frase) #appende tali frasi alla lista frasilung
    for frasee in frasilung: #per ogni frase nella lista delle frasi lunghe minimo 6 e massimo 8
        tokens = nltk.word_tokenize(frasee)#tokenizza le frasi della lista
        condizione= True #imposto variabile condizione di valore true
        for tok in tokens: #per ogni token della frase che il for precedente sta analizzando
            if (TokTot.count(tok)<=2): #se la frequenza del token è minore uguale a 2
                condizione= False  #la condizione viene impostata a falsa
        if (condizione): #se la condizione non è False (ovvero i token della frase non hanno frequenza minore uguale a 2)
            frasiperM.append(frasee) #allora vuol dire che è maggiore di 2 quindi la frase è idonea, e la si appende a una nuova lista
    return frasiperM

#funzione che calcola per ogni frase la probabilità usando il modello di Markov di ordine 0 
def MarkovZero(ListaIdoneaM,TokTot):
    probMax=0.0 #variabile che a fine esecuzione della funzione, conterrà il valore della probabilità massima
    FraseMax=[] #variabile che a fine esecuzione della funzione, conterrà la frase con probabilità massima
    probMarkov0=1.0 #valore della probabilità, inizializzato a 1.0

    for frase in ListaIdoneaM: #per ogni frase dentro la lista delle frasi che rispettano le condizioni per l'applicazione di Markov
        FraseTokenizzata=nltk.word_tokenize(frase) #tokenizza la frase 
        for tok in FraseTokenizzata:  #per ogni token all'interno della frase tokenizzata
            probMarkov0=probMarkov0*((TokTot.count(tok))/(len(TokTot)*1.0)) #la probabilità del token viene calcolata dividendo la frequenza del token con la cardinalità del corpus, e viene poi moltiplicata con la probabilità di tutti gli altri token della frase, man mano che vengono passati al for
        if probMarkov0>probMax: #se il valore appena calcolato della probabilità è maggiore del valore della variabile probMax
            probMax=probMarkov0 #probMax assume il valore appena calcolato della probabilità
            FraseMax=frase #FraseMax assume il valore della stringa frase con la probabilità massima
    print "La frase con probabilità più alta calcolata attraverso un modello di Markov di ordine 0 è:\"",FraseMax,"\"con probabilità",probMax

#funzione che calcola per ogni frase la probabilità usando il modello di Markov di ordine 1 
def MarkovUno(ListaIdoneaM,TokTot):
    probMax=0.0 #variabile che a fine esecuzione della funzione, conterrà il valore della probabilità massima
    FraseMax=[] #variabile che a fine esecuzione della funzione, conterrà la frase con probabilità massima
    probMarkov1=1.0 #valore della probabilità, inizializzato a 1.0
    listabig=list(bigrams(TokTot)) #crea la lista dei bigrammi estratti dal corpus
    for frase in ListaIdoneaM: #per ogni frase tra le idonee
        FraseTokenizzata=nltk.word_tokenize(frase) #tokenizza la frase
        bigrammiFrasi=list(bigrams(FraseTokenizzata)) #crea la lista dei bigrammi estratti dalla frase passata al for
        indiceTok=0 #ideale indice che punterà i token della frase uno alla volta, man mano che scorre il for (inizializzato a 0, ovvero il primo token della frase)
        for indiceTok in range(0, len(FraseTokenizzata)): #per ogni indice, che scorre dallo 0 fino alla lunghezza della frase passata al for precedente
            if indiceTok==0: #se indice "punta" al primo token della frase
                token=FraseTokenizzata[indiceTok] #variabile token assume il valore del primo token della frase considerata
                probMarkov1=(((TokTot.count(token))/(len(TokTot)*1.0))) #nel calcolo di Markov di ordine 1, la probabilità del primo token si calcola come la probabilità di un qualsiasi token in Markov di ordine 0
            else: #se invece l'indice "punta" qualsiasi altro token che non sia il primo della frase
                token=FraseTokenizzata[indiceTok-1] #la variabile token assumerà il valore del token precente a quello puntato dall'indice nel ciclo for 
                FrequenzaBigramma=listabig.count(bigrammiFrasi[indiceTok-1]) #la variabile FrequenzaBigramma assumerà il valore della frequenza del bigramma (della frase) che contiene il token precedente a quello puntato dall'indice e il token puntato
                probMarkov1=probMarkov1*(FrequenzaBigramma/((TokTot.count(token))*1.0)) #viene moltiplicato il valore della probabilità del primo token (calcolato precedentemente) con le successive probabilità calcolate dividendo la frequenza del bigramma (descritto nel commento a riga 165) con la frequenza del token precente a quello puntato dall'indice nel ciclo for
            if probMarkov1>probMax: #se il valore appena calcolato della probabilità è maggiore del valore della variabile probMax
                probMax=probMarkov1 #probMax assume il valore appena calcolato della probabilità
                FraseMax=frase #FraseMax assume il valore della stringa frase con la probabilità massima
    print "La frase con probabilità più alta calcolata attraverso un modello di Markov di ordine 1 è:\"",FraseMax,"\"con probabilità",probMax
   

def main(fileP,fileN):
	#assegno alle due variabili la rispettiva codifica del file dato in input nella shell in UTF-8
    fileInputP = codecs.open(fileP, "r", "utf-8")
    fileInputN = codecs.open(fileN, "r", "utf-8")
    #assegno alle due variabili i file letti, che assumeranno valore di tipo String
    rawP = fileInputP.read()
    rawN= fileInputN.read()
    print "Progetto di information extraction svolto su recensioni Amazon di Alexa Dot di terza generazione - programma 2"
    #definisco la funzione di NLTK, che dividerà i testi in frasi 
    Tokenizzatore= nltk.data.load('tokenizers/punkt/english.pickle')
    #applico tale funzione utilizzando la funzione tokenize(Sting) a entrambi i file e salvo il testo diviso in frasi in due variabili
    frasiP = Tokenizzatore.tokenize(rawP)
    frasiN = Tokenizzatore.tokenize(rawN)
    #definisco due variabili "contatore" per salvarci dentro i valori ottenuti sommando i tokens ad ogni iterazione ciclo di for, ovvero la somma totale dei token
    TokTotP=[]
    TokTotN=[]
    #due cicli for che per i 2 file, calcolano il numero totale di tokens, sommando ogni token al precedente (grazie al ciclo for) e salvando la somma nella variabile "contatore" rispettiva
    for frase in frasiP:
    	tokensP = nltk.word_tokenize(frase)
    	TokTotP=TokTotP+tokensP
    for frase in frasiN:
    	tokensN = nltk.word_tokenize(frase)
    	TokTotN=TokTotN+tokensN
    #distribuzione di frequenza per i token dei due corpus
    distribFreqTokP=nltk.FreqDist(TokTotP)
    distribFreqTokN=nltk.FreqDist(TokTotN)
    #POS-tag dei due corpus
    TokPOSP=nltk.pos_tag(TokTotP)
    TokPOSN=nltk.pos_tag(TokTotN)
    #assegnamo alle variabili "distribuzione" la lista dei token POStaggati con relativa frequenza, utilizzando la funzione .FreqDist(lista) di nltk
    distribuzionefP=nltk.FreqDist(TokPOSP)
    distribuzionefN=nltk.FreqDist(TokPOSN)
    #assegnamo alle variabili "listatokenordinata"la lista dei token POStaggati ordinati in modo decrescente rispetto alla frequenza, utilizzando la funzione .most_common(elementi) di nltk
    listatokenordinataP=distribuzionefP.most_common(len(distribuzionefP))
    listatokenordinataN=distribuzionefN.most_common(len(distribuzionefN))
    #chiamate di funzioni su entrambi i corpus per i 20 token più frequenti escludendo la punteggiatura
    print "I 20 token più frequenti escludendo la punteggiatura presenti in", fileP,"sono:"
    tok20piufreq(listatokenordinataP)
    print "I 20 token più frequenti escludendo la punteggiatura presenti in", fileN,"sono:"
    tok20piufreq(listatokenordinataN)
    print "I 20 sostantivi più frequenti in", fileP,"sono:"
    SOST20piufreq(listatokenordinataP)
    print "I 20 sostantivi più frequenti in", fileN,"sono:"
    SOST20piufreq(listatokenordinataN)
    print "I 20 agettivi più frequenti in", fileP,"sono:"
    AGG20piufreq(listatokenordinataP)
    print "I 20 agettivi più frequenti in", fileN,"sono:"
    AGG20piufreq(listatokenordinataN)

    #creo la lista dei bigrammi di token a partire dalla lista dei token postaggati (per entrambi i corpus)
    listabigP=list(bigrams(TokPOSP))
    listabigN=list(bigrams(TokPOSN))
    #creo la lista dei bigrammi di token POStaggati con le rispettive frequenze (per entrambi i corpus)
    DISTFreqBigP=nltk.FreqDist(listabigP)
    DISTFreqBigN=nltk.FreqDist(listabigN)
    #creo la lista dei bigrammi di token POStaggati ordinati in base alla frequenza (per entrambi i corpus)
    listabigrammiordinataP=DISTFreqBigP.most_common(len(DISTFreqBigP))
    listabigrammiordinataN=DISTFreqBigN.most_common(len(DISTFreqBigN))
    print "I 20 bigrammi di token più frequenti che non contengono punteggiatura, articoli e congiunzioni in",fileP, "sono:"
    bigrNoPunArtCong(listabigrammiordinataP)
    print "I 20 bigrammi di token più frequenti che non contengono punteggiatura, articoli e congiunzioni in",fileN, "sono:"
    bigrNoPunArtCong(listabigrammiordinataN)
    print "Le 10 Part-of-Speech più frequenti in", fileP,"sono:"
    POSfreq10(listatokenordinataP)
    print "Le 10 Part-of-Speech più frequenti in", fileN,"sono:"
    POSfreq10(listatokenordinataN)
    print "I 10 bigrammi di Part-of-Speech più frequenti in",fileP,"sono:"
    POSBigrfreq10(listabigrammiordinataP)
    print "I 10 bigrammi di Part-of-Speech più frequenti in",fileN,"sono:"
    POSBigrfreq10(listabigrammiordinataN)

    #creo la lista dei trigrammi di token a partire dalla lista dei token postaggati (per entrambi i corpus)
    listaTrigP=list(trigrams(TokPOSP))
    listaTrigN=list(trigrams(TokPOSN))
    #creo la lista dei trigrammi di token POStaggati con le rispettive frequenze (per entrambi i corpus)
    DISTFreqTrigP=nltk.FreqDist(listaTrigP)
    DISTFreqTrigN=nltk.FreqDist(listaTrigN)
    #creo la lista dei trigrammi di token POStaggati ordinati in base alla frequenza (per entrambi i corpus)
    listaTrigrammiordinataP=DISTFreqTrigP.most_common(len(DISTFreqTrigP))
    listaTrigrammiordinataN=DISTFreqTrigN.most_common(len(DISTFreqTrigN))
    print "I 10 trigrammi di Part-of-Speech più frequenti in",fileP,"sono:"
    POSTrigrfreq10(listaTrigrammiordinataP)
    print "I 10 trigrammi di Part-of-Speech più frequenti in",fileN,"sono:"
    POSTrigrfreq10(listaTrigrammiordinataN)
    
    #Liste (per entrambi i corpus)che contengono i bigrammi Aggettivo-Soggetto con i singoli token che lo compongono con frequenza maggiore di 2 (valore resitutito dalla funzione)
    ListBigSoggAggP=BigrSostAGG(listabigP,TokTotP)
    ListBigSoggAggN=BigrSostAGG(listabigN,TokTotN)
    print "I 20 bigrammi con frequenza massima composti da Aggettivo e Sostantivo (dove ogni token deve avere una frequenza maggiore di 2) in", fileP,"sono:"
    ListaFreqOrdP=FreqMaxSogAgg(ListBigSoggAggP,TokTotP)
    print "I 20 bigrammi con frequenza massima composti da Aggettivo e Sostantivo (dove ogni token deve avere una frequenza maggiore di 2) in", fileN,"sono:"
    ListaFreqOrdN=FreqMaxSogAgg(ListBigSoggAggN,TokTotN)
    print "I 20 bigrammi con probabilità congiunta massima, composti da Aggettivo e Sostantivo (dove ogni token deve avere una frequenza maggiore di 2) in", fileP,"sono:"
    ProbCong20(TokTotP, listabigP, ListaFreqOrdP)
    print "I 20 bigrammi con probabilità congiunta massima, composti da Aggettivo e Sostantivo (dove ogni token deve avere una frequenza maggiore di 2) in", fileN,"sono:"
    ProbCong20(TokTotN, listabigN, ListaFreqOrdN)
    print "I 20 bigrammi con forza associativa massima, composti da Aggettivo e Sostantivo (dove ogni token deve avere una frequenza maggiore di 2) in", fileP,"sono:"
    LMI20(TokTotP,ListBigSoggAggP,ListaFreqOrdP)
    print "I 20 bigrammi con forza associativa massima, composti da Aggettivo e Sostantivo (dove ogni token deve avere una frequenza maggiore di 2) in", fileN,"sono:"
    LMI20(TokTotN,ListBigSoggAggN,ListaFreqOrdN)

    #salviamo in due variabili la lista delle frasi idonee al calcolo di Markov secondo caratteristiche specifiche richieste
    ListaIdoneaM_P=frasiPerMarkov(frasiP,TokTotP)
    ListaIdoneaM_N=frasiPerMarkov(frasiN,TokTotN)
    print "Calcoli di probabilità delle frasi utilizzando modelli Markoviani per",fileP,":"
    MarkovZero(ListaIdoneaM_P,TokTotP)
    MarkovUno(ListaIdoneaM_P,TokTotP)
    print
    print "Calcoli di probabilità delle frasi utilizzando modelli Markoviani per",fileN,":"
    MarkovZero(ListaIdoneaM_N,TokTotN)
    MarkovUno(ListaIdoneaM_N,TokTotN)
    
main(sys.argv[1], sys.argv[2])