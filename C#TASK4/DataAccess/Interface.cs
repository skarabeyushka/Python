using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using RESTful_API.Controllers;
using RESTful_API.Models;

namespace RESTful_API.DataAccess
{
    public interface IDataAccessProvider
    {
        void AddGoodsRecord(Goods g);
        void UpdateGoodsRecord(Goods g);
        void DeleteGoodsRecord(string id);
        Goods GetGoodsSingleRecord(string id);
        List<Goods> GetGoodsRecords();
        IQueryable<Goods> GetGoodsWithOperations(OperationInGet operation);
        List<Order> GetOrderRecords();
        IQueryable<Goods> GetRecords(OwnerParameters ownerParameters);
        bool MeetingExists(string id);
        bool InOrder(string id);
    }
}
