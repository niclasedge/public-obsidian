using System;

namespace B_Schueler_V1
{
    public class Schueler
    {
        private String name;

        private String klasse;

        private Int16 einschulungsjahr;

            
        public void WechselKlasse(String neueklasse)
        {
            if (neueklasse.Substring(0, 2) == "FA" || neueklasse.Substring(0, 2) == "FS")
            {
                this.klasse = neueklasse;
            }
            else
            {
                Console.WriteLine("Der Klassenwechsel konnte nicht erfolgen: Falsche Klassenbezeichnung");
            }
        }


        public void DruckeInfo()
        {
            Console.WriteLine("Azubi:"+this.name);
            Console.WriteLine("Klasse: " + this.klasse + "   Einschulungsjahr: " + this.einschulungsjahr);  
        }

    }   
}
