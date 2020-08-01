# TaTeti
# Como #)&%! Reducir codigo / How can i reduce de code?
def dibujaTablero(ranura):
    # El panel se creo como lista (trate de hacerlo con for y range(1:10), pero no me resultó).
    print(    '|' + ranura[1] + '|' + ranura[2] + '|' + ranura[3] + '|' + '\n' 
        + '|' + ranura[4] + '|' + ranura[5] + '|' + ranura[6] + '|' + '\n'
        + '|' + ranura[7] + '|' + ranura[8] + '|' + ranura[9] + '|' + '\n')
        
# la idea es que comience en 1 y termine en 9. Además, que tome la forma de la matriz de arriba.
# The idea is start in 1 and finish in 9. Also, get the matrix shape showed on top.
def dibujaTablero(ranura):
    for i in range(1:len(ranura)):
        for j in range(len(ranura[i])):
            print(" |",ranura[i], end="")
        print(" |")
