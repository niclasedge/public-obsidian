using System; //Bibliothek importieren

namespace B_Schueler_V1 //Damit alle Klassen sich untereinander erkennen 
{
    public class Schueler //Klassenname, sollte gleich sein wie der Dateiname
    {
        private String name;

        private String nachname;

        private String klasse;

        private Int16 einschulungsjahr;


        public Schueler(string v)
        {
            this.name = v;
        }

        public Schueler(string v, string n, string k, Int16 j)
        {
            this.name = v;
            this.nachname = n;
            this.klasse = k;
            this.einschulungsjahr = j;
        }




        public void WechselKlasse(String neueklasse)
        {
            if (neueklasse.Substring(0, 2) == "FA" || neueklasse.Substring(0, 2) == "FS")
            {
                this.klasse = neueklasse; //variable wird neu zugewiesen
 
            }
            else
            {
                Console.WriteLine("Der Klassenwechsel konnte nicht erfolgen: Falsche Klassenbezeichnung");
            }
        }

        public void Wechselname(String neuervorname, String neuernachname)
        {
            if (this.name != neuervorname || this.nachname != neuernachname)
            {
                this.name = neuervorname; //variable wird neu zugewiesen
                this.nachname = neuernachname;

            }
            else
            {
                Console.WriteLine("Der Name ist gleich wie vorher. Namenswechsel konnte nicht erfolgen");
            }
        }

        public String getname()
        {
            return name;
        }

        public void DruckeInfo()
        {
            Console.WriteLine("Schuelerdatei angepasst:");
            Console.WriteLine("Azubi: "+this.name + "   Nachname: " + this.nachname);                    
            Console.WriteLine("Klasse: " + this.klasse + "   Einschulungsjahr: " + this.einschulungsjahr);
            Console.WriteLine("");
        }

    }   
}

