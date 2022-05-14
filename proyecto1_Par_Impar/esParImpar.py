




def esPar(_numero) :
   while _numero < 1000 : 
    if _numero % 2 == 0:
        print(_numero, " es par")
        _numero = float(input("Elije otro numero"))  
        

    else  :
        print(_numero, " es impar") 
        _numero = float(input("Elije otro numero"))     
   else :
       print("El numero ingresado no es menor a 1000 , ADIOS!")
    
    