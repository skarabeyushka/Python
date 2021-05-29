using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;

namespace RESTful_API.Models
{
    public class OrderForm
    {
        [Required]
        public string GoodsId { get; set; }
    }
}
