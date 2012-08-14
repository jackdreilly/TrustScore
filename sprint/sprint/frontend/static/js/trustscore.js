function graph_history(history) {
  console.log(history);
  var data, data_t, h, max, pb, pl, pr, pt, ticks, version, vis, w, x, y, _ref;
  version = Number(document.location.hash.replace('#', ''));
  data_t = history.t_points;
  data = history.y_points;
  _ref = [30, 30, 30, 30], pt = _ref[0], pl = _ref[1], pr = _ref[2], pb = _ref[3];
  w = 600 - (pl + pr);
  h = 300 - (pt + pb);
  max = d3.max(data);
  min = d3.min(data);
  max_t = data_t.length - 1;
  x = d3.scale.linear().domain([0, max_t]).range([0, w]);
  y = d3.scale.linear().domain([min, max]).range([h, 0]);
  vis = d3.select('#chart').style('margin', '20px auto').style('width', "" + w + "px").append('svg:svg').attr('width', w + (pl + pr)).attr('height', h + pt + pb).attr('class', 'viz').append('svg:g').attr('transform', "translate(" + pl + "," + pt + ")");
  vis.selectAll('path.line').data([data]).enter().append("svg:path").attr("d", d3.svg.line().x(function(d, i) {
    return x(i);
  }).y(y));

  ticks = vis.selectAll('.ticky').data(y.ticks(7)).enter().append('svg:g').attr('transform', function(d) {
    return "translate(0, " + (y(d)) + ")";
  }).attr('class', 'ticky');

  ticks.append('svg:line').attr('y1', 0).attr('y2', 0).attr('x1', 0).attr('x2', w);

  ticks.append('svg:text').text(function(d) {
    return d;
  }).attr('text-anchor', 'end').attr('dy', 2).attr('dx', -4);

  ticks = vis.selectAll('.tickx').data(x.ticks(data.length)).enter().append('svg:g').attr('transform', function(d, i) {
    return "translate(" + (x(i)) + ", 0)";
  }).attr('class', 'tickx');

  ticks.append('svg:line').attr('y1', h).attr('y2', 0).attr('x1', 0).attr('x2', 0);

  ticks.append('svg:text').text(function(d, i) {
    return data_t[i];
  }).attr('y', h).attr('dy', 15).attr('dx', -2);

  vis.selectAll('.point')
    .data(data)
    .enter()
    .append("svg:circle")
    .attr("class", function(d, i) {
    return 'point';
  }).attr("r", function(d, i) {
      return 10;
  }).attr("cx", function(d, i) {
    return x(i);
  }).attr("cy", function(d) {
    return y(d);
  }).on('mouseover', function(d,i) {
    d3.select(this).attr('r', 30);
    d3.select(this).attr('class', 'point max');
  }).on('mouseout', function() {
    d3.select(this).attr('r', 10);
    d3.select(this).attr('class', 'point');
  }).each(function(d,i){
    var title, content;
    if (i < 1) {
      title = 'Creation';
      content = 'The beginning of time is ' + history.creation_date;
    } else {
      var prop_event = history.propagations[i - 1];
      title = prop_event.actor;
      content = 'Event ' + prop_event.event + ', ' + prop_event.date;
    }
    $(this).popover({
      'title': title,
      'content': content,
      'placement': 'top',
      'trigger': 'hover'
      });
    });
  }


$(document).ready(function() {

  // call table sorter and attach to all tables with class ".tablesorter"
  $(".tablesorter").tablesorter();
  $("#actor-table").tablesorter(
      { headers: {3: {sorter:false} }  }
  );
  
  // agents - on row click, open subsequent hidden row showing loan information
  /* code doesn't work
  $("tr.click").click(function() {
    $("tr.hide").next().show();
  )};*/
});


