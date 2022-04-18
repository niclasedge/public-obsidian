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
           
           Schueler objRuediger = new Schueler();
           Schueler objChrista = new Schueler();
           objRuediger.DruckeInfo();
           objChrista.WechselKlasse("FI22");
           objChrista.DruckeInfo();
           Console.ReadLine();
        }
    }
}
