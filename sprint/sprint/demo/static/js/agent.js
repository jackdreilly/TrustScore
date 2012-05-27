function endorserTSCallback(data) {
	var endorsers = data.endorsers;
	var names = _.map(endorsers, function (endorser) {
			return endorser.name;
	});
	
	var scores = _.map(endorsers, function (endorser) {
		return endorser.trust_score;
	});
	

	
	var height = 140;
	var width = 300;
	
	var x = d3
		.scale
		.pow()
		.domain([d3.max([0,d3.min(scores) - d3.min(scores)*.05 ]), d3.max(scores)])
		.range([0,width]);
		
	var y = d3
		.scale
		.ordinal()
		.domain(names)
		.rangeBands([0, height*.8]);

	
	var chart = d3
		.select("#graph")
		.append("svg")
		.attr("class", "chart")
		.attr("width", width)
		.attr("height", height)
		.append('g')
		.attr('transform', 'translate(10,15)');

	chart
		.selectAll("line")
		.data(x.ticks(10))
		.enter().append("line")
		.attr("x1", x)
		.attr("x2", x)
		.attr("y1", 0)
		.attr("y2", 120)
		.style("stroke", "#ccc");
		
	chart
		.selectAll("rect")
		.data(endorsers)
		.enter()
		.append('rect')
		.attr('y', function(d) {return 4 +  y(d.name);})
		.attr('width', 0)
		.attr('height', y.rangeBand())
		.attr("data-content", function(d){return sprintf("%s: %.2f", d.name, d.trust_score);})
		.attr('style', function(d) {
			var color = "steelblue";
			if (d.score < 0) color = "darkred";
			if (d.score > 0.0) color = "darkgreen";
			if (d.score == 0.0) color = "gray";
			return "fill:" + color + ";";
		});
						
	chart
		.selectAll("text")
		.data(endorsers)
		.enter()
		.append("text")
		.attr("x", function(d,i){return x(d.trust_score);})
		.attr("y", function(d,i) { 
			return y(d.name) + y.rangeBand() / 2 + 4; 
		})
		.attr("dx", -10) // padding-right
		.attr("dy", ".35em") // vertical-align: middle
		.attr("text-anchor", "end") // text-align: right
		.text(function(d){return sprintf("%s: %.2f", d.name, d.trust_score);});

	chart
		.selectAll(".rule")
		.data(x.ticks(10))
		.enter()
		.append("text")
		.attr("class", "rule")
		.attr("x", x)
		.attr("y", 0)
		.attr("dy", -3)
		.attr("text-anchor", "middle")
		.text(String);
			
	chart
		.append("line")
		.attr('y1', 0)
		.attr('y2', 120)
		.style('stroke', '#000');
		
	$("#graph rect").popover({
		placement: "left"
	});
	
	chart
		.selectAll("rect")
		.data(endorsers)
		.transition()
		.duration(1000)
		.attr('width', function(d) {
			return x(d.trust_score);
		});
}
var trustScoreCBGenerator = Dajaxice.demo.endorser_trust_scores;
$("#graph-button").click( function (e) {
	Dajaxice.demo.endorser_trust_scores(endorserTSCallback, {'pk': pk});
});
