using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace RESTful_API.Models
{
    public class OperationInGet
    {
        public int PageN { get; set; } = 1;
        public int PageSize { get => pageSize; set => pageSize = value; }
        public string Sort_by { get => sort_by; set => sort_by = value; }
        public string Sort_type { get => sort_type; set => sort_type = value; }
        public string Search { get => search; set => search = value; }

        private int pageSize;
        private string sort_by = "title";
        private string sort_type = "asc";
        private string search;

    }
}
