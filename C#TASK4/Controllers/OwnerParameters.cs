﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace RESTful_API.Controllers
{
    public class OwnerParameters
    {
		private string _sort_by = "Owner";
		private string _sort_type = "asc";
		private string _search;

		public string Sort_by
		{
			get { return _sort_by; }
			set { _sort_by = value; }
		}
		public string Sort_type
		{
			get { return _sort_type; }
			set { _sort_type = value; }
		}
		public string Search
		{
			get { return _search; }
			set { _search = value; }
		}
	}
}
