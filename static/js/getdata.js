var chart;

/**
 * Request data from the server, add it to the graph and set a timeout
 * to request again
 */
function requestData() {
    $.ajax({
        url: '/data',
        success: function(point) {
            var series = chart.series[0],
                shift = series.data.length > 20; // shift if the series is
                                                 // longer than 20
                
            // add the point
            chart.series[0].addPoint(point, true, shift);
            charta.series[0].addPoint(point, true, shift);
            chartb.series[0].addPoint(point, true, shift);
            chartc.series[0].addPoint(point, true, shift);

            // call it again after one second
            setTimeout(requestData, 1000);
        },
        cache: false
    });
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

