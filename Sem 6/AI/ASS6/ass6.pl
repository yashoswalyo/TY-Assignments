wife(komal,salman).
husband(salman,komal).
brother(virat,komal).
brother(ramesh,salman).
sister(deepika,komal).
sister(rutuja,salman).
father(rohit,salman).
father(ashwin,komal).
father(salman,arjun).
father(salman,sara).
mother(pooja,salman).
mother(ria,komal).
mother(komal,arjun).
mother(komal,sara).

uncle(X,Z):- brother(X,Y), father(Y,Z).
sala(X,Z):- brother(X,Y), wife(Y,Z).
chacha(X,Z):- brother(X,Y), father(Y,Z). 
mama(X,Z):- brother(X,Y), mother(Y,Z).
maasi(X,Z):- sister(X,Y), mother(Y,Z).
fufi(X,Z):- sister(X,Y), father(Y,Z). 
dada(X,Z):- father(X,Y), father(Y,Z).
dadi(X,Z):- mother(X,Y), father(Y,Z).
nana(X,Z):- father(X,Y), mother(Y,Z).
nani(X,Z):- mother(X,Y), mother(Y,Z).