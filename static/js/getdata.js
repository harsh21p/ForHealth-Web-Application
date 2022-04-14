var chart;
var chartb;

var i=0;
var j=0;
var k=0;
var l=0;

function requestData() {


    if(j==5){
        
        $.ajax({
            url: '/torque',
            success: function(point) {
                var series = chart.series[0],
                    shift = series.data.length > 20;
                chart.yAxis[0].setExtremes(0,30000);
                chart.series[0].addPoint(point, true, shift);
            },
            cache: false
        });
        j=0;

    }

    if(i==5){
        
        $.ajax({
            url: '/angle',
            success: function(point) {

                document.getElementById("angle").innerHTML ="Angle = <b>"+point+"°</b>";

            },
            cache: false
        });
        i=0;

    }

    if(k==5){
        
        $.ajax({
            url: '/repetition',
            success: function(point) {

                document.getElementById("repetition").innerHTML ="<b>"+point+"</b>";

            },
            cache: false
        });
        

    }

    if(l==5){
        
        $.ajax({
            url: '/breakstate',
            success: function(point) {
                if(point==1){
                document.getElementById("break").style.backgroundColor = "#14FF00";
                }else{

                    document.getElementById("break").style.backgroundColor = "#FF0000";

                }

            },
            cache: false
        });
        l=0;

    }

    if(k==5){
        $.ajax({
            url: '/speed',
            success: function(point) {
                var series = chartb.series[0],
                    shift = series.data.length > 20; 
                                                 
                chartb.yAxis[0].setExtremes(0,1500);
                chartb.series[0].addPoint(point, true, shift);
            },
            cache: false
        });
        k=0;
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
            text: 'Torque '
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
        plotOptions: {
            
            series: {
                color:'hsl(18, 84%, 59%)',
                allowPointSelect: true,
                marker: {
                    fillColor: 'hsl(18, 84%, 59%)',
                    states: {
                        select: {
                            fillColor: 'red',
                            lineWidth: 0
                        }
                    }
                }
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
            renderTo: 'data-container1',
            defaultSeriesType: 'spline',
            events: {
                load: requestData
            }
        },
        title: {
            text: 'Speed'
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
        plotOptions: {
            
            series: {
                color:'hsl(18, 84%, 59%)',
                allowPointSelect: true,
                marker: {
                    fillColor: 'hsl(18, 84%, 59%)',
                    states: {
                        select: {
                            fillColor: 'red',
                            lineWidth: 0
                        }
                    }
                }
            }
        },
        series: [{
            name: 'Data',
            data: []
        }]
    });
});