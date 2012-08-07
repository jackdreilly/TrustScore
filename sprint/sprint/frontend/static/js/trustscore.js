function graph_history(history) {
    var data, data_t, h, max, pb, pl, pr, pt, ticks, version, vis, w, x, y, _ref;
    version = Number(document.location.hash.replace('#', ''));
    data_t = history.t_points;
    data = history.y_points;
    _ref = [20, 20, 20, 20], pt = _ref[0], pl = _ref[1], pr = _ref[2], pb = _ref[3];
    w = 800 - (pl + pr);
    h = 300 - (pt + pb);
    max = d3.max(data);
    min = d3.min(data);
    max_t = d3.max(data_t);
    x = d3.scale.linear().domain([0, max_t]).range([0, w]);
    y = d3.scale.linear().domain([min, max]).range([h, 0]);
    vis = d3.select('#chart').style('margin', '20px auto').style('width', "" + w + "px").append('svg:svg').attr('width', w + (pl + pr)).attr('height', h + pt + pb).attr('class', 'viz').append('svg:g').attr('transform', "translate(" + pl + "," + pt + ")");
    vis.selectAll('path.line').data([data]).enter().append("svg:path").attr("d", d3.svg.line().x(function(d, i) {
      return x(data_t[i]);
    }).y(y));
    if (version < 2 && version !== 0) {
      return;
    }
    ticks = vis.selectAll('.ticky').data(y.ticks(7)).enter().append('svg:g').attr('transform', function(d) {
      return "translate(0, " + (y(d)) + ")";
    }).attr('class', 'ticky');
    ticks.append('svg:line').attr('y1', 0).attr('y2', 0).attr('x1', 0).attr('x2', w);
    ticks.append('svg:text').text(function(d) {
      return d;
    }).attr('text-anchor', 'end').attr('dy', 2).attr('dx', -4);
    ticks = vis.selectAll('.tickx').data(x.ticks(data.length)).enter().append('svg:g').attr('transform', function(d, i) {
      return "translate(" + (x(data_t[i])) + ", 0)";
    }).attr('class', 'tickx');
    ticks.append('svg:line').attr('y1', h).attr('y2', 0).attr('x1', 0).attr('x2', 0);
    ticks.append('svg:text').text(function(d, i) {
      return data_t[i];
    }).attr('y', h).attr('dy', 15).attr('dx', -2);
    if (version < 3 && version !== 0) {
      return;
    }
    return vis.selectAll('.point').data(data).enter().append("svg:circle").attr("class", function(d, i) {
      if (d === max) {
        return 'point max';
      } else {
        return 'point';
      }
    }).attr("r", function(d, i) {
      if (d === max) {
        return 6;
      } else {
        return 4;
      }
    }).attr("cx", function(d, i) {
      return x(data_t[i]);
    }).attr("cy", function(d) {
      return y(d);
    }).on('mouseover', function() {
      return d3.select(this).attr('r', 8);
    }).on('mouseout', function() {
      return d3.select(this).attr('r', 4);
    }).on('click', function(d, i) {
      return console.log(d, i);
    });
  }

$(document).ready(function() {
//	$('#tab3 td:first a').click(function() {
//  		$('#tab3').slideToggle('slow', function() {
//  });
});
