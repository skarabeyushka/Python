﻿using System;
using System.Linq;
using System.Text;
using System.IO;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace Task_1
{

    class MainProgram
    {
        static void Main(string[] args)
        {
            ORDER ls = new ORDER();
            string file_name = Input.ValidateFileName();
            ls.FillorderFile(file_name);
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
                string value = "";
                if (userchoice.All(char.IsDigit) == false)
                {
                    Console.WriteLine("please enter a number mentioned above!");
                    continue;
                }
                if (Int32.Parse(userchoice) >= 1 && Int32.Parse(userchoice) < 5)
                {
                    Console.WriteLine("Type value: ");
                    value = Console.ReadLine();
                }
                if (userchoice == "1")
                {
                    ls.Search(value);
                }
                else if (userchoice == "2")
                {
                    ls.Sort(value);
                }
                else if (userchoice == "3")
                {
                    ls.Remove(value, file_name);
                }
                else if (userchoice == "4")
                {
                    ls.AddTo(value, file_name);
                }
                else if (userchoice == "5")
                {
                    Console.WriteLine("Type id:");
                    string id = Console.ReadLine();
                    Console.WriteLine("Type value: ");
                    value = Console.ReadLine();
                    ls.Edit(id, value, file_name);
                }
                else if (userchoice == "6")
                {
                    ls.Print();
                }
                else
                {
                    break;
                }
            }
        }
    }
}