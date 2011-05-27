chart = null;

chart_runcount();

function chart_runcount() {
   chart = new Highcharts.Chart({
      chart: { renderTo: 'chart_runstats', type: 'spline' },
      credits: { enabled: false },
      legend: { align: 'right', verticalAlign: 'top', floating: true },
      title: { text: 'Integrated Number of Runs (Test)' },
      xAxis: { type: 'datetime' },
      yAxis: { title: {text: '# Runs'}, min: 0 },
      series: [{
         name: 'All Runs',
         data: [
            [Date.UTC(2010,  9, 27), 5],
            [Date.UTC(2010, 10, 10), 5],
            [Date.UTC(2010, 10, 18), 5],
            [Date.UTC(2010, 11,  2), 6],
            [Date.UTC(2010, 11,  9), 6],
            [Date.UTC(2010, 11, 16), 6],
            [Date.UTC(2010, 11, 28), 6],
            [Date.UTC(2011,  0,  1), 6],
            [Date.UTC(2011,  0,  8), 6],
            [Date.UTC(2011,  0, 12), 6],
            [Date.UTC(2011,  0, 27), 6],
            [Date.UTC(2011,  1, 10), 6],
            [Date.UTC(2011,  1, 18), 10],
            [Date.UTC(2011,  1, 24), 10],
            [Date.UTC(2011,  2,  4), 10],
            [Date.UTC(2011,  2, 11), 10],
            [Date.UTC(2011,  2, 15), 10],
            [Date.UTC(2011,  2, 25), 10],
            [Date.UTC(2011,  3,  2), 10],
            [Date.UTC(2011,  3,  6), 10],
            [Date.UTC(2011,  3, 13), 20],
            [Date.UTC(2011,  4,  3), 20],
            [Date.UTC(2011,  4, 26), 20],
            [Date.UTC(2011,  5,  9), 20],
            [Date.UTC(2011,  5, 12), 20]
         ]
      }]
   });
}   
