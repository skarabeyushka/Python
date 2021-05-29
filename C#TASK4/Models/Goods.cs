using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Threading.Tasks;

namespace RESTful_API.Models
{
    public class Goods
    {
        public string id { get; set; }
        [Required]
        [StringLength(11, ErrorMessage = "Code lenght must be 11!")]
        [RegularExpression(@"([0-9]{3}-[0-9]{3}-[0-9]{3})*$", ErrorMessage = "Wrong code format!")]
        public string code { get; set; }
        [Required]
        [StringLength(128, ErrorMessage = "Title lenght can't be more than 50!")]
        [RegularExpression(@"^[A-Z]+[a-zA-Z]*$", ErrorMessage = "Invalid title!")]
        public string title { get; set; }
        [Required]
        [StringLength(128, ErrorMessage = "Type lenght can't be more than 50!")]
        [RegularExpression(@"^[A-Z]+[a-zA-Z]*$", ErrorMessage = "Invalid type!")]
        public string type { get; set; }
        [Required]
        [Range(0, int.MaxValue, ErrorMessage = "Amount can't be less than 0!")]
        public int amount { get; set; }
        [Required]
        [Column(TypeName = "decimal(18, 2)")]
        [Range(0, double.MaxValue, ErrorMessage = "Price can't be less than 0!")]
        public double price { get; set; }
        [Required]
        [Range(typeof(DateTime), "01.01.0001 0:00:00", "18.05.2021 0:00:00", ErrorMessage = "Date can't be more than today's!")]
        public DateTime date { get; set; }

    }
}
