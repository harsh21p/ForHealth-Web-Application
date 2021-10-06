var chart;

/**
 * Request data from the server, add it to the graph and set a timeout
 * to request again
 */
var i=0;
var j=0;
var k=0;
var l=0;

function requestData() {

    if(i==20){
        $.ajax({
            url: '/data1',
            success: function(point) {
                var series = chart.series[0],
                    shift = series.data.length > 20; // shift if the series is
                                                     // longer than 20
                    
                // add the point
                
                charta.series[0].addPoint(point, true, shift);
               
    
               
            },
            cache: false
        });
        i=0;
    }

    if(j==5){
        $.ajax({
            url: '/data',
            success: function(point) {
                var series = chart.series[0],
                    shift = series.data.length > 20; // shift if the series is
                                                    // longer than 20
                    
                // add the point
                chart.series[0].addPoint(point, true, shift);
            

                // call it again after one second
            },
            cache: false
        });
        j=0;

    }

    if(k==10){
        $.ajax({
            url: '/data2',
            success: function(point) {
                var series = chart.series[0],
                    shift = series.data.length > 20; // shift if the series is
                                                    // longer than 20
                    
                // add the point
                
                chartb.series[0].addPoint(point, true, shift);
            

                // call it again after one second
                
            },
            cache: false
        });
        k=0;
    }

   
    if(l==15){
        $.ajax({
            url: '/data3',
            success: function(point) {
                var series = chart.series[0],
                    shift = series.data.length > 20; // shift if the series is
                                                    // longer than 20
                    
                // add the point
                
                chartc.series[0].addPoint(point, true, shift);
            

                // call it again after one second
                
            },
            cache: false
        });
        l=0;
    }

    i=i+1;
    j=j+1;
    k=k+1;
    l=l+1;

    setTimeout(requestData, 300);
}



$(document).ready(function() {
    chart = new Highcharts.Chart({
        chart: {
            renderTo: 'data-container',
            defaultSeriesType: 'spline',
            events: {
                load: requestData
            }
        },
        title: {
            text: 'Live1'
        },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 150,
            maxZoom: 20 * 1000
        },
        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: 'Value',
                margin: 10
            }
        },
        series: [{
            name: 'Data',
            data: []
        }]
    });
});



$(document).ready(function() {
    charta = new Highcharts.Chart({
        chart: {
            renderTo: 'data-container1',
            defaultSeriesType: 'spline',
            events: {
                load: requestData
            }
        },
        title: {
            text: 'Live2'
        },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 150,
            maxZoom: 20 * 1000
        },
        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: 'Value',
                margin: 10
            }
        },
        series: [{
            name: 'Data',
            data: []
        }]
    });
});

$(document).ready(function() {
    chartb = new Highcharts.Chart({
        chart: {
            renderTo: 'data-container2',
            defaultSeriesType: 'spline',
            events: {
                load: requestData
            }
        },
        title: {
            text: 'Live3'
        },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 150,
            maxZoom: 20 * 1000
        },
        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: 'Value',
                margin: 0
            }
        },
        series: [{
            name: 'Data',
            data: []
        }]
    });
});


$(document).ready(function() {
    chartc = new Highcharts.Chart({
        chart: {
            renderTo: 'data-container3',
            defaultSeriesType: 'spline',
            events: {
                load: requestData
            }
        },
        title: {
            text: 'Live4'
        },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 50,
            maxZoom: 20 * 1000
        },
        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: 'Value',
                margin: 0
            }
        },
        series: [{
            name: 'Data',
            data: []
        }]
    });
});

