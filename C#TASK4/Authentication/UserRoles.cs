using Microsoft.AspNetCore.Authorization;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace RESTful_API.Authentication
{
    //public static class UserRoles
    //{
    //    public const string Admin = "Admin";
    //    public const string User = "User";
    //    //public const string Admin = "Admin";
    //    //public const string User = "User";
    //}
    [Flags]
    public enum UserRoles
    {
        Admin,
        User
    }
    public class MyAuthorizeAttribute : AuthorizeAttribute
    {
        private UserRoles roleEnum;
        public UserRoles RoleEnum
        {
            get { return roleEnum; }
            set { roleEnum = value; base.Roles = value.ToString(); }
        }
    }
}
