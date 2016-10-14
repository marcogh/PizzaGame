# PizzaGame

Al centro di una stanza è presente un tavolo con numero n di pizze impilate una sopra l'altra, ma attenzione, l'ultima pizza di questa pila è avvelenata!!! Il primo giocatore che mangia la pizza avvelenata perde.

### Regole del gioco

1. I giocatori in gioco devono essere 2
2. Il numero di pizze viene determinato randomicamente all'inizio del gioco e deve essere sempre maggiore di 10
3. Ogni giocatore, durante il proprio turno, puó mangiare 1, 2 o 3 pizze alla volta
4. Ogni giocatore non puó saltare il proprio turno
5. Ogni giocatore non puó ripetere la scelta fatta in precedenza dall'avversario (per esempio: se il giocatore di turno decide di mangiare 1 pizza, allora l'altro giocatore è obbligato a mangiare 2 oppure 3 pizze)
6. Se un giocatore durante il proprio turno non ha mosse valide (per esempio: rimane ancora 1 pizza sul tavolo e il giocatore precedente ha mangiato 1 pizza) allora viene obbligato a saltare il proprio turno. A questo punto l'altro giocatore sarà obbligato a mangiare la torta avvelenata e, di conseguenza, a perdere. Questo è l'unico caso nel quale è consentito il salto del turno
