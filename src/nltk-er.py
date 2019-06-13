from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.chunk import conlltags2tree, tree2conlltags

 
text = "El mirlo capiblanco (Turdus torquatus) es una especie de Aves paseriforme de la familia Turdidae del género Turdus''.\
        Está estrechamente emparentado con el mirlo común (Turdus merula) del que se diferencia fácilmente por la zona de plumaje blanco que destaca sobre su pecho a modo de babero. El resto del cuerpo es negro en el caso de los machos, mientras que las hembras son pardas y provistas de un babero por estar salpicado de plumas leonadas. Los bordes de las alas son más pálidos que el resto del cuerpo. Todos los jóvenes de menos de un año presentan la coloración femenina, independientemente de su sexo.\
        Algunas de las plumas se vuelven grisáceas en otoño, dándole un aspecto escamoso a esta especie. \
        El canto está formado por varias frases cortas que se repiten de 2 a 4 veces (tac-tac-tac, chuc-chuc-chuc-chuc), generalmente en una rama o el suelo, aunque a veces también se produce en pleno vuelo. En este caso el sonido se produce una sola vez, siendo parecido a un chuirrr. \
        El mirlo capiblanco habita en zonas de montaña, donde sustituye al mirlo común. Su hábitat característico es el bosque subalpino aclarado, con preferencia por los de pino negro. Se reproduce en las Islas Británicas, Escandinavia, Pirineos, varias localidades de Europa central y el Cáucaso. Al final del verano emigra hacia el sur para pasar el invierno, llegando hasta el norte de África. En España inverna en los montes de Teruel, la serranía de Ronda (Málaga) y la sierra de Tramontana (Mallorca), preferentemente en zonas cubiertas de Sabinas (botánica), cuyos frutos ingiere en esta época.\
        Los mirlos capiblancos se reúnen en grupos mayores durante el invierno, mientras que el resto del año llevan una vida solitaria o en grupos pequeños.\
        Se alimenta  de insectos, Lumbricidae de tierra, frutos de sabina y otros frutos silvestres.\
        Retorna a sus áreas de cría entre marzo y abril. Durante la época de reproducción deposita numerosos huevo en nidos confeccionados sobre las ramas de un arbusto."

ne_tree = ne_chunk(pos_tag(word_tokenize(text)))
 
iob_tagged = tree2conlltags(ne_tree)

def wordextractor(text):

    #bring the tuple back to lists to work with it
    words, tags, pos = zip(*text)
    words = list(words)
    pos = list(pos)
    c = list()
    i=0
    while i<= len(text)-1:
        #get words with have pos B-PERSON or I-PERSON
        if pos[i] == 'B-PERSON':
            c = c+[words[i]]
        elif pos[i] == 'I-PERSON':
            c = c+[words[i]]
        i=i+1

    return c
 
print(wordextractor(tree2conlltags(ne_chunk(pos_tag(word_tokenize(text))))))