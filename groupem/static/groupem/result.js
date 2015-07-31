data = [[{  "name": "Donna Harper"}, {  "name": "Ronald Willis"}, {
  "name": "Amy Scott"
}, {
  "name": "Shirley Robertson"
}, {
  "name": "Eugene Reyes"
}, {
  "name": "Richard Johnson"
}, {
  "name": "Catherine Ramirez"
}, {
  "name": "Jimmy Baker"
}, {
  "name": "Jesse Stanley"
}, {
  "name": "Elizabeth Nichols"
}], [{
  "name": "Donna Bryant"
}, {
  "name": "Albert Graham"
}, {
  "name": "Emily Lopez"
}, {
  "name": "Lillian Hunt"
}, {
  "name": "Rose Carpenter"
}, {
  "name": "Edward James"
}, {
  "name": "Andrea Montgomery"
}, {
  "name": "Nancy Fowler"
}, {
  "name": "Kelly Ruiz"
}, {
  "name": "Ann Berry"
}], [{
  "name": "Patrick Roberts"
}, {
  "name": "Matthew Lee"
}, {
  "name": "Mary Hamilton"
}, {
  "name": "Douglas Chapman"
}, {
  "name": "Ruth Hunter"
}, {
  "name": "Samuel Thomas"
}, {
  "name": "Diana Spencer"
}, {
  "name": "Phyllis Morrison"
}, {
  "name": "Jean Stevens"
}, {
  "name": "Ronald Hamilton"
}]]


var module_table = d3.select("#result_info").append("table"), 
    module_thead = module_table.append("thead"), 
    module_tbody = module_table.append("tbody");
var columns = ["Team 1", "Team 2", "Team 3", "Team 4", "Team 5", "Team 6", "Team 7", "Team 8", "Team 9","Team 10"]

// append the header row
module_thead.append("tr")
    .selectAll("th")
    .data(columns)
    .enter()
    .append("th")
    .style("text-align","center")
    .text(function(column) { return column; });

//create the table body
var module_rows = module_tbody.selectAll("tr")
      .data(data);
// row exit
module_rows.exit().remove();

// row update
var module_cols = module_rows.selectAll("td")
      .data(function(row) {return row;});

module_cols.attr("class","update")
			.style("text-align","center")
			.text(function(d) { return d.name;});


module_cols.exit().remove()

module_cols.enter()
      .append("td")
      .style("text-align","center")
      .text(function(d) {return d;});

// row enter
var new_module_cols = module_rows.enter()
						          .append("tr")
						          .selectAll("td")
						          .data(function(row) { return row;});
new_module_cols.enter()
				.append("td")
				.attr("class", "enter")
				.style("text-align","center")
				.text(function(d) {return d.name;});
new_module_cols.exit().remove();