using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;
using System.Threading.Tasks;
using System.Text.RegularExpressions;

namespace Task_2
{
    class MainProgram
    {
        public static class FillCollection<T> where T : OnlineOrder, new()
        {
            public static Collection<T> Method(string file)
            {
                Collection<T> a = new Collection<T>();
                string[] lines = File.ReadAllLines(file);
                File.WriteAllText(file, string.Empty);
                foreach (string line in lines)
                {
                    using (StreamWriter sw = File.AppendText(file))
                    {
                        sw.WriteLine(line);
                        var instance = Activator.CreateInstance<T>();
                        try
                        {
                            instance = Activator.CreateInstance(typeof(T), new object[] { line }) as T;
                          
                        }
                        catch 
                        {
                            
                            Console.WriteLine("Wrong format of some values!");
                            continue;
                        }
                        Console.WriteLine(instance);
                        a.AddTo(instance, "None");
                    }
                }
                a.RewriteFile(file);
                return a;
            }
        }
        static void Main(string[] args)
        {
          
            string file_name = Input.ValidateFileName();
            Collection<OnlineOrder> ls = FillCollection<OnlineOrder>.Method(file_name);
        
            while (true)
            {
                Console.WriteLine(@"WELCOME USER Enter your choice:
              1.) Search ordes by  value
              2.) Sort by parametr
              3.) Delete order by ID
              4.) Add order
              5.) Edit order by ID
              6.) See all available orders
              7.) Exit");
                string userchoice = Console.ReadLine();
                string val = "";
                if (userchoice.All(char.IsDigit) == false)
                {
                    Console.WriteLine("Number should contain digits!");
                    continue;
                }
                if (Int32.Parse(userchoice) >= 1 && Int32.Parse(userchoice) < 5)
                {
                    Console.WriteLine("Type value: ");
                    val = Console.ReadLine();
                }
                if (userchoice == "1")
                {
                    ls.Search(val);
                }
                else if (userchoice == "2")
                {
                    ls.Sort(val);
                }
                else if (userchoice == "3")
                {
                    ls.Remove(val, file_name);
                }
                else if (userchoice == "4")
                {
                    OnlineOrder obj = new OnlineOrder();
                    try
                    {
                        obj = new OnlineOrder(val);
                    }
                    catch
                    {
                        Console.WriteLine("Rewrite values!");
                        continue;
                    }
                    ls.AddTo(obj, file_name);
                }
                else if (userchoice == "5")
                {
                    Console.WriteLine("Type id:");
                    string id = Console.ReadLine();
                    Console.WriteLine("Type value: ");
                    val = Console.ReadLine();
                    ls.Edit(id, val, file_name);
                }
                else if (userchoice == "6")
                {
                    ls.Print();
                }
                else if (userchoice == "7")
                {
                    break;
                }
            }
        }

        
    }
}