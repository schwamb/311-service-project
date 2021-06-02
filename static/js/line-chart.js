

d3.json("http://127.0.0.1:5000/api/v1.0/311_data").then((service_data) => {
    // function filterStatusData(SR_TYPE) {
    //     return SR_TYPE.STATUS === "COMPLETED";
    //   }
      // Use filter() to pass the function as its argument
    // var filteredReqeusts = service_data.filter(filterStatusData);
  // Use filter() to pass the function as its argument
    // var SRType = filteredReqeusts.map(SR_TYPE => SR_TYPE.SR_TYPE);
    var ward = service_data.map(WARD => WARD.WARD);
    var created_date = service_data.map(CREATED_DATE => CREATED_DATE.CREATED_DATE);
    var tat = service_data.map(TIME_TO_COMPLETION => TIME_TO_COMPLETION.TIME_TO_COMPLETION);
    // var SRType = service_data.map(SR_TYPE => SR_TYPE.SR_TYPE);
    // console.log(SRType)
    console.log(created_date)
  // Create your trace.
  var traceSRType = {
    x: created_date,
    y: tat,
    type: "bar"
  };

  var traceward = {
    x: ward,
    y: tat,
    type: "bar"
  }; 




//   var tracetrust = {
//     x: country2020,
//     y: trust2020,
//     type: "bar"
//   }; 
  // Create the data array for our plot
  var srt = [traceSRType];
  var ward = [traceward];
  var data = [];
//   var trust = [tracetrust];


function init() {
  data
  ;
  var layout = {
    title: "Happiness Scores by Country",
    xaxis: { title: "Country"},
    yaxis: { title: "Happiness Score"}
  };
  Plotly.newPlot("bar-plot", data, layout);
}
// Plotly.update("bar-plot", srt, layout);
// d3.selectAll("#selDataset").on("change", updatePlotly);
// // This function is called when a dropdown menu item is selected
// function updatePlotly() {
//   // Use D3 to select the dropdown menu
//   var dropdownMenu = d3.select("#selDataset");
//   // Assign the value of the dropdown menu option to a variable
//   var dataset = dropdownMenu.node().value;

//  var data = []
 

//   if (dataset === 'srt') {
//       data = srt;
//       var layout = {
//         title: "Happiness Scores by Country",
//         xaxis: { title: "Country"},
//         yaxis: { title: "Happiness Score"}
//       };
//   };
//   if (dataset === 'ward') {
//     data = ward;
//     var layout = {
//       title: "GDP by Country",
//       xaxis: { title: "Country"},
//       yaxis: { title: "GDP"}
//     };
//   };
// //   if (dataset === 'Trust Score') {
// //     data = trust;
// //     var layout = {
// //       title: "Trust Score by Country",
// //       xaxis: { title: "Country"},
// //       yaxis: { title: "Trust Score"}
// //     };
// //   };
//   // Define the plot layout

//   // Plot the chart to a div tag with id "bar-plot"
//   Plotly.newPlot("bar-plot", data, layout);
// }
init();
});