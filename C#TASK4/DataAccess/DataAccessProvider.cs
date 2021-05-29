using RESTful_API.Authentication;
using RESTful_API.Controllers;
using RESTful_API.Models;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Linq.Expressions;
using System.Threading.Tasks;

namespace RESTful_API.DataAccess
{
    public class DataAccessProvider : IDataAccessProvider
    {
        private readonly ApplicationDbContext context;
        private bool b = false;

        public DataAccessProvider(ApplicationDbContext cont)
        {
            context = cont;
        }
        public void AddGoodsRecord(Goods g)
        {
            context.goods.Add(g);
            context.SaveChanges();
        }

        public void DeleteGoodsRecord(string id)
        {
            var entity = context.goods.FirstOrDefault(g => g.id == id);
            context.goods.Remove(entity);
            context.SaveChanges();
        }

        public List<Goods> GetGoodsRecords()
        {
            return context.goods.ToList();
        }

        public Goods GetGoodsSingleRecord(string id)
        {
            return context.goods.FirstOrDefault(g => g.id == id);
        }

        public void UpdateGoodsRecord(Goods g)
        {
            context.goods.Update(g);
            context.SaveChanges();
        }

        public IQueryable<Goods> GetGoodsWithOperations(OperationInGet operation)
        {
            /*if (!b)
            {
                Goods a = new Goods { id = "aiglglvdhsbscc5g4", code = "123-456-456", title = "Boots", type = "Shoes", amount = 12, price = 710.5, date = new DateTime(2019, 10, 4) };
                Goods c = new Goods { id = "isusjhslvdhsbscc5g4", code = "123-456-556", title = "Milk", type = "Food", amount = 10, price = 10.99, date = new DateTime(2021, 4, 4) };
                Goods d = new Goods { id = "tiglglvokdldld5g4", code = "123-456-466", title = "Bread", type = "Food", amount = 20, price = 16.75, date = new DateTime(2021, 5, 4) };
                Goods e = new Goods { id = "figlg785dyhsbscc", code = "123-456-996", title = "Shirt", type = "Clothes", amount = 17, price = 310.5, date = new DateTime(2020, 10, 4) };
                Goods f = new Goods { id = "higlsyrr88bscc5g4", code = "123-456-756", title = "Cheese", type = "Food", amount = 8, price = 30.99, date = new DateTime(2021, 4, 30) };
                context.Items.Add(a);
                context.SaveChanges();
                context.Items.Add(c);
                context.SaveChanges();
                context.Items.Add(d);
                context.SaveChanges();
                context.Items.Add(e);
                context.SaveChanges();
                context.Items.Add(f);
                context.SaveChanges();
                b = true;
            }*/
            IQueryable<Goods> goods = context.goods;
            var prop = typeof(Goods).GetProperty(operation.Sort_by);
            if (prop != null)
            {
                var parametr = Expression.Parameter(typeof(Goods));
                var expr = Expression.Lambda<Func<Goods, object>>(Expression.Convert(Expression.Property(parametr, prop), typeof(object)), parametr);
                if (operation.Sort_type == "desc")
                {
                    goods = goods.OrderByDescending(expr);
                }
                else
                {
                    goods = goods.OrderBy(expr);
                }
            }
            var goods1 = (from g in goods select g).AsEnumerable();
            if (!string.IsNullOrEmpty(operation.Search))
            {
                var properties = typeof(Goods).GetProperties();
                goods1 = goods1.Where(c => properties.Any(p => p.GetValue(c, null).ToString().Contains(operation.Search)));
            }
            return goods1.AsQueryable();
        }

        public List<Order> GetOrderRecords()
        {
            return context.orders.ToList();
        }
        public IQueryable<Goods> GetRecords(OwnerParameters ownerParameters)
        {
            IQueryable<Goods> query = context.goods;

            var type = typeof(Goods);
            var prop = type.GetProperty(ownerParameters.Sort_by);
            if (prop != null)
            {
                var param = Expression.Parameter(type);
                var expr = Expression.Lambda<Func<Goods, object>>(
                    Expression.Convert(Expression.Property(param, prop), typeof(object)),
                    param
                );
                if (ownerParameters.Sort_type == "desc")
                {
                    query = query.OrderByDescending(expr);
                }
                else
                {
                    query = query.OrderBy(expr);
                }
            }
            var list = (from r in query select r).AsEnumerable();
            if (!string.IsNullOrEmpty(ownerParameters.Search))
            {
                var stringProperties = typeof(Goods).GetProperties();
                list = list.Where(c => stringProperties.Any(prop => prop.GetValue(c, null).ToString().Contains(ownerParameters.Search)));
            }
            var list1 = list.AsQueryable();
            return list1;
        }
        public bool MeetingExists(string id)
        {
            return context.goods.Any(e => e.id == id);
        }

        public bool InOrder(string id)
        {
            IQueryable<Order> query = context.orders;
            foreach (var o in query)
            {
                if (o.GoodsId == id)
                {
                    return true;
                }
            }
            return false;
        }
    }
}
