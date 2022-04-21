var chart;
var chartb;

var i=0;
var j=0;
var k=0;
var l=0;

var input = document.getElementById('input');

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

                init(point);
               

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


function init(angle) {
    var svg = Snap('#svg');

    var SIZE = svg.attr('viewBox').width;
    var CENTER = SIZE / 2;

    var pointerLine = svg.select('#pointerLine');

    var pointerMarker = svg.select('#pointerMarker');
    var pointerText = svg.select('#pointerText');
    var arc = svg.select('#arc');
    var arcText = svg.select('#arcText');



    function setAngle(angle) {
        input.value = angle;
        animateAngle(angle);
    }

    function animateAngle(angle) {
        var normAngle = angle % 360;
        drawPointerLine(normAngle);
        drawPointerTriangle(normAngle);
        drawPointerText(normAngle, angle);
        drawArc(normAngle);
        drawArcText(normAngle, angle + '°');
      
    }

    function calcPos(angle, length) {
        var radians = angle * Math.PI / 180;
        return {
            x: CENTER + length * Math.cos(radians),
            y: CENTER - length * Math.sin(radians)
        }
    }

    function drawPointerLine(angle) {
        var pos = calcPos(angle, CENTER - 3);
        pointerLine.animate({x2: pos.x, y2: pos.y}, 500, mina.linear);
    }

    function drawPointerText(angle, text) {
        var pos = calcPos(angle, CENTER - 1);
        pointerText.attr({text: text});
        pointerText.animate({x: pos.x, y: pos.y}, 100, mina.linear);
    }

    function drawPointerTriangle(angle) {
        var pos0 = calcPos(angle, CENTER - 3);
        var pos1 = calcPos(angle - 2, CENTER - 2);
        var pos2 = calcPos(angle + 2, CENTER - 2);

        var d = [
            'M', pos0.x, ',', pos0.y,
            'L', pos1.x, ',', pos1.y,
            'L', pos2.x, ',', pos2.y,
            'Z'
        ].join('');

        pointerMarker.animate({d: d}, 100, mina.linear);
    }


    function drawArc(angle) {
        if (angle === 0) {
            arc.animate({d: 'M' + CENTER + ',' + CENTER}, 100, mina.linear);
            return;
        }

        var size1 = 14;
        var pos = calcPos(angle, size1);
        var size2 = 11.3;
        var pos2 = calcPos(angle, size2);

        var xRot = angle > 180 ? 0 : 1;
        var largeFlag = angle <= 180 ? 0 : 1;

        var d = [
            'M', CENTER, ',', CENTER,
            'L', CENTER + size1, ',', CENTER,
            'A', size1, ',', size1, ',', xRot, ',', largeFlag, ',0,', pos.x, ',', pos.y,
            'L', pos2.x, ',', pos2.y,
            'A', size2, ',', size2, ',', xRot, ',', largeFlag, ',1,', CENTER + size2, ',', CENTER,
            'Z'
        ].join('');

        arc.animate({d: d}, 100, mina.linear);
    }



    function drawArcText(angle, text) {
        if (angle >= 10) {
            var pos = calcPos(angle / 2, 10);
            arcText.attr({text: text});
            arcText.animate({x: pos.x, y: pos.y}, 100, mina.linear);
        } else {
            arcText.attr({x: CENTER, y: CENTER, text: ''});
        }
    }



    setAngle(angle);

}
