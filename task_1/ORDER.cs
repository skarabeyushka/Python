using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Globalization;
using System.IO;
using System.Threading.Tasks;

namespace Task_1
{
    public class Sorting
    {
        public static String[] fields = { "id","order_status" ,"amount", "discount", "order_date", "shipped_date" };
    }
    public class ORDER
    {
        List<OnlineOrder> lis;
        int size;

        public ORDER()
        {
            lis = new List<OnlineOrder>();
            size = 0;
        }

        public void FillorderFile(string file)
        {
            string[] lines = File.ReadAllLines(file);
            File.WriteAllText(file, string.Empty);
            foreach (string line in lines)
            {
                Validation v = new Validation(line);
                if (v.ValidateAll("add") == true)
                {
                    using (StreamWriter sw = File.AppendText(file))
                    {
                        sw.WriteLine(line);
                        OnlineOrder obj = new OnlineOrder(line);
                        lis.Add(obj);
                        size++;
                    }
                }
            }
        }
        public void AddTo(string val, string file)
        {
            if (Input.ValidateInput(val, "add") == false)
            {
                Console.WriteLine("Values are incorrect!");
                return;
            }
            OnlineOrder m = new OnlineOrder(val);
            lis.Add(m);
            size++;
            RewriteFile(file);
        }

        public void Remove(string id, string file)
        {
            foreach (OnlineOrder i in lis)
            {
                if (i.Get("id") == id)
                {
                    lis.Remove(i);
                    Id.ids.Remove(id);
                    size--;
                    RewriteFile(file);
                    return;
                }
            }
            Console.WriteLine("No such order");
        }

        public void Edit(string id, string val, string file)
        {
            if (Input.ValidateInput(val, "edit") == false)
            {
                Console.WriteLine("Values are incorrect!");
                return;
            }
            String[] arr = val.Split(';');
            if (arr[0] != id)
            {
                Console.WriteLine("You can't change id!");
                return;
            }
            for (int i = 0; i < size; i++)
            {
                if (lis[i].Get("id") == id)
                {
                    OnlineOrder a = new OnlineOrder(val);
                    lis[i] = a;
                    RewriteFile(file);
                    return;
                }
            }
            Console.WriteLine("No such id");
        }


        public bool Compare(string param, OnlineOrder a, OnlineOrder b)
        {
            string x = a.Get(param);
            string y = b.Get(param);
             if (param == "order_date" || param == "shipped_date" )
            {
                DateTime d = DateTime.Parse(x);
                DateTime d1 = DateTime.Parse(y);
                return DateTime.Compare(d, d1) > 0;
            }
            else if (param == "id")
            {
                return Int32.Parse(x) > Int32.Parse(y);
            }
            else if (param == "amount")
            {
                return Int32.Parse(x) > Int32.Parse(y);
            }
            else if (param == "discount")
            {
                return Int32.Parse(x) > Int32.Parse(y);
            }
            else
            {
                return true;
            }
        }

        public void Sort(string param)
        {
            if (Sorting.fields.Contains(param) == false)
            {
                Console.WriteLine("no sorting with this parametr");
                return;
            }
            for (int i = 0; i < size - 1; i++)
            {
                for (int j = 0; j < size - i - 1; j++)
                {
                    if (Compare(param, lis[j], lis[j + 1]))
                    {
                        OnlineOrder tmp = lis[j];
                        lis[j] = lis[j + 1];
                        lis[j + 1] = tmp;
                    }
                }
            }
        }

        public void RewriteFile(string file)
        {
            File.WriteAllText(file, string.Empty);
            foreach (OnlineOrder obj in lis)
            {
                using (StreamWriter sw = File.AppendText(file))
                {
                    sw.WriteLine(obj.FileFormat());
                }
            }
        }

        public void Search(string val)
        {
            foreach (OnlineOrder i in lis)
            {
                if (i.search(val))
                {
                    Console.WriteLine(i);
                }
            }
        }

        public void Print()
        {
            foreach (OnlineOrder i in lis)
            {
                Console.WriteLine(i);
            }
        }
    }
}