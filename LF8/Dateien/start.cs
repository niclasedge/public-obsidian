using System;
namespace B_Schueler_V1
{
 class Start
 {
 static void Main(string[] args)
 {

 Schueler azubi1 = new Schueler();
 Schueler azubi2 = new Schueler();
 azubi2.DruckeInfo();
 azubi1.WechselKlasse("FI22");
 azubi1.DruckeInfo();
 Console.Read();
 }
 }
}
