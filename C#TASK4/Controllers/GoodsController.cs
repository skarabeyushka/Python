using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using RESTful_API.Models;
using RESTful_API.DataAccess;
using LightQuery;

namespace RESTful_API.Controllers
{
    [Route("api/Goods")]
    [ApiController]
    public class GoodsController : Controller
    {
        private readonly IDataAccessProvider dataAccessProvider;

        public GoodsController(IDataAccessProvider data)
        {
            dataAccessProvider = data;
        }

        [LightQuery(forcePagination: false, defaultPageSize: 10)]
        [ProducesResponseType(typeof(IEnumerable<Goods>), 200)]
        [HttpGet]
        public IActionResult Get([FromQuery] OperationInGet operation)
        {
            var res = dataAccessProvider.GetGoodsWithOperations(operation);
            return Ok(res);
        }

        [HttpPost]
        public IActionResult Create([FromBody] Goods g)
        {
            if (ModelState.IsValid)
            {
                Guid obj = Guid.NewGuid();
                g.id = obj.ToString();
                dataAccessProvider.AddGoodsRecord(g);
                return Ok("Goods was posted succesfully!");
            }
            return BadRequest();
        }

        [HttpGet("{id}")]
        public Goods Details(string id)
        {
            return dataAccessProvider.GetGoodsSingleRecord(id);
        }

        [HttpPut]
        public IActionResult Edit([FromBody] Goods g)
        {
            if (ModelState.IsValid)
            {
                dataAccessProvider.UpdateGoodsRecord(g);
                return Ok("Goods was edited succesfully!");
            }
            return BadRequest();
        }

        [HttpPut("{id}")]
        public IActionResult Edit(string id, [FromBody] Goods g)
        {
            if (ModelState.IsValid)
            {
                if (id != g.id)
                {
                    return BadRequest();
                }
                dataAccessProvider.UpdateGoodsRecord(g);
                return Ok("Goods was edited succesfully!");
            }
            return BadRequest();
        }

        [HttpDelete("{id}")]
        public IActionResult DeleteConfirmed(string id)
        {
            var data = dataAccessProvider.GetGoodsSingleRecord(id);
            if (data == null)
            {
                return NotFound();
            }
            dataAccessProvider.DeleteGoodsRecord(id);
            return Ok("Goods was deleted succesfully!");
        }
    }
}
