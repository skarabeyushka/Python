using RESTful_API.Authentication;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.Text.Json.Serialization;
using System.Threading.Tasks;

namespace RESTful_API.Models
{
    public class Order
    {
        public string OrderId { get; set; }
        public string ApplicationUserId { get; set; }
        [JsonIgnore]
        [IgnoreDataMember]
        public virtual ApplicationUser ApplicationUser { get; set; }
        public string GoodsId { get; set; }
        [JsonIgnore]
        [IgnoreDataMember]
        //public Meeting Meeting { get; set; }
        public virtual Goods Goods { get; set; }
    }
}
