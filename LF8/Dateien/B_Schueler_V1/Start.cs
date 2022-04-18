using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace B_Schueler_V1
{
    class Start
    {
        static void Main(string[] args)
        {
           
           Schueler objRuediger = new Schueler("Ruediger");
            objRuediger.DruckeInfo();
            Schueler objChrista = new Schueler("Christa","Schmitz", "FS23", 2021);
           objChrista.DruckeInfo();
            objChrista.WechselKlasse("FS33");
            objChrista.DruckeInfo();
            objChrista.Wechselname("Marie", "Berger");
            objChrista.DruckeInfo();
            Console.ReadLine();

            Console.WriteLine(objChrista.getname()); //spricht ein bestimmtes Objekt an und returned den namen
            // wenn name "public" wäre, könnte man ihn via objChrista.name direkt abrufen
        }
    }
}
