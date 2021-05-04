# Tic-Tac-Toe with Minimax
En este proyecto se implementa el juego Tic-Tac-Toe haciendo uso del algoritmo Minimax. La logica de dicho juego se encuentra
en el archivo TicTacToe.py. Aqui se encuentra el algoritmo MInimax encargado de devolver la mejor posicion que puede hacer la AI 
dado un tablero determinado. Para ello se calculan los valores de los nodos hoja dandole un valor de -1,1,0 en dependencia de si gana 
eljugador humano, la AI o hay un empate. A partir de ese punto cuando ascendemos en la recursividad el nodo padre se queda con la posicion
tal que minimice el resultado o lo maximice, en el caso de la AI nos quedaremos con el maximo resultado de lo que computan los nodos hijo.

Los demas metodos de la clase se encargan de moderar la logica del juego. En el archivo main.py se deben ofrecer los argumentos iniciales
para comenzar el juego y es este el que se debe ejecutar para probar.
