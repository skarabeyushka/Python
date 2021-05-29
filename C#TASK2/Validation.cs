using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;
using System.Reflection;
using System.Threading.Tasks;
using System.Text.RegularExpressions;

namespace Task_2
{
    public class Input
    {
        public static string ValidateFileName()
        {
            while (true)
            {
                Console.WriteLine("Write file name:");
                string val = Console.ReadLine();
                try
                {
                    if (File.Exists(val) == false)
                    {
                        throw new Exception("File doensn't exist");
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
    }
    public class Validate
    {
        public static DateTime TimeConflict(DateTime a, DateTime b)
        {
            if (a > b)
            {
                Console.WriteLine("We have time conflict");
                throw new Exception("We have time conflict");
            }
            else
            {
                return b;
            }
        }
       
        public static string Checkemail(string val)

        {
            var mailformat = @"\A(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)\Z";

            if (Regex.IsMatch(val,mailformat) == false)
            {
                Console.WriteLine("Wrong email");
                throw new Exception("Wrong email");
            }
            else
            {
                return val;
            }
        }
        public static string CheckDate(string val)
        {
            DateTime dt = DateTime.Parse(val);
            DateTime dt1 = DateTime.Now;
            if (dt < dt1)
            {
                Console.WriteLine("Date conflict");
                throw new Exception("Date conflict");
            }
            else
            {
                return val;
            }
        }
        public static string Checkorderstatus(string val)
        {
            
           
                string[] stringarr;
                stringarr = new string[3] { "paid", "notpaid", "refunded" };
                if (stringarr.Contains(val)==false)
                 {
                     Console.WriteLine("orderstatus wrong");
                      throw new Exception("wrong order status");


                 }                        
                else
                {
                return val;
                }
            
            

        }

        public static string checkdiscount(string val)
        {
            
                string value = "%";
                if (value.Contains(val)==false) 
                 {

                      Console.WriteLine("discount  wrong");
                      throw new Exception("discount  wrong");

                 }
                else
                {
                return val;
                }
           
            

        }
    }
}