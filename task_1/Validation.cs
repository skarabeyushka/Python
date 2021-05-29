using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using System.Text;
using System.Globalization;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.Net.Mail;

namespace Task_1
{
    public class Id
    {
        public static List<string> ids = new List<string>();
    }
    public class Input
    {
        public static bool ValidateInput(string val, string str)
        {
            Validation obj = new Validation(val);
            return obj.ValidateAll(str);
        }

        public static string ValidateFileName()
        {
            while (true)
            {
                Console.WriteLine("enter file name:");
                string val = Console.ReadLine();
                try
                {
                    if (File.Exists(val) == false)
                    {
                        throw new Exception("file don't exist");
                    }

                }
                catch (Exception z)
                {
                    Console.WriteLine(z.Message);
                    continue;
                }
                return val;
            }
        }

        public static void ValidateFileInput(string file)
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
                    }
                }
            }
        }
    }
    class Validation
    {
        String[] l = { };

        public Validation(string s)
        {
            this.l = s.Split(';');
        }
        public bool CheckLength()
        {
            try
            {
                if (l.Length != 7)
                {
                    throw new Exception("Wrong Length!");
                }
            }
            catch (Exception z)
            {
                Console.WriteLine(z.Message);
                return false;
            }
            return true;
        }
        public bool CheckEMAil()
        {
            try
            {
                string email = l[6];
               
                string pattern = @"\A(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)\Z";

                if (Regex.IsMatch(email, pattern))
                {
                   
                }
                else
                {
                    throw new Exception("Wrong email!");
                }

            }
            catch (Exception z)
            {
                Console.WriteLine(z.Message);
                return false;
            }
            return true;
        }
    
        
        public bool CheckDate()
        {
            try
            {
                DateTime dt = DateTime.Parse(l[4]);
                DateTime dt1 = DateTime.Parse(l[5]);
                if (dt > dt1)
                {
                    throw new Exception("Wrong date");
                }
            }
            catch (Exception z)
            {
                Console.WriteLine(z.Message);
                return false;
            }
            return true;
        }
        public bool Checkorderstatus()
        {
            try
            {
                string order = l[1];
                string[] stringarr;
                stringarr = new string[3] { "paid", "notpaid", "refunded" };
                if (stringarr.Contains(order)) { }
                else
                {
                    throw new Exception("wrong order status");
                }
            }
            catch (Exception z)
            {
                Console.WriteLine(z.Message);
                return false;
            }
            return true;

        }

        public bool checkdiscount()
        {
            try
            {
                string discount = l[3];
                string val =  "%"; 
                if (discount.Contains(val)) { }
                else
                {
                    throw new Exception("wrong discount ");
                }
            }
            catch(Exception z)
            {
                Console.WriteLine(z.Message);
                return false;
            }
            return true;

        }

        public bool CheckId()
        {
            try
            {
                if (Id.ids.Contains(l[0]) || l[0].All(char.IsDigit) == false)
                {
                    throw new Exception("Wrong id!");
                }
                else if (Int32.Parse(l[0]) == 0)
                {
                    throw new Exception("Id can't be zero!");
                }
            }
            catch (Exception z)
            {
                Console.WriteLine(z.Message);
                return false;
            }
            Id.ids.Add(l[0]);
            return true;
        }
        public bool ValidateAll(string str)
        {
            if (CheckLength() && checkdiscount()&&  Checkorderstatus() && CheckDate() && CheckEMAil())
            {
                if (str == "add")
                {
                    return CheckId();
                }
                return true;
            }
            if (Id.ids.Contains(l[0]))
            {
                Id.ids.Remove(l[0]);
            }
            return false;
        }
    }
}