using Microsoft.AspNetCore.Identity;
using RESTful_API.Authentication;
using RESTful_API.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace RESTful_API.DataAccess
{
    public class Help
    {
        private readonly ApplicationDbContext _context;

        public Help(ApplicationDbContext context)
        {
            _context = context;
        }
        public bool AlreadySubscribed(string id, IdentityUser user)
        {
            IQueryable<Order> query = _context.orders;
            var list = (from r in query select r).AsEnumerable();
            list = list.Where(c => c.ApplicationUser.Id == user.Id && c.GoodsId == id);
            return list.Count() > 0;
        }
    }
}
