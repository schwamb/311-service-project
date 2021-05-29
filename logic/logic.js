

d3.select("#predict").on("click", function(){
    var srType = d3.select("#selectSR").node().value;
    var ward = d3.select("#selectWard").node().value;
    // Assign the value of the dropdown menu option to a variable
    var raw_param = d3.select("#meeting-time").node().value;
    console.log(raw_param)
    var stringDate = raw_param.toString()
    console.log(stringDate)
    var month = parseFloat(stringDate.slice(5,7))
    console.log(month)
    var hour = parseFloat(stringDate.slice(8,10))
    console.log(hour)

    var url = `./predict?srType=${srType}&ward=${ward}&month=${month}&hour=${hour}`
    d3.json(url).then(function(data){
        d3.select("#prediction").text(data)
    })
})





// d3.json("http://127.0.0.1:5000//api/v1.0/test").then((algorithm) => {
// console.log(algorithm)    
// return algorithm;
// })
// d3.select("#selectSR").on("change", updateSRType);
// function updateSRType() {
//     // Use D3 to select the dropdown menu
//     var param1 = d3.select(this).property("value")
//     // Assign the value of the dropdown menu option to a variable
//     // var dataset = dropdownMenu.node().value;
//     console.log(param1)
//     return param1
// }
// console.log(param1)
// d3.select("#selected-dropdown").text("Abandoned Vehicle Complaint");
// d3.select("#selected-dropdown").text("Abandoned Vehicle Complaint");

// d3.select("select")
//   .on("change",function(d){
//     var param1 = d3.select("#selectSR").node().value;
//     console.log( param1 );
//     // d3.select("#selected-dropdown").text(param1);
// })

// d3.selectAll("#selectWard").on("change", updateWard);
// function updateWard() {
//     // Use D3 to select the dropdown menu
//     var param2 = d3.select("#selectWard").node().value;
//     // Assign the value of the dropdown menu option to a variable
//     console.log(param2)
//     return param2
// }
// d3.selectAll("#meeting-time").on("change", updateDate);
// function updateDate() {
//     // Use D3 to select the dropdown menu
//     var raw_param = d3.select("#meeting-time").node().value;
//     // Assign the value of the dropdown menu option to a variable
//     // var dataset = dropdownMenu.node().value;
//     param3 = raw_param.slice[5,6]
//     param4 = raw_param.slice[11,12]
//     console.log(param3)
//     return param3
// }

// function updateHour() {
//     // Use D3 to select the dropdown menu
//     var param4 = d3.select("#selDatasetSR");
//     // Assign the value of the dropdown menu option to a variable
//     // var dataset = dropdownMenu.node().value;
//     return param4
// }

  