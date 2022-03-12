function solucion = ExpIzqDer(base, divisor)
  vector = dec2bin(divisor - 1)

  x = 1;

  for i = 1 : length(vector)
      x = x^2;
      if vector(i) == '1'
        x = mod(x*base,divisor);
        fprintf("%d & %d ** \n",i, x);
        solucion(i) = x;
      else
        x = mod(x,divisor);
        fprintf("%d & %d ** \n",i, x);
        solucion(i) = x;
      endif
  endfor
endfunction