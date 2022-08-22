from typing import BinaryIO
import math

def switch():
 print  ('introduzca 1 para pasar de decimal a binario ', ' intrduzca 2 para pasar de binario a decimal ','Introduzca 3 para pasar de Decimal a Hexadecimal', 'Introduzca 4 para pasar de Hexadecimal a Decimal', 'Introduzca 5 para pasar de Binario a Hexadecimal', 'Introduzca 6 para pasar de Decimal a Octal', 'Introduzca 7 para pasar de Octal a Decimal',     sep = '._.')
 Opcion = input ('introduzca su opcion')

 if Opcion == 1 :
    
   def decimal_a_binario(numero_decimal):

       numero_binario = 0
       multiplicador = 1

   while numero_decimal != 0:
        numero_binario = numero_binario + numero_decimal % 2 * multiplicador
        numero_decimal //= 2
        multiplicador *= 10
        return numero_binario
   Nd = input("digite un numero decimal: ")
   Nd = int (Nd)       
   print(decimal_a_binario(Nd))

 elif Opcion == 2 :
     def binario_a_decimal(binario):

          posicion = 0
          decimal = 0

          binario = binario[::-1]
     for digito in BinaryIO:

         multiplicador = 2**posicion
         decimal += int(digito) * multiplicador
         posicion += 1
         return decimal
     
         binario = input("Ingresa un número binario: ")
         decimal = binario_a_decimal(binario)
         print(decimal)

 elif Opcion == 3 :
     def decimalahexa(valor):
     # Lo necesitamos como cadena
      valor = str(valor)
      equivalencias = {
        "10": "a",
        "11": "b",
        "12": "c",
        "13": "d",
        "14": "e",
        "15": "f",
          }
      if valor in equivalencias:
        return equivalencias[valor]
      else:
        return valor


     def decimal_a_hexadecimal(decimal):
        hexadecimal = ""
     while decimal > 0:
        residuo = decimal % 16
        verdadero_caracter = hexadecimal(residuo)
        hexadecimal = verdadero_caracter + hexadecimal
        decimal = int(decimal / 16)
        return hexadecimal


     decimal = int(
     input("Escribe un número decimal, yo lo convertiré a hexadecimal: "))
     hexadecimal = decimal_a_hexadecimal(decimal)
     print(f"El decimal {decimal} es {hexadecimal} en hexadecimal")

 elif Opcion == 4 :

     hex = input("Ingresa un Numero Hexadecimal ")
 
     c = count = i = 0
     len = len(hex) - 1
     while len>=0:
      if hex[len]>='0' and hex[len]<='9':
        rem = int(hex[len])
      elif hex[len]>='A' and hex[len]<='F':
        rem = ord(hex[len]) - 55
      elif hex[len]>='a' and hex[len]<='f':
        rem = ord(hex[len]) - 87
      else:
        c = 1
        break
     count = count + (rem * (16 ** i))
     len = len - 1
     i = i+1
 
     if c == 0:
       print("\nValor Decimal = ", count)
     else:
       print("\nValor Incorrecto!")

 elif Opcion == 5:

     def binarioadecimal(binario):
         binario1 = int(binario)
         decimal, i, n = 0, 0, 0

         while(binario1 != 0):
          dec = binario1 % 10
          decimal = decimal + dec * pow(2, i)
          binario1 = binario1//10
          i+= 1
         return(decimal)
      
     def DecAHexa(n):

         hexaDeciNum = ['0'] * 100
         i = 0
         while(n !=0):
           temp = 0
           temp = n % 16
         if(temp < 10):
           hexaDeciNum[i] = chr(temp + 48)
         else:
           hexaDeciNum[i] = chr(temp + 55)
           i = i + 1
         n = int(n / 16)


 elif Opcion == 6:
     def decimal_a_octal(decimal):
         octal = ""
         while decimal > 0:
           residuo = decimal % 8
           octal = str(residuo) + octal
           decimal = int(decimal / 8)
           return octal
     decimal = int(input("Ingresa un número decimal: "))
     octal = decimal_a_octal(decimal)
     print(f"El decimal {decimal} es {octal} en octal")
      

 elif Opcion == 7:
     def octal_a_decimal(octal):
         print(f"Convirtiendo el octal {octal}...")
         decimal = 0
         posicion = 0

         octal = octal[::-1]
         for digito in octal:
             print(f"El número decimal es {decimal}")
             valor_entero = int(digito)
             numero_elevado = int(8 ** posicion)
             equivalencia = int(numero_elevado * valor_entero)
             print(
                 f"Elevamos el 8 a la potencia {posicion} (el resultado es {numero_elevado}) y multiplicamos por el carácter actual: {valor_entero}")
             decimal += equivalencia
             print(f"Sumamos {equivalencia} a decimal. Ahora es {decimal}")
             posicion += 1
         return decimal


     octal = input("Ingresa un número octal: ")
     decimal = octal_a_decimal(octal)
     print(f"El octal {octal} es {decimal} en decimal")

     switch()


