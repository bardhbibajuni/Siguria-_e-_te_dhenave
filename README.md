Implementimi Manual i Base64

Pershkrimi i Projektit

Ky projekt implementon manualisht algoritmin Base64 ne Python pa perdorur bibliotekat apo funksionet e gatshme te Base64.

Programi mundeson:

- Kodimin (Encoding)
- Dekodimin (Decoding)
- Menu interaktive per perdoruesin

Qellimi i projektit eshte te kuptohet funksionimi i algoritmit Base64 duke perdorur manipulimin e biteve dhe tabelen standarde Base64.



Teknologjite e Perdorura

- Python
- PyCharm
- GitHub



Shenim i Rendesishem

Ne kete projekt NUK jane perdorur bibliotekat e gatshme te Base64.

Funksionet e meposhtme nuk jane perdorur:

-------------------
import base64
base64.b64encode()
base64.b64decode()
------------------

Algoritmi eshte implementuar manualisht duke perdorur:

- Operacione binare
- Manipulim te biteve
- Tabelen Base64



Tabela Base64

-----------------------------------------------------------------------------------
BASE64_TABLE = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
-----------------------------------------------------------------------------------

Tabela Base64 permban 64 karaktere sepse Base64 punon me grupe prej 6 bitash.


Si Funksionon Encoding

1. Teksti konvertohet ne vlera ASCII.
2. Vlerat ASCII konvertohen ne binary.
3. Binary ndahet ne blloqe prej 24 bitash.
4. Blloku prej 24 bitash ndahet ne kater grupe prej 6 bitash.
5. Cdo vlere 6-bit perdoret si indeks ne tabelen Base64.
6. Gjenerohet teksti Base64.

Shembull:

-------------------
Man -> TWFu
-------------------

 Si Funksionon Decoding

1. Karakteret Base64 konvertohen ne indekse.
2. Indekset konvertohen ne binary.
3. Binary bashkohet ne blloqe prej 24 bitash.
4. Blloku prej 24 bitash ndahet ne byte prej 8 bitash.
5. Byte konvertohen perseri ne karaktere.

Shembull:

-----------------
TWFu -> Man
-----------------


Karakteristikat e Programit

- Encoding manual i Base64
- Decoding manual i Base64
- Menu interaktive
- Opsion per dalje nga programi
- Nuk perdoren biblioteka te jashtme



# Shembull i Ekzekutimit

---------------------------------------
BASE64 PROGRAM
1. Encoding
2. Decoding

Choose option: 1

Write text for encoding: Mani

Encoded text:
TWFuaQ==

Do you want to exit? yes

Program closed.
------------------------------------



Ndarja e Projektit ne Grup

Personi 1

* Tabela Base64
* Funksioni Encoding

Personi 2

* Funksioni Decoding

Personi 3

* Menu interaktive
* Testimi i programit



Perfundimi

Ky projekt demonstron funksionimin e algoritmit Base64 pa perdorur funksione apo biblioteka te gatshme. Implementimi eshte realizuar manualisht duke perdorur operacione binare dhe tabelen standarde Base64.
