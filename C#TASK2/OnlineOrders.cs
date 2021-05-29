using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Reflection;
using System.Threading.Tasks;
using System.ComponentModel;

namespace Task_2
{
    public class Default
    {
        public static string m = DateTime.Now.AddDays(5).ToString("dd.MM.yyyy");
        public static string[] values = { "1","paid"," 230", "50%", "chaTRGE.HAJ11@GMAIL.COM" };
    }
    public class OnlineOrder
    {
        int id;
        string order_status;
        int amount;
        string discount;
        DateTime order_date;
        DateTime shipped_date;
        string email;


        public int ID
        {
            get { return id; }
            set { id = value; }
        }
        public string Order_status
        {
            get { return order_status; }
            set { order_status = Validate.Checkorderstatus(value); }
        }
        public int Amount
        {
            get { return amount; }
            set { amount = value; }
        }
        public DateTime Order_date
        {
            get { return order_date; }
            set { order_date = value; }
        }
        public DateTime Shipped_date
        {
            get { return shipped_date; }
            set { shipped_date = value; }
        }
        public string Discount
        {
            get { return discount; }
            set { discount = Validate.checkdiscount(value); }
        }
       

        public string Email
        {
            get { return email; }
            set { email = Validate.Checkemail(value); }
        }
       
        public OnlineOrder()
        {
            int i = 0;
            PropertyInfo[] props = this.GetType().GetProperties();
            foreach (var prop in props)
            {
                prop.SetValue(this, Convert.ChangeType(Default.values[i], prop.PropertyType));
                i++;
            }
        }
        public OnlineOrder(string s)
        {
            string[] l = s.Split(';');
            if (l.Length != 7)
            {
                List<string> m = l.ToList();
                m.AddRange(Enumerable.Repeat("", 7 - l.Length));
            }
            int i = 0;
            PropertyInfo[] props = this.GetType().GetProperties();
            foreach (var prop in props)
            {
                prop.SetValue(this, Convert.ChangeType(l[i], prop.PropertyType));
                i++;
            }
        }
        public string Get(string s)
        {
            PropertyInfo[] props = this.GetType().GetProperties();
            foreach (var item in props)
            {
                if (item.Name == s)
                {
                    return Convert.ToString(item.GetValue(this));
                }
            }
            return "No such field";
        }
        public bool search(string s)
        {
            PropertyInfo[] props = this.GetType().GetProperties();
            foreach (var item in props)
            {
                string m = Convert.ToString(item.GetValue(this));
                if (m.Contains(s))
                {
                    return true;
                }
            }
            return false;
        }
        public override String ToString()
        {
            string res = "";
            PropertyInfo[] props = this.GetType().GetProperties();
            foreach (var prop in props)
            {
                if (prop.Name == "order_date" || prop.Name == "shipped_date")
                {
                    DateTime dt = DateTime.Parse(prop.GetValue(this).ToString());
                    res += Convert.ToString(dt.TimeOfDay) + ";";

                    continue;
                }
                res += prop.GetValue(this).ToString() + ";";
            }
            res = res.Substring(0, res.Length - 1);
            return res;
        }
    }
}