function endorserTSCallback(data) {
	var endorsers = data.endorsers;
	var names = _.map(endorsers, function (endorser) {
			return endorser.name;
	});
	var scores = _.map(endorsers, function (endorser) {
		return 1 + .1*endorser.trust_score;
	});
	var x = d3
		.scale
		.log()
		.domain([1, d3.max(scores)])
		.range(["0px", "200px"]);
	
	var chart = d3.select("#name").append("div").attr("class","chart");
	chart
		.selectAll(".chart")
		.data(endorsers)
		.enter()
		.append('div')
		.style('width', function(d) {
			return x(1 + .1*d.trust_score);
		})
		.text(function (d){return d.name;});
}
var trustScoreCBGenerator = Dajaxice.demo.endorser_trust_scores;
$("#graph-button").click( function (e) {
	Dajaxice.demo.endorser_trust_scores(endorserTSCallback, {'pk': pk});
});
