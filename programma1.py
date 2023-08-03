# -*- coding: utf-8 -*-
import sys
import codecs
import nltk

#funzione che calcola i caratteri totali di tutti i token di un documento
def Char(Tokens): 
    CharTotali=0.0 #si assegna alla variabile un valore iniziale decimale
    for token in Tokens:
        CharTotali = CharTotali+len(token) #il ciclo si itera finchè la lunghezza di tutti i token del testo (ovvero i caratteri) non viene aggiunta alla variabile CharTotali
    return CharTotali

#funzione che calcola la TTR, ovvero la grandezza del vocabolario fratto la grandezza del corpus per porzioni incrementali di 1000 tokens; il vocabolario è calcolabile applicando la funzione set() al totale dei token (ovvero il corpus)
def VocbTTR(tokens):
	#il ciclo si itera per ogni token nell arco di mille parole grazie alla funzione range, che ha come punto iniziale dell'intervallo 1000, come punto finale il numero totale dei token del testo, e ha passo di avanzamento di 1000
    for tok in range(1000, len(tokens), 1000):
        vocb = set(tokens[:tok]) #la funzione set() permette di selezionare tutti gli elementi differenti dell'argomento che gli si passa (che in questo caso sono i tokens totali a intervalli di 1000)
        ttr = len(vocb)*1.0/tok  
        print "per",tok, "token si ha |V|=", len(vocb), "e TTR=", ttr #stampa la cardinalità dell'intervallo di corpus, la stringa "è", la grandezza del vocabolario e la ttr per ogni intervallo di 1000 tokens
        voctot = set(tokens) #vocabolario totale del documento, servirà per calcolare l'ultimo intervallo, fino alla fine del corpus
    print "per",len(tokens)," token si ha |V|=", len(voctot), "e TTR=", len(voctot)*1.0/len(tokens) #stampa la cardinalità deò corpus, la stringa "è", la grandezza del vocabolario e la ttr per l'ultimo intervallo di tokens (ovvero quello da 5000 fino alla fine del corpus)

#funzione che calcola le classi di frequenza |V3|,|V6|,|V9| dei primi 5000 token, ovvero quante parole hanno frequenza di 3, 6 e 9
def classiFreq(tokens):
    V3 = 0
    V6 = 0
    V9 = 0 #contatori inizializzati a zero
    vocb5= set(tokens[:5000]) #assegnamo alla variabile vocb5 i primi 5000 token del testo che analizza
    #per ogni token dei primi 5000 token, conta il numero di occorrenze del token (grazie alla funzione L.count(elemento)) e se il determinato token ha frequenza 3,6 o 9, viene incrementato il rispettivo contatore
    for token in vocb5:
        freq = tokens.count(token) 
        if freq == 3:
            V3 = V3+1
        elif freq == 6:
            V6 = V6+1
        elif freq == 9:
            V9 = V9+1
    #stampa il numero di token con le frequenze di 3,6 o 9
    print "I token con frequenza 3 sono", V3
    print "I token con frequenza 6 sono", V6
    print "I token con frequenza 9 sono", V9

#funzione che categorizza grammaticalmente i token, individua il numero medio di Sostantivi, Aggettivi e Verbi per fras e individua le altre categorie necessarie per il calcolo della densità lessicale 
def ClassificazioneEDensLes(tokenstotali,frasi):
	#salva in una variabile tutti i token di un documento POS-taggati, ovvero una lista di coppie (token, POS)
    tokensPOS=nltk.pos_tag(tokenstotali)
    #inizializzo variabili "contatore" a 0.0, ovvero un valore decimale in modo da ottenere maggior precisione
    Sost=0.0
    Verb=0.0
    Agg=0.0
    Avv=0.0
    Virgole=0.0
    Punti=0.0
    #per ogni token nella lista di coppie tokensPOS viene controllato se token[1] ovvero la categoria grammaticale del token (che è token[0]) appartiene a una delle categorie che ci interessano, e nel caso aumenta il rispettivo contatore 
    for token in tokensPOS:
        if token[1] == "NNS" or token[1]=="NN" or token[1]=="NNP" or token[1]=="NNPS":
            Sost=Sost+1
        elif token[1]=="JJ" or token[1] =="JJR" or token[1]=="JJS":
            Agg=Agg+1
        elif token[1]=="VB" or token[1] =="VBD" or token[1]=="VBG" or token[1]=="VBN" or token[1]=="VBP" or token[1]=="VBZ":
            Verb=Verb+1
        elif token[1]=="RB" or token[1] =="RBR" or token[1] =="RBS":
            Avv=Avv+1
        elif token[1]==".":
            Punti=Punti+1
        elif token[1]==",":
            Virgole=Virgole+1
    #stampa a schermo in numero medio di sostantivi, aggettivi e verbi per frase, dati dal numero degli stessi diviso il numero delle frasi totali
    print "Il numero medio di sostantivi per frase è",Sost/len(frasi) 
    print "Il numero medio di aggettivi per frase è",Agg/len(frasi)
    print "Il numero medio di verbi per frase è",Verb/len(frasi)
    #stampa a schermo la densità lessicale, data dal rapporto tra il numero totale di occorrenze nel testo delle categorie richieste e il corpus, escluse le virgole e i punti
    print "La densità lessicale è", (Sost+Verb+Avv+Agg)/(len(tokenstotali)-(Virgole+Punti))


def main(fileP,fileN):
	#assegno alle due variabili la rispettiva codifica del file dato in input nella shell in UTF-8
    fileInputP = codecs.open(fileP, "r", "utf-8")
    fileInputN = codecs.open(fileN, "r", "utf-8")
    #assegno alle due variabili i file letti, che assumeranno valore di tipo string
    rawP = fileInputP.read()
    rawN= fileInputN.read()
    print "Progetto di information extraction svolto su recensioni Amazon di Alexa Dot di terza generazione - programma 1" 
 
    #definisco la funzione di NLTK, che dividerà il testo passatogli in frasi 
    Tokenizzatore= nltk.data.load('tokenizers/punkt/english.pickle')
    #applico tale funzione utilizzando la funzione tokenize(sting) a entrambi i file e salvo il testo diviso in frasi in due variabili
    frasiP = Tokenizzatore.tokenize(rawP)
    frasiN = Tokenizzatore.tokenize(rawN)
    #stampo a schermo il numero di frasi per ogni file (utilizzando la funzione len(string) che calcola la lunghezza della variabile contenente il testo diviso in frasi, ovvero il numero di frasi) 
    print "Il numero totale di frasi di", fileP, "è",len(frasiP) 
    print "Il numero totale di frasi di", fileN, "è",len(frasiN) 
    #definisco due variabili a cui assegnare i valori ottenuti sommando i tokens ad ogni iterazione ciclo di for, ovvero la somma totale dei token
    TokTotP=[]
    TokTotN=[]
    #due cicli for che per i 2 file, calcolano il numero totale di tokens, sommando ogni token al precedente (grazie al ciclo for) e assegnando la somma alla variabile rispettiva
    for frase in frasiP:
    	tokensP = nltk.word_tokenize(frase)
    	TokTotP=TokTotP+tokensP
    for frase in frasiN:
    	tokensN = nltk.word_tokenize(frase)
    	TokTotN=TokTotN+tokensN
    #stampa a schermo il numero di tokens per ogni file (utilizzando la funzione len(string) che calcola la lunghezza della variabile contenente le frasi divise in tokens, ovvero il numero di tokens)
    print "Il numero totale di token di", fileP, "è",len(TokTotP) 
    print "Il numero totale di token di", fileN, "è",len(TokTotN) 
    
    #la lunghezza media delle frasi in termini di token è data dal numero dei token totali del testo diviso il numero di frasi, ottenibili attraverso la funzione len(); moltiplichiamo il dividendo per 1.0 così da ottenere un risultato decimale, quindi più preciso
    MediaLunFrasiP= len(TokTotP)*1.0/len(frasiP)
    print "La lunghezza media delle frasi in termini di token di", fileP, "è",MediaLunFrasiP
    MediaLunFrasiN= len(TokTotN)*1.0/len(frasiN)
    print "La lunghezza media delle frasi in termini di token di", fileN, "è",MediaLunFrasiN
    #la lunghezza media dei token in termini di caratteri è data dal numero dei caratteri totali del testo diviso il numero di token
    #il numero di caratteri viene calcolato attraverso una funzione esterna al main, mentre il numero dei token totali è ottenibile attraverso la funzione len()
    MediaLunTokP= Char(TokTotP)/len(TokTotP)
    print "La lunghezza media dei token in termini di caratteri di", fileP, "è",MediaLunTokP
    MediaLunTokN= Char(TokTotN)/len(TokTotN)
    print "La lunghezza media dei token in termini di caratteri di", fileN, "è",MediaLunTokN

    print "La grandezza del vocabolario e la Type Token Ratio all'aumentare del corpus per porzioni incrementali di 1000 token per",fileP,":"
    VocbTTR(TokTotP)
    print "La grandezza del vocabolario e la Type Token Ratio all'aumentare del corpus per porzioni incrementali di 1000 token per",fileN,":"
    VocbTTR(TokTotN)
  
    print "Classi di frequenza nel file", fileP,":"
    classiFreq(TokTotP)
    print "Classi di frequenza nel file", fileN,":"
    classiFreq(TokTotN)
    
    print "Informazioni morfo-sintattiche sul file", fileP,":"
    ClassificazioneEDensLes(TokTotP,frasiP)
    print "Informazioni morfo-sintattiche sul file", fileN,":"
    ClassificazioneEDensLes(TokTotN,frasiN)

main(sys.argv[1], sys.argv[2])