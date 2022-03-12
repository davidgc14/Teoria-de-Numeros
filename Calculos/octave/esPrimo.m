function loes = esPrimo(n)
  contador = 1;
  loes = true;
  vector_primos = primes(ceil(sqrt(n)));
  while loes && contador<=length(vector_primos)
    if mod(n,vector_primos(contador)) == 0
      loes = false;
    endif
    contador++;
  endwhile
endfunction