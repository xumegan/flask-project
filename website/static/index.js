function deletenote(noteId){
  fetch('/delete-note',{
    method:'POST',
    body:JSON.stringify({noteId:noteId}),
  }).then((_res)=>{
    window.location.href ="/";
  });
}

// //charts
// var chartdata = []
// var volume = []

// function processData(data)
// {
//     var data = data.res;
//     for (var i=0; i < data.length; i++)
//     {
//         chartdata.push([
//             data[i][0], // the date
//             data[i][1], // open
//             data[i][2], // high
//             data[i][3], // low
//             data[i][4] // close
//         ]);
//         volume.push([
//             data[i][0], // the date
//             data[i][5] // the volume
//         ]);
//     }
// }


// function plotCharts(){
//     Highcharts.stockChart('container', {
//         navigation: {
//             bindings: {
//                 rect: {
//                     annotationsOptions: {
//                         shapeOptions: {
//                             fill: 'rgba(255, 0, 0, 0.8)'
//                         }
//                     }
//                 }
//             },
//             annotationsOptions: {
//                 typeOptions: {
//                     line: {
//                         stroke: 'rgba(255, 0, 0, 1)',
//                         strokeWidth: 10
//                     }
//                 }
//             }
//         },
//         yAxis: [{
//             labels: {
//                 align: 'left'
//             },
//             height: '80%'
//         }, {
//             labels: {
//                 align: 'left'
//             },
//             top: '80%',
//             height: '20%',
//             offset: 0
//         }],
//         series: [{
//             type: 'line',
//             id: 'aapl-ohlc',
//             name: 'AAPL Stock Price',
//             data: chartdata
//         }, {
//             type: 'column',
//             id: 'aapl-volume',
//             name: 'AAPL Volume',
//             data: volume,
//             yAxis: 1
//         }]
//     });


// }

// $( document ).ready(function()
// {
//     $.getJSON('/pipe', function(data){
//         processData(data);
//         plotCharts();
//     });
// });