clear all;

clc;

base = 11;
divisor = 45352583;

vector = dec2bin(divisor - 1);

  x = 1;

  for i = 1 : length(vector)
      x = x^2;
      if vector(i) == '1'
        x = mod(x*base,divisor);
        fprintf("%2d & %d \n",i,x);
        solucion(i) = x;
      else
        x = mod(x,divisor);
        fprintf("%2d & %d \n",i,x);
        solucion(i) = x;
      endif
  endfor
  
